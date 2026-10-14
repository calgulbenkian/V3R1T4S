# Novelty Panel Report — Partial Win p1 on Erdos Problem #757 (erdos757-sidon-in-45-sets)

context: subagent
context: subagent (fable)
date_utc: 2026-10-14T04:14:55Z
target_id: erdos757-sidon-in-45-sets
claimed_object: claim/witness_n21_s12.json (SHA-256: 6478bc3cabcce580910f07fd9e3fee3a15d5b398ba12c9f9f557cfa7af7f2539)
claimed_bound: Partial Win p1 — explicit 21-element (4,5)-set A_21 of integers (size 21 not a multiple of 14) with certified exact maximum Sidon subset size s(A_21) = 12 and Sidon density ratio s(A_21)/|A_21| = 12/21 = 4/7

## 1. Honest Single-GET Live Fetch of Primary Sources

Each primary scoreboard, paper, and status table for `erdos757-sidon-in-45-sets` was fetched once via live HTTP GET (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

1. **Ma and Tang (Feb 2026), *Largest Sidon subsets in weak Sidon sets* (`arXiv:2602.23282`)**
   - URL: `https://arxiv.org/html/2602.23282`
   - Fetch Timestamp (UTC): `2026-10-14T04:14:34Z`
   - HTTP Status: `200` (61,806 bytes)
   - SHA-256: `d1aace4ca6e952deda0f2dbad7336e7e539b74c2e83eaef5a1954c2c1bd6bc29`
   - Extracted Standing Bound & Witness: Theorem 1.6 proves that the optimal Sidon subset density constant `c*` in `(4,5)`-sets satisfies `9/17` to `4/7` (i.e. `c*` is at least `9/17` and at most `4/7`). In Section 4, the upper bound `4/7` is witnessed on the 14-element set `A_14 = {0, 136, 200, 243, 246, 249, 272, 286, 298, 323, 400, 528, 596, 1056}` (`|A_14| = 14`, maximum Sidon subset `s(A_14) = 8`, ratio `8/14 = 4/7`), together with disjoint dilated/translated copies of cardinality `14k`.
   - Non-Multiple-of-14 Check: `arXiv:2602.23282` exhibits **only** `A_14` and disjoint affine blow-ups of size `14k`; it contains **no** `(4,5)`-set of cardinality `21` (or any cardinality not divisible by 14) achieving ratio `4/7`.

2. **Erdos Problems Page (#757)**
   - URL: `https://www.erdosproblems.com/757`
   - Fetch Timestamp (UTC): `2026-10-14T04:14:35Z`
   - HTTP Status: `200` (31,898 bytes)
   - SHA-256: `a870db664b368e2cfe99f1823ce790d1c561e3ee5f86b5ac7aa3e2f88ec7d48b`
   - Extracted Status: Problem #757 is listed as `OPEN`, recording the Gyarfas-Lehel (1995) bounds (`1/2` to `3/5`) and the Ma-Tang (2026) bounds (`9/17` to `4/7`). No witness with ratio strictly below `4/7` and no non-multiple-of-14 extremal witness at ratio `4/7` is listed.

3. **Tao Optimization Problems Benchmark Table (`constants/5b.html`)**
   - URL: `https://teorth.github.io/optimizationproblems/constants/5b.html`
   - Fetch Timestamp (UTC): `2026-10-14T04:14:36Z`
   - HTTP Status: `200` (2,705 bytes)
   - SHA-256: `c8fdf1c39dd9299201ab433554e909efa08ccb8c99df859e6a2fe3cd3d6330dc`
   - Extracted Table Entry for `C_5b` ("Sidon set density inside (4,5) sets"):
     - Known upper bounds: `1` (Trivial), `3/5 = 0.6` (`[GL95]`), `4/7 approx 0.5714` (`[MT26]`, Jie Ma and Quanyu Tang, `arXiv:2602.23282`, 2026).
     - Known lower bounds: `1/2` (`[GL95]`), `1/2 + 1/(141 * 76) approx 0.500093` (`[GL95]`), `9/17 approx 0.5294` (`[MT26]`).
   - Confirms `4/7` remains the live best upper bound ratio.

4. **EinsteinArena (`einsteinarena.com`)**
   - URL: `https://einsteinarena.com/`
   - Fetch Timestamp (UTC): `2026-10-14T04:14:36Z`
   - HTTP Status: `200` (90,744 bytes)
   - SHA-256: `67e90de63944f771ff96ccfc1121e13e546bd84cc59de0f3d9e32dec668bf53e`
   - Extracted Activity: Live scoreboard feed shows active submissions on Kissing Number (dim 12), Prime Number Theorem, Autocorrelation Inequalities, and Kakeya Needle; no public submission beats `4/7` or exhibits a size-21 extremal `(4,5)`-set.

## 2. Audit of `repo/TROPHY_CASE.md` and Open Pull Requests

- **`repo/TROPHY_CASE.md`**: Audited all 53 rows across all six result families in `repo/TROPHY_CASE.md` (degree-diameter graphs, constant-weight codes, Lehmer's totient problem, fast matrix multiplication, Bouchaudy commitments, VNN-COMP 2026, RobustBench CIFAR-100). There are **zero entries** for `erdos757-sidon-in-45-sets` or Erdos Problem #757 in `repo/TROPHY_CASE.md`.
- **Open Pull Requests**: Fetched `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` at `2026-10-14T04:14:37Z` (HTTP `200`, 539,314 bytes, SHA-256 `c60288a7f1e565592419e5cabe300a5ce44855e8559108543b7adb8bdee93bd9`). Exactly 28 open PRs exist (#1–#28: PRs #1 and #9 infrastructure fixes, PRs #2–#7 `fmm-catalogue-small-format-rank`, PRs #8 and #28 `constant-weight-codes`, PRs #10–#27 `fmm-additive-complexity-records`). **Zero open PRs** touch `erdos757-sidon-in-45-sets`.

## 3. Literature Search (2024–2026) and Partial Win `p1` Novelty Analysis

A comprehensive search of 2024–2026 literature on `(4,5)`-sets, weak Sidon sets, and Erdos Problem #757 confirms that:
1. The live best upper bound on `c*` is `4/7` (Ma and Tang, `arXiv:2602.23282`, Feb 2026). No subsequent paper or preprint has improved `4/7`.
2. In `claim/target.md`, Partial Win `p1` is explicitly defined as:
   - *"p1: A new extremal witness: a (4,5)-set A with |A| NOT a multiple of 14 (e.g. |A| = 21 with s = 12) whose certified exact maximum Sidon subset gives s/|A| exactly equal to the live best ratio (4/7 on 2026-10-03), verified by the same two-method pipeline. Disjoint unions of dilated copies of the Ma-Tang 14-set only reach multiples of 14, so this is a structurally new extremal example."*
3. The claimed witness `A_21 = {0, 1360, 2000, 2430, 2460, 2490, 2720, 2860, 2980, 3230, 4000, 5280, 5960, 9815, 10560, 11223, 11264, 11305, 12631, 13957, 16650}` in `claim/witness_n21_s12.json` (documented in `claim/claim.md`, `claim/status_record.md`, and `claim/REPRODUCE.md`) has cardinality `|A_21| = 21` (`21 mod 14 = 7`, not a multiple of 14), satisfies the `(4,5)`-set property on all 5,985 four-element subsets, and has exact maximum Sidon subset size `s(A_21) = 12`, giving `s(A_21)/|A_21| = 12/21 = 4/7`.
4. Neither `arXiv:2602.23282`, `erdosproblems.com/757`, `teorth/optimizationproblems`, `einsteinarena.com`, `repo/TROPHY_CASE.md`, nor any open PR contains a `(4,5)`-set of cardinality not divisible by 14 achieving the extremal Sidon density `4/7`.

## 4. Verdict

The claimed 21-element `(4,5)`-set `claim/witness_n21_s12.json` (`|A_21| = 21`, `s(A_21) = 12`, ratio `12/21 = 4/7`) is a genuinely new extremal construction not obtainable by disjoint unions of Ma and Tang's 14-element witness, and satisfies all novelty criteria for Partial Win `p1` on `erdos757-sidon-in-45-sets`.

pass: true
