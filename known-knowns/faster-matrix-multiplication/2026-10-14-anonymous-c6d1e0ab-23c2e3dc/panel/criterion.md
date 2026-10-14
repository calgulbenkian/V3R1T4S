# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Full Win) — Format `(15, 15, 16)` at Rank 2129 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/15x15x16_r2129_Q.json` (`717505` bytes, SHA-256 `23c2e3dca666f4b9e60a3f05f27534f98baba50c924b973bdc59a703f723450e`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Full Win) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/15x15x16_r2129_Q.json` (`717505` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2129 x 225`), `v` (`2129 x 240`), and `w` (`2129 x 240`) in `vocab_rle_v1` encoding with exact rational entries (`n = [15, 15, 16]`, `m = 2129`, `ring = "Q"`, `375`-entry rational vocabulary). All `2129` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` at most 16 and `sorted(n, m, p) not in {(3, 3, 3), (4, 4, 4)}` (Full Success Criterion)**:
   - **PASS.** The sorted format is `(15, 15, 16)` (`15x15x16`), which satisfies `max(15, 15, 16) = 16` (at most 16) and `(15, 15, 16) not in {(3, 3, 3), (4, 4, 4)}`.
3. **Number of rank-one terms `r` strictly less than ALL four live criterion sources and `TROPHY_CASE.md`**:
   - **PASS.** Here `r = 2129`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2132` (`2129` is strictly below `2132`, saving `-3`).
     - `fmm.univ-lille.fr/15x15x16.html` (SHA-256 `69f7757285fa5b71cff67e74cedef6f262f599c0858c6b251e67e5e427a6fc69`): rank `2132` (`2129` is strictly below `2132`, saving `-3`).
     - `dronperminov/FastMatrixMultiplication` `README.md` minimum over `ZT / Z / Q`: `2132` (`2129` is strictly below `2132`).
     - `MerlijnW70/fmm-schemes`: `unlisted`.
     - `TROPHY_CASE.md` prior for `(15, 15, 16)`: `unlisted` (`2129` is strictly below all prior records).
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/15x15x16_r2129_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 50400`, scaled numerator sum bound `S = 12192415004`, CRT bound `2 * L * (S + 1) = 1228995432504000` with bit length `51`) and deterministically verifies all `225 * 240 * 240 = 12960000` Brent equations over `Q` via `2` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2129` is strictly below every listed rank (`2132`).
   - **Single format per claim**: This claim folder covers exclusively format `(15, 15, 16)`.

## 2. Confirmed Scope

confirmed_scope: Full Win on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/15x15x16_r2129_Q.json (sha256 23c2e3dca666f4b9e60a3f05f27534f98baba50c924b973bdc59a703f723450e, 717505 bytes) for format (15, 15, 16) with rank r = 2129, deterministically verified across all 12960000 Brent equations over Q and strictly beating fmm_sota.json (2132, margin -3), fmm.univ-lille.fr/15x15x16.html (2132, margin -3), Perminov FastMatrixMultiplication min over ZT/Z/Q (2132), MerlijnW70/fmm-schemes (unlisted), and TROPHY_CASE.md (unlisted).

pass: true
