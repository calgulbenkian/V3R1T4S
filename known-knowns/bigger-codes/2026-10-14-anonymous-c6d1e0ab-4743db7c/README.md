# Binary Constant-Weight Code Record: `A(52, 8, 7) >= 3802`

## What

Explicit binary constant-weight code in claim/A52_8_7_3802.txt (sha256 4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c, 201506 bytes) establishing A(52, 8, 7) at least 3802 via 3802 distinct binary codewords of length 52 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 7225701 pairs and 133070 disjoint 4-subsets, below Johnson upper bound 7577), strictly beating Brouwer Andw.html (3797, +5), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (3799, +3).

In this package, the explicit codeword list is stored at `object/A52_8_7_3802.txt` (identical bytes, SHA-256 `4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c`, 201,506 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-4743db7c/`), run:

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
| Brouwer `Andw.html` | `A(52, 8, 7)` | `3797` | **`3802`** | **`+5`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(52, 8, 45)` | unlisted | **`3802`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(52, 8, 7)` | `3799` | **`3802`** | **`+3`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(52, 8, 7)` | none | **`3802`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(52, 8, 7)` | `3797` | **`3802`** | **`+5`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(52, 8, 7)` | none | **`3802`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(52, 8, 7) >= 3802` (and by bitwise complementation `A(52, 8, 45) >= 3802`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A52_8_7_3799.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
