# Reproduction & Independent Verification Report: `cage-upper-bounds`

context: subagent (astra)
role: REPRODUCE skeptic
target: cage-upper-bounds
submission_type: CONFIRMED_PARTIAL (Partial Win p2: Mixed-Cage Upper Bounds)

## 1. Quoted Mathematical Definitions from `claim/target.md` and `claim/CLAIM.md`

From `claim/target.md` (`Partial Win p2`):
- "A graph strictly beating a live entry of the separate girth-diameter cage table (arXiv 2511.21144) or the mixed-cage table (arXiv 2506.20003), verified exactly against that table's own definition; logged as a partial win, never as a cage record."

From `claim/CLAIM.md` (Sections 1 and 2):
- **`[z, r; g]`-mixed graph and mixed girth definition**:
  "We construct and verify five explicit `[z, r; 6]`-mixed graphs (`in-degree = z`, `out-degree = z`, `undirected degree = r`, `mixed girth = 6`) that strictly beat five open rows of `arXiv:2506.20003` (Exoo, Jajcay, and Rook 2025, *Table 1: Best known bounds on the order of mixed cages with girth 6*), and four of which (`z = 2, r in {7, 8, 9, 11}`) also strictly beat the projective-plane incidence construction `2(q^2 + q + 1)` of Jajcayova and Jajcay (`arXiv:2511.20286`, Theorems 3.5 and 3.6)."
- **Bi-Cayley Mixed Graph `BiCay(Z_M; S, A_0, A_1)` and Girth-6 Sumset Characterization**:
  "Let `M at least 1` and define the bipartite bi-Cayley mixed graph `G = BiCay(Z_M; S, A_0, A_1)` on `N = 2M` vertices `V_0 disjoint-union V_1` (`V_0 = {0, ..., M-1}`, `V_1 = {M, ..., 2M-1}`), where for pairwise disjoint subsets `S, A_0, A_1 subset Z_M` with `|S| = r` and `|A_0| = |A_1| = z`:
  - Undirected edges join `x in V_0` and `M + ((x + s) mod M) in V_1` for all `s in S`.
  - Directed arcs go from `x in V_0` to `M + ((x + a_0) mod M) in V_1` for all `a_0 in A_0`.
  - Directed arcs go from `M + y in V_1` to `(y - a_1) mod M in V_0` (equivalently, from `M + ((x + a_1) mod M) in V_1` to `x in V_0`) for all `a_1 in A_1`."
  "Consequently, `G` has mixed girth `6` if and only if:
  1. `S` is a Sidon set in `Z_M`, so `Sigma_S = S + S` has exact size `r*(r+1)/2`; and
  2. The three sumsets `Sigma_S = S + S`, `Sigma_0 = (S + A_0) union (A_0 + A_0)`, and `Sigma_1 = (S + A_1) union (A_1 + A_1)` are pairwise disjoint in `Z_M`."

---

## 2. Independent Verification Before Reading `claim/verify_cage.py`

Before viewing `claim/verify_cage.py`, I wrote and executed an independent Python verifier from scratch directly from the definition of a `[z, r; g]`-mixed graph `G = (V, E, A)` (`arXiv:2506.20003`):
1. **Simple Mixed Graph & Degree Audit**:
   - Verified `V = {0, ..., N-1}`, zero undirected self-loops, zero directed self-loops, zero duplicate undirected edges, zero duplicate directed arcs, zero anti-parallel arc pairs `(u, v)` and `(v, u)`, and zero overlap between undirected edges `{u, v}` and directed arcs `(u, v)`.
   - Verified at every vertex `v in V` that `deg_undir(v) == r`, `deg_in(v) == z`, and `deg_out(v) == z`.
2. **Bi-Cayley Algebraic & Twin-Cluster Sidon Sumset Audit**:
   - Verified that `edges` and `arcs` in each JSON file match `BiCay(Z_M; S, A_0, A_1)` edge-for-edge and arc-for-arc (`|E| = M * r`, `|A| = 2 * M * z`).
   - Verified in `Z_M` that `S, A_0, A_1` are pairwise disjoint, `|Sigma_S| = |S + S| = r*(r+1)/2`, and `Sigma_S`, `Sigma_0 = (S + A_0) union (A_0 + A_0)`, `Sigma_1 = (S + A_1) union (A_1 + A_1)` are pairwise disjoint.
   - Confirmed the Twin-Cluster Sidon compression: whereas generic disjointness without internal difference overlaps requires `|Sigma_0|, |Sigma_1| = 2r + 3`, the internal difference collision `a - a' in S - S` inside `A_0` and `A_1` compresses `|Sigma_0|` and `|Sigma_1|` below `2r + 3` (`16` vs `17` at `r=7`, `18` vs `19` at `r=8`, `20` vs `21` at `r=9`, `24` vs `25` at `r=11`).
3. **Exact Mixed Girth `g = 6` via Two Independent Shortest-Cycle Algorithms**:
   - **Astra Algorithm 1 (All-Roots Non-Backtracking Path Enumeration)**: From every root `s in V`, enumerates all simple directed paths `s = v_0, v_1, ..., v_L` (where each step traverses either an undirected edge in `{u, v} in E` or a forward arc `(u, v) in A`, with all visited vertices distinct) for `L in {2, 3, 4, 5}`, checking whether `v_L` has a valid step back to `s`. Confirmed zero simple cycles of length `3, 4, 5` from all `N` roots, counted the exact number of simple 6-cycles rooted at vertex `0`, and extracted an explicit 6-cycle witness.
   - **Astra Algorithm 2 (Exact Integer Transition-Matrix & 2-Path Multiplicity Check)**: Let `U` be the `N x N` symmetric undirected adjacency matrix, `D` the `N x N` directed arc adjacency matrix, and `T = U + D`. Because `G` is simple and mixed (`U hadamard D = 0`, `D hadamard D^T = 0`), any closed 2-walk uses an undirected edge twice (`tr(T^2) = tr(U^2) = 2|E|`). Computed `U^2, T^2, T^3, T^5` over exact integers and verified:
     - `tr(T^3) == 0` (zero 3-cycles),
     - `sum_{u != v} ((T^2)_{u,v} * (T^2)_{v,u} - (U^2)_{u,v}) == 0` (zero simple 4-cycles, since every closed 4-walk `u, x, v, y, u` with `u != v` has `x == y` iff both steps are undirected edges in `U^2`), and
     - `tr(T^5) == 0` (zero 5-cycles).
4. **Negative-Control Corruption Tests**:
   - **Link overlap corruption**: Replacing arc `0` with `[edges[0][0], edges[0][1]]` is immediately rejected for edge-arc overlap and degree violation.
   - **Degree-preserving 2-arc swap**: Swapping the targets of two existing arcs `(u_old, 0)` and `(w_v1, x_old)` where `w_v1 = M + ((S[0] - S[1] + S[2]) mod M)` preserves exact `(z, z, r)`-regularity at all `N` vertices and simple mixed graph structure while creating a simple 4-cycle through vertex `0`, which both our independent checker and `claim/verify_cage.py` immediately catch and reject (`Mixed girth = 4 != 6`).

### Summary of Independent Verification Across All 4 Strictly Novel `[2, r; 6]` Graphs (+ `[1, 7; 6]`)

| File (relative to `claim/`) | `[z, r; g]` | Verified `N` (`M`) | `2506.20003` Tab 1 UB (`Delta`) | `2511.20286` UB (`Delta`) | `|E|, |A|` | Sumset Sizes `|Sigma_S|, |Sigma_0|, |Sigma_1|` | `tr(T^3), c4_mat, tr(T^5)` | Simple 6-Cycles at `v=0` (Witness) | Degree-Preserving 2-Arc Swap Negative Test |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| `claim/mixed_z2_r7_g6_N184.json` | `[2, 7; 6]` | **`184`** (`92`) | `196` (**`-12`**) | `266` (**`-82`**) | `644, 368` | `28, 16, 16` | `0, 0, 0` | `4140` (`(0, 92, 8, 100, 27, 105)`) | Rejected (`4-cycle (0, 92, 75, 95)`) |
| `claim/mixed_z2_r8_g6_N234.json` | `[2, 8; 6]` | **`234`** (`117`) | `252` (**`-18`**) | `266` (**`-32`**) | `936, 468` | `36, 18, 18` | `0, 0, 0` | `6173` (`(0, 117, 9, 126, 20, 209)`) | Rejected (`4-cycle (0, 117, 96, 120)`) |
| `claim/mixed_z2_r9_g6_N294.json` | `[2, 9; 6]` | **`294`** (`147`) | `320` (**`-26`**) | `366` (**`-72`**) | `1323, 588` | `45, 20, 21` | `0, 0, 0` | `8921` (`(0, 147, 13, 160, 26, 174)`) | Rejected (`4-cycle (0, 147, 146, 193)`) |
| `claim/mixed_z2_r11_g6_N450.json` | `[2, 11; 6]` | **`450`** (`225`) | `480` (**`-30`**) | `514` (**`-64`**) | `2475, 900` | `66, 24, 24` | `0, 0, 0` | `16082` (`(0, 225, 8, 233, 7, 288)`) | Rejected (`4-cycle (0, 225, 224, 230)`) |
| `claim/mixed_z1_r7_g6_N146.json` | `[1, 7; 6]` | **`146`** (`73`) | `192` (**`-46`**) | `146` (`0`, ties) | `511, 146` | `28, 8, 8` | `0, 0, 0` | `2328` (`(0, 73, 2, 75, 26, 106)`) | Rejected (`4-cycle (0, 73, 70, 83)`) |

---

## 3. Artifact Integrity & SHA-256 Hashes

| File (relative to `claim/`) | Size (bytes) | SHA-256 Digest |
| :--- | ---: | :--- |
| `claim/verify_cage.py` | `21414` | `4ae5dc1d2a4fc06e5f8640bc7febc8d21b6e9ac07d60ff8caca7f6e924e3121d` |
| `claim/mixed_z2_r7_g6_N184.json` | `11126` | `7783a2b9dcaf14fc309c663a27ac902e46db4a06bb77959fb7814be6fdcea2ab` |
| `claim/mixed_z2_r8_g6_N234.json` | `15728` | `879cb5f756b16355b5afb9eb6c9f182e43eccccebd7849cf395070822a051229` |
| `claim/mixed_z2_r9_g6_N294.json` | `21706` | `a61b36576b49191399e6881ad34153ac1b9b9893a4513252b583b34916078d93` |
| `claim/mixed_z2_r11_g6_N450.json` | `39066` | `c04fa003c1474a615f252960788061395ba80f6bf0681572cd048990467ead63` |
| `claim/mixed_z1_r7_g6_N146.json` | `21580` | `1f3fade2c4218975762e06531ea5d37ae0611b8441d036701c05b1c1aced8b81` |

---

## 4. Audit and Execution of Author's Verifier (`claim/verify_cage.py`)

After completing my independent verification, I inspected `claim/verify_cage.py` and executed it on all claimed `.json` files plus the corrupted 2-arc-swapped graph:
1. **Execution on the 4 strictly novel `[2, r; 6]` graphs (and `[1, 7; 6]`)**:
   - Command: `python3 claim/verify_cage.py claim/mixed_z2_r7_g6_N184.json claim/mixed_z2_r8_g6_N234.json claim/mixed_z2_r9_g6_N294.json claim/mixed_z2_r11_g6_N450.json claim/mixed_z1_r7_g6_N146.json`
   - Exit code: `0`
   - Outputs:
     - `mixed_z2_r7_g6_N184.json`: `Simple mixed graph: PASS (|V|=184, |E|=644, |A|=368)`, `Regularity (in=2, out=2, undir=7 at all 184 vertices): PASS`, `Strong connectivity: PASS`, `Alg A: 6`, `Alg B: 6 (tr(T^3)=0, offdiag((T^2)*(T^2)^T - U^2)=0, tr(T^5)=0)`, `Explicit 6-cycle witness verified: [0, 92, 18, 110, 36, 109]`, `RESULT: PASS`
     - `mixed_z2_r8_g6_N234.json`: `Simple mixed graph: PASS (|V|=234, |E|=936, |A|=468)`, `Regularity (in=2, out=2, undir=8 at all 234 vertices): PASS`, `Strong connectivity: PASS`, `Alg A: 6`, `Alg B: 6`, `Explicit 6-cycle witness verified: [0, 117, 9, 126, 35, 141]`, `RESULT: PASS`
     - `mixed_z2_r9_g6_N294.json`: `Simple mixed graph: PASS (|V|=294, |E|=1323, |A|=588)`, `Regularity (in=2, out=2, undir=9 at all 294 vertices): PASS`, `Strong connectivity: PASS`, `Alg A: 6`, `Alg B: 6`, `Explicit 6-cycle witness verified: [0, 147, 13, 160, 78, 194]`, `RESULT: PASS`
     - `mixed_z2_r11_g6_N450.json`: `Simple mixed graph: PASS (|V|=450, |E|=2475, |A|=900)`, `Regularity (in=2, out=2, undir=11 at all 450 vertices): PASS`, `Strong connectivity: PASS`, `Alg A: 6`, `Alg B: 6`, `Explicit 6-cycle witness verified: [0, 225, 8, 233, 170, 226]`, `RESULT: PASS`
     - `mixed_z1_r7_g6_N146.json`: `Simple mixed graph: PASS (|V|=146, |E|=511, |A|=146)`, `Regularity (in=1, out=1, undir=7 at all 146 vertices): PASS`, `Strong connectivity: PASS`, `Alg A: 6`, `Alg B: 6`, `Explicit 6-cycle witness verified: [0, 73, 2, 75, 43, 76]`, `RESULT: PASS`
2. **Corrupted negative test on `claim/verify_cage.py`**:
   - Passing the degree-preserving 2-arc-swapped copy of `claim/mixed_z2_r7_g6_N184.json` exits with code `1` and raises `ValueError: Mixed girth mismatch: AlgA=4, AlgB=4 (4-cycle count = 48 != 0), target=6`.

All independent and author verification checks succeed.

pass: true
