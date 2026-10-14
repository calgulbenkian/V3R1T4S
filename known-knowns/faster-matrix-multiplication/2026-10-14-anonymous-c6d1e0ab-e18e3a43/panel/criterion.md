# Criterion Skeptic Report: `fmm-catalogue-small-format-rank` (Partial Win p1) — Format `(16, 16, 17)` at Rank 2392 over `Q`

context: subagent

## 1. Clause-by-Clause Verification Against `claim/target.md`

We audit the claimed bilinear scheme artifact `claim/16x16x17_r2392_Q.json` (`976624` bytes, SHA-256 `e18e3a43ba7b29da2e9683b93ec8dcfabed75f35c4c6aa515dc8d7f7a4fe183b`), documented in `claim/CLAIM.md` and `claim/table_record.md` and reproducible via `claim/REPRODUCE.md` and `claim/verify_brent.py`, against every literal requirement of `fmm-catalogue-small-format-rank` (Partial Win p1) in `claim/target.md`:

1. **Explicit bilinear scheme `(u_k, v_k, w_k)_{k=1..r}`**:
   - **PASS.** `claim/16x16x17_r2392_Q.json` (`976624` bytes, strictly under the `1,000,000`-byte cap) stores explicit bilinear factor matrices `u` (`2392 x 256`), `v` (`2392 x 272`), and `w` (`2392 x 272`) in `vocab_rle_v1` encoding with exact rational entries (`n = [16, 16, 17]`, `m = 2392`, `ring = "Q"`, `209`-entry rational vocabulary). All `2392` factor triples `(u_k, v_k, w_k)` have strictly non-zero `u_k`, `v_k`, and `w_k`.
2. **Format `(n, m, p)` with `max(n, m, p)` in `17..32` (Partial Win `p1`)**:
   - **PASS.** The sorted format is `(16, 16, 17)` (`16x16x17`), which satisfies `max(16, 16, 17) = 17` in `17..32` (outside Perminov's 16x16x16 table and inside the Lille catalogue, claimed as Partial Win `p1` / `partial_win_claim`).
3. **Number of rank-one terms `r` strictly below live `fmm_sota.json` and `fmm.univ-lille.fr` per-format page (and `TROPHY_CASE.md`)**:
   - **PASS.** Here `r = 2392`. Per `claim/CLAIM.md` and `claim/table_record.md`:
     - `fmm_sota.json` (SHA-256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`): rank `2492` (`2392` is strictly below `2492`, saving `-100`).
     - `fmm.univ-lille.fr/16x16x17.html` (SHA-256 `86c19ca3ead6424fe55c8aaa03ac43a792756999ab1eec2d5660c429d2ced774`): rank `2560` (`2392` is strictly below `2560`, saving `-168`).
     - `TROPHY_CASE.md` prior for `(16, 16, 17)`: unlisted.
4. **Verified in exact arithmetic over the claimed ring `Q`**:
   - **PASS.** Running `claim/verify_brent.py` on `claim/16x16x17_r2392_Q.json` parses every entry as an exact `fractions.Fraction` (common term denominator LCM `L = 50400`, scaled numerator sum bound `S = 15573307352`, CRT bound `2 * L * (S + 1) = 1569789381182400` with bit length `51`) and deterministically verifies all `256 * 272 * 272 = 18939904` Brent equations over `Q` via `2` distinct 30-bit primes whose product strictly exceeds `2 * L * (S + 1)`.
5. **Exclusions & Null-Model / Subsumption Checks**:
   - **Not a GF(2)-only scheme**: Valid over characteristic-0 ring `Q`.
   - **Not a plain composition already listed at rank `r`, ring upgrade at an existing `Q` rank, or addition-reduction claim**: Rank `2392` is strictly below every listed rank (`2492`).
   - **Single format per claim**: This claim folder covers exclusively format `(16, 16, 17)`.

## 2. Confirmed Scope

confirmed_scope: Partial Win p1 on fmm-catalogue-small-format-rank is verified by the explicit exact rational (ring Q) bilinear scheme in claim/16x16x17_r2392_Q.json (sha256 e18e3a43ba7b29da2e9683b93ec8dcfabed75f35c4c6aa515dc8d7f7a4fe183b, 976624 bytes) for format (16, 16, 17) with max dimension 17 in 17..32 and rank r = 2392, deterministically verified across all 18939904 Brent equations over Q and strictly beating fmm_sota.json (2492, margin -100) and fmm.univ-lille.fr/16x16x17.html (2560, margin -168).

pass: true
