context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: spherical-codes-cohn-table
claim_id: claim_28_70

# Novelty Verification Report: Spherical Code `(d = 28, N = 70)` at `c* = 0.0517863124041101353861329`

## 1. Executive Verdict

- **Claimed Record**: Explicit spherical code of `N = 70` unit vectors in `R^28` (`32` significant digits per coordinate) whose 60-digit normalized maximum pairwise inner product (cosine of the minimal angle) is `c* = 0.0517863124041101353861329` (minimum angle `87.031535037277` degrees).
- **Standing World Record (`c_table`)**: `0.051797462893` on Henry Cohn's `spherical-codes.org` live table (`28,70,0.051797462893` in `/plain`; provenance on the HTML index: `"Orthogonal union of 66 points in 26 dimensions and 4 points in 2 dimensions."`, with NO `&ast;` optimal mark and NO `'needs more optimization'` flag).
- **Improvement Margin**: `c_table - c* = 0.0000111504888898646138671` (`1.115049e-5`), which is strictly greater than the `10^-10` threshold by more than `111,504x`, and dimension `d = 28` is strictly outside the `9 to 23` kissing-number / Levenshtein exclusion zone.
- **Certificate Artifacts**: `claim/object/code_28_70.json` (`93,832` bytes, SHA-256 `cd7c56d206970b5e9b3b44ef5f31395908b4e84acf22f807c46a543556f05263`) and `claim/object/code_28_70.txt` (`75,309` bytes, SHA-256 `f6f1082ef27f21b7b885dcde6dec1daf4ed06c879a547b5732a011839779cc15`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_spherical.py`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`solution_claim`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary spherical code tables and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `(28, 70)` |
|---|---|---|---|---|---|---|
| Henry Cohn Spherical Codes HTML Index | `https://spherical-codes.org/` | `2026-10-14T08:39:49Z` | `200` | `4,734,460` | `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5` | `c_table = 0.051797462893`, `starred = false`, `needs_opt = false`, Provenance: `"Orthogonal union of 66 points in 26 dimensions and 4 points in 2 dimensions."` |
| Henry Cohn Spherical Codes Plain CSV | `https://spherical-codes.org/plain` | `2026-10-14T08:39:51Z` | `200` | `402,199` | `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f` | `28,70,0.051797462893` |
| Baseline Coordinates Snapshot | `claim/data/codes/code_28_70.txt` (`https://spherical-codes.org/data/28/70`) | `2026-10-14T08:08:00Z` | `200` | `36,279` | `b4fe496ca5198eb8b2420cb5041c8033ed380017145d09ff0ecd8266501a07a0` | Recomputed 60-digit normalized `c_base` matches `0.051797462893` to `6.13e-13` (`base_ok = True`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:39:52Z` | `200` | `1,312,848` | `25918a88499ed6a0ffea061a979e7e4c2fcfafd4c9ef495f678768d3342d6e22` | `68` open PRs; `0` PRs on `spherical-codes-cohn-table` or `(28, 70)` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `spherical-codes-cohn-table`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, MIT DSpace, and `numaro.tech` (2024–2026) confirm that Henry Cohn's `spherical-codes.org` table already incorporates the latest 2026 updates, and no newer paper or preprint supersedes `(d = 28, N = 70)` beyond `0.051797462893`.

---

## 4. Novelty Gate Conclusion

The `70`-point spherical code in `R^28` certified in `claim/object/code_28_70.json` (`claim/object/code_28_70.txt`) achieves `c* = 0.0517863124041101353861329`, strictly lowering the live `spherical-codes.org` record `0.051797462893` by `1.115049e-5` on an unstarred row without `'needs more optimization'`, outside the kissing-number exclusion zone, and with no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
