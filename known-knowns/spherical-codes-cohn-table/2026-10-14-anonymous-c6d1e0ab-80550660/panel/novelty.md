context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: spherical-codes-cohn-table
claim_id: claim_29_145

# Novelty Verification Report: Spherical Code `(d = 29, N = 145)` at `c* = 0.1106960891058149669538693`

## 1. Executive Verdict

- **Claimed Record**: Explicit spherical code of `N = 145` unit vectors in `R^29` (`32` significant digits per coordinate) whose 60-digit normalized maximum pairwise inner product (cosine of the minimal angle) is `c* = 0.1106960891058149669538693` (minimum angle `83.644556400262` degrees).
- **Standing World Record (`c_table`)**: `0.110701844288` on Henry Cohn's `spherical-codes.org` live table (`29,145,0.110701844288` in `/plain`; provenance on the HTML index: `"Vadim Borisov, 2026, https://numaro.tech/."`, with NO `&ast;` optimal mark and NO `'needs more optimization'` flag).
- **Improvement Margin**: `c_table - c* = 0.0000057551821850330461307` (`5.755182e-6`), which is strictly greater than the `10^-10` threshold by more than `57,551x`, and dimension `d = 29` is strictly outside the `9 to 23` kissing-number / Levenshtein exclusion zone.
- **Certificate Artifacts**: `claim/object/code_29_145.json` (`201,516` bytes, SHA-256 `80550660490b9e5148590d6e502ab71a9ed0067eb476238da3784ad47b23b083`) and `claim/object/code_29_145.txt` (`161,887` bytes, SHA-256 `4e4787fc145320dad4cc5361b10833df8c845a054ec69ee1562623bd728ffa8b`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_spherical.py`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`solution_claim`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary spherical code tables and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `(29, 145)` |
|---|---|---|---|---|---|---|
| Henry Cohn Spherical Codes HTML Index | `https://spherical-codes.org/` | `2026-10-14T08:39:49Z` | `200` | `4,734,460` | `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5` | `c_table = 0.110701844288`, `starred = false`, `needs_opt = false`, Provenance: `"Vadim Borisov, 2026, https://numaro.tech/."` |
| Henry Cohn Spherical Codes Plain CSV | `https://spherical-codes.org/plain` | `2026-10-14T08:39:51Z` | `200` | `402,199` | `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f` | `29,145,0.110701844288` |
| Baseline Coordinates Snapshot | `claim/data/codes/code_29_145.txt` (`https://spherical-codes.org/data/29/145`) | `2026-10-14T08:08:00Z` | `200` | `85,746` | `e57378f38ff4c7119ac96b2d48b18493e8e9d423861f92f87309610b82acb14d` | Recomputed 60-digit normalized `c_base` matches `0.110701844288` to `7.58e-13` (`base_ok = True`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:39:52Z` | `200` | `1,312,848` | `25918a88499ed6a0ffea061a979e7e4c2fcfafd4c9ef495f678768d3342d6e22` | `68` open PRs; `0` PRs on `spherical-codes-cohn-table` or `(29, 145)` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `spherical-codes-cohn-table`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, MIT DSpace, and `numaro.tech` (2024–2026) confirm that the standing `(29, 145)` entry `0.110701844288` on `spherical-codes.org` is already the 2026 record by Vadim Borisov (`numaro.tech`), and no newer paper or preprint supersedes it.

---

## 4. Novelty Gate Conclusion

The `145`-point spherical code in `R^29` certified in `claim/object/code_29_145.json` (`claim/object/code_29_145.txt`) achieves `c* = 0.1106960891058149669538693`, strictly lowering the live `spherical-codes.org` 2026 record `0.110701844288` by `5.755182e-6` on an unstarred row without `'needs more optimization'`, outside the kissing-number exclusion zone, and with no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
