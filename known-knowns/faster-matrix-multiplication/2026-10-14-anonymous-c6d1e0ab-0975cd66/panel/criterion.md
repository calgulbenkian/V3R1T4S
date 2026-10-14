# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(16, 18, 18)` at Rank 2900 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/16x18x18_r2900_Q.json` (`241556` bytes, SHA-256 `0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/16x18x18_r2900_Q.json` (`241556` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2900 x 288`), `v` (`2900 x 324`), and `w` (`2900 x 288`) in `vocab_rle_b64_v1` encoding with exact rational entries (`n = [16, 18, 18]`, `m = 2900`, `ring = "Q"`, `633`-entry rational vocabulary). All `2900` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(16, 18, 18)` (`16x18x18`), which satisfies `max(16, 18, 18) = 18` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2900`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2916` (`2900` is strictly below `2916`, saving `-16`).
     - `fmm.univ-lille.fr/16x18x18.html` (SHA-256 `bd47237d6ce7563726067407d49e177b0e889ad0ab3e0b104b0af142ac9bbc7d`): rank `2916` (`2900` is strictly below `2916`, saving `-16`).
     - `TROPHY_CASE.md` prior for `(16, 18, 18)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/16x18x18_r2900_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 242020800`, scaled numerator sum bound `S = 4361678740150`, CRT bound `2 * L * (S + 1) = 2111233956068674281600` with bit length `71`) and deterministically verifies all `288 * 324 * 288 = 26873856` Brent equations over `Q` via `3` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2900` is strictly below every listed rank (`2916`).
   - **Single format per claim**: This claim folder covers exclusively format `(16, 18, 18)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/16x18x18_r2900_Q.json (sha256 0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3, 241556 bytes) for format (16, 18, 18) with max dimension 18 in 17..32 and rank r = 2900, deterministically verified across all 26873856 Brent equations over Q and strictly beating fmm_sota.json (2916, margin -16) and fmm.univ-lille.fr/16x18x18.html (2916, margin -16).

pass: true
