# Criterion Skeptic Report (`fmm-catalogue-small-format-rank`)

context: subagent
target_id: fmm-catalogue-small-format-rank
confirmed_scope: The explicit rational bilinear matrix multiplication scheme in claim/13x15x15_r1763_Q.json (SHA-256 710c8ff6593f7c6e578a9ae83b4d7083ed5381db72fd734e614a3108d7c87465) is verified in exact rational arithmetic over ring Q to satisfy all 8,555,625 Brent equations for format (13, 15, 15) with tensor rank 1763, strictly beating all four criterion sources (fmm_sota.json at 1776, fmm.univ-lille.fr/13x15x15.html at 1797, Perminov FastMatrixMultiplication README.md ZT/Z/Q minimum at 1776 from 1797/1797/1776, and MerlijnW70/fmm-schemes with no entry).

## Clause-by-Clause Criterion Audit

1. **Explicit Bilinear Scheme & Format Eligibility**:
   - Artifact `claim/13x15x15_r1763_Q.json` (SHA-256 `710c8ff6593f7c6e578a9ae83b4d7083ed5381db72fd734e614a3108d7c87465`) provides explicit `u`, `v`, `w` factor matrices in `sparse_flat_pairs` encoding with `n = [13, 15, 15]`, `m = 1763`, and `ring = "Q"`.
   - All 1763 rows in `u` (width 195), `v` (width 225), and `w` (width 195) are non-zero rational vectors, giving `r = 1763` rank-one terms.
   - Format `(13, 15, 15)` satisfies `max(13, 15, 15) = 15` (at most 16) and `sorted(13, 15, 15) = (13, 15, 15)`, which is not in `{(3, 3, 3), (4, 4, 4)}`.

2. **Strict Rank Improvement Over All Four Criterion Scoreboards (Verified Live)**:
   - `sedoglavic/fmm_digest` (`fmm_sota.json`): lists `format: [13, 15, 15]`, `rank: 1776`. Claimed rank `1763` is strictly less than `1776` (margin `-13`).
   - Lille per-format catalogue page (`fmm.univ-lille.fr/13x15x15.html`): lists rank `1797`. Claimed rank `1763` is strictly less than `1797` (margin `-34`).
   - `dronperminov/FastMatrixMultiplication` (`README.md` `ZT / Z / Q` columns): lists `1797 (?) | 1797 (1803) | 1776 (1803)` (and `[1776](schemes/results/Q/13x15x15_m1776_Q.json)`), with minimum `min(1797, 1797, 1776) = 1776`. Claimed rank `1763` is strictly less than `1776` (margin `-13`).
   - `MerlijnW70/fmm-schemes` (`SHA256SUMS`): contains no scheme for `13x15x15` in any orientation.
   - Additional checks recorded in `claim/table_record.md` (`solven-eu/matmulcatalog` `COVERAGE.md` at `1797 / 1797`, repository trophy table with no `13x15x15` entry, and `0` open pull requests) confirm the minimum pre-existing rank across all sources is `1776`, which `r = 1763` beats strictly.

3. **Exact Arithmetic Verification & Ring Scope**:
   - Running `python3 claim/verify_brent.py claim/13x15x15_r1763_Q.json` (as specified in `claim/REPRODUCE.md`) parses every coefficient as an exact `fractions.Fraction` and verifies all `195 * 225 * 195 = 8,555,625` Brent equations over `Q` via Chinese Remainder Theorem over 2 primes near `2^30` (`log2_bound = 48`), returning `PASS file=13x15x15_r1763_Q.json format=13x15x15 rank=1763 primes=2 log2_bound=48`.
   - Because the scheme is valid over `Q` (characteristic 0), the `GF(2)`-only restriction does not apply (and `1763` is also strictly below the `F2` column value `1797` in `COVERAGE.md`).

4. **Non-Subsumption & Exclusion Checks**:
   - The submission claims a single format `(13, 15, 15)` and a single explicit scheme file `claim/13x15x15_r1763_Q.json`.
   - Because `r = 1763` is strictly less than every listed rank (`1776` and `1797`), it is not a composition, padding, or block-splitting matching an already listed rank.
   - It achieves a new overall minimum tensor rank over `Q` (`1763` vs `1776`), so it is neither a ternary/integer re-derivation of an existing `Q` rank (`fmm-ternary-integer-ring-upgrade`) nor an additive-complexity reduction at an existing rank (`fmm-additive-complexity-records`).

pass: true
