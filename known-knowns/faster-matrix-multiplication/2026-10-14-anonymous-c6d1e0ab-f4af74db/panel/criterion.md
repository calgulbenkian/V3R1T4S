# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(16, 17, 18)` at Rank 2850 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/16x17x18_r2850_Q.json` (`245889` bytes, SHA-256 `f4af74db369b2724e4ee67c937c5f66381994bfaf4fbfde4cce65da43d330773`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/16x17x18_r2850_Q.json` (`245889` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2850 x 272`), `v` (`2850 x 306`), and `w` (`2850 x 288`) in `vocab_rle_b64_v1` encoding with exact rational entries (`n = [16, 17, 18]`, `m = 2850`, `ring = "Q"`, `841`-entry rational vocabulary). All `2850` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(16, 17, 18)` (`16x17x18`), which satisfies `max(16, 17, 18) = 18` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2850`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2884` (`2850` is strictly below `2884`, saving `-34`).
     - `fmm.univ-lille.fr/16x17x18.html` (SHA-256 `b0a5bf46a84c41e7f6a9ed200e6d7c7766f5d97213ba4c16da6a0205410b65c3`): rank `2884` (`2850` is strictly below `2884`, saving `-34`).
     - `TROPHY_CASE.md` prior for `(16, 17, 18)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/16x17x18_r2850_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 242020800`, scaled numerator sum bound `S = 4370331438239`, CRT bound `2 * L * (S + 1) = 2115422221895990784000` with bit length `71`) and deterministically verifies all `272 * 306 * 288 = 23970816` Brent equations over `Q` via `3` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2850` is strictly below every listed rank (`2884`).
   - **Single format per claim**: This claim folder covers exclusively format `(16, 17, 18)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/16x17x18_r2850_Q.json (sha256 f4af74db369b2724e4ee67c937c5f66381994bfaf4fbfde4cce65da43d330773, 245889 bytes) for format (16, 17, 18) with max dimension 18 in 17..32 and rank r = 2850, deterministically verified across all 23970816 Brent equations over Q and strictly beating fmm_sota.json (2884, margin -34) and fmm.univ-lille.fr/16x17x18.html (2884, margin -34).

pass: true
