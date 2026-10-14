# Reproduction & Independent Verification Report — Plain Covering Design `C(38, 16, 3)` Upper Bound `b = 25`

context: subagent
context: subagent (astra)

## 1. Executive Summary
- **Target**: `covering-designs-record` (`Covering designs C(v,k,t): beat a repository entry`)
- **Parameters**: `(v, k, t) = (38, 16, 3)` (plain covering design with `m = t = 3`)
- **Claimed Upper Bound**: `C(38, 16, 3) at most 25` blocks (strictly improving the standing record `b = 26` in `coveringrepository.com` and Zenodo `v1.2`, and `b = 27` in `dmgordo/LJCR` GitHub, by `-1` block(s); Schonheim lower bound `L(38, 16, 3) = 19`)
- **Artifact**: `claim/C_38_16_3_b25.json` (`1412` bytes, SHA-256 `fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643`)
- **Verdict**: **PASS** — Both our independent first-principles verifier (written and executed before reading `claim/verify_covering.py`) and the author's standalone verifier confirm that `claim/C_38_16_3_b25.json` contains `25` pairwise distinct `16`-element blocks drawn from `(1, Ellipsis, {38})` (`0` malformed or duplicate blocks), satisfies `b = 25` at least `L(38, 16, 3) = 19`, and exhaustively covers 100% of all `C(38, 3) = 8,436` triples (`covered = 8,436 / 8,436`, `uncovered = 0`). Both verifiers also immediately reject 1-block-deleted and 1-point-mutated negative controls (`exit = 1`).

---

## 2. Verbatim Success Criterion & Claim Summary (`claim/target.md` and `claim/CLAIM.md`)

### 2.1 Target Success Criterion (`claim/target.md`)
  - **Statement**: A `(v,k,t)` covering design is a collection of `k`-subsets (blocks) of a `v`-set such that every `t`-subset lies in at least one block. `C(v,k,t)` is the minimum number of blocks. The repository tables list the best known upper bounds for `v` at most `99`, `k` at most `25`, `t` at most `8`.
  - **Success Criterion**: `b` blocks, each a `k`-subset of a `v`-set (no repeated points), covering every `t`-subset (checked exhaustively), where `b` is STRICTLY SMALLER (direction: min) than EVERY one of the following, each re-fetched at verification time: the live `coveringrepository.com` plain `(v,k,t)` value (`m=t` section, `https://coveringrepository.com/`), the live LJCR value (`https://dmgordon.org/covering-designs/`), and the `dmgordo/LJCR` GitHub/Zenodo value. Parameters must be within `v` at most `99`, `k` at most `25`, `t` at most `8`, `C(v,t)` at most `5*10^9`, and `b` must be at least the Schonheim bound `L(v,k,t)`.

### 2.2 Claim Summary (`claim/CLAIM.md`)
  - **One-Sentence Claim**: An explicit `25`-block `(38, 16, 3)` plain covering design in `claim/C_38_16_3_b25.json` (every 3-subset of `{1, ..., 38}` is contained in at least one `16`-element block), improving the standing upper bound `C(38, 16, 3) at most 26` (Franco Atzeni (local search, 27/06/2024)) in `coveringrepository.com` and the La Jolla / Dan Gordon covering tables by `1` block(s).

---

## 3. Step 1 — Independent First-Principles Verification (Executed Before Reading `claim/verify_covering.py`)

Before reading `claim/verify_covering.py`, we implemented and ran an independent Python verifier directly from the mathematical definition of a `(v, k, t)` covering design.

### 3.1 Artifact Integrity, Parameter Range & Block Validity Audit
- **File**: `claim/C_38_16_3_b25.json`
- **Byte Size**: `1412` bytes
- **SHA-256**: `fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643`
- **Parameter Range Check**:
  - `v = 38` (at most `99`), `k = 16` (at most `25`), `t = 3` (at most `8`), `m = 3 == t`
  - `C(38, 3) = 8,436` (at most `5,000,000,000`)
- **Block Audit**:
  - `len(blocks) = 25`
  - `bad_blocks = 0` (every block is a list of `16` distinct integers in `1..38`)
  - `unique_blocks = 25 == 25` (zero duplicate blocks)

### 3.2 Recursive Schonheim Lower Bound Re-Derivation
Using the exact recursive Schonheim formula `L(v, k, 0) = 1` and `L(v, k, r) = ceil((v / k) * L(v - 1, k - 1, r - 1))`:
- `L(36, 14, 1) = ceil(36 / 14) = 3`
- `L(37, 15, 2) = ceil((37 / 15) * 3) = 8`
- `L(38, 16, 3) = ceil((38 / 16) * 8) = 19`
- **Lower Bound Check**: `b = 25` is at least `L(38, 16, 3) = 19` (and at least the Zenodo tabulated lower bound `22`).

### 3.3 Exhaustive `C(38, 3) = 8,436` Triple Coverage & Multiplicity Histogram
Enumerating all `C(16, 3) = 364` (for `k=14`) or `560` (for `k=16`) triples per block across all `25` blocks and comparing against the full universe of `C(38, 3) = 8,436` triples of `{1, ..., 38}`:
- **Total Triples in Universe `C(38, 3)`**: `8,436`
- **Covered Triples (`lambda(T)` at least `1`)**: `8,436` (`100.0%`)
- **Uncovered Triples (`lambda(T) == 0`)**: `0`
- **Total Block-Triple Incidences (`b * C(16, 3)`)**: `14,000`
- **Exact Coverage Multiplicity Histogram**: `{1: 5708, 2: 1088, 3: 656, 4: 852, 5: 88, 6: 20, 7: 12, 8: 12}` (`mult=1: 5,708, mult=2: 1,088, mult=3: 656, mult=4: 852, mult=5: 88, mult=6: 20, mult=7: 12, mult=8: 12`; sum of `mult * count` = `14,000`). In particular, `5,708` triples are covered with multiplicity `1`.

### 3.4 Independent Adversarial Corruption Tests
1. **1-Block Deletion Test**: Removing the last block (`24` blocks) leaves `264` triples uncovered (`uncovered = 264` above `0`), immediately rejected by our independent checker.
2. **Single-Point Mutation Test**: Replacing point `2` in block `0` (which participates in uniquely covered triple `[2, 4, 5]`) with `1` (preserving `b = 25` blocks of size `k = 16`) leaves `54` triples uncovered (`uncovered = 54` above `0`), immediately rejected by our independent checker.

---

## 4. Step 2 — Audit & Execution of Author's Verifier (`claim/verify_covering.py`)

After completing our independent verification, we read `claim/verify_covering.py` and executed it on the clean artifact and both corrupted negative controls.

### 4.1 Execution Results
1. **Clean Artifact (`python3 claim/verify_covering.py claim/C_38_16_3_b25.json`)**:
   - **Exit Code**: `0`
   - **Stdout**: `file=C_38_16_3_b25.json PASS kind=plain params=C(38,16,3) blocks=25 schonheim=19 covered=8436/8436`
2. **1-Block-Deleted Artifact (`24` blocks)**:
   - **Exit Code**: `1` (non-zero rejection)
   - **Stdout**: `file=del1_C_38_16_3_b25.json FAIL: plain covering C(38,16,3) with b=24 leaves 264/8436 3-subsets uncovered`
3. **1-Point-Mutated Block `0` Artifact (`25` blocks of size `16`, point `2` replaced by `1`)**:
   - **Exit Code**: `1` (non-zero rejection)
   - **Stdout**: `file=mut_C_38_16_3_b25.json FAIL: plain covering C(38,16,3) with b=25 leaves 54/8436 3-subsets uncovered`

---

## 5. Summary Verification Table

| Criterion / Check | Method | Scope | Result | Status |
|---|---|---|---|---|
| Artifact SHA-256 & Size | `hashlib.sha256` | `1412` bytes | `fd58604086de7221...` | PASS |
| Parameter Range & Block Validity | Set & range audit | `25` blocks of size `16` in `1..38` | `bad_blocks=0, unique_blocks=25` | PASS |
| Schonheim Lower Bound | Exact recursive formula | `L(38, 16, 3) = 19` | `b = 25` at least `19` | PASS |
| Exhaustive Triple Coverage | All `C(38, 3)` 3-subsets | `8,436` triples | `covered = 8,436/8,436, uncov = 0` | PASS |
| Strictly Beats Standing Tables | `coveringrepository.com` / LJCR | Standing `b = 26` (GitHub `27`) | `25` below `26` (`-1`) | PASS |
| 1-Block Deletion Control | Drop block `24` | `24` blocks | Rejected (`uncov = 264`, `rc = 1`) | PASS |
| 1-Point Mutation Control | Mutate `2` to `1` in block `0` | `25` blocks of size `16` | Rejected (`uncov = 54`, `rc = 1`) | PASS |

pass: true
