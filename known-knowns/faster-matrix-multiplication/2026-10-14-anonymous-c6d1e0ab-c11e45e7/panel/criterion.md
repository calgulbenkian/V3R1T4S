# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` — Format `(14, 14, 15)` at Rank 1715 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed artifact `claim/14x14x15_r1715_Q.json` (SHA-256 `c11e45e7d7b5bd90af4d5d4f74e943bd76855bcf80599af30ffb64971485b417`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/14x14x15_r1715_Q.json` stores explicit bilinear factor matrices `u`, `v`, `w` in `sparse_flat_pairs` encoding with exact rational entries (`n = [14, 14, 15]`, `m = 1715`, `ring = "Q"`). All 1715 factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k` (length `14 * 14 = 196`), `v_k` (length `14 * 15 = 210`), and `w_k` (length `15 * 14 = 210`).
2. **Format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) not in {(3, 3, 3), (4, 4, 4)}`**:
   - **PASS.** The sorted format is `(14, 14, 15)`, which satisfies `max(14, 14, 15) = 15` (at most 16) and `(14, 14, 15) not in {(3, 3, 3), (4, 4, 4)}`.
3. **Number of rank-one terms `r` strictly less than ALL four live criterion sources and `TROPHY_CASE.md`**:
   - **PASS.** Here `r = 1715`. Per the live criterion sources recorded in `claim/CLAIM.md` (fetched `2026-10-14T02:29:22Z`):
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `1789` (`1715` is strictly below `1789`).
     - `fmm.univ-lille.fr/14x14x15.html` (SHA-256 `63ce18bf1085d0f315839876c397d7ff9bfe725fa5fd998883f382a14e6b907a`): rank `1798` (`1715` is strictly below `1798`).
     - `dronperminov/FastMatrixMultiplication` `README.md` (SHA-256 `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`) minimum over `ZT / Z / Q`: `1798 / 1798 / 1790`, minimum `1790` (`1715` is strictly below `1790`).
     - `MerlijnW70/fmm-schemes` (SHA-256 `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`): no scheme for `(14, 14, 15)`.
     - `solven-eu/matmulcatalog` `COVERAGE.md` (SHA-256 `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`) `F2 / RQZ`: `1798 / 1798` (`1715` is strictly below `1798`).
     - `TROPHY_CASE.md` prior for `(14, 14, 15)`: rank `1716` (`1715` is strictly below `1716`).
     Thus `r = 1715` strictly improves upon the minimum across all four criterion sources (`1789`, improvement by `-74`) and strictly beats the prior `TROPHY_CASE.md` record (`1716`, improvement by `-1`).
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/14x14x15_r1715_Q.json` parses every entry as an exact `fractions.Fraction` (denominators in `{1, 2, 5, 10, 17, 20, 25, 34, 50, 80, 85, 100, 170, 200, 272, 320, 400, 680, 1088, 1360, 3200, 5440}`, common term denominator LCM `L = 54400`, scaled numerator sum bound `S = 7087569934`, CRT bound `2 * L * (S + 1) = 771127608928000` with bit length `50`) and deterministically verifies all `(14 * 14) * (14 * 15) * (15 * 14) = 8,643,600` Brent equations over `Q` via two 30-bit primes whose product exceeds `2^59`, which strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: The scheme is valid over characteristic-0 ring `Q` and also strictly beats the `matmulcatalog` `F2` bound (`1715` vs `1798`).
   - **Not a listed composition, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `1715` is strictly below every listed external rank (`1789`) and prior Trophy Case rank (`1716`).
   - **Single format per claim**: This claim folder covers exclusively format `(14, 14, 15)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact rational (ring Q) bilinear matrix-multiplication scheme in claim/14x14x15_r1715_Q.json (sha256 c11e45e7d7b5bd90af4d5d4f74e943bd76855bcf80599af30ffb64971485b417) for format (14, 14, 15) with rank r = 1715, verified across all 8643600 Brent equations over Q and strictly beating fmm_sota.json (1789), fmm.univ-lille.fr (1798), Perminov FastMatrixMultiplication min over ZT/Z/Q (1790), MerlijnW70/fmm-schemes (unlisted), matmulcatalog F2/RQZ (1798), and TROPHY_CASE.md (1716).

pass: true
