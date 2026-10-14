# REPRODUCE Skeptic Report — Packomania Equal Spheres in a Cube (`packomania-scu-spheres-in-cube`)

- **target**: `packomania-scu-spheres-in-cube`
- **panel_role**: REPRODUCE Skeptic
- context: subagent
- context: subagent (astra)

## 1. Exact Mathematical Definition Quoted from `claim/target.md` and `claim/CLAIM.md`

From `claim/target.md` (lines 14 and 29) and `claim/CLAIM.md` (lines 8-10):
- **Container**: Centered unit cube $[-1/2, 1/2]^3 \subset \mathbb{R}^3$ of edge length $1$ centered at the origin.
- **Configuration**: $N$ sphere centers $c = (c_1, \dots, c_N)$ with $c_i = (x_i, y_i, z_i) \in [-1/2, 1/2]^3$.
- **Exact Feasible Radius $r^*(c)$**:
  $$r_{\text{pair}}(c) = \frac{1}{2} \min_{1 \le i \neq j \le N} \|c_i - c_j\|_2, \qquad r_{\text{bound}}(c) = \frac{1}{2} - \max_{1 \le i \le N} \max(|x_i|, |y_i|, |z_i|),$$
  $$r^*(c) = \min\bigl(r_{\text{pair}}(c),\; r_{\text{bound}}(c)\bigr).$$
- **Full Win Criterion**:
  1. $r^*(c) - r_{\text{table}}(N) \ge 10^{-11}$, where $r_{\text{table}}(N)$ is the 30-decimal table entry in `data/radius.txt` (`https://packomania.com/scu/txt/radius.txt`).
  2. Non-isometry: the sorted pairwise Euclidean distance multiset of $c$ differs from that of the posted reference configuration in `data/seeds/scu{N}.txt`.
  3. Queue and update-log compliance against `scu.html` and `pending-requests.html`.
- **Partial Win `p1`**: A certified improvement under the same rule for an $N$ whose live author in `data/author.txt` is `Michael Goldberg`, `Hugo Pfoertner`, or `Dave Boll`.
- **Partial Win `p3`**: Data-integrity audit re-deriving the 30-decimal table radius from posted coordinate files and identifying rows where the posted coordinates do not achieve the posted table radius.

---

## 2. Independent 70-Digit `decimal.Decimal` Verification (Written Before Inspecting `claim/verify_scu.py`)

Before reading `claim/verify_scu.py`, I wrote and executed an independent Python verifier using `decimal.Decimal` with `getcontext().prec = 70`. For each of the 13 claimed files in `claim/`:
1. Verified the exact SHA-256 digest, line count $N$, 1-based sequential indices $1 \dots N$, and 36-decimal 3D coordinate strings $(x_i, y_i, z_i) \in [-1/2, 1/2]^3$.
2. Computed exact 70-digit pairwise Euclidean distances $\|c_i - c_j\|_2 = \sqrt{(x_i-x_j)^2 + (y_i-y_j)^2 + (z_i-z_j)^2}$ across all $N(N-1)/2$ pairs and exact boundary clearances $1/2 - \max(|x_i|, |y_i|, |z_i|)$ across all $3N$ coordinates.
3. Evaluated $r_{\text{pair}}(c)$, $r_{\text{bound}}(c)$, and $r^*(c) = \min(r_{\text{pair}}(c), r_{\text{bound}}(c))$, and compared against `data/radius.txt`, `data/author.txt`, and the reference coordinates in `data/seeds/scu{N}.txt`.

### Complete 13-Claim Independent Verification Table (36-Digit Exact Results)

| $N$ | Certificate File | SHA-256 (prefix) | Author (`data/author.txt`) | Table Radius $r_{\text{table}}(N)$ (`data/radius.txt`) | Independent $r^*(c)$ (first 36 decimals) | $\|r_{\text{pair}} - r_{\text{bound}}\|$ | Gain $\Delta r = r^*(c) - r_{\text{table}}(N)$ | Ratio $\Delta r / 10^{-11}$ | Max Sorted Pairwise Distance Diff vs Reference | Tight Contacts ($\le 10^{-12}$: pair / wall) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1596** | `claim/scu1596.txt` | `17ad9561bd7a7f21` | `Michael Goldberg` | `0.045385736359615385798733074995` | `0.045873685240229747068212434814917178` | `6.51e-37` | `+0.000487948880614361269479359820` (`+4.879489e-04`) | `48,794,888.06x` | `4.792249e-02` | `6420 / 565` | **PASS (Full Win + `p1`)** |
| **812** | `claim/scu812.txt` | `b4ef136473f35c33` | `Eckard Specht` | `0.056959450361781703936323533204` | `0.056962823157162590720289755717346378` | `2.98e-37` | `+0.000003372795380886783966222513` (`+3.372795e-06`) | `337,279.54x` | `7.253612e-02` | `2 / 2` | **PASS (Full Win)** |
| **101** | `claim/scu101.txt` | `605bc0591017c7a2` | `Eckard Specht` | `0.110240604605984488395300868556` | `0.110240606233695265468856021376768575` | `1.17e-37` | `+0.000000001627710777073555152821` (`+1.627711e-09`) | `162.77x` | `3.555072e-02` | `6 / 4` | **PASS (Full Win)** |
| **793** | `claim/scu793.txt` | `1c017482412f0f96` | `Eckard Specht` | `0.057356312222008810279000968621` | `0.057356313101938118309456188665167160` | `3.26e-37` | `+0.000000000879929308030455220044` (`+8.799293e-10`) | `87.99x` | `4.329656e-02` | `1288 / 186` | **PASS (Full Win)** |
| **630** | `claim/scu630.txt` | `6d1b8f3299eaf5e0` | `Eckard Specht` | `0.061949671549650065797038760848` | `0.061949671758532088700924620369910023` | `2.56e-37` | `+0.000000000208882022903885859522` (`+2.088820e-10`) | `20.89x` | `2.829947e-02` | `10 / 4` | **PASS (Full Win)** |
| **632** | `claim/scu632.txt` | `277bfc6a2364e387` | `Eckard Specht` | `0.061949671549647706846377765805` | `0.061949671758524842833475299749941559` | `5.53e-38` | `+0.000000000208877135987097533945` (`+2.088771e-10`) | `20.89x` | `2.952880e-02` | `10 / 4` | **PASS (Full Win)** |
| **631** | `claim/scu631.txt` | `ab0e5bdcb3875d14` | `Eckard Specht` | `0.061949671549657821193834961183` | `0.061949671758498235727065581655485909` | `7.88e-37` | `+0.000000000208840414533230620472` (`+2.088404e-10`) | `20.88x` | `2.626935e-02` | `10 / 4` | **PASS (Full Win)** |
| **467** | `claim/scu467.txt` | `66125d4a47294cc7` | `Eckard Specht` | `0.067898240894769256234850175248` | `0.067898241051356988413398240297943910` | `2.45e-37` | `+0.000000000156587732178548065050` (`+1.565877e-10`) | `15.66x` | `2.837370e-03` | `168 / 23` | **PASS (Full Win)** |
| **468** | `claim/scu468.txt` | `2ea8af5d391598dc` | `Eckard Specht` | `0.067898240894769256234850175248` | `0.067898241051356515264205650656427762` | `1.93e-37` | `+0.000000000156587259029355475408` (`+1.565873e-10`) | `15.66x` | `8.377587e-02` | `176 / 23` | **PASS (Full Win)** |
| **466** | `claim/scu466.txt` | `6be37ca99afd5dd5` | `Eckard Specht` | `0.067898240894769256234850176022` | `0.067898241051355201396095879179994220` | `1.46e-37` | `+0.000000000156585945161245703158` (`+1.565859e-10`) | `15.66x` | `4.059495e-02` | `162 / 23` | **PASS (Full Win)** |
| **470** | `claim/scu470.txt` | `d31613aa605c9718` | `Eckard Specht` | `0.067898240894670536184764825826` | `0.067898241049419029535261829608001026` | `8.96e-37` | `+0.000000000154748493350497003782` (`+1.547485e-10`) | `15.47x` | `1.961193e-02` | `352 / 79` | **PASS (Full Win)** |
| **471** | `claim/scu471.txt` | `71702210656fae68` | `Eckard Specht` | `0.067898240894670536184764825826` | `0.067898241042897910706805143111229135` | `7.73e-37` | `+0.000000000148227374522040317285` (`+1.482274e-10`) | `14.82x` | `3.079186e-02` | `15 / 2` | **PASS (Full Win)** |
| **472** | `claim/scu472.txt` | `ca6a9077d3d117ca` | `Eckard Specht` | `0.067898240894670536184764825826` | `0.067898240998505114761175793622902648` | `5.15e-37` | `+0.000000000103834578576410967797` (`+1.038346e-10`) | `10.38x` | `4.215108e-02` | `24 / 5` | **PASS (Full Win)** |

### Tightest Witness Pairs and Boundary Spheres (70-Digit Independent Check)
- `claim/scu101.txt`: minimizing pair $(1, 7)$ (`r_pair = 0.110240606233695265468856021376768575`), boundary witness sphere $7$ axis $y$ (`r_bound = 0.110240606233695265468856021376768575`).
- `claim/scu466.txt`: minimizing pair $(147, 195)$ (`r_pair = 0.067898241051355201396095879179994220`), boundary witness sphere $195$ axis $y$ (`r_bound = 0.067898241051355201396095879179994220`).
- `claim/scu467.txt`: minimizing pair $(112, 168)$ (`r_pair = 0.067898241051356988413398240297943910`), boundary witness sphere $12$ axis $z$ (`r_bound = 0.067898241051356988413398240297943910`).
- `claim/scu468.txt`: minimizing pair $(99, 147)$ (`r_pair = 0.067898241051356515264205650656427762`), boundary witness sphere $12$ axis $z$ (`r_bound = 0.067898241051356515264205650656427762`).
- `claim/scu470.txt`: minimizing pair $(396, 464)$ (`r_pair = 0.067898241049419029535261829608001026`), boundary witness sphere $10$ axis $z$ (`r_bound = 0.067898241049419029535261829608001027`).
- `claim/scu471.txt`: minimizing pair $(76, 86)$ (`r_pair = 0.067898241042897910706805143111229136`), boundary witness sphere $86$ axis $x$ (`r_bound = 0.067898241042897910706805143111229135`).
- `claim/scu472.txt`: minimizing pair $(84, 86)$ (`r_pair = 0.067898240998505114761175793622902649`), boundary witness sphere $62$ axis $y$ (`r_bound = 0.067898240998505114761175793622902648`).
- `claim/scu630.txt`: minimizing pair $(560, 629)$ (`r_pair = 0.061949671758532088700924620369910023`), boundary witness sphere $1$ axis $z$ (`r_bound = 0.061949671758532088700924620369910023`).
- `claim/scu631.txt`: minimizing pair $(1, 88)$ (`r_pair = 0.061949671758498235727065581655485909`), boundary witness sphere $1$ axis $y$ (`r_bound = 0.061949671758498235727065581655485910`).
- `claim/scu632.txt`: minimizing pair $(258, 303)$ (`r_pair = 0.061949671758524842833475299749941559`), boundary witness sphere $1$ axis $y$ (`r_bound = 0.061949671758524842833475299749941559`).
- `claim/scu793.txt`: minimizing pair $(651, 731)$ (`r_pair = 0.057356313101938118309456188665167160`), boundary witness sphere $402$ axis $y$ (`r_bound = 0.057356313101938118309456188665167160`).
- `claim/scu812.txt`: minimizing pair $(624, 627)$ (`r_pair = 0.056962823157162590720289755717346378`), boundary witness sphere $521$ axis $x$ (`r_bound = 0.056962823157162590720289755717346378`).
- `claim/scu1596.txt`: minimizing pair $(1491, 1596)$ (`r_pair = 0.045873685240229747068212434814917178`), boundary witness sphere $10$ axis $z$ (`r_bound = 0.045873685240229747068212434814917179`).

### Reference Calibration and Partial Win `p3` Verification
- For all 13 claimed $N$, our independent 70-digit evaluation of `data/seeds/scu{N}.txt` reproduces `data/radius.txt` to within $9.10 \times 10^{-31} \le 10^{-20}$.
- For Partial Win `p3`, our independent 70-digit evaluation of `data/seeds/scu469.txt` and `data/seeds/scu629.txt` confirms the data-integrity finding reported in `claim/CLAIM.md`:
  - `data/seeds/scu469.txt` achieves $r^* = 0.067898241050927994885858599318544646$, which falls short of the 12-decimal rounded `data/radius.txt` entry `0.067898241051000000000000000000` by $-7.200511 \times 10^{-14}$ (and is strictly beaten by `claim/scu466.txt`, `claim/scu467.txt`, and `claim/scu468.txt`).
  - `data/seeds/scu629.txt` achieves $r^* = 0.061949671761730316605613408051125552$, which falls short of the 12-decimal rounded `data/radius.txt` entry `0.061949671762000000000000000000` by $-2.696834 \times 10^{-13}$.

---

## 3. Audit of `claim/verify_scu.py` and Negative-Control Corruption Tests

1. **Audit and Execution of `claim/verify_scu.py`**:
   - Inspected `claim/verify_scu.py` (202 lines). It sets `getcontext().prec = 65`, parses all 3D coordinates as exact `Decimal` instances, computes $r_{\text{bound}} = 1/2 - \max_{i,k} |c_{i,k}|$ and $r_{\text{pair}} = \min_{i \neq j} \|c_i - c_j\|_2 / 2$, checks seed calibration ($\le 10^{-20}$), checks non-isometry against `data/seeds/scu{N}.txt`, and enforces $r^* - r_{\text{table}}(N) \ge 10^{-11}$. There are no hard-coded return values, tolerance relaxations, or bypasses.
   - Executed `python3 claim/verify_scu.py claim/scu*.txt`: all 13 files passed (`RESULT: PASS (CONFIRMED_SOLUTION)` on 12 files and `RESULT: PASS (CONFIRMED_SOLUTION + PARTIAL WIN p1)` on `claim/scu1596.txt`, exit code `0`), matching `claim/verification.log` and our independent 70-digit verifier.
2. **Negative-Control 1-Digit Perturbation Tests**:
   - **`claim/scu101.txt`**: Perturbed coordinate $y_7$ of boundary-contact sphere $7$ outward by $10^{-4}$ (from `-0.389759393766304734531143978623231425` to `-0.389859393766304734531143978623231425`). Both our independent verifier and `claim/verify_scu.py` reported $r^*(c_{\text{bad}}) = 0.110140606233695265468856021376768575$, dropping $\Delta r$ to $-9.999837 \times 10^{-5}$ below $r_{\text{table}}(101)$ and failing with `Threshold check: FAIL` / `RESULT: FAIL` (exit code `1`).
   - **`claim/scu1596.txt`**: Perturbed coordinate $z_{10}$ of boundary-contact sphere $10$ outward by $10^{-3}$ (from `-0.454126314759770252931787565185082821` to `-0.455126314759770252931787565185082821`). Both our independent verifier and `claim/verify_scu.py` reported $r^*(c_{\text{bad}}) = 0.044873685240229747068212434814917179$, dropping $\Delta r$ to $-5.120511 \times 10^{-4}$ below $r_{\text{table}}(1596)$ and failing with `Threshold check: FAIL` / `RESULT: FAIL` (exit code `1`).
   - All temporary scripts and corrupted test files were deleted after verification.

pass: true
