# Binary Constant-Weight Code Record: `A(27, 8, 10) >= 1740`

## What

Explicit binary constant-weight code in claim/A27_8_10_1740.txt (sha256 bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe, 48720 bytes) establishing A(27, 8, 10) at least 1740 via 1740 distinct binary codewords of length 27 and Hamming weight 10 with minimum pairwise Hamming distance 8 (verified across all 1512930 pairs and 208800 disjoint 7-subsets, below Johnson upper bound 7020), strictly beating Brouwer Andw.html (1728, +12), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (1737, +3).

In this package, the explicit codeword list is stored at `object/A27_8_10_1740.txt` (identical bytes, SHA-256 `bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe`, 48,720 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-bdbf1cf2/`), run:

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
| Brouwer `Andw.html` | `A(27, 8, 10)` | `1728` | **`1740`** | **`+12`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(27, 8, 17)` | unlisted | **`1740`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(27, 8, 10)` | `1737` | **`1740`** | **`+3`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(27, 8, 10)` | none | **`1740`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(27, 8, 10)` | `1728` | **`1740`** | **`+12`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(27, 8, 10)` | none | **`1740`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(27, 8, 10) >= 1740` (and by bitwise complementation `A(27, 8, 17) >= 1740`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A27_8_10_1737.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
