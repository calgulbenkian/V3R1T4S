# Binary Constant-Weight Code Record: `A(45, 8, 7) >= 1910`

## What

Explicit binary constant-weight code in claim/A45_8_7_1910.txt (sha256 e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966, 87860 bytes) establishing A(45, 8, 7) at least 1910 via 1910 distinct binary codewords of length 45 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 1823095 pairs and 66850 disjoint 4-subsets, below Johnson upper bound 4050), strictly beating Brouwer Andw.html (1904, +6), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (1907, +3).

In this package, the explicit codeword list is stored at `object/A45_8_7_1910.txt` (identical bytes, SHA-256 `e9a786a8af3ad130a62167977ca106c4f1ffc99d134f798959fafb319e21c966`, 87,860 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-e9a786a8/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: < 2 seconds.
- **Expected last line**: `ALL CHECKS PASS`

## Compared to

All criterion sources were fetched live on `2026-10-14` (`07:29:12Z`-`07:29:15Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T07-29-12Z.json`):

| Source | Cell | Listed Lower Bound | Our Code Size `M` | Gain | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|
| Brouwer `Andw.html` | `A(45, 8, 7)` | `1904` | **`1910`** | **`+6`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(45, 8, 38)` | unlisted | **`1910`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(45, 8, 7)` | `1907` | **`1910`** | **`+3`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(45, 8, 7)` | none | **`1910`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(45, 8, 7)` | `1904` | **`1910`** | **`+6`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(45, 8, 7)` | none | **`1910`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(45, 8, 7) >= 1910` (and by bitwise complementation `A(45, 8, 38) >= 1910`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A45_8_7_1907.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
