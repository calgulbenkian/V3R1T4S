# Criterion Skeptic Report: `degree-diameter-table` — Largest Known `(Delta=14, D=3)` Graph (`N = 1,117`)

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed graph artifact `claim/G_14_3_N1117.edges` (`62,388` bytes, SHA-256 `3fc25411941fa666946464317bc9672386a4923bcb01a24e2c42ec7239b8c3a4`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md`, `claim/live_general_cells.json` (SHA-256 `d7c8986745ec3967bac7915035ce3e1ff0236d2a7db22d473fec10d5407e7c29`), and `claim/verify_dd.py` (SHA-256 `8464dd93d20ffcf7aa61895706852fb4847b0a422f98fd7a7390548f5e13dbff`), against every literal clause of the `degree-diameter-table` Full Success Criterion in `claim/target.md`:

1. **Clause (1): Explicit adjacency/edge list of a simple undirected graph `G` on `N` vertices**:
   - **PASS.** `claim/G_14_3_N1117.edges` (`62,388` bytes, strictly under the `1,000,000`-byte cap) specifies a simple undirected graph `G` on `N = 1,117` vertices (`0..1116`, `unused_labels = 0`, `unparsable_lines = 0`) with `7,785` undirected edges, `loops = 0`, and `duplicates = 0` (`0` multi-edges).

2. **Clause (2): Maximum degree at most `Delta`**:
   - **PASS.** For `Delta = 14`, every vertex of `G` has degree in `{13, 14}` (`mindeg = 13`, `maxdeg = 14`, degree histogram `{13: 68, 14: 1049}`, edge handshake check `(68 * 13 + 1049 * 14) / 2 = 15570 / 2 = 7785`), so `maxdeg = 14` is at most `Delta = 14`.

3. **Clause (3): `G` connected with diameter at most `D`, checked by all-pairs BFS**:
   - **PASS.** Exhaustive all-pairs BFS from all `1,117` vertices in `claim/verify_dd.py` confirms that `G` is connected and every ordered vertex pair `(u, v)` is at shortest-path distance at most `D = 3`:
     - `r = 0`: `1,117` ordered pairs
     - `r = 1`: `16,687` ordered pairs (`1,117 + 2 * 7,785 = 16,687`)
     - `r = 2`: `208,029` ordered pairs (`far_pairs_at_D_minus_1 = 1,247,689 - 208,029 = 1,039,660`, confirming the `D - 1 = 2` negative control rejects)
     - `r = 3`: `1,247,689 = 1,117^2` ordered pairs (`far_pairs_at_D = 0`, `exact_diameter = 3`).

4. **Clause (4): `N` strictly greater than the `(Delta, D)` entry of the live Comellas general-graph table (and not already in `TROPHY_CASE.md` or open PRs)**:
   - **PASS.** Per `claim/CLAIM.md` and `claim/live_general_cells.json` (fetched `2026-10-14T07:29:43Z` from `https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html`, HTML SHA-256 `69e48062289d175a9cc464a9110c3d4ea23ab28ccd26784e293b0415860c8cd6`), the live `(14, 3)` entry in the Comellas general undirected graph table is `1,116` (`raw: "∘  1 116"`, `bold: false`). Neither `TROPHY_CASE.md` nor any open pull request contains a `(14, 3)` entry (`trophy_case_entry = null`). Thus `N = 1,117` strictly beats the live general-graph table bound `1,116` by `+1` vertex.

5. **Clause (5): `N` at most the Moore bound `M(Delta, D)`, and `(Delta, D)` is not a boldface proven-optimal entry**:
   - **PASS.** The Moore bound for `(Delta = 14, D = 3)` is `M(14, 3) = 1 + 14 * (1 + 13 + 13^2) = 1 + 14 * 183 = 2,563`. Here `N = 1,117` is well below `2,563`, and cell `(14, 3)` has `live_bold_optimal = false`.

## 2. Confirmed Scope

confirmed_scope: Explicit simple undirected graph in claim/G_14_3_N1117.edges (sha256 3fc25411941fa666946464317bc9672386a4923bcb01a24e2c42ec7239b8c3a4, 62388 bytes) for degree-diameter parameters (Delta=14, D=3) on N=1117 vertices and 7785 edges (0 loops, 0 multi-edges, degree distribution 68 of degree 13 and 1049 of degree 14, exact diameter 3 verified across all 1247689 ordered vertex pairs via all-pairs BFS, below Moore bound 2563), strictly beating the live Comellas general-graph table entry 1116 by +1 vertex (with no prior TROPHY_CASE.md or open PR entry for (14, 3)).

pass: true
