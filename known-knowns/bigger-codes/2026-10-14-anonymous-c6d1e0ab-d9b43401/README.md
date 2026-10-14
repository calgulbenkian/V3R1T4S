# Binary Constant-Weight Code Record: `A(54, 8, 7) >= 4204`

## What

Explicit binary constant-weight code in claim/A54_8_7_4204.txt (sha256 d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca, 231220 bytes) establishing A(54, 8, 7) at least 4204 via 4204 distinct binary codewords of length 54 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 8834706 pairs and 147140 disjoint 4-subsets, below Johnson upper bound 8447), strictly beating Brouwer Andw.html (4173, +31), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (4193, +11).

In this package, the explicit codeword list is stored at `object/A54_8_7_4204.txt` (identical bytes, SHA-256 `d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca`, 231,220 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-d9b43401/`), run:

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
| Brouwer `Andw.html` | `A(54, 8, 7)` | `4173` | **`4204`** | **`+31`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(54, 8, 47)` | unlisted | **`4204`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(54, 8, 7)` | `4193` | **`4204`** | **`+11`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(54, 8, 7)` | none | **`4204`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(54, 8, 7)` | `4173` | **`4204`** | **`+31`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(54, 8, 7)` | none | **`4204`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(54, 8, 7) >= 4204` (and by bitwise complementation `A(54, 8, 47) >= 4204`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A54_8_7_4193.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
