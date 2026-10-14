# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(15, 15, 17)` at Rank 2257 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/15x15x17_r2257_Q.json` (`724999` bytes, SHA-256 `b9c2ff0681dca344541f2bb281f4fc6e7ebd9e3762160ba1a29f58a814f2d8af`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/15x15x17_r2257_Q.json` (`724999` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2257 x 225`), `v` (`2257 x 255`), and `w` (`2257 x 255`) in `vocab_rle_v1` encoding with exact rational entries (`n = [15, 15, 17]`, `m = 2257`, `ring = "Q"`, `292`-entry rational vocabulary). All `2257` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(15, 15, 17)` (`15x15x17`), which satisfies `max(15, 15, 17) = 17` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2257`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2320` (`2257` is strictly below `2320`, saving `-63`).
     - `fmm.univ-lille.fr/15x15x17.html` (SHA-256 `e7eb1b2f6a12f152870323127a4de1be12363ab2eb40c29075bb9d7caa1408fb`): rank `2320` (`2257` is strictly below `2320`, saving `-63`).
     - `TROPHY_CASE.md` prior for `(15, 15, 17)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/15x15x17_r2257_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 50400`, scaled numerator sum bound `S = 5923815402`, CRT bound `2 * L * (S + 1) = 597120592622400` with bit length `50`) and deterministically verifies all `225 * 255 * 255 = 14630625` Brent equations over `Q` via `2` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2257` is strictly below every listed rank (`2320`).
   - **Single format per claim**: This claim folder covers exclusively format `(15, 15, 17)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/15x15x17_r2257_Q.json (sha256 b9c2ff0681dca344541f2bb281f4fc6e7ebd9e3762160ba1a29f58a814f2d8af, 724999 bytes) for format (15, 15, 17) with max dimension 17 in 17..32 and rank r = 2257, deterministically verified across all 14630625 Brent equations over Q and strictly beating fmm_sota.json (2320, margin -63) and fmm.univ-lille.fr/15x15x17.html (2320, margin -63).

pass: true
