# Binary Constant-Weight Code Record: `A(56, 8, 7) >= 4691`

## What

Explicit binary constant-weight code in claim/A56_8_7_4691.txt (sha256 e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1, 267387 bytes) establishing A(56, 8, 7) at least 4691 via 4691 distinct binary codewords of length 56 and Hamming weight 7 with minimum pairwise Hamming distance 8 (verified across all 11000395 pairs and 164185 disjoint 4-subsets, below Johnson upper bound 10264), strictly beating Brouwer Andw.html (4674, +17), arXiv:2607.19550/2608.13906/2609.35051, open PRs, and TROPHY_CASE.md (4685, +6).

In this package, the explicit codeword list is stored at `object/A56_8_7_4691.txt` (identical bytes, SHA-256 `e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1`, 267,387 bytes).

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-e12d11fa/`), run:

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
| Brouwer `Andw.html` | `A(56, 8, 7)` | `4674` | **`4691`** | **`+17`** | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| Brouwer `Andw.html` (complement) | `A(56, 8, 49)` | unlisted | **`4691`** | — | `https://aeb.win.tue.nl/codes/Andw.html` | `2026-10-14T07:29:12Z` |
| `TROPHY_CASE.md` (`bigger-codes`) | `A(56, 8, 7)` | `4685` | **`4691`** | **`+6`** | `TROPHY_CASE.md` | `2026-10-14T07:29:15Z` |
| Lysenstøen (`arXiv:2607.19550`) | `A(56, 8, 7)` | none | **`4691`** | — | `https://arxiv.org/abs/2607.19550` | `2026-10-14T07:29:14Z` |
| Echols (`arXiv:2608.13906`) | `A(56, 8, 7)` | `4674` | **`4691`** | **`+17`** | `https://arxiv.org/abs/2608.13906` | `2026-10-14T07:29:14Z` |
| Yang et al. (`arXiv:2609.35051`) | `A(56, 8, 7)` | none | **`4691`** | — | `https://arxiv.org/abs/2609.35051` | `2026-10-14T07:29:15Z` |

## Not claimed

- Scope: Constructive lower bound `A(56, 8, 7) >= 4691` (and by bitwise complementation `A(56, 8, 49) >= 4691`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive checker shipped here; not peer reviewed.

## Credits

- **A. E. Brouwer**, *Table of general binary codes / Bounds for binary constant weight codes* (`https://aeb.win.tue.nl/codes/Andw.html`).
- **V3R1T4S `bigger-codes` contributors** (`known-knowns/bigger-codes/`): our search warm-starts from `known-knowns/bigger-codes/codes/A56_8_7_4685.txt`.
- **W. Echols** (`arXiv:2608.13906`), **C. Lysenstøen** (`arXiv:2607.19550`), **Y. Yang et al.** (`arXiv:2609.35051`).
- Contributor credit: `anonymous-c6d1e0ab`.
