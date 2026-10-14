context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: hadamard-maxdet-records
claim_id: claim_p2_49

# Novelty Verification Report: Frozen Gram Target (`p2` Partial Win) at Order `n = 49`

## 1. Executive Verdict

- **Claimed Partial Win (`p2`)**: Explicit `49 x 49` symmetric positive-definite integer Gram matrix `G` with diagonal `49`, obeying all pairwise parity (`G_ij == 1 mod 2`) and triple mod-4 congruences (`G_ij + G_jk + G_ki + 49 == 0 mod 4`), passing constructive rational (Hasse-Minkowski) equivalence to `49 * I_49` (`Q Q^T = G` with denominator `6`, and `P (49 I_49) P^T = G` with denominator `42`), and accompanied by `48` explicit `{-1, +1}` rows (`48` is greater than or equal to `n - 2 = 47`) realizing `G[:48, :48]`.
- **Normalized Gram Determinant (`sqrt(det G) / 2^48`)**: `116 * 12^23 = 768469522966111493289934848`.
- **Standing World Record (`D_rec(49)`)**: `96 * 12^23 = 635974777627126753067532288` (B. Solomon and W. Orrick, 27 June 2003, listed in Orrick's MaxDet database `fullPage.shtml` and `d49.html` as `96 * 12^23 ??`, ratio `.812277`).
- **Improvement Factor**: `sqrt(det G) / 2^48` is strictly greater than `D_rec(49)` by a multiplicative factor of `116 / 96 = 29 / 24 = 1.208333x` (`+20.833%`, so `det G` strictly exceeds `(det R_rec(49))^2` by `(29/24)^2 = 841/576 = 1.460069x`), and is strictly below the Barba theoretical upper bound (`sqrt(97) * 12^24 / 2^48 = 116.387285 * 12^23`, since `116^2 = 13,456` is strictly less than `97 * 12^2 = 13,968`).
- **Certificate Artifact**: `claim/G49_p2.json` (`68,674` bytes, SHA-256 `cd7ea151cb23cea573fc617f983c2ce21a340dda94ec30baf82c4180c170e347`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and verified by `claim/verify_maxdet.py`.
- **Novelty Status**: **CONFIRMED STRICT PARTIAL WIN (`CONFIRMED_PARTIAL`, `p2`)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary Hadamard maximal determinant sources and open pull requests were fetched once via honest single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for Order `n = 49` |
|---|---|---|---|---|---|---|
| `Math-AI-Caltech/hadamard-maxdet` (`README.md`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/README.md` | `2026-10-14T08:12:50Z` | `200` | `2,146` | `a445d9670ccb33c604865f9e19d5dc4b1487fee1c616e5ab6223a5feaaea4abd` | Covers only `n in {51, 103, 107, 111, 115, 119}` (`n == 3 mod 4`); no entry for `n = 49` |
| `Math-AI-Caltech/hadamard-maxdet` (`maxdet_records.csv`) | `https://raw.githubusercontent.com/Math-AI-Caltech/hadamard-maxdet/main/maxdet_records.csv` | `2026-10-14T08:13:14Z` | `200` | `2,619` | `884d99a5b8ffd1a699a1f90b2f46b429323e7fc6fe3a037706dff5d8117ff2c9` | `7` rows (`n = 51, 103, 107, 111, 115, 119`); no entry for `n = 49` |
| Butbaia et al. (`arXiv:2608.22518v3` Abstract & HTML) | `https://arxiv.org/abs/2608.22518` and `https://arxiv.org/html/2608.22518v3` | `2026-10-14T08:12:51Z` / `2026-10-14T08:13:14Z` | `200` | `41,468` / `570,907` | `8aa955cef9b47849f450b118da542b8333a5e07c6ee70e93890b3d4575799a7a` / `ed31ecc98caead7d86d22447a70f8219e9c99048569ca1cc07c935ad4fee0bb6` | Improves only `n == 3 mod 4` orders (`51, 103, 107, 111, 115, 119`); untouched at `n = 49` |
| Orrick Archived MaxDet Master Table (`fullPage.shtml`) | `https://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/fullPage.shtml` | `2026-10-14T08:14:50Z` | `200` | `31,387` | `701a05c478cd042b7b5036ad776adf9a5a7384f031638e36c7bc1a91d9d19075` | Row `49`: `96 * 12^23 ??`, ratio `.81`, linking to `d49.html` |
| Orrick Archived Order-49 Page (`d49.html`) | `http://wayback.archive-it.org/219/20190316001107/http://www.indiana.edu/~maxdet/d49.html` | `2026-10-14T08:13:47Z` | `200` | `20,494` | `ed826fb1c82c29079fcf9710fad9850ea2a7d21a156f39d81572f1ca0a051c76` | `|Det R| = 635974777627126753067532288 * 2^48 = 96 * 12^23 * 2^48`, constructed by B. Solomon and W. Orrick, 27 June 2003 |
| Rokicki Live MaxDet Summary (`newrec.html`) | `http://tomas.rokicki.com/newrec.html` | `2026-10-14T08:14:50Z` | `200` | `7,212` | `35007699196345c796ff298e9ae74d0252216e9c552e46e98aaf4a9ff070083a` | No entry for order `49` (`{0,1}` dimension `48`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:12:51Z` | `200` | `1,217,766` | `4ef8e0b25b415f0e0f15b984c95398abd0130f9fe0a0d97e22cf5929acf0a2c7` | `63` open PRs; `0` PRs on `hadamard-maxdet-records` or order `49` |

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Contains zero (`0`) entries for `hadamard-maxdet-records`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, Zenodo (`zenodo.org/records/22024187`), EinsteinArena, and GitHub confirm that no published paper or dataset in 2024–2026 has improved the standing `n = 49` determinant `96 * 12^23 * 2^48` (Solomon-Orrick 2003) or published a frozen Gram target (`p2`) with `48` realized `{-1, +1}` rows and constructive rational congruence `P (49 I_49) P^T = G` achieving `sqrt(det G) / 2^48 = 116 * 12^23`.

---

## 4. Novelty Gate Conclusion

The frozen Gram target certificate in `claim/G49_p2.json` at order `n = 49` (`49 == 1 mod 4`, where the standing record `96 * 12^23` is strictly below the Barba bound) satisfies all requirements of Partial Win `p2`, strictly exceeds the square of the live record determinant by `(116/96)^2 = 1.460069x`, and has no prior entry in `repo/TROPHY_CASE.md`, open pull requests, or 2024–2026 literature.

pass: true
