# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(14, 17, 17)` at Rank 2403 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/14x17x17_r2403_Q.json` (`821962` bytes, SHA-256 `b70300a45b0a9ae1de0ce9196b43e1c546a49f072943d9f90c139e2686c7ebb9`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/14x17x17_r2403_Q.json` (`821962` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2403 x 238`), `v` (`2403 x 289`), and `w` (`2403 x 238`) in `vocab_rle_v1` encoding with exact rational entries (`n = [14, 17, 17]`, `m = 2403`, `ring = "Q"`, `322`-entry rational vocabulary). All `2403` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(14, 17, 17)` (`14x17x17`), which satisfies `max(14, 17, 17) = 17` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2403`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2456` (`2403` is strictly below `2456`, saving `-53`).
     - `fmm.univ-lille.fr/14x17x17.html` (SHA-256 `17c39f116fe98fa4a887167817f47bceed390ce332a45eb6244a88d050804b62`): rank `2456` (`2403` is strictly below `2456`, saving `-53`).
     - `TROPHY_CASE.md` prior for `(14, 17, 17)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/14x17x17_r2403_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 50400`, scaled numerator sum bound `S = 8603804632`, CRT bound `2 * L * (S + 1) = 867263507006400` with bit length `50`) and deterministically verifies all `238 * 289 * 238 = 16370116` Brent equations over `Q` via `2` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2403` is strictly below every listed rank (`2456`).
   - **Single format per claim**: This claim folder covers exclusively format `(14, 17, 17)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/14x17x17_r2403_Q.json (sha256 b70300a45b0a9ae1de0ce9196b43e1c546a49f072943d9f90c139e2686c7ebb9, 821962 bytes) for format (14, 17, 17) with max dimension 17 in 17..32 and rank r = 2403, deterministically verified across all 16370116 Brent equations over Q and strictly beating fmm_sota.json (2456, margin -53) and fmm.univ-lille.fr/14x17x17.html (2456, margin -53).

pass: true
