# Reproduction & Independent Verification Report: Spherical Code (29, 145)

context: subagent (astra)
role: REPRODUCE skeptic
target: spherical-codes-cohn-table
submission_type: solution_claim (Full Win)
parameters: (d = 29, N = 145)

## 1. Executive Summary

I independently verified the claimed spherical code in `R^29` with `N = 145` unit vectors located in `claim/object/code_29_145.json` and `claim/object/code_29_145.txt`. Prior to inspecting the author's verification script `claim/verify_spherical.py`, I wrote and executed an independent 60-digit arbitrary-precision verifier using Python's standard library `decimal.Decimal` (`getcontext().prec = 60`) directly from the mathematical definition of a spherical code on `S^28`.

Both my independent 60-digit verifier and the author's standalone verifier confirm every structural, numerical, and live-table requirement:
- **Dimension and cardinality**: Exactly `N = 145` vectors in `R^29` (`4205` coordinates total), identical between `claim/object/code_29_145.json` and `claim/object/code_29_145.txt`.
- **Coordinate precision**: Every coordinate string carries `33` significant digits (exceeding the minimum requirement of `20` significant digits).
- **Unit-sphere normalization**: Raw Euclidean norms satisfy `max_i abs(||v_i||_2 - 1) = 7.174e-34`; after explicit 60-digit normalization `u_i = v_i / sqrt(sum_k v_{i,k}^2)`, post-normalization norms satisfy `max_i abs(||u_i||_2 - 1) = 1.000e-59`.
- **Exact 60-digit maximum pairwise inner product**: Across all `N*(N-1)/2 = 10440` distinct vector pairs, the maximum inner product is:
  - `c* (60-digit rounded to 28 decimals) = 0.1106960891058149669538693017`
  - `c* (reported 25 decimals)            = 0.1106960891058149669538693`
  achieved at pair `i = 45, j = 95` (with `157` pairs within `1e-8` of `c*`, `1` pairs within `1e-10` of `c*`, and minimum inner product `c_min = -0.6204247549270507`).
- **Strict improvement over the live Cohn-Ballinger table**:
  - Live table value (`claim/data/plain.csv` and `claim/data/index_metadata.json`): `c_table = 0.110701844288` (`theta_table = 83.644224613445` deg)
  - Baseline coordinate verification (`claim/data/codes/code_29_145.txt`): `c_base = 0.1107018442872420674008210` (`abs(c_base - c_table) = 7.58e-13`, well within `1e-11`)
  - Claimed code value: `c* = 0.1106960891058149669538693` (`theta* = 83.644556400262` deg)
  - Improvement margin: `Delta c = c_table - c* = 0.0000057551821850330461307` (`5.755182e-06`), which is `57,551.82x` larger than the required `1e-10` threshold (`Delta theta = +3.317868e-04` deg).
- **Eligibility & scope checks**:
  - `s = 0` (`starred = false`, not proven optimal in `claim/data/index_metadata.json`)
  - `o = 0` (`needs_opt = false`, eligible for `solution_claim` Full Win because it does not carry the "needs more optimization" label)
  - Kissing-number low-dimension exclusion (`9 .. d .. 23` and `c* at most 0.5`): False (`d = 29` is outside `9 .. 23`).

---

## 2. Artifact Integrity

| File (relative to `claim/`) | Size (bytes) | SHA-256 Digest |
| :--- | ---: | :--- |
| `claim/object/code_29_145.json` | `201516` | `80550660490b9e5148590d6e502ab71a9ed0067eb476238da3784ad47b23b083` |
| `claim/object/code_29_145.txt` | `161887` | `4e4787fc145320dad4cc5361b10833df8c845a054ec69ee1562623bd728ffa8b` |
| `claim/data/codes/code_29_145.txt` | `85746` | `e57378f38ff4c7119ac96b2d48b18493e8e9d423861f92f87309610b82acb14d` |

Exact string-by-string comparison confirms that `claim/object/code_29_145.json` (`"vectors"` array) and `claim/object/code_29_145.txt` (`145` lines of `29` comma-separated decimal strings) contain the exact same `145` vectors of dimension `29`.

---

## 3. Independent 60-Digit Verification (Before Reading Author Code)

Before viewing `claim/verify_spherical.py`, I implemented a standalone checker using `decimal.Decimal` at 60-digit precision (`getcontext().prec = 60`) that:
1. Parses all `145` vectors of dimension `29` from both `claim/object/code_29_145.json` and `claim/object/code_29_145.txt`, verifying equality and checking that every coordinate string has at least 20 significant digits (found `33` significant digits across all `4205` entries).
2. Normalizes each vector `v_i` in 60-digit Decimal arithmetic via `u_i = v_i / (sum_k v_{i,k}^2).sqrt()`.
3. Exhaustively evaluates all `145*(145-1)/2 = 10440` pairwise dot products `sum_k u_{i,k} * u_{j,k}` in 60-digit Decimal arithmetic (without any float64 pre-screening).
4. Evaluates the baseline code `claim/data/codes/code_29_145.txt` in 60-digit Decimal arithmetic and checks agreement with `claim/data/plain.csv` and `claim/data/index_metadata.json`.
5. Performs a negative-control corruption test by duplicating vector `0` into vector `1` (`u_1 = u_0`), confirming that the maximum pairwise inner product becomes `c* = 1.0000000000` (`Delta c = -0.889298155712`), which is strictly rejected.

### Summary of Independent Measurements

| Quantity | Independent 60-Digit Value | Status |
| :--- | :--- | :--- |
| Dimension `d`, Point count `N` | `d = 29, N = 145` (`10440` pairs) | PASS |
| Coordinate significant digits | `min = 33, max = 33` (required: at least `20`) | PASS |
| Max pre-normalization norm error | `7.174e-34` | PASS |
| Max post-normalization norm error | `1.000e-59` | PASS |
| Baseline `c_base` (`claim/data/codes/code_29_145.txt`) | `0.1107018442872420674008210` (`abs(c_base - c_table) = 7.58e-13`) | PASS |
| Table value `c_table` (`claim/data/plain.csv`) | `0.110701844288` | PASS |
| Claimed `c*` (`max_{i != j} dot(u_i, u_j)`) | `0.1106960891058149669538693` | PASS |
| Improvement `Delta c = c_table - c*` | `0.0000057551821850330461307` (`5.755182e-06`, required: at least `1e-10`) | PASS |
| Minimum separation angle `theta*` | `83.644556400262` deg vs `83.644224613445` deg (`+3.317868e-04` deg) | PASS |
| Metadata flags (`claim/data/index_metadata.json`) | `s = 0` (`starred = false`), `o = 0` (`needs_opt = false`) | PASS |
| Negative control (duplicate vector `0` into `1`) | `c*_corrupted = 1.0` (`Delta c = -0.889298`, rejected) | PASS |

---

## 4. Audit and Execution of Author's Verifier (`claim/verify_spherical.py`)

After completing my independent check, I inspected `claim/verify_spherical.py` and executed it on the claimed JSON file, the claimed TXT file, and a corrupted JSON file (with vector `1` set equal to vector `0`).

### Code Audit of `claim/verify_spherical.py`
- Sets `decimal.getcontext().prec = 60` at module import.
- Normalizes every vector in 60-digit Decimal (`normalize_vec`).
- For `N` at most `250` (here `N = 145`), `thresh = -10.0`, so `max_inner_product` computes the exact 60-digit Decimal dot product for every single pair `(i, j)`.
- Verifies `(d, N)` against `claim/data/plain.csv`, `claim/data/index_metadata.json`, and `claim/data/codes/code_29_145.txt`.

### Execution Outputs
1. **JSON verification (`python3 verify_spherical.py object/code_29_145.json`)**:
   - Exit code: `0`
   - Output: `file=code_29_145.json PASS kind=solution_claim params=(29,145) needs_opt=False c_table=0.110701844288 c_star=0.1106960891058149669538693 gain=5.755182e-06 min_angle_deg=83.644556400262 base_ok=True(diff=7.58e-13)`
2. **TXT verification (`python3 verify_spherical.py --d 29 --N 145 object/code_29_145.txt`)**:
   - Exit code: `0`
   - Output: `file=code_29_145.txt PASS kind=solution_claim params=(29,145) needs_opt=False c_table=0.110701844288 c_star=0.1106960891058149669538693 gain=5.755182e-06 min_angle_deg=83.644556400262 base_ok=True(diff=7.58e-13)`
3. **Corrupted negative test (duplicate vector `0` into vector `1`)**:
   - Exit code: `1` (non-zero, properly rejected)
   - Output: `FAIL: gain c_table - c* = -8.892981557120000e-01 ... (c_table=0.110701844288, c*=1.00000000000000000000)`

All reproduction and exact-arithmetic verification checks succeed.

pass: true
