# Reproduction & Independent Verification Report — `degree-diameter-table` (`Delta = 14, D = 3, N = 1,117`)

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target ID**: `degree-diameter-table` (`New largest known (Delta, D) graph in the degree-diameter table`)
- **Cell**: General undirected graphs with maximum degree `Delta = 14` and diameter `D = 3`
- **Claimed Order**: `N = 1,117` vertices and `E = 7,785` undirected edges (strictly beating the live Comellas general-graph table record `N_0 = 1,116` by `+1` vertex; Moore bound `M(14, 3) = 2,563`)
- **Artifact**: `claim/G_14_3_N1117.edges` (`62,388` bytes, SHA-256 `3fc25411941fa666946464317bc9672386a4923bcb01a24e2c42ec7239b8c3a4`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_dd.py` or `claim/ddcheck.c`) and the author's standalone Python (`claim/verify_dd.py`) and multi-threaded C99 (`claim/ddcheck.c`) verifiers confirm that `claim/G_14_3_N1117.edges` is a simple connected undirected graph on `N = 1,117` vertices (`0` loops, `0` duplicate edges, `0` unused labels in `0..1116`), with minimum degree `13`, maximum degree `14` (`68` vertices of degree `13` and `1,049` vertices of degree `14`), and exact all-pairs shortest-path diameter `3` (`0` ordered pairs at distance above `3` out of all `1,117 x 1,117 = 1,247,689` ordered pairs, and `1,039,660` ordered pairs at distance `3`). All three checkers also reject both `D - 1 = 2` and a 1-edge-deleted corrupted graph (`exit = 1`).

---

## 2. Verbatim Success Criterion from `claim/target.md`

  - **Statement**: For maximum degree `Delta` and diameter `D`, find a graph with more vertices than the current entry in the Comellas degree-diameter table. The table covers degree up to 20 and diameter up to 10.
  - **Success Criterion**: (1) Explicit adjacency list of a simple undirected graph `G` on `N` vertices. (2) Maximum degree at most `Delta`. (3) `G` connected with diameter at most `D`, checked by all-pairs BFS, or by one BFS plus a machine-checked vertex-transitivity proof (explicit Cayley group and generators regenerating exactly the submitted edge set). (4) `N` STRICTLY GREATER than the `(Delta,D)` entry of the live Comellas general-graph table at `https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html`, re-fetched immediately before claiming (the table changes daily). (5) `N` at most Moore bound; boldface (proven-optimal) entries cannot be beaten, so beating one signals a bug.

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_dd.py` or `claim/ddcheck.c`)

Before reading `claim/verify_dd.py` or `claim/ddcheck.c`, we wrote and executed an independent Python verifier (`collections.deque` all-pairs BFS + exact set/degree audit) directly from the mathematical definition in `claim/target.md`.

### 3.1 Artifact Integrity & Graph Simplicity Audit
- **File**: `claim/G_14_3_N1117.edges`
- **Byte Size**: `62,388` bytes (`7,785` lines)
- **SHA-256**: `3fc25411941fa666946464317bc9672386a4923bcb01a24e2c42ec7239b8c3a4` (matches `claim/CLAIM.md`)
- **Line & Edge Audit**:
  - `unparsable_lines = 0`
  - `loops = 0` (no edge has `u == v`)
  - `duplicates = 0` (all `7,785` canonicalized undirected edges `(min(u,v), max(u,v))` are distinct)
  - `unused_labels = 0` (every vertex label in `0..1116` appears, confirming `N = 1,117`)

### 3.2 Vertex Degree Distribution & Moore Bound Check
- **Degree Bounds**: `mindeg = 13`, `maxdeg = 14` (satisfies `maxdeg` at most `Delta = 14`)
- **Exact Degree Histogram**:
  - Degree `13`: `68` vertices
  - Degree `14`: `1,049` vertices
  - Handshaking identity check: `68 * 13 + 1049 * 14 = 884 + 14,686 = 15,570 == 2 * 7,785`
- **Inserted Vertex `1116` Neighborhood**: `[47, 89, 160, 249, 302, 375, 453, 506, 699, 804, 818, 873, 983, 1062]` (degree `14`, matching `claim/CLAIM.md`)
- **Moore Bound & Baseline Check**:
  - `M(14, 3) = 1 + 14 * (1 + 13 + 13^2) = 1 + 14 * 183 = 2,563`
  - `N = 1,117` is at most `M(14, 3) = 2,563`
  - In `claim/live_general_cells.json`, cell `"(14,3)"` has `"N": 1116` and `"bold": false`, so `N = 1,117` strictly beats `1,116` by `+1` vertex and does not claim to beat a proven-optimal boldface entry.

### 3.3 Exhaustive All-Pairs BFS Shortest-Path Verification
Running an independent breadth-first search from each of the `1,117` vertices over all `1,117 x 1,117 = 1,247,689` ordered pairs `(u, v)` yields:
- **Exact Distance Distribution**:
  - `dist(u, v) == 0`: `1,117` ordered pairs
  - `dist(u, v) == 1`: `15,570` ordered pairs (`2 * 7,785`)
  - `dist(u, v) == 2`: `191,342` ordered pairs
  - `dist(u, v) == 3`: `1,039,660` ordered pairs
  - `dist(u, v)` above `3` or disconnected: `0` ordered pairs
- **Cumulative Ordered Pairs Within Distance `r`**:
  - `r = 0`: `1,117`
  - `r = 1`: `16,687`
  - `r = 2`: `208,029`
  - `r = 3`: `1,247,689 == 1,117^2`
- **Exact Diameter**: `3` (`G` is connected and every ordered pair has shortest-path distance at most `3`).

### 3.4 Independent Negative Controls (`D - 1 = 2` and 1-Edge Deletion)
1. **Diameter `D - 1 = 2` Test**: Testing `claim/G_14_3_N1117.edges` against diameter `2` rejects with `far_pairs = 1,039,660` ordered pairs at distance `3`.
2. **Single-Edge Deletion Test**: Deleting a single edge (the last line `1064 1072` of `claim/G_14_3_N1117.edges`, leaving `7,784` edges) increases the diameter to `4` and causes our independent BFS checker to reject with `far_pairs = 66` ordered pairs (`33` unordered pairs) at distance `4`.

---

## 4. Step 2 — Audit & Execution of Author's Verifiers (`claim/verify_dd.py` and `claim/ddcheck.c`)

After completing our independent verification, we read and executed `claim/verify_dd.py` and `claim/ddcheck.c`.

### 4.1 Code Audit
- `claim/verify_dd.py`: Pure Python 3 stdlib verifier that parses the edge list, checks `bad == 0`, `loops == 0`, `dup == 0`, `unused == 0`, `maxdeg` at most `Delta`, `N` at most `moore_bound(Delta, D)`, and performs all-pairs bitset BFS across all `N` sources, verifying `far_d == 0`, `far_d_minus_1` above `0`, and `N` strictly greater than `baseline_to_beat = 1116`.
- `claim/ddcheck.c`: Standalone multi-threaded C99 verifier using `64 * W`-source bitset ball expansion (`__builtin_popcountll`) across all `N * N` ordered pairs.

### 4.2 Execution Results on Clean & Corrupted Inputs

1. **`python3 claim/verify_dd.py --table-json claim/live_general_cells.json claim/G_14_3_N1117.edges 14 3`** (`exit = 0`):
```json
{"file": "G_14_3_N1117.edges", "file_bytes": 62388, "N": 1117, "edges": 7785, "loops": 0, "duplicates": 0, "unparsable_lines": 0, "unused_labels": 0, "mindeg": 13, "maxdeg": 14, "DELTA": 14, "D": 3, "moore_bound": 2563, "live_table_entry": 1116, "live_bold_optimal": false, "trophy_case_entry": null, "baseline_to_beat": 1116, "degree_histogram": {"13": 68, "14": 1049}, "ordered_pairs_within_distance": {"0": 1117, "1": 16687, "2": 208029, "3": 1247689}, "far_pairs_at_D": 0, "far_pairs_at_D_minus_1": 1039660, "exact_diameter": 3, "negative_control_D_minus_1_rejects": true, "beats_record": true, "margin_over_baseline": 1, "valid": true}
```

2. **Compiled `claim/ddcheck.c` on `claim/G_14_3_N1117.edges 14 3 4`** (`exit = 0`):
```text
file=claim/G_14_3_N1117.edges
N=1117 edges=7785 loops=0 duplicates=0 unused_labels=0 mindeg=13 maxdeg=14 (DELTA=14, D=3)
degree_histogram: 13:68 14:1049
ordered_pairs_within_distance: r=0:1117 r=1:16687 r=2:208029 r=3:1247689
ordered_pairs_at_distance_gt_3=0 (of 1247689)
VALID
```

3. **Negative Control `D = 2` on `claim/verify_dd.py` and `claim/ddcheck.c`** (`exit = 1`):
   - Both checkers reject `D = 2` with `far_pairs_at_D = 1,039,660` (`ordered_pairs_at_distance_gt_2=1039660`, `valid: false` / `INVALID`).

4. **Negative Control (Deleting Edge `1064 1072`) on `claim/verify_dd.py` and `claim/ddcheck.c`** (`exit = 1`):
   - Both checkers reject the 7,784-edge graph (`r=0:1117, r=1:16685, r=2:207983, r=3:1247623`, `far_pairs_at_D = 66` ordered pairs at distance above `3`, `valid: false` / `INVALID`).

---

## 5. Summary Verification Table

| Criterion / Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `62,388` bytes | `3fc25411941fa666...` | PASS |
| Simple Undirected Graph (1) | Independent & author parsers | `N=1,117`, `E=7,785` | `loops=0, dup=0, unused=0` | PASS |
| Max Degree at most `14` (2) | Vertex degree histogram | All `1,117` vertices | `mindeg=13 (68), maxdeg=14 (1049)` | PASS |
| Connected & Diameter at most `3` (3) | Independent & author all-pairs BFS | All `1,247,689` ordered pairs | `r=3: 1,247,689`, `far_pairs=0` | PASS |
| Strictly Beats Live Table (4) | `claim/live_general_cells.json` | `(14,3)` cell = `1,116` | `1,117` beats `1,116` (`+1`) | PASS |
| At Most Moore Bound & Non-Bold (5) | Exact formula & table flag | `M(14,3) = 2,563` | `1,117` at most `2,563`, `bold=false` | PASS |
| Adversarial Corruption Tests | `D=2` & 1-edge deletion (`1064 1072`) | Independent + `verify_dd.py` + `ddcheck.c` | Rejected (`far_pairs=1,039,660` & `66`, `rc=1`) | PASS |

pass: true
