# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(17, 18, 18)` at Rank 2968 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/17x18x18_r2968_Q.json` (`250827` bytes, SHA-256 `4eb5b3ba86815ff31b05fbb949342c14d177914edd72c52b2d41937bd04c63c8`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/17x18x18_r2968_Q.json` (`250827` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2968 x 306`), `v` (`2968 x 324`), and `w` (`2968 x 306`) in `vocab_rle_b64_v1` encoding with exact rational entries (`n = [17, 18, 18]`, `m = 2968`, `ring = "Q"`, `570`-entry rational vocabulary). All `2968` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(17, 18, 18)` (`17x18x18`), which satisfies `max(17, 18, 18) = 18` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2968`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `3031` (`2968` is strictly below `3031`, saving `-63`).
     - `fmm.univ-lille.fr/17x18x18.html` (SHA-256 `99856ce47adbbaa431905b3dae7d37122cd9fde7fa6cf503025ad8b99ad931ae`): rank `3175` (`2968` is strictly below `3175`, saving `-207`).
     - `TROPHY_CASE.md` prior for `(17, 18, 18)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/17x18x18_r2968_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 242020800`, scaled numerator sum bound `S = 4346769824925`, CRT bound `2 * L * (S + 1) = 2104017420888900921600` with bit length `71`) and deterministically verifies all `306 * 324 * 306 = 30338064` Brent equations over `Q` via `3` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2968` is strictly below every listed rank (`3031`).
   - **Single format per claim**: This claim folder covers exclusively format `(17, 18, 18)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/17x18x18_r2968_Q.json (sha256 4eb5b3ba86815ff31b05fbb949342c14d177914edd72c52b2d41937bd04c63c8, 250827 bytes) for format (17, 18, 18) with max dimension 18 in 17..32 and rank r = 2968, deterministically verified across all 30338064 Brent equations over Q and strictly beating fmm_sota.json (3031, margin -63) and fmm.univ-lille.fr/17x18x18.html (3175, margin -207).

pass: true
