# Hadamard Maximal Determinant Record (`n=109`)

## What

Verified that claim/M109_2119202655125403624550373680790052808829003860176536932438843923020304438454497.txt (29,067 bytes, SHA-256 0108345c2f3cbffdd58f23eef8aba73546583f02062a013a5b64ab95e198faa6) is an explicit 109x109 {-1,+1} matrix with exact normalized determinant |det X| / 2^108 = 291 * 27^53 = 2119202655125403624550373680790052808829003860176536932438843923020304438454497, strictly improving by 1.128746x upon the standing Orrick/Rokicki and Math-AI-Caltech record 1877483841834222713683125485573890072927341503771574105042244268774869908324352 while remaining below the Barba bound.

In this package, the explicit artifact is stored at `object/M109_2119202655125403624550373680790052808829003860176536932438843923020304438454497.txt` (identical bytes, SHA-256 `0108345c2f3cbffdd58f23eef8aba73546583f02062a013a5b64ab95e198faa6`, 29,067 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-0108345c/`), run:

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
| Orrick / Rokicki MaxDet Archive | `n = 109` | `1877483841834222713683125485573890072927341503771574105042244268774869908324352` | **`2119202655125403624550373680790052808829003860176536932438843923020304438454497`** | `https://github.com/Math-AI-Caltech/hadamard-maxdet` | `2026-10-14T08:11:00Z` |
| `Math-AI-Caltech/hadamard-maxdet` (`arXiv:2608.22518`) | `n = 109` | `1877483841834222713683125485573890072927341503771574105042244268774869908324352` | **`2119202655125403624550373680790052808829003860176536932438843923020304438454497`** | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:11:00Z` |
| `TROPHY_CASE.md` | `n = 109` | unlisted | **`2119202655125403624550373680790052808829003860176536932438843923020304438454497`** | `TROPHY_CASE.md` | `2026-10-14T08:11:00Z` |

## Not Claimed

- Scope: Constructive `{-1,+1}` matrix determinant lower bound at order `n = 109`. Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Bareiss checker shipped here; not peer reviewed.

## Credits

- **W. P. Orrick & B. Solomon**, *The Hadamard Maximal Determinant Problem* (`indiana.edu/~maxdet`, Wayback archive) and **T. Rokicki** (`rokicki_best*.html`).
- **G. Butbaia et al.** (`Math-AI-Caltech/hadamard-maxdet`, `arXiv:2608.22518`).
- Contributor credit: `anonymous-c6d1e0ab`.
