context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: spherical-codes-cohn-table
claim_id: claim_29_114

# Novelty Verification Report: Spherical Code `(d = 29, N = 114)` at `c* = 0.0886557493406558116735243`

## 1. Executive Verdict

- **Claimed Record**: Explicit spherical code of `N = 114` unit vectors in `R^29` (`32` significant digits per coordinate) whose 60-digit normalized maximum pairwise inner product (cosine of the minimal angle) is `c* = 0.0886557493406558116735243` (minimum angle `84.913721944786` degrees).
- **Standing World Record (`c_table`)**: `0.089759904426` on Henry Cohn's `spherical-codes.org` live table (`29,114,0.089759904426` in `/plain`; provenance on the HTML index: `"Orthogonal union of 112 points in 28 dimensions and 2 points in 1 dimension."`, with NO `&ast;` optimal mark and NO `'needs more optimization'` flag).
- **Improvement Margin**: `c_table - c* = 0.0011041550853441883264757` (`1.104155e-3`), which is strictly greater than the `10^-10` threshold by more than `11,041,550x`, and dimension `d = 29` is strictly outside the `9 to 23` kissing-number / Levenshtein exclusion zone.
- **Certificate Artifacts**: `claim/object/code_29_114.json` (`158,452` bytes, SHA-256 `8991f120f20e9464eeb266bc9e25cad1b440ad7d53d5dbbf21527a47685b3ccf`) and `claim/object/code_29_114.txt` (`127,286` bytes, SHA-256 `fd4e17f48c826275b2a087d3765e4f46394e2e5e6925864190ff5237cafd9108`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_spherical.py`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`solution_claim`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary spherical code tables and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `(29, 114)` |
|---|---|---|---|---|---|---|
| Henry Cohn Spherical Codes HTML Index | `https://spherical-codes.org/` | `2026-10-14T08:39:49Z` | `200` | `4,734,460` | `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5` | `c_table = 0.089759904426`, `starred = false`, `needs_opt = false`, Provenance: `"Orthogonal union of 112 points in 28 dimensions and 2 points in 1 dimension."` |
| Henry Cohn Spherical Codes Plain CSV | `https://spherical-codes.org/plain` | `2026-10-14T08:39:51Z` | `200` | `402,199` | `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f` | `29,114,0.089759904426` |
| Baseline Coordinates Snapshot | `claim/data/codes/code_29_114.txt` (`https://spherical-codes.org/data/29/114`) | `2026-10-14T08:08:00Z` | `200` | `64,888` | `00857fd20b6b32fc638d056fc4952d2bf7402c6296a479d1460e8610954dd0db` | Recomputed 60-digit normalized `c_base` matches `0.089759904426` to `1.30e-14` (`base_ok = True`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:39:52Z` | `200` | `1,312,848` | `25918a88499ed6a0ffea061a979e7e4c2fcfafd4c9ef495f678768d3342d6e22` | `68` open PRs; `0` PRs on `spherical-codes-cohn-table` or `(29, 114)` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `spherical-codes-cohn-table`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, MIT DSpace, and `numaro.tech` (2024–2026) confirm that Henry Cohn's `spherical-codes.org` table already incorporates the latest 2026 updates (including `"Henry Cohn, 2026"`, `"Antoine Jay, 2026"`, and `"Vadim Borisov, 2026, https://numaro.tech/"`), and no newer paper or preprint supersedes `(d = 29, N = 114)` beyond `0.089759904426`.

---

## 4. Novelty Gate Conclusion

The `114`-point spherical code in `R^29` certified in `claim/object/code_29_114.json` (`claim/object/code_29_114.txt`) achieves `c* = 0.0886557493406558116735243`, strictly lowering the live `spherical-codes.org` record `0.089759904426` by `1.104155e-3` on an unstarred row without `'needs more optimization'`, outside the kissing-number exclusion zone, and with no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
