context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: hadamard-maxdet-records
claim_id: claim_p2_81

# Novelty Verification Report: Frozen Gram Target (`p2` Partial Win) at Order `n = 81`

## 1. Executive Verdict

- **Claimed Partial Win (`p2`)**: Explicit `81 x 81` symmetric positive-definite integer Gram matrix `G` with diagonal `81`, obeying all pairwise parity (`G_ij == 1 mod 2`) and triple mod-4 congruences (`G_ij + G_jk + G_ki + 81 == 0 mod 4`), passing constructive rational (Hasse-Minkowski) equivalence to `81 * I_81` (`Q Q^T = G` with denominator `10`, and `P (81 I_81) P^T = G` with denominator `90`), and accompanied by `80` explicit `{-1, +1}` rows (`80` is greater than or equal to `n - 2 = 79`) realizing `G[:80, :80]`.
- **Normalized Gram Determinant (`sqrt(det G) / 2^80`)**: `252 * 20^39 = 138538465099776000000000000000000000000000000000000000`.
- **Standing World Record (`D_rec(81)`)**: `196 * 20^39 = 107752139522048000000000000000000000000000000000000000` (listed in Orrick's MaxDet database `fullPage.shtml` and `d81.html` as `196 * 20^39 ??`, ratio `.77`).
- **Improvement Factor**: `sqrt(det G) / 2^80` is strictly greater than `D_rec(81)` by a multiplicative factor of `252 / 196 = 9 / 7 = 1.285714x` (`+28.571%`, so `det G` strictly exceeds `(det R_rec(81))^2` by `(9/7)^2 = 81/49 = 1.653061x`), and is strictly below the Barba theoretical upper bound (`sqrt(161) * 20^40 / 2^80 = 253.771551 * 20^39`, since `252^2 = 63,504` is strictly less than `161 * 20^2 = 64,400`).
- **Certificate Artifact**: `claim/G81_p2.json` (`192,478` bytes, SHA-256 `03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_maxdet.py`.
- **Novelty Status**: **CONFIRMED STRICT PARTIAL WIN (`CONFIRMED_PARTIAL`, `p2`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary Hadamard maximal determinant sources and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for Order `n = 81` |
|---|---|---|---|---|---|---|
| `Math-AI-Caltech/hadamard-maxdet` (`README.md`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/README.md` | `2026-10-14T08:12:50Z` | `200` | `2,146` | `a445d9670ccb33c604865f9e19d5dc4b1487fee1c616e5ab6223a5feaaea4abd` | Covers only `n in {51, 103, 107, 111, 115, 119}` (`n == 3 mod 4`); no entry for `n = 81` |
| `Math-AI-Caltech/hadamard-maxdet` (`maxdet_records.csv`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:13:14Z` | `200` | `2,619` | `884d99a5b8ffd1a699a1f90b2f46b429323e7fc6fe3a037706dff5d8117ff2c9` | `7` rows (`n = 51, 103, 107, 111, 115, 119`); no entry for `n = 81` |
| Butbaia et al. (`arXiv:2608.22518v3` Abstract & HTML) | `https://arxiv.org/abs/2608.22518` and `https://arxiv.org/html/2608.22518v3` | `2026-10-14T08:12:51Z` / `2026-10-14T08:13:14Z` | `200` | `41,468` / `570,907` | `8aa955cef9b47849f450b118da542b8333a5e07c6ee70e93890b3d4575799a7a` / `ed31ecc98caead7d86d22447a70f8219e9c99048569ca1cc07c935ad4fee0bb6` | Improves only `n == 3 mod 4` orders (`51, 103, 107, 111, 115, 119`); untouched at `n = 81` |
| Orrick Archived MaxDet Master Table (`fullPage.shtml`) | `https://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/fullPage.shtml` | `2026-10-14T08:14:50Z` | `200` | `31,387` | `701a05c478cd042b7b5036ad776adf9a5a7384f031638e36c7bc1a91d9d19075` | Row `81`: `196 * 20^39 ??`, ratio `.77`, linking to `d81.html` |
| Orrick Archived Order-81 Page (`d81.html`) | `http://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/d81.html` | `2026-10-14T08:13:48Z` | `200` | `10,167` | `e0f26c62ec6c1923021a7768956bf525f2e919bb57423f2cb327cac09a3ad169` | Standing normalized determinant `196 * 20^39 = 107752139522048000000000000000000000000000000000000000` |
| Rokicki Live MaxDet Summary (`newrec.html`) | `http://tomas.rokicki.com/newrec.html` | `2026-10-14T08:14:50Z` | `200` | `7,212` | `35007699196345c796ff298e9ae74d0252216e9c552e46e98aaf4a9ff070083a` | No entry for order `81` (`{0,1}` dimension `80`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:12:51Z` | `200` | `1,217,766` | `4ef8e0b25b415f0e0f15b984c95398abd0130f9fe0a0d97e22cf5929acf0a2c7` | `63` open PRs; `0` PRs on `hadamard-maxdet-records` or order `81` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `hadamard-maxdet-records`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, Zenodo (`zenodo.org/records/22024187`), EinsteinArena, and GitHub confirm that no published paper or dataset in 2024–2026 has improved the standing `n = 81` determinant `196 * 20^39 * 2^80` or published a frozen Gram target (`p2`) with `80` realized `{-1, +1}` rows and constructive rational congruence `P (81 I_81) P^T = G` achieving `sqrt(det G) / 2^80 = 252 * 20^39`.

---

## 4. Novelty Gate Conclusion

The frozen Gram target certificate in `claim/G81_p2.json` at order `n = 81` (`81 == 1 mod 4`, where the standing record `196 * 20^39` is strictly below the Barba bound) satisfies all requirements of Partial Win `p2`, strictly exceeds the square of the live record determinant by `(252/196)^2 = (9/7)^2 = 1.653061x`, and has no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
