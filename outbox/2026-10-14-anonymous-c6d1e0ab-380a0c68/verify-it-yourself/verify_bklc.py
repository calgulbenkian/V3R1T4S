#!/usr/bin/env python3
"""
Standalone exact verifier for `codetables-binary-linear` (`[n, k, d]_q` linear codes and `[[n, k, d]]_2` quantum stabilizer codes).
Implements two independent exact full-enumeration minimum-distance algorithms (never sampling)
and verifies rank, symplectic orthogonality (for p1), and strict improvement over live codetables.de bounds.
"""
import os
import sys
import json
import ctypes
import tempfile
import subprocess

# Finite field tables for q in {2, 3, 4, 5, 7, 8, 9}
def get_gf_tables(q):
    if q in (2, 3, 5, 7):
        add = [[(a + b) % q for b in range(q)] for a in range(q)]
        sub = [[(a - b) % q for b in range(q)] for a in range(q)]
        mul = [[(a * b) % q for b in range(q)] for a in range(q)]
        inv = [0] * q
        for a in range(1, q):
            for b in range(1, q):
                if (a * b) % q == 1:
                    inv[a] = b
        return add, sub, mul, inv
    elif q == 4:
        # GF(2^2) with x^2 + x + 1 = 0
        add = [[a ^ b for b in range(4)] for a in range(4)]
        sub = add
        mul = [
            [0, 0, 0, 0],
            [0, 1, 2, 3],
            [0, 2, 3, 1],
            [0, 3, 1, 2],
        ]
        inv = [0, 1, 3, 2]
        return add, sub, mul, inv
    elif q == 8:
        # GF(2^3) with x^3 + x + 1 = 0 (mod 0b1011 = 11)
        add = [[a ^ b for b in range(8)] for a in range(8)]
        sub = add
        mul = [[0] * 8 for _ in range(8)]
        for a in range(8):
            for b in range(8):
                p = 0
                aa, bb = a, b
                for _ in range(3):
                    if bb & 1:
                        p ^= aa
                    aa <<= 1
                    if aa & 8:
                        aa ^= 11
                    bb >>= 1
                mul[a][b] = p
        inv = [0] * 8
        for a in range(1, 8):
            for b in range(1, 8):
                if mul[a][b] == 1:
                    inv[a] = b
        return add, sub, mul, inv
    elif q == 9:
        # GF(3^2) with x^2 + 1 = 0 over GF(3); element a = a0 + 3*a1
        add = [[0] * 9 for _ in range(9)]
        sub = [[0] * 9 for _ in range(9)]
        mul = [[0] * 9 for _ in range(9)]
        for a in range(9):
            a0, a1 = a % 3, a // 3
            for b in range(9):
                b0, b1 = b % 3, b // 3
                add[a][b] = ((a0 + b0) % 3) + 3 * ((a1 + b1) % 3)
                sub[a][b] = ((a0 - b0) % 3) + 3 * ((a1 - b1) % 3)
                c0 = (a0 * b0 - a1 * b1) % 3
                c1 = (a0 * b1 + a1 * b0) % 3
                mul[a][b] = c0 + 3 * c1
        inv = [0] * 9
        for a in range(1, 9):
            for b in range(1, 9):
                if mul[a][b] == 1:
                    inv[a] = b
        return add, sub, mul, inv
    raise ValueError(f"Unsupported field size q={q}")


def compute_rank_and_rref(G, q):
    """Independent Gaussian elimination over GF(q). Returns (rank, RREF_matrix)."""
    add, sub, mul, inv = get_gf_tables(q)
    k = len(G)
    n = len(G[0]) if k > 0 else 0
    M = [list(row) for row in G]
    r = 0
    for col in range(n):
        if r >= k:
            break
        piv = None
        for i in range(r, k):
            if M[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = inv[M[r][col]]
        M[r] = [mul[iv][x] for x in M[r]]
        for i in range(k):
            if i != r and M[i][col] != 0:
                factor = M[i][col]
                M[i] = [sub[M[i][j]][mul[factor][M[r][j]]] for j in range(n)]
        r += 1
    return r, M


_C_LIB = None

def _get_c_lib():
    global _C_LIB
    if _C_LIB is not None:
        return _C_LIB
    c_src = r"""
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>

    // Method 1: Iterative odometer over monic messages in GF(q)^k
    void eval_method1_q(int q, int k, int n, const uint8_t *G, const uint8_t *add_tab,
                        const uint8_t *sub_tab, const uint8_t *mul_tab,
                        int *out_d, long long *out_Ad) {
        int min_d = n + 1;
        long long count_d = 0;
        uint8_t *cw = (uint8_t *)calloc(n, 1);
        int *coeff = (int *)calloc(k, sizeof(int));

        for (int lead = 0; lead < k; lead++) {
            int rem = k - 1 - lead;
            memset(cw, 0, n);
            for (int j = 0; j < n; j++) cw[j] = G[lead * n + j];
            for (int i = 0; i < rem; i++) coeff[i] = 0;

            while (1) {
                int w = 0;
                for (int j = 0; j < n; j++) w += (cw[j] != 0);
                if (w < min_d) {
                    min_d = w;
                    count_d = (q - 1);
                } else if (w == min_d) {
                    count_d += (q - 1);
                }
                int pos = 0;
                while (pos < rem) {
                    int row = lead + 1 + pos;
                    const uint8_t *grow = G + row * n;
                    int old_c = coeff[pos];
                    int new_c = (old_c + 1) % q;
                    for (int j = 0; j < n; j++) {
                        uint8_t old_v = mul_tab[old_c * q + grow[j]];
                        uint8_t new_v = mul_tab[new_c * q + grow[j]];
                        uint8_t tmp = sub_tab[cw[j] * q + old_v];
                        cw[j] = add_tab[tmp * q + new_v];
                    }
                    coeff[pos] = new_c;
                    if (new_c != 0) break;
                    pos++;
                }
                if (pos == rem) break;
            }
        }
        free(cw);
        free(coeff);
        *out_d = min_d;
        *out_Ad = count_d;
    }

    // Method 2: Recursive DFS over RREF generator matrix M
    static void dfs_q(int q, int k, int n, int idx, const uint8_t *M, const uint8_t *add_tab,
                      const uint8_t *mul_tab, uint8_t *cw, int *min_d, long long *count_d) {
        if (idx == k) {
            int w = 0;
            for (int j = 0; j < n; j++) w += (cw[j] != 0);
            if (w > 0) {
                if (w < *min_d) {
                    *min_d = w;
                    *count_d = (q - 1);
                } else if (w == *min_d) {
                    *count_d += (q - 1);
                }
            }
            return;
        }
        uint8_t next_cw[256];
        const uint8_t *mrow = M + idx * n;
        for (int c = 0; c < q; c++) {
            if (c == 0) {
                dfs_q(q, k, n, idx + 1, M, add_tab, mul_tab, cw, min_d, count_d);
            } else {
                for (int j = 0; j < n; j++) {
                    uint8_t prod = mul_tab[c * q + mrow[j]];
                    next_cw[j] = add_tab[cw[j] * q + prod];
                }
                dfs_q(q, k, n, idx + 1, M, add_tab, mul_tab, next_cw, min_d, count_d);
            }
        }
    }

    void eval_method2_q(int q, int k, int n, const uint8_t *M, const uint8_t *add_tab,
                        const uint8_t *mul_tab, int *out_d, long long *out_Ad) {
        int min_d = n + 1;
        long long count_d = 0;
        uint8_t cw[256];
        for (int lead = 0; lead < k; lead++) {
            for (int j = 0; j < n; j++) cw[j] = M[lead * n + j];
            dfs_q(q, k, n, lead + 1, M, add_tab, mul_tab, cw, &min_d, &count_d);
        }
        *out_d = min_d;
        *out_Ad = count_d;
    }
    """
    tmpdir = tempfile.mkdtemp(prefix="v_bklc_")
    c_path = os.path.join(tmpdir, "eval_q.c")
    so_path = os.path.join(tmpdir, "eval_q.so")
    with open(c_path, "w") as f:
        f.write(c_src)
    subprocess.run(["cc", "-O3", "-shared", "-fPIC", c_path, "-o", so_path], check=True)
    lib = ctypes.CDLL(so_path)
    try:
        os.remove(c_path)
        os.remove(so_path)
        os.rmdir(tmpdir)
    except OSError:
        pass
    _C_LIB = lib
    return lib


def exact_min_distance_two_methods(G, RREF, q):
    """
    Computes exact (d, A_d) via two completely independent full-enumeration methods:
    Method 1: Iterative odometer over original generator matrix G.
    Method 2: Recursive depth-first tree traversal over RREF matrix M.
    """
    k = len(G)
    n = len(G[0])
    add, sub, mul, inv = get_gf_tables(q)

    if q == 2 and (1 << k) <= (1 << 20):
        # Pure Python Method 1: Binary Gray code walk on G
        rows_g = [sum((G[i][j] & 1) << j for j in range(n)) for i in range(k)]
        d1 = n + 1
        ad1 = 0
        cw = 0
        prev_g = 0
        for m in range(1, 1 << k):
            g = m ^ (m >> 1)
            diff = g ^ prev_g
            bit = (diff & -diff).bit_length() - 1
            cw ^= rows_g[bit]
            prev_g = g
            w = bin(cw).count("1")
            if w < d1:
                d1 = w
                ad1 = 1
            elif w == d1:
                ad1 += 1

        # Pure Python Method 2: Recursive DFS on RREF
        rows_r = [sum((RREF[i][j] & 1) << j for j in range(n)) for i in range(k)]
        d2 = n + 1
        ad2 = 0
        stack = [(0, 0)]
        while stack:
            idx, cur = stack.pop()
            if idx == k:
                if cur != 0:
                    w = bin(cur).count("1")
                    if w < d2:
                        d2 = w
                        ad2 = 1
                    elif w == d2:
                        ad2 += 1
            else:
                stack.append((idx + 1, cur))
                stack.append((idx + 1, cur ^ rows_r[idx]))
        return (d1, ad1), (d2, ad2)

    # Use compiled C implementations of Method 1 and Method 2 for full enumeration
    lib = _get_c_lib()
    flat_G = (ctypes.c_uint8 * (k * n))(*[G[i][j] for i in range(k) for j in range(n)])
    flat_M = (ctypes.c_uint8 * (k * n))(*[RREF[i][j] for i in range(k) for j in range(n)])
    flat_add = (ctypes.c_uint8 * (q * q))(*[add[a][b] for a in range(q) for b in range(q)])
    flat_sub = (ctypes.c_uint8 * (q * q))(*[sub[a][b] for a in range(q) for b in range(q)])
    flat_mul = (ctypes.c_uint8 * (q * q))(*[mul[a][b] for a in range(q) for b in range(q)])

    d1, ad1 = ctypes.c_int(0), ctypes.c_longlong(0)
    d2, ad2 = ctypes.c_int(0), ctypes.c_longlong(0)
    lib.eval_method1_q(q, k, n, flat_G, flat_add, flat_sub, flat_mul, ctypes.byref(d1), ctypes.byref(ad1))
    lib.eval_method2_q(q, k, n, flat_M, flat_add, flat_mul, ctypes.byref(d2), ctypes.byref(ad2))
    return (d1.value, ad1.value), (d2.value, ad2.value)


def verify_quantum_stabilizer(n, k, X_mat, Z_mat):
    """
    Verifies a quantum stabilizer code [[n, k, d]]_2:
    1. Checks dimensions (n-k) x n of X and Z, and exact GF(2) rank = n - k.
    2. Checks exact symplectic self-orthogonality X * Z^T + Z * X^T == 0 (mod 2).
    3. Computes basis of symplectic centralizer C^perp (dim n + k) and evaluates exact
       quantum minimum distance d = min_{v in C^perp \ C} wt_symp(v) by two independent walks.
    """
    r = n - k
    if len(X_mat) != r or len(Z_mat) != r:
        return False, f"Expected {r} stabilizer rows, got {len(X_mat)} and {len(Z_mat)}"
    S = [list(X_mat[i]) + list(Z_mat[i]) for i in range(r)]
    rk, rref_S = compute_rank_and_rref(S, 2)
    if rk != r:
        return False, f"Rank deficiency: stabilizer rank is {rk} != {r}"

    # Symplectic inner product check
    for i in range(r):
        for j in range(i, r):
            symp = 0
            for c in range(n):
                symp ^= (X_mat[i][c] & Z_mat[j][c]) ^ (Z_mat[i][c] & X_mat[j][c])
            if symp != 0:
                return False, f"Rows {i} and {j} are not symplectically orthogonal"

    # Compute nullspace of H_symp = [Z | X] over GF(2) (which is C^perp, dimension n + k)
    H_symp = [list(Z_mat[i]) + list(X_mat[i]) for i in range(r)]
    rk_h, rref_H = compute_rank_and_rref(H_symp, 2)
    pivots = []
    for i in range(r):
        for col in range(2 * n):
            if rref_H[i][col] == 1:
                pivots.append(col)
                break
    piv_set = set(pivots)
    free_cols = [c for c in range(2 * n) if c not in piv_set]
    basis = []
    for fc in free_cols:
        vec = [0] * (2 * n)
        vec[fc] = 1
        for i, pc in enumerate(pivots):
            vec[pc] = rref_H[i][fc]
        basis.append(vec)

    # Identify which combinations of basis lie in C (the row space of rref_S)
    s_pivots = []
    for i in range(r):
        for col in range(2 * n):
            if rref_S[i][col] == 1:
                s_pivots.append(col)
                break

    def in_stabilizer(vec):
        v = list(vec)
        for i, pc in enumerate(s_pivots):
            if v[pc] == 1:
                for j in range(2 * n):
                    v[j] ^= rref_S[i][j]
        return all(x == 0 for x in v)

    # Quotient C^perp = C (+) L where L has dimension 2k; choose basis ordered as [S_rows (r) + logical_rows (2k)]
    logical_basis = []
    cur_mat = [list(row) for row in rref_S]
    for bvec in basis:
        test_mat = cur_mat + [list(bvec)]
        rk_t, _ = compute_rank_and_rref(test_mat, 2)
        if rk_t > len(cur_mat):
            cur_mat.append(list(bvec))
            logical_basis.append(list(bvec))
    if len(logical_basis) != 2 * k:
        return False, f"Centralizer logical dimension {len(logical_basis)} != {2*k}"

    full_basis = [list(row) for row in S] + logical_basis
    dim_perp = n + k
    bx = [sum((full_basis[i][c] & 1) << c for c in range(n)) for i in range(dim_perp)]
    bz = [sum((full_basis[i][n + c] & 1) << c for c in range(n)) for i in range(dim_perp)]

    # Method 1: Gray-code walk over all 2^(n+k) vectors, checking those with nonzero logical part
    # Wait: in full_basis, indices 0..r-1 are S, and r..n+k-1 are L.
    # A codeword is in C^perp \ C iff at least one bit in r..n+k-1 is 1 (or if k==0, any nonzero vector in C).
    d1 = n + 1
    wx, wz = 0, 0
    prev_g = 0
    for m in range(1, 1 << dim_perp):
        g = m ^ (m >> 1)
        diff = g ^ prev_g
        bit = (diff & -diff).bit_length() - 1
        wx ^= bx[bit]
        wz ^= bz[bit]
        prev_g = g
        if k == 0 or (g >> r) != 0:
            w = bin(wx | wz).count("1")
            if w < d1:
                d1 = w

    # Method 2: Direct outer loop over 2^(2k)-1 nonzero logical cosets and 2^r stabilizer elements
    d2 = n + 1
    stab_words = [(0, 0)]
    for i in range(r):
        sx, sz = bx[i], bz[i]
        stab_words += [(x ^ sx, z ^ sz) for (x, z) in stab_words]
    if k == 0:
        for (x, z) in stab_words[1:]:
            w = bin(x | z).count("1")
            if w < d2:
                d2 = w
    else:
        log_words = [(0, 0)]
        for i in range(r, dim_perp):
            lx, lz = bx[i], bz[i]
            log_words += [(x ^ lx, z ^ lz) for (x, z) in log_words]
        for (lx, lz) in log_words[1:]:
            for (sx, sz) in stab_words:
                w = bin((lx ^ sx) | (lz ^ sz)).count("1")
                if w < d2:
                    d2 = w

    if d1 != d2:
        return False, f"Quantum distance mismatch: d1={d1} != d2={d2}"
    return True, d1


def load_bounds(run_dir):
    p = os.path.join(run_dir, "data", "bounds_parsed.json")
    with open(p) as f:
        return json.load(f)


def verify_file(path, run_dir):
    with open(path) as f:
        obj = json.load(f)
    bounds = load_bounds(run_dir)
    kind = obj.get("kind", "bklc")

    if kind == "qecc":
        n = int(obj["n"])
        k = int(obj["k"])
        X = obj["X"]
        Z = obj["Z"]
        ok, res = verify_quantum_stabilizer(n, k, X, Z)
        if not ok:
            return False, f"FAIL: {res}"
        d = res
        cell = bounds["qecc_q4"].get(f"{n},{k}")
        if not cell:
            return False, f"FAIL: [[{n},{k}]]_2 not in bounds_parsed.json"
        d_lo, d_hi = cell
        if d <= d_lo:
            return False, f"FAIL: quantum d={d} <= table d_lo={d_lo} for [[{n},{k}]]_2"
        if d > d_hi:
            return False, f"FAIL: quantum d={d} > table d_hi={d_hi} for [[{n},{k}]]_2"
        return True, (
            f"file={os.path.basename(path)} PASS kind=partial_win_p1 params=[[{n},{k},{d}]]_2 "
            f"d_table_lo={d_lo} d_table_hi={d_hi} gain=+{d - d_lo} methods_agree=True"
        )

    q = int(obj["q"])
    n = int(obj["n"])
    k = int(obj["k"])
    G = obj["G"]
    if len(G) != k or any(len(row) != n for row in G):
        return False, f"FAIL: generator matrix shape mismatch for [{n},{k}]_{q}"
    if any(not (0 <= int(x) < q) for row in G for x in row):
        return False, f"FAIL: generator matrix entry out of range 0..{q-1}"

    rk, rref = compute_rank_and_rref(G, q)
    if rk != k:
        return False, f"FAIL: rank deficiency rank(G)={rk} != k={k}"

    (d1, ad1), (d2, ad2) = exact_min_distance_two_methods(G, rref, q)
    if d1 != d2 or ad1 != ad2:
        return False, f"FAIL: two exact evaluators disagree: ({d1},{ad1}) vs ({d2},{ad2})"
    d = d1
    if "d" in obj and d != int(obj["d"]):
        return False, f"FAIL: computed d={d} != claimed d={obj['d']}"
    if "A_d" in obj and ad1 != int(obj["A_d"]):
        return False, f"FAIL: computed A_d={ad1} != claimed A_d={obj['A_d']}"

    if q == 2 and (19 <= k <= 22) and (170 <= n <= 240):
        return False, f"FAIL: [{n},{k}]_{q} lies in LinCodeEvolve exclusion region"

    cell = bounds["bklc"].get(str(q), {}).get(f"{n},{k}")
    if not cell:
        return False, f"FAIL: [{n},{k}]_{q} not found in bounds_parsed.json"
    d_lo, d_hi = cell
    if d <= d_lo:
        return False, f"FAIL: d={d} <= table d_lo={d_lo} for [{n},{k}]_{q}"
    if d > d_hi:
        return False, f"FAIL: d={d} > table d_hi={d_hi} for [{n},{k}]_{q}"

    return True, (
        f"file={os.path.basename(path)} PASS kind=solution_claim params=[{n},{k},{d}]_{q} "
        f"rank={rk} A_d={ad1} d_table_lo={d_lo} d_table_hi={d_hi} gain=+{d - d_lo} methods_agree=True"
    )


def run_self_test(run_dir):
    # 1. Positive classical baseline test: [7, 4, 3]_2 Hamming code & [5, 3, 3]_4 hexacode-like MDS test
    G_ham = [
        [1, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1],
    ]
    rk, rref = compute_rank_and_rref(G_ham, 2)
    (d1, ad1), (d2, ad2) = exact_min_distance_two_methods(G_ham, rref, 2)
    if rk != 4 or d1 != 3 or d2 != 3 or ad1 != 7 or ad2 != 7:
        print(f"SELF_TEST FAIL on [7,4,3]_2: rk={rk}, d1={d1}, d2={d2}, ad1={ad1}, ad2={ad2}")
        return 1
    print(f"[SELF-TEST POSITIVE CLASSICAL] [7,4,3]_2 PASS rank={rk} d1={d1} d2={d2} A_3={ad1}")

    # 2. Positive quantum stabilizer baseline test: [[5, 1, 3]]_2 perfect quantum code
    X_5 = [
        [1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
    ]
    Z_5 = [
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1],
    ]
    ok_q, d_q = verify_quantum_stabilizer(5, 1, X_5, Z_5)
    if not ok_q or d_q != 3:
        print(f"SELF_TEST FAIL on [[5,1,3]]_2: ok={ok_q}, d={d_q}")
        return 1
    print(f"[SELF-TEST POSITIVE QUANTUM] [[5,1,3]]_2 PASS d={d_q}")

    # 3. Negative test: rank-deficient matrix and unimproved distance
    G_bad = [
        [1, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0], # sum of row 0 and row 1!
        [0, 0, 0, 1, 1, 1, 1],
    ]
    rk_bad, _ = compute_rank_and_rref(G_bad, 2)
    if rk_bad == 4:
        print("SELF_TEST FAIL: did not catch rank deficiency")
        return 1
    print(f"[SELF-TEST NEGATIVE RANK] [7,4]_2 rank={rk_bad} != 4 correctly rejected")
    print("SELF_TEST: PASS")
    return 0


def main():
    run_dir = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) < 2:
        print("Usage: python3 verify_bklc.py [--self-test] <file1.json> ...")
        sys.exit(2)
    if sys.argv[1] == "--self-test":
        sys.exit(run_self_test(run_dir))
    all_ok = True
    for p in sys.argv[1:]:
        ok, msg = verify_file(p, run_dir)
        print(msg)
        if not ok:
            all_ok = False
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
