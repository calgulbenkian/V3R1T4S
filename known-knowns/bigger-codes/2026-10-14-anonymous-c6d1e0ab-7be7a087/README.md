# Binary Constant-Weight Code Record: `A(53, 8, 7) >= 3992`

## What

Explicit binary constant-weight code in claim/A53_8_7_3992.txt (sha256 7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29, 215568 bytes) establishing A(53, 8, 7) at least 3992 via 3992 distinct binary codewords of length 53 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 7966036 pairs and 139720 disjoint 4-subsets, below Johnson upper bound 8003), strictly beating Brouwer Andw.html (3980, +12), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (3987, +5).

In this package, the explicit codeword list is stored at `object/A53_8_7_3992.txt` (identical bytes, SHA-256 `7be7a08730ebb932aa2700285fab3cfcd0cd464759ca72013f3a238ee3a60a29`, 215,568 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-7be7a087/`), run:

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
| Brouwer `Andw.html` | `A(53, 8, 7)` | `3980` | **`3992`** | **`+12`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(53, 8, 46)` | unlisted | **`3992`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(53, 8, 7)` | `3987` | **`3992`** | **`+5`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(53, 8, 7)` | none | **`3992`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(53, 8, 7)` | `3980` | **`3992`** | **`+12`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(53, 8, 7)` | none | **`3992`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(53, 8, 7) >= 3992` (and by bitwise complementation `A(53, 8, 46) >= 3992`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A53_8_7_3987.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
