# Novelty Panel Report — Largest Known (Delta=14, D=3) Graph on N = 1,117 Vertices

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T07:37:35Z
target_id: degree-diameter-table
claimed_object: claim/G_14_3_N1117.edges (62,388 bytes, SHA-256: 3fc25411941fa666946464317bc9672386a4923bcb01a24e2c42ec7239b8c3a4)
claimed_bound: explicit simple undirected graph on N = 1,117 vertices with maximum degree at most 14 and diameter at most 3

## 1. Honest Single-GET Live Fetch of Primary Scoreboards

Each primary degree-diameter status page and open pull-request listing was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Comellas General-Graph Degree-Diameter Table (`table_degree_diameter.html`)**
   - URL: `https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html`
   - Fetch Timestamp (UTC): `2026-10-14T07:37:19Z`
   - HTTP Status: `200` (47,580 bytes)
   - SHA-256: `69e48062289d175a9cc464a9110c3d4ea23ab28ccd26784e293b0415860c8cd6`
   - Extracted Cell for `(Delta = 14, D = 3)` (consistent with `claim/live_general_cells.json`):
     - Vertex Count (`N`): **1,116** (`raw: "1 116"`, background `99EF99`)
     - Boldface (Proven-Optimal) Status: `false` (Moore bound `M(14, 3) = 1 + 14 + 14*13 + 14*13^2 = 2,563`)
     - Cayley Flag: `false` (general undirected graph)

2. **Comellas Diameter-3 Construction Descriptions (`desc_g/desc_g3.html`)**
   - URL: `https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html`
   - Fetch Timestamp (UTC): `2026-10-14T07:37:20Z`
   - HTTP Status: `200` (49,120 bytes)
   - SHA-256: `0edff426ce79be1e8ba42d267ac7f3cf508609968efe15fcbe29ba04d369bf16`
   - Last Modification Recorded on Page: `October 6, 2026`
   - Extracted Section `DEGREE = 14, DIAM = 3`:
     - Current Record: `Dhar_1116` (`Degree = 14, Diameter = 3; Order = 1116; Moore bound = 2563`), contributed by Dharunish Yugeswardeenoo (Sept. 14, 2026; adjacency list `adjacencies/adjD3/deg14_diam3_n1116_adjlist.txt`), obtained by adding 28 vertices to R. Rajiv's 1,088-vertex `(14, 3)` graph.
     - Prior Entries Listed: Mark Marosi `graph_14_3_n1094.txt` (`N = 1,094`), R. Rajiv (`N = 1,088`), and V. Pelekhaty `n916d14k3.txt` (`N = 916`).

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows of `repo/TROPHY_CASE.md`. Rows 1–7 cover the `degree-diameter` family: `(15, 4)` at 13,365, `(15, 3)` at 1,620, `(14, 4)` at 8,424, `(9, 4)` at 1,700, `(13, 4)` at 6,630, `(13, 6)` at 535,495, and `(15, 6)` at 1,424,896. There is **no entry** for `(14, 3)` in `repo/TROPHY_CASE.md` (nor any entry exceeding 1,116 for `(14, 3)`).
- **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T07:37:21Z` (HTTP `200`, 1,141,792 bytes, SHA-256 `105434013401c9ebf0475bd2962199d24fedab119be3ef9edb080633377eaac8`). Exactly 59 open PRs exist (#1–#59); **zero open PRs** touch `degree-diameter-table`, `biggest-graphs`, or cell `(14, 3)`.

## 3. Literature Search (2024–2026)

Reviewed 2024–2026 literature and preprints on the degree-diameter problem, including:
- Cames van Batenburg & Korsky, *Asymptotically attaining the Moore bound* (`arXiv:2608.03965`, Aug 2026, partial-flag graphs `H_{k,q}`)
- Mizuno, *New lower bounds for the degree/diameter problem via interaction with a browser-accessible LLM* (`arXiv:2606.15860`, June 2026)
- Rajiv, Zenodo `10.5281/zenodo.23052995` (Sep 2026)
- Yugeswardeenoo, September 2026 submission `Dhar_1116` (`N = 1,116`) on the Comellas table
- Classical surveys and constructions by Miller & Siran (2013), Exoo & Jajcay, Delorme & Farhi (1984), and Comellas & Gomez

No published paper, preprint, or public repository constructs a `(Delta = 14, D = 3)` graph on more than **1,116** vertices. Our claimed graph `claim/G_14_3_N1117.edges` has **N = 1,117** vertices, strictly beating the best known order `1,116` by `+1` vertex while remaining strictly below the Moore bound `M(14, 3) = 2,563`.

## 4. Verdict

The claimed `(Delta = 14, D = 3)` graph `claim/G_14_3_N1117.edges` (documented in `claim/CLAIM.md`, `claim/target.md`, `claim/REPRODUCE.md`, and `claim/live_general_cells.json`) on **N = 1,117** vertices strictly exceeds the live Comellas general-graph table record (`1,116`, margin `+1` vertex), has no prior entry in `repo/TROPHY_CASE.md` or open pull requests, and beats all 2024–2026 literature.

pass: true
