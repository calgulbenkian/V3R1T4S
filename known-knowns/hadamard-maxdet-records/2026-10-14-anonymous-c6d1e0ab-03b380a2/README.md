# Hadamard Maximal Determinant Record (`n=81(p2)`)

## What

Verified that claim/G81_p2.json (192,478 bytes, SHA-256 03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992) defines a valid Partial Win p2 (Frozen Gram Target) at order n = 81 consisting of an 81x81 symmetric positive-definite integer Gram matrix G with diagonal 81, valid pairwise and triple mod-4 congruences, exact normalized root-determinant sqrt(det G) / 2^80 = 252 * 20^39 = 138538465099776000000000000000000000000000000000000000 strictly beating the live record 196 * 20^39 = 107752139522048000000000000000000000000000000000000000, constructive exact rational congruence P (81 I_81) P^T = G (and Q Q^T = G), and 80 realized {-1,+1} rows M0 matching the leading 80x80 principal block of G.

In this package, the explicit artifact is stored at `object/G81_p2.json` (identical bytes, SHA-256 `03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992`, 192,478 bytes).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-03b380a2/`), run:

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
| Orrick / Rokicki MaxDet Archive | `n = 81` | `107752139522048000000000000000000000000000000000000000` | **`138538465099776000000000000000000000000000000000000000`** | `https://github.com/Math-AI-Caltech/hadamard-maxdet` | `2026-10-14T08:11:00Z` |
| `Math-AI-Caltech/hadamard-maxdet` (`arXiv:2608.22518`) | `n = 81` | `107752139522048000000000000000000000000000000000000000` | **`138538465099776000000000000000000000000000000000000000`** | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:11:00Z` |
| `TROPHY_CASE.md` | `n = 81` | unlisted | **`138538465099776000000000000000000000000000000000000000`** | `TROPHY_CASE.md` | `2026-10-14T08:11:00Z` |

## Not Claimed

- Scope: Constructive Frozen Gram target (`p2` partial win) at order `n = 81`. Does not claim proof of global optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exact Bareiss checker shipped here; not peer reviewed.

## Credits

- **W. P. Orrick & B. Solomon**, *The Hadamard Maximal Determinant Problem* (`indiana.edu/~maxdet`, Wayback archive) and **T. Rokicki** (`rokicki_best*.html`).
- **G. Butbaia et al.** (`Math-AI-Caltech/hadamard-maxdet`, `arXiv:2608.22518`).
- Contributor credit: `anonymous-c6d1e0ab`.
