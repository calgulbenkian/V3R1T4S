# Reproduction & Independent Verification Report — Plain Covering Design `C(45, 14, 3)` Upper Bound `b = 58`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `covering-designs-record` (`Covering designs C(v,k,t): beat a repository entry`)
- **Parameters**: `(v, k, t) = (45, 14, 3)` (plain covering design with `m = t = 3`)
- **Claimed Upper Bound**: `C(45, 14, 3) at most 58` blocks (strictly improving the standing record `b = 59` in `coveringrepository.com` and Zenodo `v1.2`, and `b = 59` in `dmgordo/LJCR` GitHub, by `-1` block(s); Schonheim lower bound `L(45, 14, 3) = 45`)
- **Artifact**: `claim/C_45_14_3_b58.json` (`2807` bytes, SHA-256 `3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_covering.py`) and the author's standalone verifier confirm that `claim/C_45_14_3_b58.json` contains `58` pairwise distinct `14`-element blocks drawn from `(1, Ellipsis, {45})` (`0` malformed or duplicate blocks), satisfies `b = 58` at least `L(45, 14, 3) = 45`, and exhaustively covers 100% of all `C(45, 3) = 14,190` triples (`covered = 14,190 / 14,190`, `uncovered = 0`). Both verifiers also immediately reject 1-block-deleted and 1-point-mutated negative controls (`exit = 1`).

---

## 2. Verbatim Success Criterion & Claim Summary (`claim/target.md` and `claim/CLAIM.md`)

### 2.1 Target Success Criterion (`claim/target.md`)
  - **Statement**: A `(v,k,t)` covering design is a collection of `k`-subsets (blocks) of a `v`-set such that every `t`-subset lies in at least one block. `C(v,k,t)` is the minimum number of blocks. The repository tables list the best known upper bounds for `v` at most `99`, `k` at most `25`, `t` at most `8`.
  - **Success Criterion**: `b` blocks, each a `k`-subset of a `v`-set (no repeated points), covering every `t`-subset (checked exhaustively), where `b` is STRICTLY SMALLER (direction: min) than EVERY one of the following, each re-fetched at verification time: the live `coveringrepository.com` plain `(v,k,t)` value (`m=t` section, `https://coveringrepository.com/`), the live LJCR value (`https://dmgordon.org/covering-designs/`), and the `dmgordo/LJCR` GitHub/Zenodo value. Parameters must be within `v` at most `99`, `k` at most `25`, `t` at most `8`, `C(v,t)` at most `5*10^9`, and `b` must be at least the Schonheim bound `L(v,k,t)`.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **One-Sentence Claim**: An explicit `58`-block `(45, 14, 3)` plain covering design in `claim/C_45_14_3_b58.json` (every 3-subset of `{1, ..., 45}` is contained in at least one `14`-element block), improving the standing upper bound `C(45, 14, 3) at most 59` (Jan de Heer and Steve Muir (11/10/2011)) in `coveringrepository.com` and the La Jolla / Dan Gordon covering tables by `1` block(s).

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_covering.py`)

Before reading `claim/verify_covering.py`, we implemented and ran an independent Python verifier directly from the mathematical definition of a `(v, k, t)` covering design.

### 3.1 Artifact Integrity, Parameter Range & Block Validity Audit
- **File**: `claim/C_45_14_3_b58.json`
- **Byte Size**: `2807` bytes
- **SHA-256**: `3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6`
- **Parameter Range Check**:
  - `v = 45` (at most `99`), `k = 14` (at most `25`), `t = 3` (at most `8`), `m = 3 == t`
  - `C(45, 3) = 14,190` (at most `5,000,000,000`)
- **Block Audit**:
  - `len(blocks) = 58`
  - `bad_blocks = 0` (every block is a list of `14` distinct integers in `1..45`)
  - `unique_blocks = 58 == 58` (zero duplicate blocks)

### 3.2 Recursive Schonheim Lower Bound Re-Derivation
Using the exact recursive Schonheim formula `L(v, k, 0) = 1` and `L(v, k, r) = ceil((v / k) * L(v - 1, k - 1, r - 1))`:
- `L(43, 12, 1) = ceil(43 / 12) = 4`
- `L(44, 13, 2) = ceil((44 / 13) * 4) = 14`
- `L(45, 14, 3) = ceil((45 / 14) * 14) = 45`
- **Lower Bound Check**: `b = 58` is at least `L(45, 14, 3) = 45` (and at least the Zenodo tabulated lower bound `45`).

### 3.3 Exhaustive `C(45, 3) = 14,190` Triple Coverage & Multiplicity Histogram
Enumerating all `C(14, 3) = 364` (for `k=14`) or `560` (for `k=16`) triples per block across all `58` blocks and comparing against the full universe of `C(45, 3) = 14,190` triples of `{1, ..., 45}`:
- **Total Triples in Universe `C(45, 3)`**: `14,190`
- **Covered Triples (`lambda(T)` at least `1`)**: `14,190` (`100.0%`)
- **Uncovered Triples (`lambda(T) == 0`)**: `0`
- **Total Block-Triple Incidences (`b * C(14, 3)`)**: `21,112`
- **Exact Coverage Multiplicity Histogram**: `{1: 9631, 2: 3571, 3: 51, 4: 606, 5: 266, 6: 32, 7: 24, 8: 9}` (`mult=1: 9,631, mult=2: 3,571, mult=3: 51, mult=4: 606, mult=5: 266, mult=6: 32, mult=7: 24, mult=8: 9`; sum of `mult * count` = `21,112`). In particular, `9,631` triples are covered with multiplicity `1`.

### 3.4 Independent Adversarial Corruption Tests
1. **1-Block Deletion Test**: Removing the last block (`57` blocks) leaves `232` triples uncovered (`uncovered = 232` above `0`), immediately rejected by our independent checker.
2. **Single-Point Mutation Test**: Replacing point `4` in block `0` (which participates in uniquely covered triple `[4, 7, 41]`) with `1` (preserving `b = 58` blocks of size `k = 14`) leaves `8` triples uncovered (`uncovered = 8` above `0`), immediately rejected by our independent checker.

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_covering.py`)

After completing our independent verification, we read `claim/verify_covering.py` and executed it on the clean artifact and both corrupted negative controls.

### 4.1 Execution Results
1. **Clean Artifact (`python3 claim/verify_covering.py claim/C_45_14_3_b58.json`)**:
   - **Exit Code**: `0`
   - **Stdout**: `file=C_45_14_3_b58.json PASS kind=plain params=C(45,14,3) blocks=58 schonheim=45 covered=14190/14190`
2. **1-Block-Deleted Artifact (`57` blocks)**:
   - **Exit Code**: `1` (non-zero rejection)
   - **Stdout**: `file=del1_C_45_14_3_b58.json FAIL: plain covering C(45,14,3) with b=57 leaves 232/14190 3-subsets uncovered`
3. **1-Point-Mutated Block `0` Artifact (`58` blocks of size `14`, point `4` replaced by `1`)**:
   - **Exit Code**: `1` (non-zero rejection)
   - **Stdout**: `file=mut_C_45_14_3_b58.json FAIL: plain covering C(45,14,3) with b=58 leaves 8/14190 3-subsets uncovered`

---

## 5. Summary Verification Table

| Criterion / Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `2807` bytes | `3679cc89320bf75d...` | PASS |
| Parameter Range & Block Validity | Set & range audit | `58` blocks of size `14` in `1..45` | `bad_blocks=0, unique_blocks=58` | PASS |
| Schonheim Lower Bound | Exact recursive formula | `L(45, 14, 3) = 45` | `b = 58` at least `45` | PASS |
| Exhaustive Triple Coverage | All `C(45, 3)` 3-subsets | `14,190` triples | `covered = 14,190/14,190, uncov = 0` | PASS |
| Strictly Beats Standing Tables | `coveringrepository.com` / LJCR | Standing `b = 59` (GitHub `59`) | `58` below `59` (`-1`) | PASS |
| 1-Block Deletion Control | Drop block `57` | `57` blocks | Rejected (`uncov = 232`, `rc = 1`) | PASS |
| 1-Point Mutation Control | Mutate `4` to `1` in block `0` | `58` blocks of size `14` | Rejected (`uncov = 8`, `rc = 1`) | PASS |

pass: true
