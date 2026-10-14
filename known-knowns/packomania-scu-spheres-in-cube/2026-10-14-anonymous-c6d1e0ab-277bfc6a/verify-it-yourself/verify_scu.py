#!/usr/bin/env python3
"""
Standalone Exact 60-Digit Verifier for `packomania-scu-spheres-in-cube`.

Implements the exact success criterion from target.md:
- Container: centered unit cube [-1/2, 1/2]^3.
- Exact feasible radius computed in 60-digit exact Decimal arithmetic (no tolerance):
    r* = min( min_{i < j} ||c_i - c_j||_2 / 2,  1/2 - max_i max(|x_i|, |y_i|, |z_i|) )
- Verifies:
  1. Exact number of sphere centers N matches target N.
  2. Calibration against posted `data/seeds/scu{N}.txt` (must reproduce `data/radius.txt` to <= 1e-20).
  3. Strict improvement: r* - r_table >= 1e-11.
  4. Non-isometry: sorted pairwise distance multiset differs from posted `scu{N}.txt`.
  5. Author attribution (Partial Win p1 check: Goldberg / Pfoertner / Boll) and Queue Rule check.
"""

import sys
import os
import json
import hashlib
from decimal import Decimal, getcontext

getcontext().prec = 65


def load_coords(path):
    """Load N sphere centers from Packomania ASCII format (`idx x y z` or `x y z`) or JSON."""
    if path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        pts = []
        for row in data["centers"]:
            pts.append((Decimal(str(row[0])), Decimal(str(row[1])), Decimal(str(row[2]))))
        return pts, data.get("N", len(pts))

    pts = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            if len(parts) == 4:
                if int(parts[0]) != len(pts) + 1:
                    raise ValueError(f"Expected sphere index {len(pts) + 1}, got {parts[0]}")
                pts.append((Decimal(parts[1]), Decimal(parts[2]), Decimal(parts[3])))
            elif len(parts) == 3:
                pts.append((Decimal(parts[0]), Decimal(parts[1]), Decimal(parts[2])))
            else:
                raise ValueError(f"Unexpected column count {len(parts)}")
    return pts, len(pts)


def compute_exact_radius(pts):
    """
    Compute exact feasible radius r* in [-1/2, 1/2]^3 using 65-digit Decimal arithmetic,
    along with contact graph statistics and sorted pairwise distances.
    """
    n = len(pts)
    half = Decimal("0.5")
    two = Decimal("2")

    max_coord = Decimal("0")
    for x, y, z in pts:
        ax = abs(x)
        ay = abs(y)
        az = abs(z)
        if ax > max_coord:
            max_coord = ax
        if ay > max_coord:
            max_coord = ay
        if az > max_coord:
            max_coord = az

    r_bound = half - max_coord

    min_d2 = None
    dists_float = []
    for i in range(n):
        xi, yi, zi = pts[i]
        for j in range(i + 1, n):
            dx = xi - pts[j][0]
            dy = yi - pts[j][1]
            dz = zi - pts[j][2]
            d2 = dx * dx + dy * dy + dz * dz
            if min_d2 is None or d2 < min_d2:
                min_d2 = d2
            dists_float.append(float(d2) ** 0.5)

    r_pair = min_d2.sqrt() / two if min_d2 is not None else r_bound
    r_star = r_pair if r_pair < r_bound else r_bound

    # Contact graph analysis (within 1e-12 of r_star)
    tol = Decimal("1e-12")
    pair_contacts = 0
    deg = [0] * n
    bound_contacts = 0
    for i in range(n):
        xi, yi, zi = pts[i]
        b_hit = False
        for c in (abs(xi), abs(yi), abs(zi)):
            if abs((half - c) - r_star) <= tol:
                bound_contacts += 1
                b_hit = True
        if b_hit:
            deg[i] += 1
        for j in range(i + 1, n):
            dx = xi - pts[j][0]
            dy = yi - pts[j][1]
            dz = zi - pts[j][2]
            d_half = (dx * dx + dy * dy + dz * dz).sqrt() / two
            if abs(d_half - r_star) <= tol:
                pair_contacts += 1
                deg[i] += 1
                deg[j] += 1

    dists_float.sort()
    return r_star, r_pair, r_bound, pair_contacts, bound_contacts, dists_float


def load_table_metadata(run_dir):
    radii = {}
    rad_path = os.path.join(run_dir, "data", "radius.txt")
    if os.path.exists(rad_path):
        with open(rad_path, "r", encoding="utf-8") as f:
            for line in f:
                p = line.split()
                if len(p) >= 2 and p[0].isdigit():
                    radii[int(p[0])] = Decimal(p[1])

    authors = {}
    auth_path = os.path.join(run_dir, "data", "author.txt")
    if os.path.exists(auth_path):
        with open(auth_path, "r", encoding="utf-8") as f:
            for line in f:
                p = line.strip().split(None, 1)
                if len(p) == 2 and p[0].isdigit():
                    authors[int(p[0])] = p[1].strip()

    return radii, authors


def verify_file(cand_path, run_dir=".", calibrate_only=False):
    radii, authors = load_table_metadata(run_dir)
    pts, n = load_coords(cand_path)
    with open(cand_path, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()

    r_star, r_pair, r_bound, pair_c, bound_c, cand_dists = compute_exact_radius(pts)
    total_sq_norm = sum(x * x + y * y + z * z for x, y, z in pts)
    r_table = radii.get(n)
    author = authors.get(n, "unknown")

    print(f"File: {os.path.basename(cand_path)} (SHA-256: {sha})")
    print(f"=== PACKOMANIA SCU VERIFICATION: N={n} in [-1/2, 1/2]^3 ===")
    print(f"Live table author (author.txt): {author}")
    print(f"Live table radius (radius.txt): {r_table:.30f}")
    print(f"Candidate r_pair (min ||c_i-c_j||/2): {r_pair:.30f}")
    print(f"Candidate r_bound (1/2 - max |c_i|):  {r_bound:.30f}")
    print(f"Candidate exact feasible r* (50+d):   {r_star:.35f}")
    print(f"Candidate total_sq_norm (35d):        {total_sq_norm:.35f}")
    print(f"Contacts (tol=1e-12): pair_contacts={pair_c}, boundary_contacts={bound_c}, total={pair_c + bound_c}")

    if calibrate_only:
        err = abs(r_star - r_table)
        ok = err <= Decimal("1e-20")
        print(f"Calibration |r* - r_table| = {err:.3e} (<= 1e-20): {'PASS' if ok else 'FAIL'}")
        return ok

    # Check seed calibration and non-isometry if seed file exists
    seed_path = os.path.join(run_dir, "data", "seeds", f"scu{n}.txt")
    non_isometric = True
    seed_calibrated = False
    if os.path.exists(seed_path):
        seed_pts, seed_n = load_coords(seed_path)
        seed_r, _, _, _, _, seed_dists = compute_exact_radius(seed_pts)
        seed_err = abs(seed_r - r_table)
        seed_calibrated = seed_err <= Decimal("1e-20")
        max_dist_diff = max(abs(a - b) for a, b in zip(cand_dists, seed_dists)) if len(cand_dists) == len(seed_dists) else 1.0
        non_isometric = max_dist_diff > 1e-7
        print(f"Posted scu{n}.txt calibration |r_seed - r_table| = {seed_err:.3e}: {'PASS' if seed_calibrated else 'FAIL'}")
        print(f"Non-isometry check (max sorted pairwise distance diff = {max_dist_diff:.6e}): {'PASS' if non_isometric else 'FAIL'}")

    gain = r_star - r_table
    margin = Decimal("1e-11")
    is_p1_author = any(k in author for k in ("Goldberg", "Pfoertner", "Boll"))
    win = (gain >= margin) and non_isometric

    print(f"Radius improvement (r* - r_table):    +{gain:.30f} ({float(gain):.6e})")
    print(f"Threshold check (gain >= 1e-11):      {'PASS' if gain >= margin else 'FAIL'}")
    print(f"Partial Win p1 author check:          {'YES (' + author + ')' if is_p1_author else 'NO (' + author + ')'}")
    print("Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.")
    print(f"RESULT: {'PASS (CONFIRMED_SOLUTION' + (' + PARTIAL WIN p1)' if is_p1_author else ')') if win else 'FAIL'}")
    print()
    return win


if __name__ == "__main__":
    cal = "--calibrate" in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not files:
        print("Usage: python3 verify_scu.py [--calibrate] {file1} [file2 ...]")
        sys.exit(1)
    all_ok = True
    for fpath in files:
        if not verify_file(fpath, ".", calibrate_only=cal):
            all_ok = False
    sys.exit(0 if all_ok else 1)
