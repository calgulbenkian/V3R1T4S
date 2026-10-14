# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(14, 16, 17)` at Rank 2261 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/14x16x17_r2261_Q.json` (`734551` bytes, SHA-256 `9daa4b495e91e98bb5da76cff692af959885766b07e33042b353e7ea94de7b3d`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/14x16x17_r2261_Q.json` (`734551` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2261 x 224`), `v` (`2261 x 272`), and `w` (`2261 x 238`) in `vocab_rle_v1` encoding with exact rational entries (`n = [14, 16, 17]`, `m = 2261`, `ring = "Q"`, `327`-entry rational vocabulary). All `2261` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(14, 16, 17)` (`14x16x17`), which satisfies `max(14, 16, 17) = 17` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2261`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2306` (`2261` is strictly below `2306`, saving `-45`).
     - `fmm.univ-lille.fr/14x16x17.html` (SHA-256 `e9063f905f3cb3741449575b2c85fd3bfad236f867b7116009a726c0b472a0f9`): rank `2306` (`2261` is strictly below `2306`, saving `-45`).
     - `TROPHY_CASE.md` prior for `(14, 16, 17)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/14x16x17_r2261_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 50400`, scaled numerator sum bound `S = 9623964382`, CRT bound `2 * L * (S + 1) = 970095609806400` with bit length `50`) and deterministically verifies all `224 * 272 * 238 = 14500864` Brent equations over `Q` via `2` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2261` is strictly below every listed rank (`2306`).
   - **Single format per claim**: This claim folder covers exclusively format `(14, 16, 17)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/14x16x17_r2261_Q.json (sha256 9daa4b495e91e98bb5da76cff692af959885766b07e33042b353e7ea94de7b3d, 734551 bytes) for format (14, 16, 17) with max dimension 17 in 17..32 and rank r = 2261, deterministically verified across all 14500864 Brent equations over Q and strictly beating fmm_sota.json (2306, margin -45) and fmm.univ-lille.fr/14x16x17.html (2306, margin -45).

pass: true
