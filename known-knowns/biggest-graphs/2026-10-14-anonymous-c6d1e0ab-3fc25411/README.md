# Degree-Diameter Record: `(Delta=14, D=3)` Graph on `N = 1,117` Vertices

## What

Explicit simple undirected graph in claim/G_14_3_N1117.edges (sha256 3fc25411941fa666946464317bc9672386a4923bcb01a24e2c42ec7239b8c3a4, 62388 bytes) for degree-diameter parameters (Delta=14, D=3) on N=1117 vertices and 7785 edges (0 loops, 0 multi-edges, degree distribution 68 of degree 13 and 1049 of degree 14, exact diameter 3 verified across all 1247689 ordered vertex pairs via all-pairs BFS, below Moore bound 2563), strictly beating the live Comellas general-graph table entry 1116 by +1 vertex (with no prior TROPHY_CASE.md or open PR entry for (14, 3)).

In this package, the explicit 0-indexed undirected edge list is stored at `object/G_14_3_N1117.edges` (and `object/G_14_3_N1117.txt`, identical bytes, SHA-256 `3fc25411941fa666946464317bc9672386a4923bcb01a24e2c42ec7239b8c3a4`, 62,388 bytes, `7,785` edges).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-3fc25411/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: < 1 second.
- **Expected last line**: `ALL CHECKS PASS: G_14_3_N1117.edges verified (Delta=14, D=3, N=1117 > 1116)`

## Compared To

All criterion sources were fetched live on `2026-10-14` (`07:37:19Z`-`07:37:21Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T07-37-19Z.json`):

| Source | Cell | Listed Order `N_0` | Our Graph Order `N` | Gain | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|
| Comellas General-Graph Table | `(14, 3)` | `1116` | **`1117`** | **`+1`** | `https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html` | `2026-10-14T07:37:19Z` |
| Comellas `D=3` Descriptions | `(14, 3)` | `1116` (`Dhar_1116`) | **`1117`** | **`+1`** | `https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html` | `2026-10-14T07:37:20Z` |
| `TROPHY_CASE.md` (`biggest-graphs`) | `(14, 3)` | unlisted | **`1117`** | — | `TROPHY_CASE.md` | `2026-10-14T07:37:21Z` |

## Not Claimed

- Scope: Constructive general undirected `(Delta=14, D=3)` graph of order `N = 1,117` (Moore bound `M(14, 3) = 2,563`). Does not claim optimality or vertex-transitivity.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive all-pairs BFS checkers (`verify_dd.py` and `ddcheck.c`) shipped here; not peer reviewed.

## Credits

- **F. Comellas & C. Dalfo**, *The Degree/Diameter Problem for General Graphs* (`https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html`).
- **D. Yugeswardeenoo** (`Dhar_1116`, Sept. 14, 2026): our construction warm-starts from the public `deg14_diam3_n1116_adjlist.txt` seed.
- Contributor credit: `anonymous-c6d1e0ab`.
