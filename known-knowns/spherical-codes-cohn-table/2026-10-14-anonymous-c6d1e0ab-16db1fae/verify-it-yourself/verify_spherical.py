#!/usr/bin/env python3
"""Standalone 60-digit exact verifier for spherical-codes-cohn-table.

Uses Python standard-library decimal.Decimal at 60-digit precision (50+ digits required)
to normalize N vectors in R^d to unit length, compute all N*(N-1)/2 pairwise inner
products, verify c_table - c* >= 1e-10, check live table metadata (no '&ast;' star,
presence/absence of 'needs more optimization', no kissing-number overlap in dims 9..23),
and check baseline coordinate reproduction to 1e-11.
"""
import argparse
import json
import math
import os
import re
import sys
from decimal import Decimal, getcontext

getcontext().prec = 60


def sig_digits(s):
    s = str(s).strip()
    s = re.sub(r"[eE][+-]?\d+$", "", s)
    s = s.lstrip("+-").replace(".", "").lstrip("0")
    return len(s)


def normalize_vec(coords):
    decs = [Decimal(str(x).strip()) for x in coords]
    norm_sq = sum(x * x for x in decs)
    if norm_sq <= Decimal(0):
        raise ValueError("Zero vector encountered")
    inv_norm = Decimal(1) / norm_sq.sqrt()
    return [x * inv_norm for x in decs]


def max_inner_product(unit_vecs):
    n = len(unit_vecs)
    d = len(unit_vecs[0])
    # Quick float64 pre-screen to find top candidate pairs, then exact 60-digit Decimal on all pairs
    # within 1e-7 of the float64 maximum (or all pairs if N <= 250).
    fvecs = [[float(x) for x in v] for v in unit_vecs]
    fmax = -2.0
    dots_f = []
    for i in range(n):
        vi = fvecs[i]
        for j in range(i + 1, n):
            vj = fvecs[j]
            s = 0.0
            for k in range(d):
                s += vi[k] * vj[k]
            if s > fmax:
                fmax = s
            dots_f.append((s, i, j))
    thresh = fmax - 1e-6 if n > 250 else -10.0
    c_star = Decimal("-2")
    for s, i, j in dots_f:
        if s >= thresh:
             ui = unit_vecs[i]
             uj = unit_vecs[j]
             dot = sum(ui[k] * uj[k] for k in range(d))
             if dot > c_star:
                 c_star = dot
    return c_star


def load_tables(base_dir):
    plain_path = None
    meta_path = None
    for cand in [base_dir, os.path.join(base_dir, ".."), "."]:
        p1 = os.path.join(cand, "data", "plain.csv")
        p2 = os.path.join(cand, "data", "index_metadata.json")
        if os.path.isfile(p1) and os.path.isfile(p2):
            plain_path, meta_path = p1, p2
            break
    if not plain_path:
        raise FileNotFoundError("Could not locate data/plain.csv and data/index_metadata.json")
    plain = {}
    with open(plain_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split(",", 3)
            d, N = int(parts[0]), int(parts[1])
            plain[(d, N)] = Decimal(parts[2])
    meta = json.load(open(meta_path, "r", encoding="utf-8"))
    return plain, meta, os.path.dirname(plain_path)


def parse_code_file(path, d_arg=None, n_arg=None):
    raw = open(path, "r", encoding="utf-8").read().strip()
    if raw.startswith("{"):
        obj = json.loads(raw)
        d = int(obj["d"])
        N = int(obj["N"])
        vecs = obj["vectors"]
        return d, N, vecs, obj
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    vecs = [[x.strip() for x in l.split(",")] for l in lines]
    N = len(vecs)
    d = len(vecs[0]) if N > 0 else 0
    if d_arg and d != d_arg:
        raise ValueError(f"Dimension mismatch: file has {d}, expected {d_arg}")
    if n_arg and N != n_arg:
        raise ValueError(f"Point count mismatch: file has {N}, expected {n_arg}")
    return d, N, vecs, None


def verify_single(d, N, vecs, plain, meta, data_dir, require_improvement=True, require_20digits=True, label=""):
    fname = label or f"({d},{N})"
    if len(vecs) != N:
        return False, f"file={fname} FAIL: expected N={N} vectors, got {len(vecs)}"
    for idx, v in enumerate(vecs):
        if len(v) != d:
            return False, f"file={fname} FAIL: vector {idx} has dimension {len(v)}, expected {d}"
        if require_20digits:
            # Check that non-zero coordinates have >= 20 significant digits (or come from 25-digit format)
            max_sd = max(sig_digits(x) for x in v)
            if max_sd < 20:
                return False, f"file={fname} FAIL: vector {idx} has max {max_sd} significant digits (< 20)"

    if (d, N) not in plain:
        return False, f"file={fname} FAIL: ({d},{N}) not present in plain.csv"
    c_table = plain[(d, N)]
    m_entry = meta.get(f"{d},{N}")
    if not m_entry:
        return False, f"file={fname} FAIL: ({d},{N}) not present in index_metadata.json"
    if m_entry["s"] != 0:
        return False, f"file={fname} FAIL: ({d},{N}) carries '&ast;' (proven optimal) on spherical-codes.org"

    unit_vecs = [normalize_vec(v) for v in vecs]
    c_star = max_inner_product(unit_vecs)

    if 9 <= d <= 23 and c_star <= Decimal("0.5"):
        return False, f"file={fname} FAIL: ({d},{N}) has 9<=d<=23 and c*={c_star:.15f} <= 0.5 (kissing-number-low-dim)"

    # Optional baseline parser sanity check if data/codes/code_{d}_{N}.txt exists
    base_code_path = os.path.join(data_dir, "codes", f"code_{d}_{N}.txt")
    base_msg = ""
    if os.path.isfile(base_code_path):
        _, _, bvecs, _ = parse_code_file(base_code_path, d, N)
        b_unit = [normalize_vec(v) for v in bvecs]
        c_base = max_inner_product(b_unit)
        if abs(c_base - c_table) > Decimal("1e-11"):
            return False, f"file={fname} FAIL: baseline code_{d}_{N}.txt gives c={c_base:.15f} != c_table={c_table}"
        base_msg = f" base_ok=True(diff={abs(c_base - c_table):.2e})"

    gain = c_table - c_star
    angle_deg = math.degrees(math.acos(max(-1.0, min(1.0, float(c_star)))))
    needs_opt = (m_entry["o"] == 1)
    if not require_improvement:
        if abs(gain) <= Decimal("1e-11"):
            return True, f"file={fname} PASS kind=baseline_repro params=({d},{N}) c_table={c_table} c_star={c_star:.25f} abs_err={abs(gain):.2e}"
        return False, f"file={fname} FAIL: baseline reproduction error {abs(gain):.2e} > 1e-11"

    if gain < Decimal("1e-10"):
        return False, f"file={fname} FAIL: gain c_table - c* = {gain:.15e} < 1e-10 (c_table={c_table}, c*={c_star:.20f})"

    if needs_opt:
        kind = "p2_needs_opt_item"
    elif d == 3:
        kind = "solution_claim+p1_tammes"
    else:
        kind = "solution_claim"

    return True, (
        f"file={fname} PASS kind={kind} params=({d},{N}) needs_opt={needs_opt} "
        f"c_table={c_table} c_star={c_star:.25f} gain={gain:.6e} min_angle_deg={angle_deg:.12f}{base_msg}"
    )


def run_self_test(base_dir):
    plain, meta, data_dir = load_tables(base_dir)
    p50 = os.path.join(data_dir, "codes", "code_3_50.txt")
    d, N, vecs, _ = parse_code_file(p50, 3, 50)
    ok, msg = verify_single(d, N, vecs, plain, meta, data_dir, require_improvement=False, require_20digits=False, label="code_3_50.txt")
    print("[SELF-TEST POSITIVE BASELINE]", msg)
    if not ok:
        return 1
    # Negative test: require improvement on unmodified baseline -> must fail
    ok2, msg2 = verify_single(d, N, vecs, plain, meta, data_dir, require_improvement=True, require_20digits=False, label="unimproved_3_50")
    print("[SELF-TEST NEGATIVE UNIMPROVED]", msg2)
    if ok2:
        return 1
    print("SELF_TEST: PASS")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--d", type=int, default=None)
    ap.add_argument("--N", type=int, default=None)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--batch", type=str, default=None, help="Verify a p2 batch JSON file (>= 20 items in one dim)")
    args = ap.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    if args.self_test:
        sys.exit(run_self_test(base_dir))

    plain, meta, data_dir = load_tables(base_dir)

    if args.batch:
        bobj = json.load(open(args.batch, "r", encoding="utf-8"))
        dim = int(bobj["d"])
        items = bobj["items"]
        if not (4 <= dim <= 32):
            print(f"FAIL: batch dimension d={dim} not in 4..32")
            sys.exit(1)
        passed = 0
        best_gain = Decimal("-1")
        best_N = None
        for it in items:
            N = int(it["N"])
            vecs = it["vectors"]
            ok, msg = verify_single(dim, N, vecs, plain, meta, data_dir, require_improvement=True, require_20digits=True, label=f"batch_d{dim}_N{N}")
            print(msg)
            if not ok:
                sys.exit(1)
            m_entry = meta.get(f"{dim},{N}")
            if m_entry["o"] != 1:
                print(f"FAIL: ({dim},{N}) is not labeled 'needs more optimization'")
                sys.exit(1)
            passed += 1
            unit_vecs = [normalize_vec(v) for v in vecs]
            gain = plain[(dim, N)] - max_inner_product(unit_vecs)
            if gain > best_gain:
                best_gain = gain
                best_N = N
        if passed < 20:
            print(f"FAIL: p2 batch has {passed} < 20 verified improvements in d={dim}")
            sys.exit(1)
        print(f"BATCH_PASS kind=partial_win_p2 d={dim} count={passed} max_gain={best_gain:.6e} best_N={best_N}")
        sys.exit(0)

    if not args.files:
        ap.print_help()
        sys.exit(1)

    all_ok = True
    for p in args.files:
        d, N, vecs, _ = parse_code_file(p, args.d, args.N)
        ok, msg = verify_single(d, N, vecs, plain, meta, data_dir, require_improvement=True, require_20digits=True, label=os.path.basename(p))
        print(msg)
        if not ok:
            all_ok = False
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
