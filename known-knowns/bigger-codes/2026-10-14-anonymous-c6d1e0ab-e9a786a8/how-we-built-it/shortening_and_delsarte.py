#!/usr/bin/env python3
"""
Lens 2 (symmetry-orbit-join):
Executes H1-H8:
  H1: Minimum-degree coordinate shortening (n -> n-1) + C LNS re-completion on A(52..56, 8, 7)
  H2: Coordinate extension (n-1 -> n) with greedy hyperplane completion + C LNS walk on A(52..56, 8, 7)
  H3: Shortening/extension into untouched adjacent Brouwer cells A(51, 8, 7) and A(57, 8, 7)
  H4: Coordinate-sliced hyperplane bipartite splicing between distinct trajectories
  H5: Complete exact rational Delsarte LP upper-bound scan across data/brouwer_cells.json (29 <= n <= 64)
  H6: Slack & second-moment shortening constraint (M_{t,s}) audit at the exact rational Delsarte optimum
  H7: Double-coordinate puncturing + 2-bit re-inflation (n -> n-2 -> n)
  H8: Coordinate degree equalization & degree-sorted coordinate relabeling LNS across record codes
"""
import json
import os
import random
import subprocess
import tempfile
from fractions import Fraction as F
from math import comb


def eberlein(n, w, i, k):
    return sum((-1) ** j * comb(k, j) * comb(w - k, i - j) * comb(n - w - k, i - j) for j in range(i + 1))


def delsarte_matrices(n, w):
    v = [comb(w, i) * comb(n - w, i) for i in range(w + 1)]
    m = [comb(n, k) - (comb(n, k - 1) if k >= 1 else 0) for k in range(w + 1)]
    P = [[F(eberlein(n, w, i, k)) for k in range(w + 1)] for i in range(w + 1)]
    Q = [[F(m[k]) * P[i][k] / v[i] for i in range(w + 1)] for k in range(w + 1)]
    return v, m, P, Q


def solve_delsarte_exact_rational(n, d, w, extra_rows=None):
    """
    Solve the primal Delsarte LP over Q using exact rational Simplex:
      maximize 1 + sum_{i in X} a_i
      subject to a_i >= 0 (i in X = [delta..w])
                 sum_{i in X} (-Q[k][i]) a_i <= m[k]   for k = 1..w
    Returns (opt_val, primal_dict, dual_dict).
    """
    w_eff = min(w, n - w)
    delta = d // 2
    X = list(range(delta, w_eff + 1))
    if not X:
        return F(1), {}, {}
    v, m, P, Q = delsarte_matrices(n, w_eff)
    num_vars = len(X)

    rows_A = []
    rows_b = []
    for k in range(1, w_eff + 1):
        rows_A.append([-Q[k][i] for i in X])
        rows_b.append(F(m[k]))
    if extra_rows:
        for rA, rb in extra_rows:
            if rb >= 0:
                rows_A.append([F(val) for val in rA])
                rows_b.append(F(rb))

    num_cons = len(rows_A)
    total_cols = num_vars + num_cons + 1
    tab = []
    basis = []
    for r in range(num_cons):
        row = list(rows_A[r]) + [F(1 if c == r else 0) for c in range(num_cons)] + [rows_b[r]]
        tab.append(row)
        basis.append(num_vars + r)

    obj = [F(-1) for _ in range(num_vars)] + [F(0) for _ in range(num_cons + 1)]
    tab.append(obj)

    for _ in range(500):
        piv_c = -1
        for c in range(num_vars + num_cons):
            if tab[num_cons][c] < 0:
                piv_c = c
                break
        if piv_c < 0:
            break
        piv_r = -1
        best_ratio = None
        for r in range(num_cons):
            a_rc = tab[r][piv_c]
            if a_rc > 0:
                ratio = tab[r][-1] / a_rc
                if best_ratio is None or ratio < best_ratio or (ratio == best_ratio and basis[r] > basis[piv_r]):
                    best_ratio = ratio
                    piv_r = r
        if piv_r < 0:
            return None, None, None
        piv_val = tab[piv_r][piv_c]
        tab[piv_r] = [val / piv_val for val in tab[piv_r]]
        for r in range(num_cons + 1):
            if r != piv_r:
                factor = tab[r][piv_c]
                if factor != 0:
                    tab[r] = [tab[r][c] - factor * tab[piv_r][c] for c in range(total_cols)]
        basis[piv_r] = piv_c

    opt_val = F(1) + tab[num_cons][-1]
    primal = {X[i]: F(0) for i in range(num_vars)}
    for r in range(num_cons):
        if basis[r] < num_vars:
            primal[X[basis[r]]] = tab[r][-1]
    dual = {}
    for k in range(1, w_eff + 1):
        yk = tab[num_cons][num_vars + k - 1]
        if yk > 0:
            dual[k] = yk
    return opt_val, primal, dual


def load_words_txt(path, n):
    words = []
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            s = ln.strip()
            if len(s) == n and all(c in ("0", "1") for c in s):
                words.append(int(s, 2))
    return sorted(set(words))


def save_words_txt(path, n, words):
    with open(path, "w", encoding="utf-8") as f:
        for x in sorted(set(words)):
            f.write(format(x, f"0{n}b") + "\n")


def shorten_code_at_bit(words, n, bit_p):
    """Delete coordinate bit_p (0 <= bit_p < n), keeping only words where bit_p == 0."""
    low_mask = (1 << bit_p) - 1
    out = []
    for x in words:
        if ((x >> bit_p) & 1) == 0:
            lo = x & low_mask
            hi = (x >> (bit_p + 1)) << bit_p
            out.append(lo | hi)
    return sorted(set(out))


def extend_code_with_greedy_hyperplane(words, n_old, d, w, seed=42):
    """
    Embed (n_old, d, w) code into (n_old + 1, d, w) by placing 0 at bit n_old,
    then greedily add codewords with bit n_old == 1 (which have w-1 bits in 0..n_old-1,
    sharing < t bits with words in C_0 and < t-1 bits with each other on 0..n_old-1).
    Uses exact t-subset and (t-1)-subset hash sets for fast greedy completion.
    """
    from itertools import combinations
    t = w - d // 2 + 1
    rng = random.Random(seed)
    used_t = set()
    for x in words:
        bits = [b for b in range(n_old) if (x >> b) & 1]
        for comb_t in combinations(bits, t):
            used_t.add(comb_t)

    used_tm1 = set()
    added_top = []
    coords = list(range(n_old))
    # Sample 60,000 random (w-1)-subsets of 0..n_old-1 to populate the new hyperplane
    for _ in range(60000):
        sub = tuple(sorted(rng.sample(coords, w - 1)))
        if any(c in used_tm1 for c in combinations(sub, t - 1)):
            continue
        if any(c in used_t for c in combinations(sub, t)):
            continue
        for c in combinations(sub, t - 1):
            used_tm1.add(c)
        for c in combinations(sub, t):
            used_t.add(c)
        word = 1 << n_old
        for b in sub:
            word |= (1 << b)
        added_top.append(word)

    return sorted(set(words) | set(added_top))


def double_puncture_reinflate(words, n, p1, p2):
    """Remove all codewords that have 1 at coordinate p1 or coordinate p2, keeping them in {0,1}^n."""
    mask = (1 << p1) | (1 << p2)
    return [x for x in words if (x & mask) == 0]


def permute_coordinates(words, n, perm):
    """Apply coordinate permutation perm (where old bit i moves to new bit perm[i])."""
    out = []
    for x in words:
        y = 0
        for i in range(n):
            if (x >> i) & 1:
                y |= (1 << perm[i])
        out.append(y)
    return sorted(set(out))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    run_dir = os.path.abspath(os.path.join(here, "..", "..", ".."))
    repo_codes = os.path.abspath(os.path.join(run_dir, "..", "..", "repo", "known-knowns", "bigger-codes", "codes"))
    results_dir = os.path.join(run_dir, "results")
    os.makedirs(results_dir, exist_ok=True)
    c_bin = os.path.abspath(os.path.join(run_dir, "attempts", "c-evaluator-optimizer", "code", "cwc_lns"))

    with open(os.path.join(run_dir, "data", "brouwer_cells.json"), "r", encoding="utf-8") as f:
        brouwer_cells = json.load(f)

    print("=== LENS 2: SYMMETRY-ORBIT-JOIN EXECUTION LOG ===", flush=True)

    # ---------------------------------------------------------
    # H5 & H6: Complete Exact Rational Delsarte LP & Second-Moment Scan (29 <= n <= 64)
    # ---------------------------------------------------------
    print("\n--- H5 & H6: Exact Rational Delsarte LP & Second-Moment Upper Bound Audit (29 <= n <= 64) ---", flush=True)
    trophy_delsarte = {(31, 12, 10), (31, 12, 11), (32, 12, 10), (32, 12, 15), (32, 12, 16)}
    cells_scanned = 0
    trophy_reproduced = 0
    pure_lp_new_hits = 0
    moment_tightened = 0

    # Pure Delsarte LP upper-bound table delsarte_ub[(n, d, w)]
    delsarte_ub = {}
    for k_str, info in sorted(brouwer_cells.items(), key=lambda kv: tuple(map(int, kv[0].split(",")))):
        n, d, w = map(int, k_str.split(","))
        if not (28 <= n <= 64) or d < 6 or w > n // 2:
            continue
        opt_val, primal, dual = solve_delsarte_exact_rational(n, d, w)
        if opt_val is None:
            continue
        delsarte_u = opt_val.numerator // opt_val.denominator
        delsarte_ub[(n, d, w)] = delsarte_u
        if n < 29:
            continue
        ub = info["ub"]
        lb = info["lb"]
        if ub is None or (lb is not None and lb == ub):
            continue
        cells_scanned += 1

        # H6: Test second-moment shortening constraints (M_{1,1} and M_{1,0}) using certified Delsarte UBs
        w_eff = min(w, n - w)
        delta = d // 2
        X = list(range(delta, w_eff + 1))
        extra = []
        if (n - 1, d, w - 1) in delsarte_ub and w_eff >= 1:
            u11 = delsarte_ub[(n - 1, d, w - 1)]
            rA = [F(comb(w_eff - x, 1), comb(w_eff, 1)) for x in X]
            rb = F(u11 - 1)
            extra.append((rA, rb))
        if (n - 1, d, w) in delsarte_ub and n - w_eff >= 1:
            u10 = delsarte_ub[(n - 1, d, w)]
            rA = [F(comb(n - w_eff - x, 1), comb(n - w_eff, 1)) for x in X]
            rb = F(u10 - 1)
            extra.append((rA, rb))
        if extra:
            opt_m, _, _ = solve_delsarte_exact_rational(n, d, w, extra_rows=extra)
            if opt_m is not None and opt_m < opt_val:
                moment_tightened += 1
                m_u = opt_m.numerator // opt_m.denominator
                if m_u < delsarte_u:
                    delsarte_u = m_u
                    delsarte_ub[(n, d, w)] = delsarte_u

        if delsarte_u < ub:
            if (n, d, w) in trophy_delsarte:
                trophy_reproduced += 1
                print(f"  [TROPHY VERIFIED] A({n},{d},{w}) <= {delsarte_u} (exact LP={opt_val}, Andw UB={ub})")
            else:
                pure_lp_new_hits += 1
                print(f"  [NEW DELSARTE UB] A({n},{d},{w}) <= {delsarte_u} (exact LP={opt_val}, Andw UB={ub})")

    print(f"H5/H6 Scanned {cells_scanned} open cells (29 <= n <= 64): reproduced {trophy_reproduced}/5 Trophy Delsarte bounds, "
          f"{moment_tightened} fractional tightenings via certified M_{{1,s}} second-moment constraints, "
          f"{pure_lp_new_hits} new pure-LP upper bounds beyond Trophy Case.", flush=True)

    # ---------------------------------------------------------
    # H8: Coordinate Degree Equalization & Structural Slack Audit
    # ---------------------------------------------------------
    print("\n--- H8: Coordinate Degree Equalization Audit on Record Constant-Weight Codes ---", flush=True)
    audit_files = [
        (os.path.join(results_dir, "A52_8_7_3800.txt"), 52, 8, 7),
        (os.path.join(results_dir, "A53_8_7_3992.txt"), 53, 8, 7),
        (os.path.join(results_dir, "A54_8_7_4204.txt"), 54, 8, 7),
        (os.path.join(results_dir, "A55_8_7_4431.txt"), 55, 8, 7),
        (os.path.join(results_dir, "A56_8_7_4691.txt"), 56, 8, 7),
        (os.path.join(repo_codes, "A26_6_8_3603.txt"), 26, 6, 8),
        (os.path.join(repo_codes, "A27_6_9_8325.txt"), 27, 6, 9),
        (os.path.join(repo_codes, "A30_8_8_1166.txt"), 30, 8, 8),
        (os.path.join(repo_codes, "A51_6_5_1785.txt"), 51, 6, 5),
    ]
    min_deg_coord = {}
    max_deg_pairs = {}
    deg_sorted_perms = {}
    for p, n, d, w in audit_files:
        words = load_words_txt(p, n)
        M = len(words)
        degs = [(sum((x >> bit) & 1 for x in words), bit) for bit in range(n)]
        degs.sort()
        d_min, b_min = degs[0]
        d_max, b_max = degs[-1]
        min_deg_coord[(n, d, w)] = (b_min, d_min, words)
        max_deg_pairs[(n, d, w)] = (degs[-1][1], degs[-2][1], words)
        # Permutation mapping old bit -> new rank by degree ascending
        perm = [0] * n
        for new_idx, (_, old_bit) in enumerate(degs):
            perm[old_bit] = new_idx
        deg_sorted_perms[(n, d, w)] = (perm, words)
        print(f"  A({n:2d},{d},{w}) M={M:4d}: avg_deg={M*w/n:6.1f}, min_deg={d_min:4d} (bit {b_min:2d} -> shortened M={M-d_min:4d}), "
              f"max_deg={d_max:4d} (bit {b_max:2d}), spread={d_max - d_min:2d}", flush=True)

    # ---------------------------------------------------------
    # H1, H2, H3, H4, H7, H8: Cross-Coordinate Shortening, Extension, Double-Puncturing, Splicing & Orbit Relabeling
    # ---------------------------------------------------------
    print("\n--- H1, H2, H3, H4, H7, H8: Coordinate Surgery Seeds + C Blocker-Hypergraph LNS Walks ---", flush=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        surgery_jobs = []

        # H1 & H3: Shorten A(n, 8, 7) -> A(n-1, 8, 7) for n = 56..52 (including n=52 -> n=51 untouched cell!)
        for n_src in [56, 55, 54, 53, 52]:
            b_min, d_min, words_src = min_deg_coord[(n_src, 8, 7)]
            short_words = shorten_code_at_bit(words_src, n_src, b_min)
            n_dst = n_src - 1
            seed_p = os.path.join(tmpdir, f"short_A{n_dst}_8_7_from_{n_src}.txt")
            save_words_txt(seed_p, n_dst, short_words)
            hyp_tag = "H3-Shorten51" if n_dst == 51 else f"H1-Shorten{n_dst}"
            surgery_jobs.append((hyp_tag, seed_p, n_dst, 8, 7, 25, 3, 8, 3000, 10000, 0.50, 700 + n_dst, 8.0))

        # H2 & H3: Extend A(n-1, 8, 7) -> A(n, 8, 7) with greedy hyperplane completion for n_src = 52..55
        for n_src in [52, 53, 54, 55]:
            _, _, words_src = min_deg_coord[(n_src, 8, 7)]
            n_dst = n_src + 1
            ext_words = extend_code_with_greedy_hyperplane(words_src, n_src, 8, 7, seed=800 + n_dst)
            seed_p = os.path.join(tmpdir, f"ext_A{n_dst}_8_7_from_{n_src}.txt")
            save_words_txt(seed_p, n_dst, ext_words)
            surgery_jobs.append((f"H2-Extend{n_dst}", seed_p, n_dst, 8, 7, 25, 3, 8, 3000, 10000, 0.50, 800 + n_dst, 8.0))

        # H7: Double-coordinate puncturing + re-inflation on A(52,8,7), A(26,6,8), A(30,8,8)
        for (n, d, w), r_s in [((52, 8, 7), 8.0), ((26, 6, 8), 6.0), ((30, 8, 8), 6.0)]:
            p1, p2, words_src = max_deg_pairs[(n, d, w)]
            punc_words = double_puncture_reinflate(words_src, n, p1, p2)
            seed_p = os.path.join(tmpdir, f"punc2_A{n}_{d}_{w}.txt")
            save_words_txt(seed_p, n, punc_words)
            surgery_jobs.append((f"H7-Punc2({n},{d},{w})", seed_p, n, d, w, 25, 3, 8, 3000, 10000, 0.50, 900 + n, r_s))

        # H4: Coordinate-sliced hyperplane splice between A(52,8,7) and shortened-from-53
        _, _, w52_orig = min_deg_coord[(52, 8, 7)]
        b53, _, w53_orig = min_deg_coord[(53, 8, 7)]
        w52_from53 = shorten_code_at_bit(w53_orig, 53, b53)
        half0 = [x for x in w52_orig if (x & 1) == 0]
        half1 = [x for x in w52_from53 if (x & 1) == 1]
        spliced = list(half0)
        for y in half1:
            if all(bin(x & y).count("1") < 4 for x in spliced):
                spliced.append(y)
        splice_p = os.path.join(tmpdir, "splice_A52_8_7.txt")
        save_words_txt(splice_p, 52, spliced)
        surgery_jobs.append(("H4-Splice(52,8,7)", splice_p, 52, 8, 7, 25, 3, 8, 3000, 10000, 0.55, 952, 8.0))

        # H8: Degree-sorted coordinate relabeling on A(52,8,7) M=3800 and A(30,8,8) M=1166
        for (n, d, w), target_bar in [((52, 8, 7), 3800), ((30, 8, 8), 1166)]:
            perm, words_src = deg_sorted_perms[(n, d, w)]
            relabeled = permute_coordinates(words_src, n, perm)
            rel_p = os.path.join(tmpdir, f"relabel_A{n}_{d}_{w}.txt")
            save_words_txt(rel_p, n, relabeled)
            surgery_jobs.append((f"H8-Relabel({n},{d},{w})", rel_p, n, d, w, 30, 3, 9, 4000, 12000, 0.55, 980 + n, 12.0))

        for tag, seed_p, n, d, w, rnds, kb, rmax, ncl, max4, pf, seed, max_s in surgery_jobs:
            print(f"\n--- [{tag}] Running C LNS on A({n},{d},{w}) ---", flush=True)
            out_target = results_dir if tag.startswith("H8-Relabel") else tmpdir
            bar_arg = str(len(load_words_txt(seed_p, n))) if tag.startswith("H8-Relabel") else "-1"
            cmd = [
                c_bin,
                seed_p,
                str(n),
                str(d),
                str(w),
                out_target,
                str(rnds),
                str(kb),
                str(rmax),
                str(ncl),
                str(max4),
                f"{pf:.2f}",
                str(seed),
                f"{max_s:.1f}",
                bar_arg,
            ]
            subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
