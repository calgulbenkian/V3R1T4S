context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: spherical-codes-cohn-table
claim_id: claim_30_117

# Novelty Verification Report: Spherical Code `(d = 30, N = 117)` at `c* = 0.0883794850648560216379989`

## 1. Executive Verdict

- **Claimed Record**: Explicit spherical code of `N = 117` unit vectors in `R^30` (`32` significant digits per coordinate) whose 60-digit normalized maximum pairwise inner product (cosine of the minimal angle) is `c* = 0.0883794850648560216379989` (minimum angle `84.929613100835` degrees).
- **Standing World Record (`c_table`)**: `0.088389506027` on Henry Cohn's `spherical-codes.org` live table (`30,117,0.088389506027` in `/plain`; provenance on the HTML index: `"Vadim Borisov, 2026, https://numaro.tech/."`, with NO `&ast;` optimal mark and NO `'needs more optimization'` flag).
- **Improvement Margin**: `c_table - c* = 0.0000100209621439783620011` (`1.002096e-5`), which is strictly greater than the `10^-10` threshold by more than `100,209x`, and dimension `d = 30` is strictly outside the `9 to 23` kissing-number / Levenshtein exclusion zone.
- **Certificate Artifacts**: `claim/object/code_30_117.json` (`168,214` bytes, SHA-256 `16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19`) and `claim/object/code_30_117.txt` (`135,176` bytes, SHA-256 `87acc4414d2af1ad497ce82d953dbfb17bbec1d2978be58bff6acc2793ef62f8`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_spherical.py`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`solution_claim`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary spherical code tables and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `(30, 117)` |
|---|---|---|---|---|---|---|
| Henry Cohn Spherical Codes HTML Index | `https://spherical-codes.org/` | `2026-10-14T08:39:49Z` | `200` | `4,734,460` | `28125e4ec7b2e17b4245f88dd930307d5926e8ec546c59ac1b7b5011a4b977d5` | `c_table = 0.088389506027`, `starred = false`, `needs_opt = false`, Provenance: `"Vadim Borisov, 2026, https://numaro.tech/."` |
| Henry Cohn Spherical Codes Plain CSV | `https://spherical-codes.org/plain` | `2026-10-14T08:39:51Z` | `200` | `402,199` | `750f0b4a872e68e53dd33f82deea554afc60963b2c1d558bc0db25757856244f` | `30,117,0.088389506027` |
| Baseline Coordinates Snapshot | `claim/data/codes/code_30_117.txt` (`https://spherical-codes.org/data/30/117`) | `2026-10-14T08:08:00Z` | `200` | `71,804` | `ffb27c245d8c7e669d3c8c0b502c381498520210887c6ae3ee96bce1f479406f` | Recomputed 60-digit normalized `c_base` matches `0.088389506027` to `4.64e-14` (`base_ok = True`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:39:52Z` | `200` | `1,312,848` | `25918a88499ed6a0ffea061a979e7e4c2fcfafd4c9ef495f678768d3342d6e22` | `68` open PRs; `0` PRs on `spherical-codes-cohn-table` or `(30, 117)` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `spherical-codes-cohn-table`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, MIT DSpace, and `numaro.tech` (2024–2026) confirm that the standing `(30, 117)` entry `0.088389506027` on `spherical-codes.org` is already the 2026 record by Vadim Borisov (`numaro.tech`), and no newer paper or preprint supersedes it.

---

## 4. Novelty Gate Conclusion

The `117`-point spherical code in `R^30` certified in `claim/object/code_30_117.json` (`claim/object/code_30_117.txt`) achieves `c* = 0.0883794850648560216379989`, strictly lowering the live `spherical-codes.org` 2026 record `0.088389506027` by `1.002096e-5` on an unstarred row without `'needs more optimization'`, outside the kissing-number exclusion zone, and with no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
