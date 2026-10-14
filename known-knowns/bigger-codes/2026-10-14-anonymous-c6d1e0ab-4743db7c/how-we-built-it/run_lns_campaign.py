#!/usr/bin/env python3
"""
Lens 1 (c-evaluator-optimizer) Campaign Driver:
Compiles cwc_lns.c and runs multi-threaded incremental blocker-hypergraph LNS
plateau walks across H1-H8 target cells.
"""
import glob
import os
import re
import subprocess
import sys


def best_file_for_cell(codes_dir, results_dir, n, d, w, init_name):
    best_m = -1
    best_p = os.path.join(codes_dir, init_name)
    pat = os.path.join(results_dir, f"A{n}_{d}_{w}_*.txt")
    for p in glob.glob(pat):
        m = re.search(r"A\d+_\d+_\d+_(\d+)\.txt$", os.path.basename(p))
        if m:
            val = int(m.group(1))
            if val > best_m:
                best_m = val
                best_p = p
    return best_p


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    run_dir = os.path.abspath(os.path.join(here, "..", "..", ".."))
    repo_codes = os.path.abspath(os.path.join(run_dir, "..", "..", "repo", "known-knowns", "bigger-codes", "codes"))
    results_dir = os.path.join(run_dir, "results")
    os.makedirs(results_dir, exist_ok=True)

    c_src = os.path.join(here, "cwc_lns.c")
    c_bin = os.path.join(here, "cwc_lns")
    subprocess.run(["clang", "-O3", "-march=native", "-pthread", c_src, "-o", c_bin], check=True)

    # (hyp, init_file, n, d, w, rounds, kb, rmax, clusters, max4, pf, seed, max_s, switch_kb4)
    jobs = [
        # H1: A(52,8,7) (bar 3799; README notes walk continued to 3802 with KB=3, rmax=8, pf=0.6)
        ("H1a", "A52_8_7_3799.txt", 52, 8, 7, 90, 3, 8, 3000, 10000, 0.60, 101, 45.0, -1),
        ("H1b", "A52_8_7_3799.txt", 52, 8, 7, 90, 3, 9, 4000, 10000, 0.60, 202, 40.0, -1),
        # H2: A(53..56, 8, 7) (bars 3987, 4193, 4426, 4685)
        ("H2", "A53_8_7_3987.txt", 53, 8, 7, 70, 3, 8, 3000, 10000, 0.60, 103, 30.0, -1),
        ("H2", "A54_8_7_4193.txt", 54, 8, 7, 70, 3, 8, 3000, 10000, 0.60, 104, 30.0, -1),
        ("H2", "A55_8_7_4426.txt", 55, 8, 7, 70, 3, 8, 3000, 10000, 0.60, 105, 30.0, -1),
        ("H2", "A56_8_7_4685.txt", 56, 8, 7, 70, 3, 8, 3000, 10000, 0.60, 106, 30.0, -1),
        # H3: Shallow D-preset cells tested with KB=4, rmax=12
        ("H3", "A26_6_8_3603.txt", 26, 6, 8, 60, 4, 12, 8000, 25000, 0.35, 301, 15.0, -1),
        ("H3", "A27_6_9_8325.txt", 27, 6, 9, 60, 4, 12, 8000, 25000, 0.35, 302, 15.0, -1),
        ("H3", "A30_8_8_1166.txt", 30, 8, 8, 60, 4, 12, 8000, 25000, 0.35, 303, 15.0, -1),
        ("H3", "A51_6_5_1785.txt", 51, 6, 5, 60, 4, 12, 8000, 25000, 0.35, 304, 15.0, -1),
        # H4: High-density d=6 D-preset cells tested with KB=4, rmax=12
        ("H4", "A25_6_12_9895.txt", 25, 6, 12, 45, 4, 12, 8000, 25000, 0.35, 401, 15.0, -1),
        ("H4", "A26_6_11_12222.txt", 26, 6, 11, 45, 4, 12, 8000, 25000, 0.35, 402, 15.0, -1),
        # H8: Short P20k cells tested with extended C runs
        ("H8", "A27_8_10_1737.txt", 27, 8, 10, 50, 4, 12, 8000, 25000, 0.35, 501, 14.0, -1),
        ("H8", "A35_6_6_2217.txt", 35, 6, 6, 50, 4, 12, 8000, 25000, 0.35, 502, 14.0, -1),
        ("H8", "A45_8_7_1907.txt", 45, 8, 7, 50, 3, 10, 5000, 15000, 0.50, 503, 15.0, -1),
        ("H8", "A58_6_5_2684.txt", 58, 6, 5, 50, 4, 12, 8000, 25000, 0.35, 504, 14.0, -1),
    ]

    print("=== LENS 1: C-EVALUATOR-OPTIMIZER CAMPAIGN LOG ===", flush=True)
    for hyp, init_fn, n, d, w, rnds, kb, rmax, ncl, max4, pf, seed, max_s, sw_kb4 in jobs:
        seed_path = best_file_for_cell(repo_codes, results_dir, n, d, w, init_fn)
        print(f"\n--- [{hyp}] Running A({n},{d},{w}) from {os.path.basename(seed_path)} ---", flush=True)
        cmd = [
            c_bin,
            seed_path,
            str(n),
            str(d),
            str(w),
            results_dir,
            str(rnds),
            str(kb),
            str(rmax),
            str(ncl),
            str(max4),
            f"{pf:.2f}",
            str(seed),
            f"{max_s:.1f}",
            str(sw_kb4),
        ]
        subprocess.run(cmd, check=True)

    found = sorted(os.path.basename(p) for p in glob.glob(os.path.join(results_dir, "A*.txt")))
    print(f"\n=== CAMPAIGN COMPLETE: {len(found)} new record files in results/ ===", flush=True)
    for fn in found:
        print(f"  RECORD_FILE: {fn}", flush=True)


if __name__ == "__main__":
    main()
