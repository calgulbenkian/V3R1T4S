# Hadamard Maximal Determinant Record (`n=117`)

## What

Verified that claim/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt (33,517 bytes, SHA-256 b43221f8bfb6744869262c930cb7e1845f3a285b7f636cac39cca47844a3a3bb) is an explicit 117x117 {-1,+1} matrix with exact normalized determinant |det X| / 2^116 = 324 * 29^57 = 73659860230620869930312403886045415232575930948902221537499019577403834332848324440116, strictly improving by 1.018597x upon the standing Orrick/Rokicki and Math-AI-Caltech record 72314994254613394470813334860641212637154205430658679584420251275641935854599391452615 while remaining below the Barba bound.

In this package, the explicit artifact is stored at `object/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt` (identical bytes, SHA-256 `b43221f8bfb6744869262c930cb7e1845f3a285b7f636cac39cca47844a3a3bb`, 33,517 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-b43221f8/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: < 2 seconds.
- **Expected last line**: `ALL CHECKS PASS`

## Compared To

All criterion sources were fetched live on `2026-10-14` (`08:11:00Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T08-11-00Z.json`):

| Source | Order | Listed Normalized Value | Our Normalized Value | URL | UTC Fetch Time |
|---|---|---|---|---|---|
| Orrick / Rokicki MaxDet Archive | `n = 117` | `72314994254613394470813334860641212637154205430658679584420251275641935854599391452615` | **`73659860230620869930312403886045415232575930948902221537499019577403834332848324440116`** | `https://github.com/Math-AI-Caltech/hadamard-maxdet` | `2026-10-14T08:11:00Z` |
| `Math-AI-Caltech/hadamard-maxdet` (`arXiv:2608.22518`) | `n = 117` | `72314994254613394470813334860641212637154205430658679584420251275641935854599391452615` | **`73659860230620869930312403886045415232575930948902221537499019577403834332848324440116`** | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:11:00Z` |
| `TROPHY_CASE.md` | `n = 117` | unlisted | **`73659860230620869930312403886045415232575930948902221537499019577403834332848324440116`** | `TROPHY_CASE.md` | `2026-10-14T08:11:00Z` |

## Not Claimed

- Scope: Constructive `{-1,+1}` matrix determinant lower bound at order `n = 117`. Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Bareiss checker shipped here; not peer reviewed.

## Credits

- **W. P. Orrick & B. Solomon**, *The Hadamard Maximal Determinant Problem* (`indiana.edu/~maxdet`, Wayback archive) and **T. Rokicki** (`rokicki_best*.html`).
- **G. Butbaia et al.** (`Math-AI-Caltech/hadamard-maxdet`, `arXiv:2608.22518`).
- Contributor credit: `anonymous-c6d1e0ab`.
