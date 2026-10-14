#!/usr/bin/env python3
"""
Standalone 50-digit exact verifier and coordinate-archive auditor for
Packomania 4D/5D/6D hypersphere packings (hsp4, hsp5, hsp6).

Computes in 65-digit exact Decimal arithmetic:
    r* = min( min_{i < j} |c_i - c_j|_2 / 2,  1 - max_i |c_i|_2 )
Checks:
  1. Dimension d in {4, 5, 6} and sphere count N.
  2. Exact feasible radius r* to 50 decimal places (reported to 25 digits).
  3. Comparison against live/downloaded data/hsp<d>/radius.txt:
     requires r* - r_table >= 1e-10 for a new record.
  4. Non-isometry against posted data/coords/hsp<d>/hsp<d>-<N>.txt:
     requires max absolute difference between sorted pairwise-distance multisets > 1e-8.
  5. Contact-graph and data-integrity audit (--audit) across all listed rows.
"""

import argparse
import math
import os
import sys
from decimal import Decimal, getcontext

getcontext().prec = 65


def parse_hsp_file(path, expected_d=None, expected_n=None, allow_pad_truncated=False):
    """
    Parse a Packomania hsp<d>-<N>.txt file or plain coordinate file.
    Supports:
      - Optional first line containing single float (posted header radius)
      - N lines of either:
          idx x_1 ... x_d   (1-indexed integer idx followed by d coordinates)
        or:
          x_1 ... x_d       (d coordinates)
    Returns (header_r_or_None, dec_centers, flt_centers, raw_dim).
    """
    with open(path, "r") as f:
        raw_lines = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]

    if not raw_lines:
        raise ValueError(f"Empty coordinate file: {path}")

    header_r = None
    first_tokens = raw_lines[0].split()
    if len(first_tokens) == 1:
        header_r = Decimal(first_tokens[0])
        coord_lines = raw_lines[1:]
    elif len(first_tokens) == 2 and first_tokens[0].isdigit() and "." in first_tokens[1]:
        header_r = Decimal(first_tokens[1])
        coord_lines = raw_lines[1:]
    else:
        coord_lines = raw_lines

    dec_centers = []
    flt_centers = []
    raw_dims = set()
    for line_idx, ln in enumerate(coord_lines, start=1):
        toks = ln.split()
        # Strip leading 1-based integer index if present
        if toks and toks[0].isdigit() and int(toks[0]) == line_idx and "." not in toks[0]:
            if expected_d is None or len(toks) != expected_d:
                coords_str = toks[1:]
            else:
                # Ambiguous only if file has no index and first coordinate is integer line_idx,
                # which never happens for sphere coordinates inside unit ball (|x| < 1).
                coords_str = toks[1:]
        else:
            coords_str = toks

        raw_d = len(coords_str)
        raw_dims.add(raw_d)
        if expected_d is not None and raw_d != expected_d:
            if allow_pad_truncated and raw_d < expected_d:
                coords_str = list(coords_str) + ["0"] * (expected_d - raw_d)
            else:
                raise ValueError(
                    f"Dimension mismatch on line {line_idx} of {path}: expected d={expected_d}, got {raw_d} coordinates"
                )
        dec_centers.append([Decimal(x) for x in coords_str])
        flt_centers.append([float(x) for x in coords_str])

    if not dec_centers:
        raise ValueError(f"No coordinates parsed from {path}")
    if len(raw_dims) != 1:
        raise ValueError(f"Inconsistent coordinate column counts {raw_dims} in {path}")
    raw_dim = next(iter(raw_dims))
    if expected_n is not None and len(dec_centers) != expected_n:
        raise ValueError(f"Sphere count mismatch in {path}: expected N={expected_n}, got N={len(dec_centers)}")

    return header_r, dec_centers, flt_centers, raw_dim


def compute_exact_radius(dec_centers, flt_centers=None):
    """
    Compute exact 65-digit Decimal feasible radius:
        r* = min( min_{i < j} |c_i - c_j|_2 / 2,  1 - max_i |c_i|_2 )
    """
    n = len(dec_centers)
    d = len(dec_centers[0])

    max_sq_norm = Decimal(0)
    max_norm_idx = 0
    for i, c in enumerate(dec_centers):
        sq = sum(x * x for x in c)
        if sq > max_sq_norm:
            max_sq_norm = sq
            max_norm_idx = i
    max_norm = max_sq_norm.sqrt()
    r_wall = Decimal(1) - max_norm

    if flt_centers is None or n <= 60:
        min_sq_dist = None
        min_pair = (0, 1)
        for i in range(n):
            ci = dec_centers[i]
            for j in range(i + 1, n):
                cj = dec_centers[j]
                sq = sum((ci[k] - cj[k]) * (ci[k] - cj[k]) for k in range(d))
                if min_sq_dist is None or sq < min_sq_dist:
                    min_sq_dist = sq
                    min_pair = (i, j)
    else:
        f_min_sq = float("inf")
        pair_sq = []
        for i in range(n):
            ci = flt_centers[i]
            for j in range(i + 1, n):
                cj = flt_centers[j]
                sq = sum((ci[k] - cj[k]) * (ci[k] - cj[k]) for k in range(d))
                if sq < f_min_sq:
                    f_min_sq = sq
                pair_sq.append((sq, i, j))
        thresh = f_min_sq * 1.0001 + 1e-9
        min_sq_dist = None
        min_pair = (0, 1)
        for sq_f, i, j in pair_sq:
            if sq_f <= thresh:
                ci = dec_centers[i]
                cj = dec_centers[j]
                sq = sum((ci[k] - cj[k]) * (ci[k] - cj[k]) for k in range(d))
                if min_sq_dist is None or sq < min_sq_dist:
                    min_sq_dist = sq
                    min_pair = (i, j)

    min_half_dist = min_sq_dist.sqrt() / Decimal(2)
    r_star = min_half_dist if min_half_dist <= r_wall else r_wall
    return {
        "r_star": r_star,
        "r_pair": min_half_dist,
        "r_wall": r_wall,
        "min_pair": min_pair,
        "max_norm_idx": max_norm_idx,
    }


def compute_contact_stats(flt_centers, r_flt, tol=1e-7):
    n = len(flt_centers)
    d = len(flt_centers[0])
    deg = [0] * n
    wall_contacts = 0
    pair_contacts = 0
    for i in range(n):
        norm = math.sqrt(sum(x * x for x in flt_centers[i]))
        if abs((1.0 - norm) - r_flt) <= tol:
            wall_contacts += 1
            deg[i] += 1
        for j in range(i + 1, n):
            dist = math.sqrt(sum((flt_centers[i][k] - flt_centers[j][k]) ** 2 for k in range(d)))
            if abs(0.5 * dist - r_flt) <= tol:
                pair_contacts += 1
                deg[i] += 1
                deg[j] += 1
    rattlers = sum(1 for x in deg if x <= d)
    return wall_contacts, pair_contacts, rattlers


def sorted_pairwise_distances(flt_centers):
    n = len(flt_centers)
    d = len(flt_centers[0])
    dists = []
    for i in range(n):
        ci = flt_centers[i]
        for j in range(i + 1, n):
            cj = flt_centers[j]
            dists.append(math.sqrt(sum((ci[k] - cj[k]) ** 2 for k in range(d))))
    dists.sort()
    return dists


def load_table_radii(data_dir, d):
    path = os.path.join(data_dir, f"hsp{d}", "radius.txt")
    radii = {}
    if os.path.exists(path):
        with open(path, "r") as f:
            for ln in f:
                toks = ln.split()
                if len(toks) >= 2 and toks[0].isdigit():
                    radii[int(toks[0])] = Decimal(toks[1])
    return radii


def load_table_authors(data_dir, d):
    path = os.path.join(data_dir, f"hsp{d}", "author.txt")
    authors = {}
    if os.path.exists(path):
        with open(path, "r") as f:
            for ln in f:
                ln = ln.strip()
                if not ln:
                    continue
                parts = ln.split(None, 1)
                if len(parts) == 2 and parts[0].isdigit():
                    authors[int(parts[0])] = parts[1].strip()
    return authors


def run_audit(data_dir):
    print("=== FULL 50-DIGIT ARCHIVE & CONTACT-GRAPH AUDIT (hsp4, hsp5, hsp6) ===")
    for d in (4, 5, 6):
        radii = load_table_radii(data_dir, d)
        authors = load_table_authors(data_dir, d)
        missing_files = []
        dim_truncated = []
        discrepancies_gt_2e12 = []
        rounding_diffs = []
        plateaus = []
        non_specht = []
        n_list = sorted(radii.keys())
        for idx, n in enumerate(n_list):
            r_tab = radii[n]
            auth = authors.get(n, "unknown")
            if "Specht" not in auth:
                non_specht.append((n, r_tab, auth))
            if idx + 1 < len(n_list) and radii[n_list[idx + 1]] >= r_tab:
                plateaus.append((n, n_list[idx + 1], r_tab, radii[n_list[idx + 1]], auth))
            cpath = os.path.join(data_dir, "coords", f"hsp{d}", f"hsp{d}-{n}.txt")
            if not os.path.exists(cpath):
                missing_files.append((n, r_tab, auth))
                continue
            hdr_r, dec_c, flt_c, raw_d = parse_hsp_file(
                cpath, expected_d=d, expected_n=n, allow_pad_truncated=True
            )
            res = compute_exact_radius(dec_c, flt_c)
            diff = res["r_star"] - r_tab
            if raw_d != d:
                dim_truncated.append((n, raw_d, r_tab, res["r_star"], diff, auth))
            elif abs(diff) > Decimal("2e-12") or (hdr_r is not None and hdr_r != r_tab):
                discrepancies_gt_2e12.append((n, r_tab, hdr_r, res["r_star"], diff, auth))
            elif abs(diff) > Decimal("0.5e-12"):
                rounding_diffs.append((n, r_tab, res["r_star"], diff, auth))

        print(f"\n--- hsp{d} (listed N={min(n_list)}..{max(n_list)}, count={len(n_list)}) ---")
        print(f"  Missing coordinate files in tarball: {len(missing_files)}")
        for n, rt, au in missing_files:
            print(f"    [MISSING FILE] hsp{d}-{n}.txt (table r={rt}, author={au})")
        print(f"  Dimension-truncated coordinate files (raw_d != {d}): {len(dim_truncated)}")
        for n, rd, rt, rs, df, au in dim_truncated[:10]:
            print(f"    [DIM-TRUNCATED] N={n:3d}: raw_d={rd} (expected {d}), r_tab={rt}, 4D-projected r*={rs:.12f} (diff={df:+.3e})")
        if len(dim_truncated) > 10:
            print(f"    ... ({len(dim_truncated)} total files in hsp{d}_coords.tar.gz have raw_d={dim_truncated[0][1]} instead of {d})")
        print(f"  Full-dimension coordinate discrepancies (|r* - r_tab| > 2e-12): {len(discrepancies_gt_2e12)}")
        for n, rt, hr, rs, df, au in discrepancies_gt_2e12:
            print(f"    [DISCREPANCY] N={n:3d}: r_tab={rt} hdr_r={hr} r*={rs:.18f} diff={df:+.3e} ({au})")
        print(f"  12th-decimal last-ulp rounding deficits (0.5e-12 < |r* - r_tab| <= 2e-12): {len(rounding_diffs)}")
        if rounding_diffs:
            worst = min(rounding_diffs, key=lambda x: x[3])
            print(f"    Worst rounding deficit: N={worst[0]} r_tab={worst[1]} r*={worst[2]:.18f} diff={worst[3]:+.3e} ({worst[4]})")
        print(f"  Monotone plateau pairs (r(N) <= r(N+1)): {len(plateaus)}")
        for n1, n2, r1, r2, au in plateaus:
            print(f"    [PLATEAU] N={n1}->{n2}: r({n1})={r1} <= r({n2})={r2} ({au})")
        print(f"  Non-Specht rows: {len(non_specht)}")
        for n, rt, au in non_specht:
            print(f"    [NON-SPECHT] N={n:3d}: r={rt} author='{au}'")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", nargs="?", help="Coordinate file to verify")
    ap.add_argument("--dim", type=int, default=None, help="Dimension d in {4, 5, 6}")
    ap.add_argument("--n", type=int, default=None, help="Sphere count N")
    ap.add_argument("--data-dir", default="data", help="Directory containing hsp4/5/6 tables and coords")
    ap.add_argument("--audit", action="store_true", help="Run full archive audit across hsp4, hsp5, hsp6")
    ap.add_argument("--calibrate", action="store_true", help="Run parser calibration on sample posted files")
    args = ap.parse_args()

    if args.calibrate:
        for d, n in [(4, 2), (4, 9), (4, 10), (4, 12), (4, 19), (4, 20), (4, 24), (4, 25), (4, 100), (4, 121), (4, 300)]:
            radii = load_table_radii(args.data_dir, d)
            cpath = os.path.join(args.data_dir, "coords", f"hsp{d}", f"hsp{d}-{n}.txt")
            hdr_r, dec_c, flt_c, raw_d = parse_hsp_file(cpath, expected_d=d, expected_n=n)
            res = compute_exact_radius(dec_c, flt_c)
            diff = res["r_star"] - radii[n]
            assert abs(diff) <= Decimal("1e-11"), f"Calibration failed on hsp{d}-{n}: diff={diff}"
            print(f"[CALIBRATE OK] hsp{d}-{n:3d} (raw_d={raw_d}): r_tab={radii[n]} r*={res['r_star']:.20f} diff={diff:+.3e}")
        return

    if args.audit:
        run_audit(args.data_dir)
        return

    if not args.input:
        ap.error("Provide a coordinate file or --calibrate / --audit")

    hdr_r, dec_c, flt_c, raw_d = parse_hsp_file(
        args.input, expected_d=args.dim, expected_n=args.n, allow_pad_truncated=False
    )
    d = len(dec_c[0])
    n = len(dec_c)
    res = compute_exact_radius(dec_c, flt_c)
    r_star = res["r_star"]
    if hdr_r is not None and abs(r_star - hdr_r) > Decimal("1e-15"):
        raise ValueError(f"Header radius {hdr_r} does not match exact computed radius {r_star:.25f}")
    total_sq_norm = sum(sum(x * x for x in c) for c in dec_c)
    wc, pc, rat = compute_contact_stats(flt_c, float(r_star))

    print(f"VALID PACKING: d={d} N={n}")
    print(f"  r* (25 digits) = {r_star:.25f}")
    print(f"  r_pair         = {res['r_pair']:.25f} (pair {res['min_pair']})")
    print(f"  r_wall         = {res['r_wall']:.25f} (sphere {res['max_norm_idx']})")
    print(f"  total_sq_norm  = {total_sq_norm:.25f}")
    print(f"  contacts       = {wc} wall, {pc} pair, {rat} rattlers (tol=1e-7)")

    radii = load_table_radii(args.data_dir, d)
    authors = load_table_authors(args.data_dir, d)
    if n in radii:
        r_tab = radii[n]
        gain = r_star - r_tab
        auth = authors.get(n, "unknown")
        print(f"  r_table(d={d}, N={n}) = {r_tab:.12f} (author: {auth})")
        print(f"  gain (r* - r_table)  = {gain:+.25f} ({float(gain):+.6e})")

        ref_path = os.path.join(args.data_dir, "coords", f"hsp{d}", f"hsp{d}-{n}.txt")
        if os.path.exists(ref_path):
            _, _, ref_flt, ref_raw_d = parse_hsp_file(
                ref_path, expected_d=d, expected_n=n, allow_pad_truncated=True
            )
            d1 = sorted_pairwise_distances(flt_c)
            d2 = sorted_pairwise_distances(ref_flt)
            max_dist_diff = max(abs(a - b) for a, b in zip(d1, d2)) if d1 else 0.0
            print(f"  max sorted pairwise-distance diff vs posted hsp{d}-{n}.txt (raw_d={ref_raw_d}) = {max_dist_diff:.6e}")
            is_non_isometric = max_dist_diff > 1e-8
            print(f"  non_isometric (> 1e-8) = {is_non_isometric}")
        else:
            is_non_isometric = True
            print(f"  [NOTE] No posted reference file {ref_path} in tarball")

        if gain >= Decimal("1e-10") and is_non_isometric:
            print(f"  >>> RECORD CONFIRMED: beats live table by {float(gain):.6e} >= 1e-10 and is non-isometric! <<<")
        else:
            print(f"  [INFO] Does not meet strict record gate (gain >= 1e-10: {gain >= Decimal('1e-10')}, non_isometric: {is_non_isometric})")
            sys.exit(2)
    else:
        print(f"  [EXTENSION ROW] N={n} is beyond the listed table range for hsp{d}")


if __name__ == "__main__":
    main()
