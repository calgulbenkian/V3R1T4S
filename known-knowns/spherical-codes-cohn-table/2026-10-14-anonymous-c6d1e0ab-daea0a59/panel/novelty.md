context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: spherical-codes-cohn-table
claim_id: claim_26_232

# Novelty Verification Report: Spherical Code `(d = 26, N = 232)` at `c* = 0.1619070097691030503945036`

## 1. Executive Verdict

- **Claimed Record**: Explicit spherical code of `N = 232` unit vectors in `R^26` (`32` significant digits per coordinate) whose 60-digit normalized maximum pairwise inner product (cosine of the minimal angle) is `c* = 0.1619070097691030503945036` (minimum angle `80.682396749666` degrees).
- **Standing World Record (`c_table`)**: `0.161911811246` on Henry Cohn's `spherical-codes.org` live table (`26,232,0.161911811246` in `/plain`; provenance on the HTML index: `"Vadim Borisov, 2026, https://numaro.tech/."`, with NO `&ast;` optimal mark and NO `'needs more optimization'` flag).
- **Improvement Margin**: `c_table - c* = 0.0000048014768969496054964` (`4.801477e-6`), which is strictly greater than the `10^-10` threshold by more than `48,014x`, and dimension `d = 26` is strictly outside the `9 to 23` kissing-number / Levenshtein exclusion zone.
- **Certificate Artifacts**: `claim/object/code_26_232.json` (`289,310` bytes, SHA-256 `daea0a5983ec270c1f14df3cec70d19d99199037aba112f4e1e8b05dd4748b37`) and `claim/object/code_26_232.txt` (`232,194` bytes, SHA-256 `06a5c05efea25f4d22eb947eedd81aea210912a3f818ad9c3264baf40dfd94d7`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_spherical.py`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`solution_claim`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary spherical code tables and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `(26, 232)` |
|---|---|---|---|---|---|---|
| Henry Cohn Spherical Codes HTML Index | `https://spherical-codes.org/` | `2026-10-14T08:39:49Z` | `200` | `4,734,460` | `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5` | `c_table = 0.161911811246`, `starred = false`, `needs_opt = false`, Provenance: `"Vadim Borisov, 2026, https://numaro.tech/."` |
| Henry Cohn Spherical Codes Plain CSV | `https://spherical-codes.org/plain` | `2026-10-14T08:39:51Z` | `200` | `402,199` | `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f` | `26,232,0.161911811246` |
| Baseline Coordinates Snapshot | `claim/data/codes/code_26_232.txt` (`https://spherical-codes.org/data/26/232`) | `2026-10-14T08:08:00Z` | `200` | `122,733` | `1a5ee92eb43a339991f8942f604f202ddc33bf994f4673b591c83ece516d69d7` | Recomputed 60-digit normalized `c_base` matches `0.161911811246` to `9.22e-13` (`base_ok = True`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:39:52Z` | `200` | `1,312,848` | `25918a88499ed6a0ffea061a979e7e4c2fcfafd4c9ef495f678768d3342d6e22` | `68` open PRs; `0` PRs on `spherical-codes-cohn-table` or `(26, 232)` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `spherical-codes-cohn-table`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, MIT DSpace, and `numaro.tech` (2024–2026) confirm that the standing `(26, 232)` entry `0.161911811246` on `spherical-codes.org` is already the 2026 record by Vadim Borisov (`numaro.tech`), and no newer paper or preprint supersedes it.

---

## 4. Novelty Gate Conclusion

The `232`-point spherical code in `R^26` certified in `claim/object/code_26_232.json` (`claim/object/code_26_232.txt`) achieves `c* = 0.1619070097691030503945036`, strictly lowering the live `spherical-codes.org` 2026 record `0.161911811246` by `4.801477e-6` on an unstarred row without `'needs more optimization'`, outside the kissing-number exclusion zone, and with no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
