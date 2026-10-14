context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: hadamard-maxdet-records
claim_id: claim_105

# Novelty Verification Report: Hadamard Maximal Determinant Record at Order `n = 105`

## 1. Executive Verdict

- **Claimed Record**: Explicit `105 x 105` matrix `X` with entries in `{-1, +1}` achieving normalized determinant `D(X) = |det X| / 2^104 = 276 * 26^51 = 402299811033982511699641115457655638247621548505385285611140221022215602176`.
- **Standing World Record (`D_rec(105)`)**: `384743747284587846942188483608583600735563257274079045682562818122226665625` (Tomas Rokicki, `best104.html`, listed in Orrick's MaxDet database `fullPage.shtml` and `d105.html` as `3.847437473E74 ??`).
- **Improvement Factor**: `D(X)` is strictly greater than `D_rec(105)` by a multiplicative factor of `1.045630536x` (`+4.563%`, an exact integer gain of `+17556063749394664757452631849072037512058291231306239928577402899988936551`), raising the Barba bound ratio from `0.702238` to `0.734282` (strictly below the Barba theoretical upper bound `B_norm(105) = 547882258728472660210324664501712688349467880552241675318385825994770342169`).
- **Certificate Artifact**: `claim/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt` (`26,959` bytes, SHA-256 `eea4180adc25f6e40db1e7bac9a06f7b63183141abaadbdf7d44c83af403e50b`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_maxdet.py`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`CONFIRMED_SOLUTION`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary Hadamard maximal determinant sources and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for Order `n = 105` |
|---|---|---|---|---|---|---|
| `Math-AI-Caltech/hadamard-maxdet` (`README.md`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/README.md` | `2026-10-14T08:12:50Z` | `200` | `2,146` | `a445d9670ccb33c604865f9e19d5dc4b1487fee1c616e5ab6223a5feaaea4abd` | Covers only `n in {51, 103, 107, 111, 115, 119}` (`n == 3 mod 4`); no entry for `n = 105` |
| `Math-AI-Caltech/hadamard-maxdet` (`maxdet_records.csv`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:13:14Z` | `200` | `2,619` | `884d99a5b8ffd1a699a1f90b2f46b429323e7fc6fe3a037706dff5d8117ff2c9` | `7` rows (`n = 51, 103, 107, 111, 115, 119`); no entry for `n = 105` |
| Butbaia et al. (`arXiv:2608.22518v3` Abstract & HTML) | `https://arxiv.org/abs/2608.22518` and `https://arxiv.org/html/2608.22518v3` | `2026-10-14T08:12:51Z` / `2026-10-14T08:13:14Z` | `200` | `41,468` / `570,907` | `8aa955cef9b47849f450b118da542b8333a5e07c6ee70e93890b3d4575799a7a` / `ed31ecc98caead7d86d22447a70f8219e9c99048569ca1cc07c935ad4fee0bb6` | Improves only `n == 3 mod 4` orders (`51, 103, 107, 111, 115, 119`); untouched at `n = 105` |
| Orrick Archived MaxDet Master Table (`fullPage.shtml`) | `https://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/fullPage.shtml` | `2026-10-14T08:14:50Z` | `200` | `31,387` | `701a05c478cd042b7b5036ad776adf9a5a7384f031638e36c7bc1a91d9d19075` | Row `105`: `3.847437473E74 ??`, ratio `.70`, linking to `d105.html` |
| Orrick Archived Order-105 Page (`d105.html`) | `http://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/d105.html` | `2026-10-14T08:15:20Z` | `200` | `3,100` | `b36b226768312e26e8677f6c61f69871b9be71ef13f01581725ed6402d18d182` | Credits Tomas Rokicki (`tomas.rokicki.com/newrec.html`) |
| Rokicki Live MaxDet Summary (`newrec.html`) | `http://tomas.rokicki.com/newrec.html` | `2026-10-14T08:14:50Z` | `200` | `7,212` | `35007699196345c796ff298e9ae74d0252216e9c552e46e98aaf4a9ff070083a` | Row `104` (`{0,1}` convention `m = n - 1 = 104`): `3.84744e+74`, linking to `matresults/best104.html` |
| Rokicki Live Order-105 Certificate (`matresults/best104.html`) | `https://tomas.rokicki.com/matresults/best104.html` | `2026-10-14T08:15:04Z` | `200` | `44,022` | `89a0cb54a5c530666b5d0981948ca425069798cfc8cfc45ca8a14f6b943c85d7` | Exact integer: `Determinant 384743747284587846942188483608583600735563257274079045682562818122226665625 (3.84744e+74)` |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:12:51Z` | `200` | `1,217,766` | `4ef8e0b25b415f0e0f15b984c95398abd0130f9fe0a0d97e22cf5929acf0a2c7` | `63` open PRs; `0` PRs on `hadamard-maxdet-records` or order `105` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `hadamard-maxdet-records`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, Zenodo (`zenodo.org/records/22024187`, HTTP `200`, `5,249` bytes, SHA-256 `d1f86d97ffe6b5045ceb90523ed089d995bab1f41970ced3bcaf01096259611b`), EinsteinArena (which hosts only the order-`51` challenge), and GitHub confirm that Butbaia et al. (`arXiv:2608.22518v3`, 1 Oct 2026) improved only `n == 3 mod 4` dimensions (`51, 103, 107, 111, 115, 119`).
   - No published paper, preprint, or repository in 2024–2026 has improved order `n = 105` (`105 == 1 mod 4`) beyond Rokicki's standing value `384743747284587846942188483608583600735563257274079045682562818122226665625`.

---

## 4. Novelty Gate Conclusion

The explicit `105 x 105` `{-1, +1}` matrix in `claim/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt` achieves normalized determinant `276 * 26^51 = 402299811033982511699641115457655638247621548505385285611140221022215602176`, strictly exceeding the standing world record `384743747284587846942188483608583600735563257274079045682562818122226665625` across all live and archived MaxDet tables (`1.045631x`), with no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
