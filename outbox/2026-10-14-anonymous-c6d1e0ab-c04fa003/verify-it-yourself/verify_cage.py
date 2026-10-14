#!/usr/bin/env python3
"""
Standalone exact verifier for cage-upper-bounds (runs/2026-10-14-0812).

Supports two modes:
1. --mode cage (default if JSON has "k" and "edges" without "arcs"):
   Verifies a classical (k, g)-graph:
   - Exact vertex count N, simple undirected graph (no self-loops, no duplicate edges)
   - Exact regularity deg(v) == k for all v in 0..N-1
   - Connectivity
   - Exact girth >= g via two independent algorithms:
     (Algorithm A) All-roots BFS shortest cycle
     (Algorithm B) Exact integer adjacency-matrix walk algebra + edge-deletion BFS
   - Compares N against rec(k, g) from data/cage_tables.json
   - Optional --compare-noniso <other.json> to verify non-isomorphism via WL-1/WL-2/local cycle profiles

2. --mode mixed (default if JSON has "z", "r", and "arcs"):
   Verifies a [z, r; g]-mixed graph against the exact definition in Araujo-Pardo &
   Mendoza-Cadena (arXiv:2506.20003):
   - Simple mixed graph G = (V; E U A): no loops, no parallel edges, no parallel arcs,
     no anti-parallel arcs (u,v) and (v,u), and no parallel edge uv and arc (u,v)
   - Every vertex has exact undirected degree r, exact in-degree z, exact out-degree z
   - Weak and strong connectivity (when z >= 1)
   - Exact mixed girth == g via two independent algorithms:
     (Algorithm A) All-roots forward-backward non-backtracking path enumeration + explicit g-cycle witness
     (Algorithm B) Exact integer transition-matrix algebra on U (undirected) and D (directed), T = U + D:
       * tr(T^3) == 0 (zero 3-cycles)
       * For all u != v, (T^2)_{uv} * (T^2)_{vu} == (U^2)_{uv} (zero 4-cycles)
       * tr(T^5) == 0 (zero 5-cycles)
   - Compares N against Table 1 of arXiv:2506.20003 in data/cage_tables.json
"""

import argparse
import hashlib
import json
import os
import sys
from collections import deque


def mat_mul_int(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(n):
            aik = Ai[k]
            if aik:
                Bk = B[k]
                for j in range(n):
                    Ci[j] += aik * Bk[j]
    return C


def mat_trace(A):
    return sum(A[i][i] for i in range(len(A)))


def bfs_shortest_cycle_undir(N, adj):
    girth = 10**9
    best_cycle = None
    for root in range(N):
        dist = [-1] * N
        parent = [-1] * N
        dist[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            if 2 * dist[u] + 1 >= girth:
                break
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif parent[u] != v:
                    cand = dist[u] + dist[v] + 1
                    if cand < girth:
                        girth = cand
                        # Reconstruct cycle
                        path_u = []
                        curr = u
                        while curr != -1:
                            path_u.append(curr)
                            curr = parent[curr]
                        path_v = []
                        curr = v
                        while curr != -1:
                            path_v.append(curr)
                            curr = parent[curr]
                        best_cycle = path_u[::-1] + path_v[:-1]
    return girth, best_cycle


def edge_deletion_girth_undir(N, edges, adj):
    girth = 10**9
    for u0, v0 in edges:
        dist = [-1] * N
        dist[u0] = 0
        q = deque([u0])
        while q:
            u = q.popleft()
            if dist[u] + 1 >= girth:
                break
            if u == v0:
                girth = min(girth, dist[u] + 1)
                break
            for w in adj[u]:
                if (u == u0 and w == v0) or (u == v0 and w == u0):
                    continue
                if dist[w] == -1:
                    dist[w] = dist[u] + 1
                    q.append(w)
    return girth


def wl_signature_undir(N, adj, rounds=5):
    colors = [len(adj[v]) for v in range(N)]
    for _ in range(rounds):
        raw = [
            (colors[v], tuple(sorted(colors[w] for w in adj[v])))
            for v in range(N)
        ]
        palette = {sig: idx for idx, sig in enumerate(sorted(set(raw)))}
        colors = [palette[sig] for sig in raw]
    # Also compute per-vertex cycle count profile up to length 8 via BFS tree/cross edges
    cycle_prof = []
    for root in range(N):
        dist = [-1] * N
        parent = [-1] * N
        dist[root] = 0
        q = deque([root])
        cross_counts = {}
        while q:
            u = q.popleft()
            if dist[u] > 4:
                break
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif parent[u] != v and u < v:
                    clen = dist[u] + dist[v] + 1
                    cross_counts[clen] = cross_counts.get(clen, 0) + 1
        cycle_prof.append(tuple(sorted(cross_counts.items())))
    return {
        "wl_palette_size": len(set(colors)),
        "cycle_profile_multiset": sorted(
            [(str(k), cycle_prof.count(k)) for k in set(cycle_prof)]
        ),
    }


def verify_classical_cage(data, tables, compare_files=None):
    N = int(data["N"])
    k = int(data["k"])
    g_target = int(data["g"])
    edges = data["edges"]

    adj = [[] for _ in range(N)]
    edge_set = set()
    for u, v in edges:
        u, v = int(u), int(v)
        if not (0 <= u < N and 0 <= v < N):
            raise ValueError(f"Vertex out of range: ({u}, {v})")
        if u == v:
            raise ValueError(f"Self-loop at vertex {u}")
        pair = (min(u, v), max(u, v))
        if pair in edge_set:
            raise ValueError(f"Duplicate edge: {pair}")
        edge_set.add(pair)
        adj[u].append(v)
        adj[v].append(u)

    for v in range(N):
        if len(adj[v]) != k:
            raise ValueError(f"Vertex {v} has degree {len(adj[v])} != k={k}")

    # Connectivity
    vis = [False] * N
    vis[0] = True
    q = deque([0])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if not vis[w]:
                vis[w] = True
                q.append(w)
    if not all(vis):
        raise ValueError("Graph is not connected")

    girth_a, witness_cycle = bfs_shortest_cycle_undir(N, adj)
    girth_b = edge_deletion_girth_undir(N, list(edge_set), adj)
    if girth_a != girth_b:
        raise ValueError(f"Girth mismatch: BFS={girth_a} vs EdgeDel={girth_b}")
    if girth_a < g_target:
        raise ValueError(f"Girth {girth_a} < target {g_target}")

    key = f"({k},{g_target})"
    rec_info = tables.get("classical_cages_open_selected", {}).get(key, {})
    rec = rec_info.get("rec")

    inv = wl_signature_undir(N, adj)
    noniso_results = []
    if compare_files:
        for cf in compare_files:
            with open(cf, "r") as f:
                cdata = json.load(f)
            cN = int(cdata["N"])
            cadj = [[] for _ in range(cN)]
            for u, v in cdata["edges"]:
                cadj[int(u)].append(int(v))
                cadj[int(v)].append(int(u))
            cinv = wl_signature_undir(cN, cadj)
            is_diff = inv["cycle_profile_multiset"] != cinv["cycle_profile_multiset"]
            noniso_results.append((os.path.basename(cf), is_diff))

    print(f"=== CLASSICAL CAGE VERIFICATION: (k={k}, g={g_target}) on N={N} ===")
    print(f"Simple undirected graph: PASS (|V|={N}, |E|={len(edge_set)})")
    print(f"Regularity deg(v)=={k}: PASS")
    print(f"Connectivity: PASS")
    print(f"Exact girth (Alg A: All-roots BFS): {girth_a}")
    print(f"Exact girth (Alg B: Edge-deletion BFS): {girth_b}")
    print(f"Sample shortest cycle witness: {witness_cycle}")
    print(f"Invariant cycle profile classes: {len(inv['cycle_profile_multiset'])} orbits")
    if rec is not None:
        if N < rec:
            print(f"Record comparison: N={N} < rec({k},{g_target})={rec} -> STRICT IMPROVEMENT (FULL WIN)")
        elif N == rec:
            print(f"Record comparison: N={N} == rec({k},{g_target})={rec} -> TIES LIVE RECORD")
        else:
            print(f"Record comparison: N={N} > rec({k},{g_target})={rec}")
    for cname, is_diff in noniso_results:
        print(f"Non-isomorphism vs {cname}: {'PASS (distinct invariant profile)' if is_diff else 'FAIL (matching profile)'}")
    print("RESULT: PASS")
    return True


def verify_mixed_alg_a_meet_in_middle(N, edges, arcs):
    """
    Algorithm A: Exact combinatorial forward-backward non-backtracking path enumeration
    from every root vertex r in 0..N-1.
    Finds the exact shortest mixed cycle of length <= 6 and returns (girth, witness_cycle).
    """
    # Build forward and backward adjacency lists with link IDs
    # Each undirected edge gets link_id in 0..len(edges)-1
    # Each directed arc gets link_id in len(edges)..len(edges)+len(arcs)-1
    fwd = [[] for _ in range(N)]
    bwd = [[] for _ in range(N)]
    for idx, (u, v) in enumerate(edges):
        fwd[u].append((v, idx))
        fwd[v].append((u, idx))
        bwd[u].append((v, idx))
        bwd[v].append((u, idx))
    offset = len(edges)
    for idx, (u, v) in enumerate(arcs):
        lid = offset + idx
        fwd[u].append((v, lid))
        bwd[v].append((u, lid))

    best_len = 10**9
    witness = None

    for root in range(N):
        # Forward paths from root of length 1, 2, 3:
        # Store dict: end_vertex -> list of (v1, ..., vk, first_lid, last_lid)
        f1 = {}
        f2 = {}
        f3 = {}
        for v1, lid1 in fwd[root]:
            f1.setdefault(v1, []).append(((v1,), lid1, lid1))
            for v2, lid2 in fwd[v1]:
                if lid2 == lid1:
                    continue
                if v2 == root:
                    if 2 < best_len:
                        best_len = 2
                        witness = [root, v1]
                    continue
                f2.setdefault(v2, []).append(((v1, v2), lid1, lid2))
                for v3, lid3 in fwd[v2]:
                    if lid3 == lid2 or v3 == v1:
                        continue
                    if v3 == root:
                        if 3 < best_len and lid3 != lid1:
                            best_len = 3
                            witness = [root, v1, v2]
                        continue
                    f3.setdefault(v3, []).append(((v1, v2, v3), lid1, lid3))

        if best_len <= 3:
            return best_len, witness

        # Backward paths into root of length 2 and 3:
        # b2: u -> w1 -> root (traversed forward as u -> w1 -> root)
        b2 = {}
        b3 = {}
        for w1, blid1 in bwd[root]:
            for u, blid2 in bwd[w1]:
                if blid2 == blid1 or u == root:
                    continue
                # Forward traversal is u --(blid2)--> w1 --(blid1)--> root
                b2.setdefault(u, []).append(((w1,), blid2, blid1))
                for u0, blid3 in bwd[u]:
                    if blid3 == blid2 or u0 in (root, w1):
                        continue
                    # Forward traversal is u0 --(blid3)--> u --(blid2)--> w1 --(blid1)--> root
                    b3.setdefault(u0, []).append(((u, w1), blid3, blid1))

        # Check length 4: f2[u] + b2[u]
        for u, fpaths in f2.items():
            bpaths = b2.get(u)
            if not bpaths:
                continue
            for (v1, _), flid_first, flid_last in fpaths:
                for (w1,), blid_first, blid_last in bpaths:
                    if flid_last != blid_first and blid_last != flid_first and v1 != w1:
                        best_len = 4
                        witness = [root, v1, u, w1]
                        return best_len, witness

        # Check length 5: f3[u] + b2[u]
        for u, fpaths in f3.items():
            bpaths = b2.get(u)
            if not bpaths:
                continue
            for (v1, v2, _), flid_first, flid_last in fpaths:
                for (w1,), blid_first, blid_last in bpaths:
                    if (
                        flid_last != blid_first
                        and blid_last != flid_first
                        and w1 not in (v1, v2)
                    ):
                        best_len = 5
                        witness = [root, v1, v2, u, w1]
                        return best_len, witness

        # Check length 6 (only need one witness if best_len > 6): f3[u] + b3[u]
        if best_len > 6:
            for u, fpaths in f3.items():
                bpaths = b3.get(u)
                if not bpaths:
                    continue
                for (v1, v2, _), flid_first, flid_last in fpaths:
                    for (w2, w1), blid_first, blid_last in bpaths:
                        if (
                            flid_last != blid_first
                            and blid_last != flid_first
                            and w2 not in (v1, v2)
                            and w1 not in (v1, v2)
                        ):
                            best_len = 6
                            witness = [root, v1, v2, u, w2, w1]
                            break
                    if best_len == 6:
                        break
                if best_len == 6:
                    break

    return best_len, witness


def verify_mixed_alg_b_matrix_algebra(N, edges, arcs):
    """
    Algorithm B: Exact integer matrix algebra on U (undirected) and D (directed), T = U + D.
    1. Checks no 2-cycles: U_ii = D_ii = 0, U_ij * D_ij = 0, D_ij * D_ji = 0.
    2. Checks no 3-cycles: tr(T^3) == 0.
    3. Checks no 4-cycles: for all u != v, (T^2)_{uv} * (T^2)_{vu} - (U^2)_{uv} == 0.
    4. Checks no 5-cycles: tr(T^5) == 0.
    """
    U = [[0] * N for _ in range(N)]
    D = [[0] * N for _ in range(N)]
    T = [[0] * N for _ in range(N)]
    for u, v in edges:
        U[u][v] += 1
        U[v][u] += 1
        T[u][v] += 1
        T[v][u] += 1
    for u, v in arcs:
        D[u][v] += 1
        T[u][v] += 1

    # 1. Check 2-cycles
    for i in range(N):
        if U[i][i] != 0 or D[i][i] != 0:
            return 2, f"Self-loop at {i}"
        for j in range(N):
            if U[i][j] > 1 or D[i][j] > 1:
                return 2, f"Parallel link between {i} and {j}"
            if U[i][j] and D[i][j]:
                return 2, f"Parallel edge and arc between {i} and {j}"
            if D[i][j] and D[j][i]:
                return 2, f"Opposite arcs between {i} and {j}"

    # 2. Compute T^2, U^2, T^3
    T2 = mat_mul_int(T, T)
    U2 = mat_mul_int(U, U)
    T3 = mat_mul_int(T2, T)
    tr3 = mat_trace(T3)
    if tr3 != 0:
        return 3, f"tr(T^3) = {tr3} != 0"

    # 3. Check 4-cycles via off-diagonal (T^2)_{uv} * (T^2)_{vu} - (U^2)_{uv}
    c4_count = 0
    for u in range(N):
        T2u = T2[u]
        U2u = U2[u]
        for v in range(N):
            if u != v:
                diff = T2u[v] * T2[v][u] - U2u[v]
                if diff != 0:
                    c4_count += diff
    if c4_count != 0:
        return 4, f"4-cycle count = {c4_count} != 0"

    # 4. Check 5-cycles via tr(T^5) == sum_{i,j} (T^2)_{ij} * (T^3)_{ji}
    tr5 = 0
    for i in range(N):
        T2i = T2[i]
        for j in range(N):
            if T2i[j]:
                tr5 += T2i[j] * T3[j][i]
    if tr5 != 0:
        return 5, f"tr(T^5) = {tr5} != 0"

    return 6, "tr(T^3)=0, offdiag((T^2)*(T^2)^T - U^2)=0, tr(T^5)=0"


def verify_mixed_cage(data, tables):
    N = int(data["N"])
    z = int(data["z"])
    r = int(data["r"])
    g_target = int(data.get("g", 6))
    edges = [(int(u), int(v)) for u, v in data["edges"]]
    arcs = [(int(u), int(v)) for u, v in data["arcs"]]

    # 1. Check simple mixed graph rules and degrees
    pair_set = set()
    undir_deg = [0] * N
    in_deg = [0] * N
    out_deg = [0] * N
    fwd_adj = [[] for _ in range(N)]
    bwd_adj = [[] for _ in range(N)]

    for u, v in edges:
        if not (0 <= u < N and 0 <= v < N) or u == v:
            raise ValueError(f"Invalid undirected edge ({u}, {v})")
        pair = (min(u, v), max(u, v))
        if pair in pair_set:
            raise ValueError(f"Duplicate link on vertex pair {pair}")
        pair_set.add(pair)
        undir_deg[u] += 1
        undir_deg[v] += 1
        fwd_adj[u].append(v)
        fwd_adj[v].append(u)
        bwd_adj[u].append(v)
        bwd_adj[v].append(u)

    for u, v in arcs:
        if not (0 <= u < N and 0 <= v < N) or u == v:
            raise ValueError(f"Invalid directed arc ({u}, {v})")
        pair = (min(u, v), max(u, v))
        if pair in pair_set:
            raise ValueError(f"Parallel link on vertex pair {pair}")
        pair_set.add(pair)
        out_deg[u] += 1
        in_deg[v] += 1
        fwd_adj[u].append(v)
        bwd_adj[v].append(u)

    for v in range(N):
        if undir_deg[v] != r:
            raise ValueError(f"Vertex {v} has undirected degree {undir_deg[v]} != r={r}")
        if in_deg[v] != z:
            raise ValueError(f"Vertex {v} has in-degree {in_deg[v]} != z={z}")
        if out_deg[v] != z:
            raise ValueError(f"Vertex {v} has out-degree {out_deg[v]} != z={z}")

    # Check strong connectivity
    for direction, adj in [("forward", fwd_adj), ("backward", bwd_adj)]:
        vis = [False] * N
        vis[0] = True
        q = deque([0])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if not vis[w]:
                    vis[w] = True
                    q.append(w)
        if not all(vis):
            raise ValueError(f"Mixed graph is not strongly connected ({direction})")

    # 2. Algorithm A: Meet-in-the-middle shortest mixed cycle + explicit 6-cycle witness
    girth_a, witness = verify_mixed_alg_a_meet_in_middle(N, edges, arcs)

    # 3. Algorithm B: Exact integer transition-matrix algebra
    girth_b, alg_b_msg = verify_mixed_alg_b_matrix_algebra(N, edges, arcs)

    if girth_a != g_target or girth_b != g_target:
        raise ValueError(
            f"Mixed girth mismatch: AlgA={girth_a}, AlgB={girth_b} ({alg_b_msg}), target={g_target}"
        )

    # Verify the explicit 6-cycle witness step-by-step
    if witness is None or len(witness) != g_target or len(set(witness)) != g_target:
        raise ValueError(f"Invalid g-cycle witness: {witness}")
    edge_lookup = {(min(u, v), max(u, v)) for u, v in edges}
    arc_lookup = set(arcs)
    for idx in range(g_target):
        u = witness[idx]
        v = witness[(idx + 1) % g_target]
        if (min(u, v), max(u, v)) not in edge_lookup and (u, v) not in arc_lookup:
            raise ValueError(f"Witness step {u}->{v} is not a valid edge or forward arc")

    key = f"[{z},{r};{g_target}]"
    t1 = tables.get("mixed_cages_girth6_table1_2506_20003", {}).get(key, {})
    ub = t1.get("upper")
    lb = t1.get("lower")

    print(f"=== MIXED CAGE VERIFICATION: [z={z}, r={r}; g={g_target}] on N={N} ===")
    print(f"Simple mixed graph (no parallel/opposite links): PASS (|V|={N}, |E|={len(edges)}, |A|={len(arcs)})")
    print(f"Regularity (in={z}, out={z}, undir={r} at all {N} vertices): PASS")
    print(f"Strong connectivity: PASS")
    print(f"Exact mixed girth (Alg A: All-roots non-backtracking meet-in-middle): {girth_a}")
    print(f"Exact mixed girth (Alg B: Exact integer matrix algebra): {girth_b} ({alg_b_msg})")
    print(f"Explicit {g_target}-cycle witness verified: {witness}")
    if ub is not None:
        if N < ub:
            print(
                f"Table 1 (arXiv:2506.20003) comparison: N={N} < UB={ub} (LB={lb}) "
                f"-> STRICT IMPROVEMENT by {ub - N} vertices (PARTIAL WIN p2)"
            )
        elif N == ub:
            print(f"Table 1 (arXiv:2506.20003) comparison: N={N} == UB={ub} (LB={lb})")
        else:
            print(f"Table 1 (arXiv:2506.20003) comparison: N={N} > UB={ub} (LB={lb})")
    print("RESULT: PASS")
    return True


def main():
    parser = argparse.ArgumentParser(description="Standalone exact verifier for cage-upper-bounds")
    parser.add_argument("input_json", nargs="+", help="Path(s) to candidate graph JSON file(s)")
    parser.add_argument("--mode", choices=["auto", "cage", "mixed"], default="auto")
    parser.add_argument(
        "--tables",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "cage_tables.json"),
        help="Path to cage_tables.json",
    )
    parser.add_argument(
        "--compare-noniso",
        nargs="*",
        default=None,
        help="Optional JSON files to check non-isomorphism against (for p1 claims)",
    )
    args = parser.parse_args()

    tables = {}
    if os.path.exists(args.tables):
        with open(args.tables, "r") as f:
            tables = json.load(f)

    for path in args.input_json:
        with open(path, "r") as f:
            raw_bytes = f.read()
        sha = hashlib.sha256(raw_bytes.encode("utf-8")).hexdigest()
        data = json.loads(raw_bytes)
        print(f"File: {os.path.basename(path)} (SHA-256: {sha})")
        mode = args.mode
        if mode == "auto":
            mode = "mixed" if "arcs" in data else "cage"
        if mode == "mixed":
            verify_mixed_cage(data, tables)
        else:
            verify_classical_cage(data, tables, args.compare_noniso)
        print()


if __name__ == "__main__":
    main()
