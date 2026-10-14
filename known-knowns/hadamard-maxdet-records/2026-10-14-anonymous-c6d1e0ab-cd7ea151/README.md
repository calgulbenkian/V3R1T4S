# Hadamard Maximal Determinant Record (`n=49(p2)`)

## What

Verified that claim/G49_p2.json (68,674 bytes, SHA-256 cd7ea151cb23cea573fc617f983c2ce21a340dda94ec30baf82c4180c170e347) defines a valid Partial Win p2 (Frozen Gram Target) at order n = 49 consisting of a 49x49 symmetric positive-definite integer Gram matrix G with diagonal 49, valid pairwise and triple mod-4 congruences, exact normalized root-determinant sqrt(det G) / 2^48 = 116 * 12^23 = 768469522966111493289934848 strictly beating the live record 96 * 12^23 = 635974777627126753067532288, constructive exact rational congruence P (49 I_49) P^T = G (and Q Q^T = G), and 48 realized {-1,+1} rows M0 matching the leading 48x48 principal block of G.

In this package, the explicit artifact is stored at `object/G49_p2.json` (identical bytes, SHA-256 `cd7ea151cb23cea573fc617f983c2ce21a340dda94ec30baf82c4180c170e347`, 68,674 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-cd7ea151/`), run:

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
| Orrick / Rokicki MaxDet Archive | `n = 49` | `635974777627126753067532288` | **`768469522966111493289934848`** | `https://github.com/Math-AI-Caltech/hadamard-maxdet` | `2026-10-14T08:11:00Z` |
| `Math-AI-Caltech/hadamard-maxdet` (`arXiv:2608.22518`) | `n = 49` | `635974777627126753067532288` | **`768469522966111493289934848`** | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:11:00Z` |
| `TROPHY_CASE.md` | `n = 49` | unlisted | **`768469522966111493289934848`** | `TROPHY_CASE.md` | `2026-10-14T08:11:00Z` |

## Not Claimed

- Scope: Constructive Frozen Gram target (`p2` partial win) at order `n = 49`. Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Bareiss checker shipped here; not peer reviewed.

## Credits

- **W. P. Orrick & B. Solomon**, *The Hadamard Maximal Determinant Problem* (`indiana.edu/~maxdet`, Wayback archive) and **T. Rokicki** (`rokicki_best*.html`).
- **G. Butbaia et al.** (`Math-AI-Caltech/hadamard-maxdet`, `arXiv:2608.22518`).
- Contributor credit: `anonymous-c6d1e0ab`.
