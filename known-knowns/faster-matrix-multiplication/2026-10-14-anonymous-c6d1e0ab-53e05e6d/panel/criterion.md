# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(15, 16, 17)` at Rank 2313 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/15x16x17_r2313_Q.json` (`751346` bytes, SHA-256 `53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/15x16x17_r2313_Q.json` (`751346` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2313 x 240`), `v` (`2313 x 272`), and `w` (`2313 x 255`) in `vocab_rle_v1` encoding with exact rational entries (`n = [15, 16, 17]`, `m = 2313`, `ring = "Q"`, `246`-entry rational vocabulary). All `2313` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(15, 16, 17)` (`15x16x17`), which satisfies `max(15, 16, 17) = 17` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2313`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2448` (`2313` is strictly below `2448`, saving `-135`).
     - `fmm.univ-lille.fr/15x16x17.html` (SHA-256 `b6058e267db3da9d9d069c8646d40e24f46b753bc22f76f8e86e546e1027103b`): rank `2448` (`2313` is strictly below `2448`, saving `-135`).
     - `TROPHY_CASE.md` prior for `(15, 16, 17)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/15x16x17_r2313_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 50400`, scaled numerator sum bound `S = 6016768627`, CRT bound `2 * L * (S + 1) = 606490277702400` with bit length `50`) and deterministically verifies all `240 * 272 * 255 = 16646400` Brent equations over `Q` via `2` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2313` is strictly below every listed rank (`2448`).
   - **Single format per claim**: This claim folder covers exclusively format `(15, 16, 17)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/15x16x17_r2313_Q.json (sha256 53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57, 751346 bytes) for format (15, 16, 17) with max dimension 17 in 17..32 and rank r = 2313, deterministically verified across all 16646400 Brent equations over Q and strictly beating fmm_sota.json (2448, margin -135) and fmm.univ-lille.fr/15x16x17.html (2448, margin -135).

pass: true
