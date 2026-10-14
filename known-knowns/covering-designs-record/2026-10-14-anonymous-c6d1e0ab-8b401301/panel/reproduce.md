# Reproduction & Independent Verification Report — Plain Covering Design `C(55, 14, 3)` Upper Bound `b = 97`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `covering-designs-record` (`Covering designs C(v,k,t): beat a repository entry`)
- **Parameters**: `(v, k, t) = (55, 14, 3)` (plain covering design with `m = t = 3`)
- **Claimed Upper Bound**: `C(55, 14, 3) at most 97` blocks (strictly improving the standing record `b = 99` in `coveringrepository.com` and Zenodo `v1.2`, and `b = 101` in `dmgordo/LJCR` GitHub, by `-2` block(s); Schonheim lower bound `L(55, 14, 3) = 83`)
- **Artifact**: `claim/C_55_14_3_b97.json` (`4653` bytes, SHA-256 `8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_covering.py`) and the author's standalone verifier confirm that `claim/C_55_14_3_b97.json` contains `97` pairwise distinct `14`-element blocks drawn from `(1, Ellipsis, {55})` (`0` malformed or duplicate blocks), satisfies `b = 97` at least `L(55, 14, 3) = 83`, and exhaustively covers 100% of all `C(55, 3) = 26,235` triples (`covered = 26,235 / 26,235`, `uncovered = 0`). Both verifiers also immediately reject 1-block-deleted and 1-point-mutated negative controls (`exit = 1`).

---

## 2. Verbatim Success Criterion & Claim Summary (`claim/target.md` and `claim/CLAIM.md`)

### 2.1 Target Success Criterion (`claim/target.md`)
  - **Statement**: A `(v,k,t)` covering design is a collection of `k`-subsets (blocks) of a `v`-set such that every `t`-subset lies in at least one block. `C(v,k,t)` is the minimum number of blocks. The repository tables list the best known upper bounds for `v` at most `99`, `k` at most `25`, `t` at most `8`.
  - **Success Criterion**: `b` blocks, each a `k`-subset of a `v`-set (no repeated points), covering every `t`-subset (checked exhaustively), where `b` is STRICTLY SMALLER (direction: min) than EVERY one of the following, each re-fetched at verification time: the live `coveringrepository.com` plain `(v,k,t)` value (`m=t` section, `https://coveringrepository.com/`), the live LJCR value (`https://dmgordon.org/covering-designs/`), and the `dmgordo/LJCR` GitHub/Zenodo value. Parameters must be within `v` at most `99`, `k` at most `25`, `t` at most `8`, `C(v,t)` at most `5*10^9`, and `b` must be at least the Schonheim bound `L(v,k,t)`.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **One-Sentence Claim**: An explicit `97`-block `(55, 14, 3)` plain covering design in `claim/C_55_14_3_b97.json` (every 3-subset of `{1, ..., 55}` is contained in at least one `14`-element block), improving the standing upper bound `C(55, 14, 3) at most 99` (Franco Atzeni (local search, 03/08/2024)) in `coveringrepository.com` and the La Jolla / Dan Gordon covering tables by `2` block(s).

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_covering.py`)

Before reading `claim/verify_covering.py`, we implemented and ran an independent Python verifier directly from the mathematical definition of a `(v, k, t)` covering design.

### 3.1 Artifact Integrity, Parameter Range & Block Validity Audit
- **File**: `claim/C_55_14_3_b97.json`
- **Byte Size**: `4653` bytes
- **SHA-256**: `8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb`
- **Parameter Range Check**:
  - `v = 55` (at most `99`), `k = 14` (at most `25`), `t = 3` (at most `8`), `m = 3 == t`
  - `C(55, 3) = 26,235` (at most `5,000,000,000`)
- **Block Audit**:
  - `len(blocks) = 97`
  - `bad_blocks = 0` (every block is a list of `14` distinct integers in `1..55`)
  - `unique_blocks = 97 == 97` (zero duplicate blocks)

### 3.2 Recursive Schonheim Lower Bound Re-Derivation
Using the exact recursive Schonheim formula `L(v, k, 0) = 1` and `L(v, k, r) = ceil((v / k) * L(v - 1, k - 1, r - 1))`:
- `L(53, 12, 1) = ceil(53 / 12) = 5`
- `L(54, 13, 2) = ceil((54 / 13) * 5) = 21`
- `L(55, 14, 3) = ceil((55 / 14) * 21) = 83`
- **Lower Bound Check**: `b = 97` is at least `L(55, 14, 3) = 83` (and at least the Zenodo tabulated lower bound `83`).

### 3.3 Exhaustive `C(55, 3) = 26,235` Triple Coverage & Multiplicity Histogram
Enumerating all `C(14, 3) = 364` (for `k=14`) or `560` (for `k=16`) triples per block across all `97` blocks and comparing against the full universe of `C(55, 3) = 26,235` triples of `{1, ..., 55}`:
- **Total Triples in Universe `C(55, 3)`**: `26,235`
- **Covered Triples (`lambda(T)` at least `1`)**: `26,235` (`100.0%`)
- **Uncovered Triples (`lambda(T) == 0`)**: `0`
- **Total Block-Triple Incidences (`b * C(14, 3)`)**: `35,308`
- **Exact Coverage Multiplicity Histogram**: `{1: 20934, 2: 3561, 3: 835, 4: 118, 5: 487, 6: 261, 7: 38, 8: 1}` (`mult=1: 20,934, mult=2: 3,561, mult=3: 835, mult=4: 118, mult=5: 487, mult=6: 261, mult=7: 38, mult=8: 1`; sum of `mult * count` = `35,308`). In particular, `20,934` triples are covered with multiplicity `1`.

### 3.4 Independent Adversarial Corruption Tests
1. **1-Block Deletion Test**: Removing the last block (`96` blocks) leaves `285` triples uncovered (`uncovered = 285` above `0`), immediately rejected by our independent checker.
2. **Single-Point Mutation Test**: Replacing point `7` in block `0` (which participates in uniquely covered triple `[7, 9, 53]`) with `1` (preserving `b = 97` blocks of size `k = 14`) leaves `14` triples uncovered (`uncovered = 14` above `0`), immediately rejected by our independent checker.

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_covering.py`)

After completing our independent verification, we read `claim/verify_covering.py` and executed it on the clean artifact and both corrupted negative controls.

### 4.1 Execution Results
1. **Clean Artifact (`python3 claim/verify_covering.py claim/C_55_14_3_b97.json`)**:
   - **Exit Code**: `0`
   - **Stdout**: `file=C_55_14_3_b97.json PASS kind=plain params=C(55,14,3) blocks=97 schonheim=83 covered=26235/26235`
2. **1-Block-Deleted Artifact (`96` blocks)**:
   - **Exit Code**: `1` (non-zero rejection)
   - **Stdout**: `file=del1_C_55_14_3_b97.json FAIL: plain covering C(55,14,3) with b=96 leaves 285/26235 3-subsets uncovered`
3. **1-Point-Mutated Block `0` Artifact (`97` blocks of size `14`, point `7` replaced by `1`)**:
   - **Exit Code**: `1` (non-zero rejection)
   - **Stdout**: `file=mut_C_55_14_3_b97.json FAIL: plain covering C(55,14,3) with b=97 leaves 14/26235 3-subsets uncovered`

---

## 5. Summary Verification Table

| Criterion / Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `4653` bytes | `8b401301e40d62ee...` | PASS |
| Parameter Range & Block Validity | Set & range audit | `97` blocks of size `14` in `1..55` | `bad_blocks=0, unique_blocks=97` | PASS |
| Schonheim Lower Bound | Exact recursive formula | `L(55, 14, 3) = 83` | `b = 97` at least `83` | PASS |
| Exhaustive Triple Coverage | All `C(55, 3)` 3-subsets | `26,235` triples | `covered = 26,235/26,235, uncov = 0` | PASS |
| Strictly Beats Standing Tables | `coveringrepository.com` / LJCR | Standing `b = 99` (GitHub `101`) | `97` below `99` (`-2`) | PASS |
| 1-Block Deletion Control | Drop block `96` | `96` blocks | Rejected (`uncov = 285`, `rc = 1`) | PASS |
| 1-Point Mutation Control | Mutate `7` to `1` in block `0` | `97` blocks of size `14` | Rejected (`uncov = 14`, `rc = 1`) | PASS |

pass: true
