# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(17, 17, 18)` at Rank 2916 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/17x17x18_r2916_Q.json` (`256295` bytes, SHA-256 `824d69340a8b90327a8efca36e336677839b0f1048f9cfe2459a00277f922d8d`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/17x17x18_r2916_Q.json` (`256295` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2916 x 289`), `v` (`2916 x 306`), and `w` (`2916 x 306`) in `vocab_rle_b64_v1` encoding with exact rational entries (`n = [17, 17, 18]`, `m = 2916`, `ring = "Q"`, `858`-entry rational vocabulary). All `2916` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(17, 17, 18)` (`17x17x18`), which satisfies `max(17, 17, 18) = 18` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2916`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `3012` (`2916` is strictly below `3012`, saving `-96`).
     - `fmm.univ-lille.fr/17x17x18.html` (SHA-256 `1d06bcc4193ff6f4da848aeb03f56b80a55eed64e0100105db61f62d71df4d8d`): rank `3080` (`2916` is strictly below `3080`, saving `-164`).
     - `TROPHY_CASE.md` prior for `(17, 17, 18)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/17x17x18_r2916_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 242020800`, scaled numerator sum bound `S = 4434917601863`, CRT bound `2 * L * (S + 1) = 2146684611874413542400` with bit length `71`) and deterministically verifies all `289 * 306 * 306 = 27060804` Brent equations over `Q` via `3` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2916` is strictly below every listed rank (`3012`).
   - **Single format per claim**: This claim folder covers exclusively format `(17, 17, 18)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/17x17x18_r2916_Q.json (sha256 824d69340a8b90327a8efca36e336677839b0f1048f9cfe2459a00277f922d8d, 256295 bytes) for format (17, 17, 18) with max dimension 18 in 17..32 and rank r = 2916, deterministically verified across all 27060804 Brent equations over Q and strictly beating fmm_sota.json (3012, margin -96) and fmm.univ-lille.fr/17x17x18.html (3080, margin -164).

pass: true
