# Binary Constant-Weight Code Record: `A(35, 6, 6) >= 2218`

## What

Explicit binary constant-weight code in claim/A35_6_6_2218.txt (sha256 dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e, 79848 bytes) establishing A(35, 6, 6) at least 2218 via 2218 distinct binary codewords of length 35 and Hamming weight 6 with minimum pairwise Hamming distance 6 (verified across all 2458653 pairs and 33270 disjoint 4-subsets, below Johnson upper bound 3249), strictly beating Brouwer Andw.html (2209, +9), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (2217, +1).

In this package, the explicit codeword list is stored at `object/A35_6_6_2218.txt` (identical bytes, SHA-256 `dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e`, 79,848 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-dd2eb057/`), run:

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
| Brouwer `Andw.html` | `A(35, 6, 6)` | `2209` | **`2218`** | **`+9`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(35, 6, 29)` | unlisted | **`2218`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(35, 6, 6)` | `2217` | **`2218`** | **`+1`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(35, 6, 6)` | none | **`2218`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(35, 6, 6)` | `2209` | **`2218`** | **`+9`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(35, 6, 6)` | none | **`2218`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(35, 6, 6) >= 2218` (and by bitwise complementation `A(35, 6, 29) >= 2218`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A35_6_6_2217.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
