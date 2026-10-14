# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` — Format `(13, 13, 14)` at Rank 1499 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed artifact `claim/13x13x14_r1499_Q.json` (SHA-256 `d6ed9de8a92340b0c420c42344c915b8232853aef5ecee342fef7fa0c558a5f3`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/13x13x14_r1499_Q.json` stores explicit bilinear factor matrices `u`, `v`, `w` in `sparse_flat_pairs` encoding with exact rational entries (`n = [13, 13, 14]`, `m = 1499`, `ring = "Q"`). All 1499 factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k` (length `13 * 13 = 169`), `v_k` (length `13 * 14 = 182`), and `w_k` (length `14 * 13 = 182`).
2. **Format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) not in {(3, 3, 3), (4, 4, 4)}`**:
   - **PASS.** The sorted format is `(13, 13, 14)`, which satisfies `max(13, 13, 14) = 14` (at most 16) and `(13, 13, 14) not in {(3, 3, 3), (4, 4, 4)}`.
3. **Number of rank-one terms `r` strictly less than ALL four live criterion sources and `TROPHY_CASE.md`**:
   - **PASS.** Here `r = 1499`. Per the live criterion sources recorded in `claim/CLAIM.md` (fetched `2026-10-14T02:29:22Z`):
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `1511` (`1499` is strictly below `1511`).
     - `fmm.univ-lille.fr/13x13x14.html` (SHA-256 `60f9a6f7a1b36fb5c4e86c9111aee78abae17873544dcae7b98d0fff2ed70151`): rank `1511` (`1499` is strictly below `1511`).
     - `dronperminov/FastMatrixMultiplication` `README.md` (SHA-256 `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`) minimum over `ZT / Z / Q`: `1511 / 1511 / 1511`, minimum `1511` (`1499` is strictly below `1511`).
     - `MerlijnW70/fmm-schemes` (SHA-256 `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`): no scheme for `(13, 13, 14)`.
     - `solven-eu/matmulcatalog` `COVERAGE.md` (SHA-256 `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`) `F2 / RQZ`: `1511 / 1511` (`1499` is strictly below `1511`).
     - `TROPHY_CASE.md` prior for `(13, 13, 14)`: none.
     Thus `r = 1499` strictly improves upon the minimum across all four criterion sources (`1511`, improvement by `-12`) and has no prior `TROPHY_CASE.md` entry.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/13x13x14_r1499_Q.json` parses every entry as an exact `fractions.Fraction` (denominators in `{1, 2, 4, 5, 10, 17, 20, 25, 50, 80, 85, 100, 128, 170, 200, 272, 320, 400, 640, 680, 1088, 1360, 3200, 5440}`, common term denominator LCM `L = 54400`, scaled numerator sum bound `S = 6150690391`, CRT bound `2 * L * (S + 1) = 669195114649600` with bit length `50`) and deterministically verifies all `(13 * 13) * (13 * 14) * (14 * 13) = 5,597,956` Brent equations over `Q` via two 30-bit primes whose product exceeds `2^59`, which strictly exceeds `2 * L * (S + 1)`. (Note: `claim/CLAIM.md` line 4 contains a harmless prose typo listing `6147282` instead of `5597956` total Brent equations; `claim/verify_brent.py` checks all `5,597,956` equations determined by `n = [13, 13, 14]`.)
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: The scheme is valid over characteristic-0 ring `Q` and also strictly beats the `matmulcatalog` `F2` bound (`1499` vs `1511`).
   - **Not a listed composition, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `1499` is strictly below every listed rank (`1511`) across all rings.
   - **Single format per claim**: This claim folder covers exclusively format `(13, 13, 14)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact rational (ring Q) bilinear matrix-multiplication scheme in claim/13x13x14_r1499_Q.json (sha256 d6ed9de8a92340b0c420c42344c915b8232853aef5ecee342fef7fa0c558a5f3) for format (13, 13, 14) with rank r = 1499, verified across all 5597956 Brent equations over Q and strictly beating fmm_sota.json (1511), fmm.univ-lille.fr (1511), Perminov FastMatrixMultiplication min over ZT/Z/Q (1511), MerlijnW70/fmm-schemes (unlisted), matmulcatalog F2/RQZ (1511), and TROPHY_CASE.md (unlisted).

pass: true
