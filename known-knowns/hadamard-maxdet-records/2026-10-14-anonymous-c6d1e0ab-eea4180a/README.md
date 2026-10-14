# Hadamard Maximal Determinant Record (`n=105`)

## What

Verified that claim/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt (26,959 bytes, SHA-256 eea4180adc25f6e40db1e7bac9a06f7b63183141abaadbdf7d44c83af403e50b) is an explicit 105x105 {-1,+1} matrix with exact normalized determinant |det X| / 2^104 = 276 * 26^51 = 402299811033982511699641115457655638247621548505385285611140221022215602176, strictly improving by 1.045631x upon the standing Orrick/Rokicki and Math-AI-Caltech record 384743747284587846942188483608583600735563257274079045682562818122226665625 while remaining below the Barba bound.

In this package, the explicit artifact is stored at `object/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt` (identical bytes, SHA-256 `eea4180adc25f6e40db1e7bac9a06f7b63183141abaadbdf7d44c83af403e50b`, 26,959 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-eea4180a/`), run:

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
| Orrick / Rokicki MaxDet Archive | `n = 105` | `384743747284587846942188483608583600735563257274079045682562818122226665625` | **`402299811033982511699641115457655638247621548505385285611140221022215602176`** | `https://github.com/Math-AI-Caltech/hadamard-maxdet` | `2026-10-14T08:11:00Z` |
| `Math-AI-Caltech/hadamard-maxdet` (`arXiv:2608.22518`) | `n = 105` | `384743747284587846942188483608583600735563257274079045682562818122226665625` | **`402299811033982511699641115457655638247621548505385285611140221022215602176`** | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:11:00Z` |
| `TROPHY_CASE.md` | `n = 105` | unlisted | **`402299811033982511699641115457655638247621548505385285611140221022215602176`** | `TROPHY_CASE.md` | `2026-10-14T08:11:00Z` |

## Not Claimed

- Scope: Constructive `{-1,+1}` matrix determinant lower bound at order `n = 105`. Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Bareiss checker shipped here; not peer reviewed.

## Credits

- **W. P. Orrick & B. Solomon**, *The Hadamard Maximal Determinant Problem* (`indiana.edu/~maxdet`, Wayback archive) and **T. Rokicki** (`rokicki_best*.html`).
- **G. Butbaia et al.** (`Math-AI-Caltech/hadamard-maxdet`, `arXiv:2608.22518`).
- Contributor credit: `anonymous-c6d1e0ab`.
