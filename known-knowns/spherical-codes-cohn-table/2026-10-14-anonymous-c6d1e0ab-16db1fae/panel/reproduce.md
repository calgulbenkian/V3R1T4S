# Reproduction & Independent Verification Report: Spherical Code (30, 117)

context: subagent (astra)
role: REPRODUCE skeptic
target: spherical-codes-cohn-table
submission_type: solution_claim (Full Win)
parameters: (d = 30, N = 117)

## 1. Executive Summary

I independently verified the claimed spherical code in `R^30` with `N = 117` unit vectors located in `claim/object/code_30_117.json` and `claim/object/code_30_117.txt`. Prior to inspecting the author's verification script `claim/verify_spherical.py`, I wrote and executed an independent 60-digit arbitrary-precision verifier using Python's standard library `decimal.Decimal` (`getcontext().prec = 60`) directly from the mathematical definition of a spherical code on `S^29`.

Both my independent 60-digit verifier and the author's standalone verifier confirm every structural, numerical, and live-table requirement:
- **Dimension and cardinality**: Exactly `N = 117` vectors in `R^30` (`3510` coordinates total), identical between `claim/object/code_30_117.json` and `claim/object/code_30_117.txt`.
- **Coordinate precision**: Every coordinate string carries `33` significant digits (exceeding the minimum requirement of `20` significant digits).
- **Unit-sphere normalization**: Raw Euclidean norms satisfy `max_i abs(||v_i||_2 - 1) = 9.218e-34`; after explicit 60-digit normalization `u_i = v_i / sqrt(sum_k v_{i,k}^2)`, post-normalization norms satisfy `max_i abs(||u_i||_2 - 1) = 1.000e-59`.
- **Exact 60-digit maximum pairwise inner product**: Across all `N*(N-1)/2 = 6786` distinct vector pairs, the maximum inner product is:
  - `c* (60-digit rounded to 28 decimals) = 0.0883794850648560216379989089`
  - `c* (reported 25 decimals)            = 0.0883794850648560216379989`
  achieved at pair `i = 63, j = 71` (with `81` pairs within `1e-8` of `c*`, `1` pairs within `1e-10` of `c*`, and minimum inner product `c_min = -0.8237533736554779`).
- **Strict improvement over the live Cohn-Ballinger table**:
  - Live table value (`claim/data/plain.csv` and `claim/data/index_metadata.json`): `c_table = 0.088389506027` (`theta_table = 84.929036686159` deg)
  - Baseline coordinate verification (`claim/data/codes/code_30_117.txt`): `c_base = 0.0883895060269536115572058` (`abs(c_base - c_table) = 4.64e-14`, well within `1e-11`)
  - Claimed code value: `c* = 0.0883794850648560216379989` (`theta* = 84.929613100835` deg)
  - Improvement margin: `Delta c = c_table - c* = 0.0000100209621439783620011` (`1.002096e-05`), which is `100,209.62x` larger than the required `1e-10` threshold (`Delta theta = +5.764147e-04` deg).
- **Eligibility & scope checks**:
  - `s = 0` (`starred = false`, not proven optimal in `claim/data/index_metadata.json`)
  - `o = 0` (`needs_opt = false`, eligible for `solution_claim` Full Win because it does not carry the "needs more optimization" label)
  - Kissing-number low-dimension exclusion (`9 .. d .. 23` and `c* at most 0.5`): False (`d = 30` is outside `9 .. 23`).

---

## 2. Artifact Integrity

| File (relative to `claim/`) | Size (bytes) | SHA-256 Digest |
| :--- | ---: | :--- |
| `claim/object/code_30_117.json` | `168214` | `16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19` |
| `claim/object/code_30_117.txt` | `135176` | `87acc4414d2af1ad497ce82d953dbfb17bbec1d2978be58bff6acc2793ef62f8` |
| `claim/data/codes/code_30_117.txt` | `71804` | `ffb27c245d8c7e669d3c8c0b502c381498520210887c6ae3ee96bce1f479406f` |

Exact string-by-string comparison confirms that `claim/object/code_30_117.json` (`"vectors"` array) and `claim/object/code_30_117.txt` (`117` lines of `30` comma-separated decimal strings) contain the exact same `117` vectors of dimension `30`.

---

## 3. Independent 60-Digit Verification (Before Reading Author Code)

Before viewing `claim/verify_spherical.py`, I implemented a standalone checker using `decimal.Decimal` at 60-digit precision (`getcontext().prec = 60`) that:
1. Parses all `117` vectors of dimension `30` from both `claim/object/code_30_117.json` and `claim/object/code_30_117.txt`, verifying equality and checking that every coordinate string has at least 20 significant digits (found `33` significant digits across all `3510` entries).
2. Normalizes each vector `v_i` in 60-digit Decimal arithmetic via `u_i = v_i / (sum_k v_{i,k}^2).sqrt()`.
3. Exhaustively evaluates all `117*(117-1)/2 = 6786` pairwise dot products `sum_k u_{i,k} * u_{j,k}` in 60-digit Decimal arithmetic (without any float64 pre-screening).
4. Evaluates the baseline code `claim/data/codes/code_30_117.txt` in 60-digit Decimal arithmetic and checks agreement with `claim/data/plain.csv` and `claim/data/index_metadata.json`.
5. Performs a negative-control corruption test by duplicating vector `0` into vector `1` (`u_1 = u_0`), confirming that the maximum pairwise inner product becomes `c* = 1.0000000000` (`Delta c = -0.911610493973`), which is strictly rejected.

### Summary of Independent Measurements

| Quantity | Independent 60-Digit Value | Status |
| :--- | :--- | :--- |
| Dimension `d`, Point count `N` | `d = 30, N = 117` (`6786` pairs) | PASS |
| Coordinate significant digits | `min = 33, max = 33` (required: at least `20`) | PASS |
| Max pre-normalization norm error | `9.218e-34` | PASS |
| Max post-normalization norm error | `1.000e-59` | PASS |
| Baseline `c_base` (`claim/data/codes/code_30_117.txt`) | `0.0883895060269536115572058` (`abs(c_base - c_table) = 4.64e-14`) | PASS |
| Table value `c_table` (`claim/data/plain.csv`) | `0.088389506027` | PASS |
| Claimed `c*` (`max_{i != j} dot(u_i, u_j)`) | `0.0883794850648560216379989` | PASS |
| Improvement `Delta c = c_table - c*` | `0.0000100209621439783620011` (`1.002096e-05`, required: at least `1e-10`) | PASS |
| Minimum separation angle `theta*` | `84.929613100835` deg vs `84.929036686159` deg (`+5.764147e-04` deg) | PASS |
| Metadata flags (`claim/data/index_metadata.json`) | `s = 0` (`starred = false`), `o = 0` (`needs_opt = false`) | PASS |
| Negative control (duplicate vector `0` into `1`) | `c*_corrupted = 1.0` (`Delta c = -0.911610`, rejected) | PASS |

---

## 4. Audit and Execution of Author's Verifier (`claim/verify_spherical.py`)

After completing my independent check, I inspected `claim/verify_spherical.py` and executed it on the claimed JSON file, the claimed TXT file, and a corrupted JSON file (with vector `1` set equal to vector `0`).

### Code Audit of `claim/verify_spherical.py`
- Sets `decimal.getcontext().prec = 60` at module import.
- Normalizes every vector in 60-digit Decimal (`normalize_vec`).
- For `N` at most `250` (here `N = 117`), `thresh = -10.0`, so `max_inner_product` computes the exact 60-digit Decimal dot product for every single pair `(i, j)`.
- Verifies `(d, N)` against `claim/data/plain.csv`, `claim/data/index_metadata.json`, and `claim/data/codes/code_30_117.txt`.

### Execution Outputs
1. **JSON verification (`python3 verify_spherical.py object/code_30_117.json`)**:
   - Exit code: `0`
   - Output: `file=code_30_117.json PASS kind=solution_claim params=(30,117) needs_opt=False c_table=0.088389506027 c_star=0.0883794850648560216379989 gain=1.002096e-05 min_angle_deg=84.929613100835 base_ok=True(diff=4.64e-14)`
2. **TXT verification (`python3 verify_spherical.py --d 30 --N 117 object/code_30_117.txt`)**:
   - Exit code: `0`
   - Output: `file=code_30_117.txt PASS kind=solution_claim params=(30,117) needs_opt=False c_table=0.088389506027 c_star=0.0883794850648560216379989 gain=1.002096e-05 min_angle_deg=84.929613100835 base_ok=True(diff=4.64e-14)`
3. **Corrupted negative test (duplicate vector `0` into vector `1`)**:
   - Exit code: `1` (non-zero, properly rejected)
   - Output: `FAIL: gain c_table - c* = -9.116104939730000e-01 ... (c_table=0.088389506027, c*=1.00000000000000000000)`

All reproduction and exact-arithmetic verification checks succeed.

pass: true
