# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` — Format `(14, 16, 16)` at Rank 2119 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed artifact `claim/14x16x16_r2119_Q.json` (SHA-256 `4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/14x16x16_r2119_Q.json` stores explicit bilinear factor matrices `u`, `v`, `w` in `vocab_rle_v1` encoding with exact rational entries (`n = [14, 16, 16]`, `m = 2119`, `ring = "Q"`, 482-entry rational vocabulary). All 2119 factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k` (length `14 * 16 = 224`), `v_k` (length `16 * 16 = 256`), and `w_k` (length `16 * 14 = 224`).
2. **Format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) not in {(3, 3, 3), (4, 4, 4)}`**:
   - **PASS.** The sorted format is `(14, 16, 16)`, which satisfies `max(14, 16, 16) = 16` (at most 16) and `(14, 16, 16) not in {(3, 3, 3), (4, 4, 4)}`.
3. **Number of rank-one terms `r` strictly less than ALL four live criterion sources and `TROPHY_CASE.md`**:
   - **PASS.** Here `r = 2119`. Per the live criterion sources recorded in `claim/CLAIM.md` (fetched `2026-10-14T02:29:22Z`):
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2128` (`2119` is strictly below `2128`).
     - `fmm.univ-lille.fr/14x16x16.html` (SHA-256 `c8a6c116b6746ef25ca4eef0978d38943716a647e68fd6b7ff3e36965cb8aeb8`): rank `2128` (`2119` is strictly below `2128`).
     - `dronperminov/FastMatrixMultiplication` `README.md` (SHA-256 `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`) minimum over `ZT / Z / Q`: `2180 / 2180 / 2128`, minimum `2128` (`2119` is strictly below `2128`).
     - `MerlijnW70/fmm-schemes` (SHA-256 `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`): no scheme for `(14, 16, 16)`.
     - `solven-eu/matmulcatalog` `COVERAGE.md` (SHA-256 `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`) `F2 / RQZ`: `2180 / 2180` (`2119` is strictly below `2180`).
     - `TROPHY_CASE.md` prior for `(14, 16, 16)`: none.
     Thus `r = 2119` strictly improves upon the minimum across all four criterion sources (`2128`, improvement by `-9`) and has no prior `TROPHY_CASE.md` entry.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/14x16x16_r2119_Q.json` parses every entry as an exact `fractions.Fraction` (denominators in `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 24, 30, 35, 36, 48, 60, 70, 72, 80, 84, 144, 175, 240, 288, 350}`, common term denominator LCM `L = 29030400`, scaled numerator sum bound `S = 373229652922`, CRT bound `2 * L * (S + 1) = 21670012232431718400` with bit length `65`) and deterministically verifies all `(14 * 16) * (16 * 16) * (16 * 14) = 12,845,056` Brent equations over `Q` via three 30-bit primes whose product exceeds `2^89`, which strictly exceeds `2 * L * (S + 1)`. (Note: `claim/CLAIM.md` line 4 contains a harmless prose typo listing `12902400` instead of `12845056` total Brent equations; `claim/verify_brent.py` checks all `12,845,056` equations determined by `n = [14, 16, 16]`.)
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: The scheme is valid over characteristic-0 ring `Q` and also strictly beats the `matmulcatalog` `F2` bound (`2119` vs `2180`).
   - **Not a listed composition, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2119` is strictly below every listed rank (`2128`) across all rings.
   - **Single format per claim**: This claim folder covers exclusively format `(14, 16, 16)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact rational (ring Q) bilinear matrix-multiplication scheme in claim/14x16x16_r2119_Q.json (sha256 4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56) for format (14, 16, 16) with rank r = 2119, verified across all 12845056 Brent equations over Q and strictly beating fmm_sota.json (2128), fmm.univ-lille.fr (2128), Perminov FastMatrixMultiplication min over ZT/Z/Q (2128), MerlijnW70/fmm-schemes (unlisted), matmulcatalog F2/RQZ (2180), and TROPHY_CASE.md (unlisted).

pass: true
