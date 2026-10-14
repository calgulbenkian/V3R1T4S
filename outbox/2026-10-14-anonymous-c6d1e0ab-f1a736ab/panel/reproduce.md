# Reproduction & Independent Verification Report: `snake-coil-in-the-box`

context: subagent (astra)
role: REPRODUCE skeptic
target: snake-coil-in-the-box
submission_type: PARTIAL_PROGRESS (Milestones p1, p2, and p3)

## 1. Quoted Mathematical Definitions from `claim/target.md` and `claim/CLAIM.md`

From `claim/target.md` (`success_criterion` and `partial_wins`):
- **Induced path (snake) and induced cycle (coil) in `Q_n`**:
  "Success means a valid induced path (snake) or induced cycle (coil) in Q_n, 9 at most n at most 13, verified exhaustively (single-bit steps, distinct vertices, popcount(v_i ^ v_j) at least 2 for non-consecutive pairs, closing edge induced for coils), whose edge length is STRICTLY GREATER (direction: max) than the maximum, at verification time, of: the live primary table https://www.minortriad.com/snake/, the Math-AI-Caltech/Snake-in-the-Box README 'subsequent bounds by others' lists (https://github.com/Math-AI-Caltech/Snake-in-the-Box), the latest arXiv:2607.15270 version, the EinsteinArena value (13D snake) and any newer source from a fresh search, for that dimension and type (context on 2026-10-03: snakes Q9-Q13 191/379/750/1480/2938, coils 192/374/740/1468/2930). The verifier's checker must reproduce the exact length of at least one downloaded record file of the same n and type (length-convention calibration); without that calibration the claim is not a record."
- **Milestone `p1` (Symmetric-coil record)**:
  "A symmetric-coil record: a coil in Q_n (9 at most n at most 13) that is invariant under the symmetry required by the minortriad symmetric-coil table, verified exhaustively, whose length strictly exceeds the live minortriad symmetric-coil value for that n (context: Q9 186, Q10 370, Q11 730, Q12 1434, Q13 2830)."
- **Milestone `p2` (`Q_14` record)**:
  "A Q14 record: a snake or coil in Q14, verified exhaustively, strictly longer than every Q14 value published at verification time (arXiv:2607.15270 v3 tables, EinsteinArena, Math-AI-Caltech repo); counts only if such a published value exists for comparison."
- **Milestone `p3` (Canonical transition sequence inequivalence)**:
  "An equal-record snake or coil: length equal to the live record (as defined in the success criterion) for that n and type, 9 at most n at most 13, verified exhaustively, and inequivalent under hypercube automorphisms (coordinate permutations and translations) and reversal (plus cyclic rotation for coils) to every record file published in the Math-AI-Caltech repository and the arXiv:2607.15270 data at verification time, checked by comparing canonical relabelled transition sequences."

From `claim/CLAIM.md` (Section 2):
- **Milestone `p1`**: `claim/sym_coil_Q12_1450.txt` (`Q_12` symmetric coil, `L = 1450` vs `1434`, `+16` edges) and `claim/sym_coil_Q13_2870.txt` (`Q_13` symmetric coil, `L = 2870` vs `2830`, `+40` edges), plus secondary `claim/sym_coil_Q13_2846.txt` (`L = 2846`, `+16` edges).
- **Milestone `p2`**: `claim/coil_Q14_5854.txt` (`Q_14` coil, `L = 5854` vs `5750`, `+104` edges) and `claim/snake_Q14_5854.txt` (`Q_14` snake, `L = 5854` vs `5850`, `+4` edges), plus intermediate `claim/coil_Q13_2928.txt` (`Q_13` coil, `L = 2928`).
- **Milestone `p3`**: `claim/inequiv_co10_374.txt` (`Q_10` coil, `L = 374`), `claim/inequiv_co11_740.txt` (`Q_11` coil, `L = 740`), `claim/inequiv_co12_1468.txt` (`Q_12` coil, `L = 1468`), `claim/inequiv_co13_2930.txt` (`Q_13` coil, `L = 2930`), `claim/inequiv_sn11_750.txt` (`Q_11` snake, `L = 750`), `claim/inequiv_sn12_1480.txt` (`Q_12` snake, `L = 1480`), and `claim/inequiv_sn13_2946.txt` (`Q_13` snake, `L = 2946`).

---

## 2. Independent Verification Before Reading `claim/verify_snake.py`

Before viewing `claim/verify_snake.py`, I wrote and executed an independent Python verifier from scratch directly from the hypercube graph definition on `Q_n = {0, ..., 2^n - 1}`:
1. **Single-bit transitions & vertex reconstruction**: Parses each transition character `s_k in {0, ..., n-1}` (encoded in hexadecimal/base-36) and generates `v_0 = 0`, `v_{k+1} = v_k ^ (1 shifted left by s_k)` for `0 at most k at most L-1`, guaranteeing `popcount(v_k ^ v_{k+1}) == 1`.
2. **Cycle closure & vertex distinctness**:
   - For a **coil** of edge length `L`: verifies `v_L == v_0 == 0` (the `L`-th transition closes the cycle) and `len(set(v_0, ..., v_{L-1})) == L`.
   - For a **snake** of edge length `L`: verifies `len(set(v_0, ..., v_L)) == L + 1`.
3. **Exhaustive chordlessness check (`O(L * n)`)**: Inserts all visited vertices into a hash table mapping `v_i` to index `i`, then for every vertex `v_i` and every coordinate direction `b in {0, ..., n-1}`, checks if `v_i ^ (1 shifted left by b)` is in the hash table at index `j`:
   - For a **coil**: requires `(i - j) mod L in {1, L - 1}` (every vertex has exact induced degree `2` in `Q_n`, zero chords).
   - For a **snake**: requires `abs(i - j) == 1` (endpoints `v_0, v_L` have exact induced degree `1` and interior vertices have exact induced degree `2` in `Q_n`, zero chords).
4. **Symmetric coil invariance (`p1`)**: Verifies `L` is even and the transition sequence satisfies exact half-period translation invariance `steps[:L // 2] == steps[L // 2:]`, so the half-turn shift `i maps to (i + L/2) mod L` coincides with the fixed-point-free hypercube translation `x maps to x ^ v_{L/2}` (`v_{L/2} = 7 != 0`).
5. **Canonical transition sequence under `B_n = S_n semidirect (Z_2)^n`, reversal, and cyclic rotation (`p3`)**:
   - Because any hypercube translation `x maps to x ^ a` leaves transition directions invariant and any coordinate permutation `pi in S_n` relabels transition directions `s_k maps to pi(s_k)`, two rooted oriented transition sequences are in the same `B_n`-orbit if and only if their greedy first-appearance relabelings (mapping the `m`-th distinct coordinate encountered to `m - 1`) are identical.
   - For a **snake**, the canonical sequence is `min(relabel(steps), relabel(reversed(steps)))`.
   - For a **coil**, the canonical sequence is the lexicographic minimum of `relabel(rot_r(steps))` and `relabel(rot_r(reversed(steps)))` over all `0 at most r at most L - 1`.

### A. Length-Convention Calibration on Downloaded Reference Files (`claim/seeds/`)

My independent checker calibrated against all reference files in `claim/seeds/`:
- `claim/seeds/minortriad_records.json` (SHA-256 `4aac8e5704c2a667f0912e1683a5b78f2909fada5b06cc4ea94a79534de133fb`): verified all 37 entries (`sn1..sn13`, `co2..co13`, `sc2..sc13`), confirming exact edge-length agreement (`sn9..sn13 = 191, 379, 750, 1480, 2946`; `co9..co13 = 192, 374, 740, 1468, 2930`; `sc9..sc13 = 186, 370, 730, 1434, 2830`) and confirming `steps[:L//2] == steps[L//2:]` on every `sc*` entry.
- `claim/seeds/record_coils.csv` (SHA-256 `e2c4a5b92a394f85cacccc4cc33ddb1ec31d6319d96680aa8718cebdc172cae0`): verified all 31 coils (`Q_9: 192`, `Q_10: 374` x 12, `Q_11: 734` x 11, `Q_12: 1466` x 5, `Q_13: 2916` x 1).
- `claim/seeds/record_symmetric_coils.csv` (SHA-256 `b5bac7da71f94aa13896e74cbb14259ab9d0596f90b8284ad7d3962fcb920160`): verified all 4 symmetric coils (`Q_10: 370` x 2, `Q_11: 734` x 2).
- `claim/seeds/toner_q13_2946.txt` (SHA-256 `56676e1993ab2d74c03a3ebe2e5668194379f2bd79839689e0b0e0daec79f795`): valid `Q_13` snake, `L = 2946`, 0 chords.
- `claim/seeds/toner_q14_5850.txt` (SHA-256 `41ba6cebbc8bc8d029cfb93ae22f6a746a8bbb1fa99efca00591c9444606ee28`): valid `Q_14` snake, `L = 5850`, 0 chords.
- `claim/seeds/taylor_coil_Q14.json` (SHA-256 `48dc953893ec9b45e6f562e857210590eab4f067e42cdd3f12a81496e964c1a3`): valid `Q_14` coil, `L = 5750`, 0 chords.
- `claim/seeds/taylor_snake_Q14.json` (SHA-256 `c04dd9498a590c460675ea881dfdd3154aeac22c42f5b5b598a2ecdd0ab9fa90`): valid `Q_14` snake, `L = 5844`, 0 chords.

### B. Independent Verification of All 11 Primary Claimed Files (+ 2 Secondary Files)

| File (relative to `claim/`) | Milestone | Dim `n` | Type | Verified `L` | Live Baseline | Chords | Half-Period Symmetric (`v_{L/2}`) | Ref Bank Checked (Matches) | Canonical SHA-256 Prefix | Negative Control (1-Step Flip) |
| :--- | :---: | :---: | :---: | ---: | ---: | ---: | :---: | :---: | :--- | :--- |
| `claim/sym_coil_Q12_1450.txt` | `p1` | `12` | Sym Coil | **`1450`** | `1434` (`+16`) | `0` | `True` (`v_725 = 7`) | `0` (`0`) | `79ca8a3d85369638` | Rejected (`v_L = 96 != 0`) |
| `claim/sym_coil_Q13_2870.txt` | `p1` | `13` | Sym Coil | **`2870`** | `2830` (`+40`) | `0` | `True` (`v_1435 = 7`) | `0` (`0`) | `97a3bcd39199e950` | Rejected (`v_L = 1536 != 0`) |
| `claim/sym_coil_Q13_2846.txt` | `p1` (sec) | `13` | Sym Coil | **`2846`** | `2830` (`+16`) | `0` | `True` (`v_1423 = 7`) | `0` (`0`) | `4aaafe1f4952561a` | Rejected (`v_L = 3 != 0`) |
| `claim/coil_Q14_5854.txt` | `p2` | `14` | Coil | **`5854`** | `5750` (`+104`) | `0` | `False` | `0` (`0`) | `d6612f6f2211ccf9` | Rejected (`v_L = 3 != 0`) |
| `claim/snake_Q14_5854.txt` | `p2` | `14` | Snake | **`5854`** | `5850` (`+4`) | `0` | `False` | `0` (`0`) | `7ccc3106d420584b` | Rejected (`10 chord edges`) |
| `claim/coil_Q13_2928.txt` | `p2` (sec) | `13` | Coil | **`2928`** | `2930` (`-2`) | `0` | `False` | `0` (`0`) | `7e1f15301d94306c` | Rejected (`v_L = 24 != 0`) |
| `claim/inequiv_co10_374.txt` | `p3` | `10` | Coil | **`374`** | `374` (`=`) | `0` | `False` | `13` (`0`) | `ab9dad4b0db3d564` | Rejected (`v_L = 6 != 0`) |
| `claim/inequiv_co11_740.txt` | `p3` | `11` | Coil | **`740`** | `740` (`=`) | `0` | `False` | `1` (`0`) | `a9a399ae0cee4f0e` | Rejected (`v_L = 6 != 0`) |
| `claim/inequiv_co12_1468.txt` | `p3` | `12` | Coil | **`1468`** | `1468` (`=`) | `0` | `False` | `1` (`0`) | `c4c3f1005e82b72d` | Rejected (`v_L = 192 != 0`) |
| `claim/inequiv_co13_2930.txt` | `p3` | `13` | Coil | **`2930`** | `2930` (`=`) | `0` | `False` | `1` (`0`) | `146f71d3f995ef7a` | Rejected (`v_L = 24 != 0`) |
| `claim/inequiv_sn11_750.txt` | `p3` | `11` | Snake | **`750`** | `750` (`=`) | `0` | `False` | `1` (`0`) | `fbfa8250ff0f62b3` | Rejected (`duplicate vertex`) |
| `claim/inequiv_sn12_1480.txt` | `p3` | `12` | Snake | **`1480`** | `1480` (`=`) | `0` | `False` | `1` (`0`) | `4875b491a244f2d3` | Rejected (`8 chord edges`) |
| `claim/inequiv_sn13_2946.txt` | `p3` | `13` | Snake | **`2946`** | `2946` (`=`) | `0` | `False` | `2` (`0`) | `6c5627f5c5bdd11f` | Rejected (`7 chord edges`) |

---

## 3. Artifact Integrity & SHA-256 Hashes

| File (relative to `claim/`) | Size (bytes) | SHA-256 Digest |
| :--- | ---: | :--- |
| `claim/verify_snake.py` | `11038` | `ffa32e6b2abab00438899969f9b871b57d1ab46eda72e26ad91a3f92c7e446da` |
| `claim/sym_coil_Q12_1450.txt` | `1451` | `99b1ed6796d7742edbc672164214e4bc6b3a9e0ccd7b4d62a9159936d9339606` |
| `claim/sym_coil_Q13_2870.txt` | `2871` | `916098a5643395c31ff6ee83b41ba473c9c177fda1b1a6e52689f9ce1ce66eea` |
| `claim/sym_coil_Q13_2846.txt` | `2847` | `c625b96ed05fc23149baddf52a8584742235c47c5d75010cffb3054f9a094853` |
| `claim/coil_Q14_5854.txt` | `5855` | `508e47a18fd5083e40dd391b22f8df564f02cc9295af99977ac17e371e26b3c7` |
| `claim/snake_Q14_5854.txt` | `5855` | `47e5e3f6ef0d9d68065090f8749a15281151755cf453495da3669b4336b61935` |
| `claim/coil_Q13_2928.txt` | `2929` | `479db30f00a1963a746e2cff12972663d06fbd98e74192c185184af339e68c67` |
| `claim/inequiv_co10_374.txt` | `375` | `f1a736ab0fcc62757d46850b884bcd6c80460bebced6d2f25c6eaef1d5380755` |
| `claim/inequiv_co11_740.txt` | `741` | `3f22401b0f8250eccca65436ed4564f858bbb58e76e16da4dee6a77e5600b42d` |
| `claim/inequiv_co12_1468.txt` | `1469` | `a4b75c268608c66ec436a4b9735ac85d009462ea2e2d6e52f8d7398dd69bb198` |
| `claim/inequiv_co13_2930.txt` | `2931` | `342cc9c7a9f90b1d336f88ab2a49428d58d676f7b779d59723cdfdcc1d9498db` |
| `claim/inequiv_sn11_750.txt` | `751` | `78c2a47f837e8e4bcea2a5a69782233ee968e71cb5c7660a0e44f2d2f660b695` |
| `claim/inequiv_sn12_1480.txt` | `1481` | `2d16153c21433d994b8d787fdd360e877fd3737f96e70a4feded6975bacdaa03` |
| `claim/inequiv_sn13_2946.txt` | `2947` | `1708be3f455e2bbb75681d98e33aab6b3c533632085db9926974037eb6c41d1d` |

---

## 4. Audit and Execution of Author's Verifier (`claim/verify_snake.py`)

After running my independent verifier, I inspected `claim/verify_snake.py` and executed:
1. `python3 claim/verify_snake.py --seeds-dir claim/seeds --calibrate`:
   - Exit code: `0`
   - Confirmed `[CALIBRATE OK]` across all 37 `minortriad` records (`sn1..sn13`, `co2..co13`, `sc2..sc13`) plus `toner_q13_2946.txt` (`n=13, len=2946`), `toner_q14_5850.txt` (`n=14, len=5850`), and `taylor_coil_Q14.json` (`n=14, len=5750`).
2. `python3 claim/verify_snake.py --seeds-dir claim/seeds --check-inequiv` on all claimed `.txt` files:
   - `claim/sym_coil_Q12_1450.txt`: `VALID COIL: n=12 used_dims=12 length=1450 symmetric=True`
   - `claim/sym_coil_Q13_2870.txt`: `VALID COIL: n=13 used_dims=13 length=2870 symmetric=True`
   - `claim/sym_coil_Q13_2846.txt`: `VALID COIL: n=13 used_dims=13 length=2846 symmetric=True`
   - `claim/coil_Q14_5854.txt`: `VALID COIL: n=14 used_dims=14 length=5854 symmetric=False`
   - `claim/snake_Q14_5854.txt`: `VALID SNAKE: n=14 used_dims=14 length=5854 symmetric=False`
   - `claim/coil_Q13_2928.txt`: `VALID COIL: n=13 used_dims=13 length=2928 symmetric=False`
   - `claim/inequiv_co10_374.txt`: `VALID COIL: n=10 used_dims=10 length=374 symmetric=False` — `STRICTLY INEQUIVALENT to all 13 reference entries! (canonical prefix: 012031405430634163064206314360...)`
   - `claim/inequiv_co11_740.txt`: `VALID COIL: n=11 used_dims=11 length=740 symmetric=False` — `STRICTLY INEQUIVALENT to all 1 reference entries! (canonical prefix: 012031401203521645032103502450...)`
   - `claim/inequiv_co12_1468.txt`: `VALID COIL: n=12 used_dims=12 length=1468 symmetric=False` — `STRICTLY INEQUIVALENT to all 1 reference entries! (canonical prefix: 012031401203520146351205304320...)`
   - `claim/inequiv_co13_2930.txt`: `VALID COIL: n=13 used_dims=13 length=2930 symmetric=False` — `STRICTLY INEQUIVALENT to all 1 reference entries! (canonical prefix: 012031401203521632530563710214...)`
   - `claim/inequiv_sn11_750.txt`: `VALID SNAKE: n=11 used_dims=11 length=750 symmetric=False` — `STRICTLY INEQUIVALENT to all 1 reference entries! (canonical prefix: 012302410230153023642302160230...)`
   - `claim/inequiv_sn12_1480.txt`: `VALID SNAKE: n=12 used_dims=12 length=1480 symmetric=False` — `STRICTLY INEQUIVALENT to all 1 reference entries! (canonical prefix: 012310431234523104132654107601...)`
   - `claim/inequiv_sn13_2946.txt`: `VALID SNAKE: n=13 used_dims=13 length=2946 symmetric=False` — `STRICTLY INEQUIVALENT to all 2 reference entries! (canonical prefix: 012314254103210413067031234103...)`
3. **Corrupted negative test on `claim/verify_snake.py`**:
   - Flipping step `0` of `claim/snake_Q14_5854.txt` from `0` to `1` exits with code `1` and raises `ValueError: Chord in snake between positions 0 and 51 (vertices 0 and 4)`.

All independent and author verification checks succeed.

pass: true
