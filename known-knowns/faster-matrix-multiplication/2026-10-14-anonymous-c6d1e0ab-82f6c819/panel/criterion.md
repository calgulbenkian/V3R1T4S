# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` — Format `(13, 14, 15)` at Rank 1646 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed artifact `claim/13x14x15_r1646_Q.json` (SHA-256 `82f6c819ed1d02c0bd1aad307a76b7bea80f2852aeab041132f584c6e1800be2`), documented in `claim/CLAIM.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/13x14x15_r1646_Q.json` stores explicit bilinear factor matrices `u`, `v`, `w` in `sparse_flat_pairs` encoding with exact rational entries (`n = [13, 14, 15]`, `m = 1646`, `ring = "Q"`). All 1646 factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k` (length `13 * 14 = 182`), `v_k` (length `14 * 15 = 210`), and `w_k` (length `15 * 13 = 195`).
2. **Format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) not in {(3, 3, 3), (4, 4, 4)}`**:
   - **PASS.** The sorted format is `(13, 14, 15)`, which satisfies `max(13, 14, 15) = 15` (at most 16) and `(13, 14, 15) not in {(3, 3, 3), (4, 4, 4)}`.
3. **Number of rank-one terms `r` strictly less than ALL four live criterion sources and `TROPHY_CASE.md`**:
   - **PASS.** Here `r = 1646`. Per the live criterion sources recorded in `claim/CLAIM.md` (fetched `2026-10-14T02:29:22Z`):
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `1681` (`1646` is strictly below `1681`).
     - `fmm.univ-lille.fr/13x14x15.html` (SHA-256 `d2a562a11c213effc7df98468757cda923925f248fab408ed38c485039851158`): rank `1681` (`1646` is strictly below `1681`).
     - `dronperminov/FastMatrixMultiplication` `README.md` (SHA-256 `7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341`) minimum over `ZT / Z / Q`: `1681 / 1681 / 1681`, minimum `1681` (`1646` is strictly below `1681`).
     - `MerlijnW70/fmm-schemes` (SHA-256 `de848328881cf69cbe2a8d8309e04d94826cf1431b5b39e81db63f95af58a3fd`): no scheme for `(13, 14, 15)`.
     - `solven-eu/matmulcatalog` `COVERAGE.md` (SHA-256 `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`) `F2 / RQZ`: `1681 / 1681` (`1646` is strictly below `1681`).
     - `TROPHY_CASE.md` prior for `(13, 14, 15)`: rank `1677` (`1646` is strictly below `1677`).
     Thus `r = 1646` strictly improves upon the minimum across all four criterion sources (`1681`, improvement by `-35`) and strictly beats the prior `TROPHY_CASE.md` record (`1677`, improvement by `-31`).
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/13x14x15_r1646_Q.json` parses every entry as an exact `fractions.Fraction` (denominators in `{1, 2, 4, 5, 10, 17, 20, 25, 50, 80, 85, 100, 170, 200, 272, 320, 400, 640, 680, 1360, 3200, 5440}`, common term denominator LCM `L = 54400`, scaled numerator sum bound `S = 3255968430`, CRT bound `2 * L * (S + 1) = 354249365292800` with bit length `49`) and deterministically verifies all `(13 * 14) * (14 * 15) * (15 * 13) = 7,452,900` Brent equations over `Q` via two 30-bit primes whose product exceeds `2^59`, which strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: The scheme is valid over characteristic-0 ring `Q` and also strictly beats the `matmulcatalog` `F2` bound (`1646` vs `1681`).
   - **Not a listed composition, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `1646` is strictly below every listed external rank (`1681`) and prior Trophy Case rank (`1677`).
   - **Single format per claim**: This claim folder covers exclusively format `(13, 14, 15)`.

## 2. Confirmed Scope

confirmed_scope: Explicit exact rational (ring Q) bilinear matrix-multiplication scheme in claim/13x14x15_r1646_Q.json (sha256 82f6c819ed1d02c0bd1aad307a76b7bea80f2852aeab041132f584c6e1800be2) for format (13, 14, 15) with rank r = 1646, verified across all 7452900 Brent equations over Q and strictly beating fmm_sota.json (1681), fmm.univ-lille.fr (1681), Perminov FastMatrixMultiplication min over ZT/Z/Q (1681), MerlijnW70/fmm-schemes (unlisted), matmulcatalog F2/RQZ (1681), and TROPHY_CASE.md (1677).

pass: true
