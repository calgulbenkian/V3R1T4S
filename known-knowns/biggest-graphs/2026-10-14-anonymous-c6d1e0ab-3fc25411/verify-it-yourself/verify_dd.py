#!/usr/bin/env python3
"""verify_dd.py -- Pure Python 3 (stdlib only) exact all-pairs bitset BFS degree-diameter verifier.

Checks that an edge list is a simple undirected graph (no loops, no duplicate edges, labels 0..N-1)
with maximum degree <= DELTA, all-pairs shortest-path diameter <= D, N <= Moore bound M(DELTA, D),
negative control at D-1 (far_pairs > 0), and strict improvement over the live Comellas table and TROPHY_CASE.md.

Usage:
  python3 verify_dd.py EDGEFILE DELTA D [--table-json data/live_general_cells.json] [--bipartite] [--no-record-check]
"""
import argparse
import json
import os
import sys

TROPHY_BASELINES = {
    "(15,4)": 13365,
    "(15,3)": 1620,
    "(14,4)": 8424,
    "(9,4)": 1700,
    "(13,4)": 6630,
    "(13,6)": 535495,
    "(15,6)": 1424896,
}


def moore_bound(delta: int, d: int) -> int:
    if delta <= 2:
        return 1 + delta * d
    return 1 + delta * ((delta - 1) ** d - 1) // (delta - 2)


def check_bipartite(n: int, adj_lists: list) -> bool:
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        q = [start]
        while q:
            u = q.pop()
            cu = color[u]
            for v in adj_lists[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    q.append(v)
                elif color[v] == cu:
                    return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("edgefile", help="Path to 0-indexed undirected edge list file")
    ap.add_argument("delta", type=int, help="Maximum allowed degree Delta")
    ap.add_argument("diam", type=int, help="Maximum allowed diameter D")
    ap.add_argument("--table-json", default="data/live_general_cells.json", help="Parsed live Comellas table JSON")
    ap.add_argument("--bipartite", action="store_true", help="Also verify graph is bipartite")
    ap.add_argument("--no-record-check", action="store_true", help="Skip strict record improvement check")
    args = ap.parse_args()

    path = args.edgefile
    Delta = args.delta
    D = args.diam

    rows = []
    bad = 0
    loops = 0
    maxv = -1
    with open(path, "r", encoding="utf-8") as fh:
        for ln in fh:
            s = ln.strip()
            if not s or s.startswith("#"):
                continue
            parts = s.split()
            if len(parts) != 2 or not (parts[0].isdigit() and parts[1].isdigit()):
                bad += 1
                continue
            u, v = int(parts[0]), int(parts[1])
            if u == v:
                loops += 1
                continue
            if u > v:
                u, v = v, u
            if v > maxv:
                maxv = v
            rows.append((u, v))

    N = maxv + 1 if rows else 0
    unique_edges = set(rows)
    dup = len(rows) - len(unique_edges)
    adj_lists = [[] for _ in range(N)]
    for u, v in unique_edges:
        adj_lists[u].append(v)
        adj_lists[v].append(u)

    degs = [len(nb) for nb in adj_lists]
    unused = sum(1 for d in degs if d == 0)
    mindeg = min(degs) if N else None
    maxdeg = max(degs) if N else None
    hist = {}
    for d in degs:
        if d > 0:
            hist[d] = hist.get(d, 0) + 1
    hist = {k: hist[k] for k in sorted(hist)}

    mb = moore_bound(Delta, D)
    cell_key = f"({Delta},{D})"
    live_n = None
    live_bold = False
    if args.table_json and os.path.exists(args.table_json):
        cells = json.load(open(args.table_json, "r", encoding="utf-8"))
        if cell_key in cells:
            live_n = int(cells[cell_key]["N"])
            live_bold = bool(cells[cell_key].get("bold", False))
    trophy_n = TROPHY_BASELINES.get(cell_key)
    baseline_to_beat = max([x for x in [live_n, trophy_n] if x is not None], default=None)

    out = {
        "file": os.path.basename(path),
        "file_bytes": os.path.getsize(path),
        "N": N,
        "edges": len(unique_edges),
        "loops": loops,
        "duplicates": dup,
        "unparsable_lines": bad,
        "unused_labels": unused,
        "mindeg": mindeg,
        "maxdeg": maxdeg,
        "DELTA": Delta,
        "D": D,
        "moore_bound": mb,
        "live_table_entry": live_n,
        "live_bold_optimal": live_bold,
        "trophy_case_entry": trophy_n,
        "baseline_to_beat": baseline_to_beat,
        "degree_histogram": hist,
    }

    if bad or loops or dup or unused or N == 0:
        out["valid"] = False
        out["reason"] = "format/loops/duplicates/unused labels"
        print(json.dumps(out))
        sys.exit(1)

    # All-pairs BFS using Python arbitrary-precision integer bitsets in batches of up to 2048 sources
    batch_size = 2048
    within = [0] * (D + 1)
    for s0 in range(0, N, batch_size):
        ns = min(batch_size, N - s0)
        A = [0] * N
        for i in range(ns):
            A[s0 + i] = 1 << i
        within[0] += ns
        for r in range(1, D + 1):
            B = A[:]
            for u in range(N):
                au = B[u]
                for v in adj_lists[u]:
                    au |= A[v]
                B[u] = au
            A = B
            within[r] += sum(bin(x).count("1") for x in A)

    far_d = N * N - within[D]
    far_d_minus_1 = N * N - within[D - 1]
    exact_diam = next((r for r in range(D + 1) if within[r] == N * N), None)

    out["ordered_pairs_within_distance"] = {r: within[r] for r in range(D + 1)}
    out["far_pairs_at_D"] = int(far_d)
    out["far_pairs_at_D_minus_1"] = int(far_d_minus_1)
    out["exact_diameter"] = exact_diam
    out["negative_control_D_minus_1_rejects"] = bool(far_d_minus_1 > 0)

    if args.bipartite:
        out["is_bipartite"] = check_bipartite(N, adj_lists)

    valid_graph = (
        far_d == 0
        and maxdeg <= Delta
        and N <= mb
        and (not args.bipartite or out["is_bipartite"])
    )
    if not args.no_record_check and baseline_to_beat is not None:
        beats_record = (N > baseline_to_beat) and (not live_bold)
        out["beats_record"] = beats_record
        out["margin_over_baseline"] = N - baseline_to_beat
        out["valid"] = bool(valid_graph and beats_record)
    else:
        out["valid"] = bool(valid_graph)

    print(json.dumps(out))
    sys.exit(0 if out["valid"] else 1)


if __name__ == "__main__":
    main()
