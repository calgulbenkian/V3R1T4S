# Reproduction & Independent Verification Report: Spherical Code (28, 70)

context: subagent (astra)
role: REPRODUCE skeptic
target: spherical-codes-cohn-table
submission_type: solution_claim (Full Win)
parameters: (d = 28, N = 70)

## 1. Executive Summary

I independently verified the claimed spherical code in `R^28` with `N = 70` unit vectors located in `claim/object/code_28_70.json` and `claim/object/code_28_70.txt`. Prior to inspecting the author's verification script `claim/verify_spherical.py`, I wrote and executed an independent 60-digit arbitrary-precision verifier using Python's standard library `decimal.Decimal` (`getcontext().prec = 60`) directly from the mathematical definition of a spherical code on `S^27`.

Both my independent 60-digit verifier and the author's standalone verifier confirm every structural, numerical, and live-table requirement:
- **Dimension and cardinality**: Exactly `N = 70` vectors in `R^28` (`1960` coordinates total), identical between `claim/object/code_28_70.json` and `claim/object/code_28_70.txt`.
- **Coordinate precision**: Every coordinate string carries `33` significant digits (exceeding the minimum requirement of `20` significant digits).
- **Unit-sphere normalization**: Raw Euclidean norms satisfy `max_i abs(||v_i||_2 - 1) = 7.335e-34`; after explicit 60-digit normalization `u_i = v_i / sqrt(sum_k v_{i,k}^2)`, post-normalization norms satisfy `max_i abs(||u_i||_2 - 1) = 1.000e-59`.
- **Exact 60-digit maximum pairwise inner product**: Across all `N*(N-1)/2 = 2415` distinct vector pairs, the maximum inner product is:
  - `c* (60-digit rounded to 28 decimals) = 0.0517863124041101353861329372`
  - `c* (reported 25 decimals)            = 0.0517863124041101353861329`
  achieved at pair `i = 48, j = 50` (with `107` pairs within `1e-8` of `c*`, `1` pairs within `1e-10` of `c*`, and minimum inner product `c_min = -0.9813887894170280`).
- **Strict improvement over the live Cohn-Ballinger table**:
  - Live table value (`claim/data/plain.csv` and `claim/data/index_metadata.json`): `c_table = 0.051797462893` (`theta_table = 87.030895302736` deg)
  - Baseline coordinate verification (`claim/data/codes/code_28_70.txt`): `c_base = 0.0517974628923873451888833` (`abs(c_base - c_table) = 6.13e-13`, well within `1e-11`)
  - Claimed code value: `c* = 0.0517863124041101353861329` (`theta* = 87.031535037277` deg)
  - Improvement margin: `Delta c = c_table - c* = 0.0000111504888898646138671` (`1.115049e-05`), which is `111,504.89x` larger than the required `1e-10` threshold (`Delta theta = +6.397345e-04` deg).
- **Eligibility & scope checks**:
  - `s = 0` (`starred = false`, not proven optimal in `claim/data/index_metadata.json`)
  - `o = 0` (`needs_opt = false`, eligible for `solution_claim` Full Win because it does not carry the "needs more optimization" label)
  - Kissing-number low-dimension exclusion (`9 .. d .. 23` and `c* at most 0.5`): False (`d = 28` is outside `9 .. 23`).

---

## 2. Artifact Integrity

| File (relative to `claim/`) | Size (bytes) | SHA-256 Digest |
| :--- | ---: | :--- |
| `claim/object/code_28_70.json` | `93832` | `cd7c56d206970b5e9b3b44ef5f31395908b4e84acf22f807c46a543556f05263` |
| `claim/object/code_28_70.txt` | `75309` | `f6f1082ef27f21b7b885dcde6dec1daf4ed06c879a547b5732a011839779cc15` |
| `claim/data/codes/code_28_70.txt` | `36279` | `b4fe496ca5198eb8b2420cb5041c8033ed380017145d09ff0ecd8266501a07a0` |

Exact string-by-string comparison confirms that `claim/object/code_28_70.json` (`"vectors"` array) and `claim/object/code_28_70.txt` (`70` lines of `28` comma-separated decimal strings) contain the exact same `70` vectors of dimension `28`.

---

## 3. Independent 60-Digit Verification (Before Reading Author Code)

Before viewing `claim/verify_spherical.py`, I implemented a standalone checker using `decimal.Decimal` at 60-digit precision (`getcontext().prec = 60`) that:
1. Parses all `70` vectors of dimension `28` from both `claim/object/code_28_70.json` and `claim/object/code_28_70.txt`, verifying equality and checking that every coordinate string has at least 20 significant digits (found `33` significant digits across all `1960` entries).
2. Normalizes each vector `v_i` in 60-digit Decimal arithmetic via `u_i = v_i / (sum_k v_{i,k}^2).sqrt()`.
3. Exhaustively evaluates all `70*(70-1)/2 = 2415` pairwise dot products `sum_k u_{i,k} * u_{j,k}` in 60-digit Decimal arithmetic (without any float64 pre-screening).
4. Evaluates the baseline code `claim/data/codes/code_28_70.txt` in 60-digit Decimal arithmetic and checks agreement with `claim/data/plain.csv` and `claim/data/index_metadata.json`.
5. Performs a negative-control corruption test by duplicating vector `0` into vector `1` (`u_1 = u_0`), confirming that the maximum pairwise inner product becomes `c* = 1.0000000000` (`Delta c = -0.948202537107`), which is strictly rejected.

### Summary of Independent Measurements

| Quantity | Independent 60-Digit Value | Status |
| :--- | :--- | :--- |
| Dimension `d`, Point count `N` | `d = 28, N = 70` (`2415` pairs) | PASS |
| Coordinate significant digits | `min = 33, max = 33` (required: at least `20`) | PASS |
| Max pre-normalization norm error | `7.335e-34` | PASS |
| Max post-normalization norm error | `1.000e-59` | PASS |
| Baseline `c_base` (`claim/data/codes/code_28_70.txt`) | `0.0517974628923873451888833` (`abs(c_base - c_table) = 6.13e-13`) | PASS |
| Table value `c_table` (`claim/data/plain.csv`) | `0.051797462893` | PASS |
| Claimed `c*` (`max_{i != j} dot(u_i, u_j)`) | `0.0517863124041101353861329` | PASS |
| Improvement `Delta c = c_table - c*` | `0.0000111504888898646138671` (`1.115049e-05`, required: at least `1e-10`) | PASS |
| Minimum separation angle `theta*` | `87.031535037277` deg vs `87.030895302736` deg (`+6.397345e-04` deg) | PASS |
| Metadata flags (`claim/data/index_metadata.json`) | `s = 0` (`starred = false`), `o = 0` (`needs_opt = false`) | PASS |
| Negative control (duplicate vector `0` into `1`) | `c*_corrupted = 1.0` (`Delta c = -0.948203`, rejected) | PASS |

---

## 4. Audit and Execution of Author's Verifier (`claim/verify_spherical.py`)

After completing my independent check, I inspected `claim/verify_spherical.py` and executed it on the claimed JSON file, the claimed TXT file, and a corrupted JSON file (with vector `1` set equal to vector `0`).

### Code Audit of `claim/verify_spherical.py`
- Sets `decimal.getcontext().prec = 60` at module import.
- Normalizes every vector in 60-digit Decimal (`normalize_vec`).
- For `N` at most `250` (here `N = 70`), `thresh = -10.0`, so `max_inner_product` computes the exact 60-digit Decimal dot product for every single pair `(i, j)`.
- Verifies `(d, N)` against `claim/data/plain.csv`, `claim/data/index_metadata.json`, and `claim/data/codes/code_28_70.txt`.

### Execution Outputs
1. **JSON verification (`python3 verify_spherical.py object/code_28_70.json`)**:
   - Exit code: `0`
   - Output: `file=code_28_70.json PASS kind=solution_claim params=(28,70) needs_opt=False c_table=0.051797462893 c_star=0.0517863124041101353861329 gain=1.115049e-05 min_angle_deg=87.031535037277 base_ok=True(diff=6.13e-13)`
2. **TXT verification (`python3 verify_spherical.py --d 28 --N 70 object/code_28_70.txt`)**:
   - Exit code: `0`
   - Output: `file=code_28_70.txt PASS kind=solution_claim params=(28,70) needs_opt=False c_table=0.051797462893 c_star=0.0517863124041101353861329 gain=1.115049e-05 min_angle_deg=87.031535037277 base_ok=True(diff=6.13e-13)`
3. **Corrupted negative test (duplicate vector `0` into vector `1`)**:
   - Exit code: `1` (non-zero, properly rejected)
   - Output: `FAIL: gain c_table - c* = -9.482025371070000e-01 ... (c_table=0.051797462893, c*=1.00000000000000000000)`

All reproduction and exact-arithmetic verification checks succeed.

pass: true
