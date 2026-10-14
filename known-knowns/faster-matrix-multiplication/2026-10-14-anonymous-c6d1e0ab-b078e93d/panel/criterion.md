# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(16, 17, 17)` at Rank 2553 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/16x17x17_r2553_Q.json` (`892727` bytes, SHA-256 `b078e93d7574b8328b1cf8f865170e2d8c337ccf09b1c8b29d13462a89481540`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/16x17x17_r2553_Q.json` (`892727` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2553 x 272`), `v` (`2553 x 289`), and `w` (`2553 x 272`) in `vocab_rle_v1` encoding with exact rational entries (`n = [16, 17, 17]`, `m = 2553`, `ring = "Q"`, `210`-entry rational vocabulary). All `2553` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(16, 17, 17)` (`16x17x17`), which satisfies `max(16, 17, 17) = 17` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2553`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2723` (`2553` is strictly below `2723`, saving `-170`).
     - `fmm.univ-lille.fr/16x17x17.html` (SHA-256 `429537cee7af459e1d38b0c175c38bf78af2432208610351a1b886e9c3e16efd`): rank `2738` (`2553` is strictly below `2738`, saving `-185`).
     - `TROPHY_CASE.md` prior for `(16, 17, 17)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/16x17x17_r2553_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 50400`, scaled numerator sum bound `S = 7895173252`, CRT bound `2 * L * (S + 1) = 795833463902400` with bit length `50`) and deterministically verifies all `272 * 289 * 272 = 21381376` Brent equations over `Q` via `2` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2553` is strictly below every listed rank (`2723`).
   - **Single format per claim**: This claim folder covers exclusively format `(16, 17, 17)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/16x17x17_r2553_Q.json (sha256 b078e93d7574b8328b1cf8f865170e2d8c337ccf09b1c8b29d13462a89481540, 892727 bytes) for format (16, 17, 17) with max dimension 17 in 17..32 and rank r = 2553, deterministically verified across all 21381376 Brent equations over Q and strictly beating fmm_sota.json (2723, margin -170) and fmm.univ-lille.fr/16x17x17.html (2738, margin -185).

pass: true
