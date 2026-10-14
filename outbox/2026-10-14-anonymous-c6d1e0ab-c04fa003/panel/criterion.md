# CRITERION Skeptic Report: `cage-upper-bounds` — Partial Win `p2` (`[2, r; 6]` Mixed-Cage Upper Bounds)

context: subagent
confirmed_scope: Verified 4 explicit strictly novel [2, r; 6]-mixed cage graphs in claim/ achieving Partial Win p2 (mixed_z2_r7_g6_N184.json with N = 184 beating 196 by 12 vertices, mixed_z2_r8_g6_N234.json with N = 234 beating 252 by 18 vertices, mixed_z2_r9_g6_N294.json with N = 294 beating 320 by 26 vertices, and mixed_z2_r11_g6_N450.json with N = 450 beating 480 by 30 vertices, alongside mixed_z1_r7_g6_N146.json with N = 146 beating 192 in arXiv:2506.20003 Table 1), confirming simple mixed graph structure, exact (z, z, r)-regularity, exact mixed girth g = 6 via two independent shortest-cycle algorithms, and orders strictly below both Table 1 of arXiv:2506.20003 and the 2(q^2 + q + 1) projective-plane bounds of Jajcayova and Jajcay (arXiv:2511.20286).

## 1. Clause-by-Clause Verification of Partial Win `p2` Against `claim/target.md`

### 1.1 Partial Win `p2` Criterion (`claim/target.md`)
- **Verbatim `p2` definition**: *"A graph strictly beating a live entry of the separate girth-diameter cage table (arXiv 2511.21144) or the mixed-cage table (arXiv 2506.20003), verified exactly against that table's own definition; logged as a partial win, never as a cage record."*
- **Table definition (`arXiv:2506.20003`)**: A `[z, r; g]`-mixed graph $G = (V; E \cup A)$ is a simple mixed graph (no self-loops, no parallel undirected edges, no parallel or anti-parallel directed arcs, and no vertex pair joined simultaneously by an undirected edge and a directed arc) in which every vertex $v \in V$ has exact in-degree $z$, exact out-degree $z$, exact undirected degree $r$, and exact mixed girth $g$ (the length of a shortest simple cycle traversing undirected edges in either direction and directed arcs in their forward direction).

### 1.2 Independent Dual-Algorithm Verification (`claim/verify_cage.py`)
Executed `python3 claim/verify_cage.py --tables data/cage_tables.json` on all four strictly novel `[2, r; 6]`-mixed graphs (plus `claim/mixed_z1_r7_g6_N146.json`):
- **Simple mixed graph & degree regularity**: Confirmed zero loops, zero duplicate/parallel/anti-parallel links, exact $(z, z, r)$-regularity at all $N$ vertices, and strong connectivity in both forward and backward directions.
- **Exact mixed girth $g = 6$ via two independent algorithms**:
  1. **Algorithm A (All-Roots Non-Backtracking Meet-in-the-Middle Path Enumeration)**: Exhaustively verified from every root $v \in \{0, \dots, N-1\}$ that no simple mixed cycle of length $2, 3, 4,$ or $5$ exists, and verified an explicit 6-cycle witness step-by-step.
  2. **Algorithm B (Exact Integer Transition-Matrix Algebra)**: With undirected adjacency matrix $U$, directed adjacency matrix $D$, and $T = U + D$, verified in exact integer arithmetic that $\operatorname{tr}(T^3) = 0$ (zero 3-cycles), $\operatorname{offdiag}((T^2) \odot (T^2)^T - U^2) = 0$ (zero 4-cycles), and $\operatorname{tr}(T^5) = 0$ (zero 5-cycles).

### 1.3 Verified Artifact & Bound Comparison Table

| Cell `[z, r; g]` | Artifact (`claim/`) | Bytes | SHA-256 | Verified Order $N$ | `arXiv:2506.20003` Table 1 `[LB, UB]` | Reduction vs. Table 1 | `arXiv:2511.20286` Bound $2(q^2+q+1)$ | Reduction vs. `2511.20286` |
| :--- | :--- | ---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `[2, 7; 6]` | `claim/mixed_z2_r7_g6_N184.json` | `11,126` | `7783a2b9dcaf14fc309c663a27ac902e46db4a06bb77959fb7814be6fdcea2ab` | **`184`** | `123..196` | **`-12`** | `266` ($q=11$) | **`-82`** |
| `[2, 8; 6]` | `claim/mixed_z2_r8_g6_N234.json` | `15,728` | `879cb5f756b16355b5afb9eb6c9f182e43eccccebd7849cf395070822a051229` | **`234`** | `155..252` | **`-18`** | `266` ($q=11$) | **`-32`** |
| `[2, 9; 6]` | `claim/mixed_z2_r9_g6_N294.json` | `21,706` | `a61b36576b49191399e6881ad34153ac1b9b9893a4513252b583b34916078d93` | **`294`** | `191..320` | **`-26`** | `366` ($q=13$) | **`-72`** |
| `[2, 11; 6]` | `claim/mixed_z2_r11_g6_N450.json` | `39,066` | `c04fa003c1474a615f252960788061395ba80f6bf0681572cd048990467ead63` | **`450`** | `275..480` | **`-30`** | `514` / `546` ($q=16$) | **`-64` / `-96`** |
| `[1, 7; 6]` | `claim/mixed_z1_r7_g6_N146.json` | `21,580` | `1f3fade2c4218975762e06531ea5d37ae0611b8441d036701c05b1c1aced8b81` | **`146`** | `118..192` | **`-46`** | `146` ($q=8$) | `0` |

## 2. Verdict
All literal clauses of Partial Win `p2` in `claim/target.md` are satisfied across all four strictly novel `[2, r; 6]`-mixed cage upper bounds.

pass: true
