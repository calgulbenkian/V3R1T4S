# Binary Constant-Weight Code Record: `A(55, 8, 7) >= 4431`

## What

Explicit binary constant-weight code in claim/A55_8_7_4431.txt (sha256 37a7d62321644d15eb6d70962893f7fbbd59bb36b10230f74ac56902f21dc158, 248136 bytes) establishing A(55, 8, 7) at least 4431 via 4431 distinct binary codewords of length 55 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 9814665 pairs and 155085 disjoint 4-subsets, below Johnson upper bound 9687), strictly beating Brouwer Andw.html (4417, +14), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (4426, +5).

In this package, the explicit codeword list is stored at `object/A55_8_7_4431.txt` (identical bytes, SHA-256 `37a7d62321644d15eb6d70962893f7fbbd59bb36b10230f74ac56902f21dc158`, 248,136 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-37a7d623/`), run:

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
| Brouwer `Andw.html` | `A(55, 8, 7)` | `4417` | **`4431`** | **`+14`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(55, 8, 48)` | unlisted | **`4431`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(55, 8, 7)` | `4426` | **`4431`** | **`+5`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(55, 8, 7)` | none | **`4431`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(55, 8, 7)` | `4417` | **`4431`** | **`+14`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(55, 8, 7)` | none | **`4431`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(55, 8, 7) >= 4431` (and by bitwise complementation `A(55, 8, 48) >= 4431`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A55_8_7_4426.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
