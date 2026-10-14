#!/usr/bin/env python3
"""
Standalone Exact Verifier for Binary Constant-Weight Codes A(n, d, w):
  python3 verify_cwc.py <code_file> [n d w] [--calibrate-tie]

Checks:
  1. Format (F): every codeword line has length n and characters in {'0', '1'}.
  2. Weight & Distinctness (W): every codeword has exact Hamming weight w, and all M words are distinct.
  3. All-Pairs Distance (A): all M(M-1)/2 pairs have Hamming distance >= d (exact distance histogram).
  4. Steiner t-Subset Packing (B): for t = w - d/2 + 1, all M * C(w, t) t-subsets of 1-bits are pairwise distinct.
  5. Record Comparison (R): compares M against max(Andw.html(n,d,w), Andw.html(n,d,n-w), arXiv, TROPHY_CASE.md, open PRs).
"""
import hashlib
import itertools
import json
import os
import re
import subprocess
import sys

# Existing TROPHY_CASE.md + Open PR bars (where higher than Andw.html)
KNOWN_BARS = {
    (25, 6, 11): 8718,
    (25, 6, 12): 9895,
    (26, 6, 8): 3603,
    (26, 6, 9): 5986,
    (26, 6, 11): 12222,
    (26, 6, 13): 16225,
    (27, 6, 9): 8325,
    (27, 6, 10): 13026,  # Open PR #28
    (27, 8, 10): 1737,
    (27, 8, 11): 2421,
    (28, 8, 9): 1406,
    (28, 8, 11): 3785,
    (28, 8, 12): 4962,
    (28, 8, 14): 6359,
    (29, 6, 10): 25974,
    (29, 6, 11): 41219,
    (29, 6, 12): 61823,
    (30, 8, 8): 1166,
    (33, 8, 8): 1809,
    (34, 8, 7): 603,     # Open PR #8 (603 > TROPHY_CASE 602)
    (34, 8, 8): 1965,
    (35, 6, 6): 2217,
    (45, 8, 7): 1907,
    (51, 6, 5): 1785,
    (51, 6, 6): 11184,
    (52, 8, 7): 3799,
    (53, 8, 7): 3987,
    (54, 8, 7): 4193,
    (55, 8, 7): 4426,
    (56, 8, 7): 4685,
    (58, 6, 5): 2684,
}

C_HELPER_SRC = r"""
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(void) {
    int M, n, d, w;
    if (scanf("%d %d %d %d", &M, &n, &d, &w) != 4) return 2;
    uint64_t *words = (uint64_t *)malloc((size_t)M * sizeof(uint64_t));
    if (!words) return 2;
    for (int i = 0; i < M; i++) {
        unsigned long long x;
        if (scanf("%llu", &x) != 1) return 2;
        words[i] = (uint64_t)x;
    }
    int max_ov = w - d / 2;
    int min_dist = n + 1;
    long long bad_pairs = 0;
    long long hist[65] = {0};
    for (int i = 0; i < M; i++) {
        uint64_t xi = words[i];
        for (int j = i + 1; j < M; j++) {
            int ov = __builtin_popcountll(xi & words[j]);
            int dist = 2 * (w - ov);
            if (dist >= 0 && dist <= 64) hist[dist]++;
            if (dist < min_dist) min_dist = dist;
            if (ov > max_ov) bad_pairs++;
        }
    }
    printf("%d %lld", min_dist, bad_pairs);
    for (int k = 0; k <= n; k++) {
        if (hist[k] > 0) printf(" %d:%lld", k, hist[k]);
    }
    printf("\n");
    free(words);
    return 0;
}
"""


def get_c_helper():
    here = os.path.dirname(os.path.abspath(__file__))
    c_bin = os.path.join(here, ".c_verify_cwc")
    c_src = os.path.join(here, ".c_verify_cwc.c")
    if not os.path.exists(c_bin):
        try:
            with open(c_src, "w", encoding="utf-8") as f:
                f.write(C_HELPER_SRC)
            subprocess.run(["clang", "-O3", "-march=native", c_src, "-o", c_bin], check=True)
        except Exception:
            return None
    return c_bin


def load_bar(n, d, w):
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, "data", "brouwer_cells.json"),
        os.path.join(here, "..", "data", "brouwer_cells.json"),
    ]
    brouwer_lb = 0
    for p in candidates:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                cells = json.load(f)
            for k in (f"{n},{d},{w}", f"{n},{d},{n - w}"):
                if k in cells and cells[k].get("lb") is not None:
                    brouwer_lb = max(brouwer_lb, int(cells[k]["lb"]))
            break
    trophy_lb = max(KNOWN_BARS.get((n, d, w), 0), KNOWN_BARS.get((n, d, n - w), 0))
    return max(brouwer_lb, trophy_lb), brouwer_lb, trophy_lb


def main():
    calibrate_tie = "--calibrate-tie" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("Usage: python3 verify_cwc.py <code_file> [n d w] [--calibrate-tie]")
        sys.exit(2)

    path = args[0]
    m_fn = re.search(r"A(\d+)_(\d+)_(\d+)_(\d+)\.txt$", os.path.basename(path))
    if len(args) >= 4:
        n, d, w = int(args[1]), int(args[2]), int(args[3])
    elif m_fn:
        n, d, w = int(m_fn.group(1)), int(m_fn.group(2)), int(m_fn.group(3))
    else:
        print("ERROR: Provide n d w on command line or use filename A<n>_<d>_<w>_<M>.txt")
        sys.exit(2)

    M_claim = int(m_fn.group(4)) if m_fn else None

    if d % 2 != 0 or not (1 <= w <= n <= 64):
        print(f"INVALID_PARAMETERS: n={n} d={d} w={w}")
        sys.exit(1)

    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    raw_lines = [ln.strip() for ln in raw.decode("utf-8", errors="replace").splitlines() if ln.strip()]

    if raw_lines and " " in raw_lines[0]:
        parts = raw_lines[0].split()
        if len(parts) >= 3 and all(p.isdigit() for p in parts[:3]):
            raw_lines = raw_lines[1:]

    M = len(raw_lines)
    bad_fmt = 0
    words = []
    for ln in raw_lines:
        if len(ln) != n or any(c not in ("0", "1") for c in ln):
            bad_fmt += 1
        else:
            words.append(int(ln, 2))

    ok = True
    print(f"file={os.path.basename(path)} sha256={sha}")
    print(f"F format: lines={M} claimed_M={M_claim} bad_lines={bad_fmt}")
    if bad_fmt > 0 or M == 0 or (M_claim is not None and M != M_claim):
        ok = False

    bad_w = sum(1 for x in words if bin(x).count("1") != w)
    distinct = len(set(words))
    print(f"W weight/distinct: bad_weight={bad_w} distinct={distinct}")
    if bad_w > 0 or distinct != M:
        ok = False

    # Route B: Exact t-subset packing check (t = w - d/2 + 1)
    t = w - d // 2 + 1
    seen = set()
    total_sub = 0
    for x in words:
        pos = [i for i in range(n) if (x >> i) & 1]
        for comb in itertools.combinations(pos, t):
            mm = 0
            for p in comb:
                mm |= 1 << p
            seen.add(mm)
            total_sub += 1
    collisions = total_sub - len(seen)
    print(f"B packing: t={t} subsets={total_sub} distinct={len(seen)} collisions={collisions}")
    if collisions != 0:
        ok = False

    # Route A: All-pairs Hamming distance check (all M(M-1)/2 pairs)
    Mw = len(words)
    c_bin = get_c_helper()
    min_dist = n + 1
    bad_pairs = 0
    hist_dict = {}
    if c_bin and Mw > 0:
        inp = f"{Mw} {n} {d} {w}\n" + "\n".join(str(x) for x in words) + "\n"
        proc = subprocess.run([c_bin], input=inp, text=True, capture_output=True, check=True)
        parts = proc.stdout.strip().split()
        min_dist = int(parts[0])
        bad_pairs = int(parts[1])
        for kv in parts[2:]:
            k_s, v_s = kv.split(":")
            hist_dict[int(k_s)] = int(v_s)
    else:
        max_ov = w - d // 2
        for i in range(Mw):
            xi = words[i]
            for j in range(i + 1, Mw):
                ov = bin(xi & words[j]).count("1")
                dist = 2 * (w - ov)
                hist_dict[dist] = hist_dict.get(dist, 0) + 1
                if dist < min_dist:
                    min_dist = dist
                if ov > max_ov:
                    bad_pairs += 1
    npairs = Mw * (Mw - 1) // 2
    print(f"A all-pairs: words={Mw} pairs={npairs} min_distance={min_dist} need>={d} bad_pairs={bad_pairs} histogram={hist_dict}")
    if bad_pairs > 0 or min_dist < d:
        ok = False

    bar, brouwer_lb, trophy_lb = load_bar(n, d, w)
    strict_beat = ok and (M > bar)
    tie_or_beat = ok and (M >= bar)
    print(f"R record_check: cell=A({n},{d},{w}) M={M} composite_bar={bar} (Andw={brouwer_lb}, Trophy/PR={trophy_lb}) strict_beat={strict_beat}")
    print(f"VERDICT: {'VALID' if ok else 'INVALID'}  A({n},{d},{w}) >= {M}")

    if calibrate_tie:
        sys.exit(0 if tie_or_beat else 1)
    sys.exit(0 if strict_beat else 1)


if __name__ == "__main__":
    main()
