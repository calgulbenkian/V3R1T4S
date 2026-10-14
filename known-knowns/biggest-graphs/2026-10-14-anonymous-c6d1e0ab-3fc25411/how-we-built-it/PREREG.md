# Lens 2 Pre-Registration: `attempts/c-evaluator-optimizer/`

## 1. Architecture & Hypothesis
We implement a native C (`cc -O3`) bit-parallel BFS evaluator and simulated annealing optimizer (`sa2_opt.c`) for degree-diameter slack-vertex insertion, redundant-edge pruning, and degree-preserving 2-switch / targeted shortcut rewiring.

### Core Algorithmic Components
1. **Bitset All-Pairs Evaluator (`full_eval_store`)**:
   - Represents the $N$-vertex reachability sets as $N \times W$ arrays of `uint64_t` words ($W = \lceil N / 64 \rceil$).
   - Computes exact all-pairs shortest-path balls up to radius $D$, stores the exact bitset `BAD[v]` of vertices at distance $ above  D$ from $v$, and maintains the list of unordered bad pairs $(p, q)$ ($p  under  q$).
2. **Slack-Aware Warm-Start Inserter (`initial_insert`)**:
   - Given a valid $(\Delta, D)$ graph on $N_0$ vertices, inserts $k \ge 1$ new vertices $z \in \{N_0, \dots, N_0 + k - 1\}$.
   - Greedily attaches each new vertex $z$ to existing vertices $v$ with free degree ($\deg(v)  under  \Delta$) maximizing the newly covered bits of $B_{G_0}(v, D-1)$.
   - If $z$ still requires edges after free slots are exhausted (or when instructed to subdivide), subdivides random existing edges $(a, b)$ maximizing $B_{G_0}(a, D-1) \cup B_{G_0}(b, D-1)$ coverage, and pairs up any remaining deficient slots.
3. **Simulated Annealing with Sound Early Screening (`sa2_run`)**:
   - **Move M1 (Free Chord Addition)**: Picks a random bad pair $(x, y)$ and adds an edge $(a, b)$ between two deficient vertices ($\deg  under  \Delta$) with $\text{dist}(x, a) + 1 + \text{dist}(b, y) \le D$. Updates `BAD` exactly in $O(|P_{\text{bad}}|)$ time without a full evaluation.
   - **Move M2 (Targeted Shortcut Rewire)**: Picks a random bad pair $(x, y)$, chooses $i \in \{0, \dots, D-1\}$ and $j = D - 1 - i$, picks $a$ with $\text{dist}(x, a) = i$ and $b$ with $\text{dist}(y, b) = j$, frees 1 slot at $a$ and/or $b$ if at max degree $\Delta$ by detaching an edge pointing away from $x$ or $y$, adds $(a, b)$, and optionally reconnects the detached endpoints $(c, d)$.
   - **Move M3 (Random 2-Switch)**: Picks two disjoint edges $(a, b), (c, d)$ and switches them to $(a, d), (c, b)$.
   - **Sound Screening**: Computes exact `gain` on bad pairs by BFS from endpoints of added edges and lower bound `Lp` on newly broken pairs by BFS from endpoints of removed edges; rejects immediately if `Lp - gain  above  -T ln(u)`.
4. **Redundant-Edge Pruner (`prune`)**:
   - Iterates over edges in random order and removes any edge whose deletion keeps all-pairs diameter $\le D$, freeing degree slack for subsequent vertex insertions.

## 2. Target Cells for `c-evaluator-optimizer`
- `(14, 3)`: starting from `deg14_diam3_n1116_adjlist.txt` ($N = 1,116$, 118 free degree-14 slots) $\to$ target $N \ge 1,117$.
- `(13, 3)`: starting from `deg13_diam3_n873_adjlist.txt` ($N = 873$, 117 free degree-13 slots) $\to$ target $N \ge 874$.
- `(11, 3)`: starting from `n715d11k3_adjlist.txt` ($N = 715$, 325 free degree-11 slots) $\to$ target $N \ge 716$.
- `(9, 3)`: starting from `n585d9k3_adjlist.txt` ($N = 585$, 65 free degree-9 slots) $\to$ target $N \ge 586$.
- `(11, 2)` and `(15, 2)`: starting from `deg11_diam2_n106_adjlist.txt` ($N = 106$) and `deg15_diam2_n190_adjlist.txt` ($N = 190$).
null_test: not needed because degree-diameter-table is an exact deterministic graph problem
