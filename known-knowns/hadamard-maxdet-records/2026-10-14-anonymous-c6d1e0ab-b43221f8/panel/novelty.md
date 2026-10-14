context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: hadamard-maxdet-records
claim_id: claim_117

# Novelty Verification Report: Hadamard Maximal Determinant Record at Order `n = 117`

## 1. Executive Verdict

- **Claimed Record**: Explicit `117 x 117` matrix `X` with entries in `{-1, +1}` achieving normalized determinant `D(X) = |det X| / 2^116 = 324 * 29^57 = 73659860230620869930312403886045415232575930948902221537499019577403834332848324440116`.
- **Standing World Record (`D_rec(117)`)**: `72314994254613394470813334860641212637154205430658679584420251275641935854599391452615` (Tomas Rokicki, `best116.html`, listed in Orrick's MaxDet database `fullPage.shtml` and `d117.html` as `7.231499425E85 ??`).
- **Improvement Factor**: `D(X)` is strictly greater than `D_rec(117)` by a multiplicative factor of `1.018597332x` (`+1.860%`, an exact integer gain of `+1344865976007475459499069025404202595421725518243541953078768301761898478248932987501`), raising the Barba bound ratio from `0.718564` to `0.731929` (strictly below the Barba theoretical upper bound `B_norm(117) = 100637963222637963009859920958577753795295722943327423237910285617343105697857847003583`).
- **Certificate Artifact**: `claim/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt` (`33,517` bytes, SHA-256 `b43221f8bfb6744869262c930cb7e1845f3a285b7f636cac39cca47844a3a3bb`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_maxdet.py`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`CONFIRMED_SOLUTION`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary Hadamard maximal determinant sources and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for Order `n = 117` |
|---|---|---|---|---|---|---|
| `Math-AI-Caltech/hadamard-maxdet` (`README.md`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/README.md` | `2026-10-14T08:12:50Z` | `200` | `2,146` | `a445d9670ccb33c604865f9e19d5dc4b1487fee1c616e5ab6223a5feaaea4abd` | Covers only `n in {51, 103, 107, 111, 115, 119}` (`n == 3 mod 4`); no entry for `n = 117` |
| `Math-AI-Caltech/hadamard-maxdet` (`maxdet_records.csv`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:13:14Z` | `200` | `2,619` | `884d99a5b8ffd1a699a1f90b2f46b429323e7fc6fe3a037706dff5d8117ff2c9` | `7` rows (`n = 51, 103, 107, 111, 115, 119`); no entry for `n = 117` |
| Butbaia et al. (`arXiv:2608.22518v3` Abstract & HTML) | `https://arxiv.org/abs/2608.22518` and `https://arxiv.org/html/2608.22518v3` | `2026-10-14T08:12:51Z` / `2026-10-14T08:13:14Z` | `200` | `41,468` / `570,907` | `8aa955cef9b47849f450b118da542b8333a5e07c6ee70e93890b3d4575799a7a` / `ed31ecc98caead7d86d22447a70f8219e9c99048569ca1cc07c935ad4fee0bb6` | Improves only `n == 3 mod 4` orders (`51, 103, 107, 111, 115, 119`); untouched at `n = 117` |
| Orrick Archived MaxDet Master Table (`fullPage.shtml`) | `https://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/fullPage.shtml` | `2026-10-14T08:14:50Z` | `200` | `31,387` | `701a05c478cd042b7b5036ad776adf9a5a7384f031638e36c7bc1a91d9d19075` | Row `117`: `7.231499425E85 ??`, ratio `.72`, linking to `d117.html` |
| Orrick Archived Order-117 Page (`d117.html`) | `http://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/d117.html` | `2026-10-14T08:15:20Z` | `200` | `3,100` | `f1b542734f5347a52184e7f930e0cc03fcfcb569d03ad44eafaf3794cd1aa74b` | Credits Tomas Rokicki (`tomas.rokicki.com/newrec.html`) |
| Rokicki Live MaxDet Summary (`newrec.html`) | `http://tomas.rokicki.com/newrec.html` | `2026-10-14T08:14:50Z` | `200` | `7,212` | `35007699196345c796ff298e9ae74d0252216e9c552e46e98aaf4a9ff070083a` | Row `116` (`{0,1}` convention `m = n - 1 = 116`): `7.2315e+85`, linking to `matresults/best116.html` |
| Rokicki Live Order-117 Certificate (`matresults/best116.html`) | `https://tomas.rokicki.com/matresults/best116.html` | `2026-10-14T08:15:05Z` | `200` | `54,643` | `53d891db25bcdb56055edc10c13d3a92d0c07b3f5e96fd638032dfe88e9a9973` | Exact integer: `Determinant 72314994254613394470813334860641212637154205430658679584420251275641935854599391452615 (7.2315e+85)` |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:12:51Z` | `200` | `1,217,766` | `4ef8e0b25b415f0e0f15b984c95398abd0130f9fe0a0d97e22cf5929acf0a2c7` | `63` open PRs; `0` PRs on `hadamard-maxdet-records` or order `117` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `hadamard-maxdet-records`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, Zenodo (`zenodo.org/records/22024187`, HTTP `200`, `5,249` bytes, SHA-256 `d1f86d97ffe6b5045ceb90523ed089d995bab1f41970ced3bcaf01096259611b`), EinsteinArena (order-`51` challenge only), and GitHub confirm that Butbaia et al. (`arXiv:2608.22518v3`, 1 Oct 2026) improved only `n == 3 mod 4` dimensions (`51, 103, 107, 111, 115, 119`).
   - No published paper, preprint, or repository in 2024–2026 has improved order `n = 117` (`117 == 1 mod 4`) beyond Rokicki's standing value `72314994254613394470813334860641212637154205430658679584420251275641935854599391452615`.

---

## 4. Novelty Gate Conclusion

The explicit `117 x 117` `{-1, +1}` matrix in `claim/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt` achieves normalized determinant `324 * 29^57 = 73659860230620869930312403886045415232575930948902221537499019577403834332848324440116`, strictly exceeding the standing world record `72314994254613394470813334860641212637154205430658679584420251275641935854599391452615` across all live and archived MaxDet tables (`1.018597x`), with no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
