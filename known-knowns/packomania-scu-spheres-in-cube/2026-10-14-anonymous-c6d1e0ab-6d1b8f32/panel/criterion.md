# CRITERION Skeptic Report: `packomania-scu-spheres-in-cube` — 13 Full Wins plus Partial Wins `p1` and `p3`

context: subagent
confirmed_scope: Verified 13 explicit 36-decimal-place sphere-in-cube packings in claim/ for N in {101, 466, 467, 468, 470, 471, 472, 630, 631, 632, 793, 812, 1596} inside [-1/2, 1/2]^3, highlighted by claim/scu1596.txt (201,096 bytes, SHA-256 17ad9561bd7a7f216eac6525ed3ed67de13668b78707c2187c5421ae4f40d589, Michael Goldberg row achieving 65-digit r* = 0.045873685240229747068212434815 vs live scu/txt/radius.txt 0.045385736359615385798733074995, gain +4.879489e-04 for both Full Win and Partial Win p1) and claim/scu812.txt (102,312 bytes, SHA-256 b4ef136473f35c336af549b452ceb08996ed207204969e68c194e2cbdbea700c, achieving r* = 0.056962823157162590720289755717 vs 0.056959450361781703936323533204, gain +3.372795e-06), with all 13 non-isometric to posted coordinates and beating live scu/txt/radius.txt by at least 1e-11, alongside Partial Win p3 data-integrity findings on posted scu469.txt and scu629.txt.

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Full Win (`CONFIRMED_SOLUTION` Across 13 Listed Rows) & Partial Win `p1` (`N = 1596`)
Executed `python3 claim/verify_scu.py claim/scu*.txt` across all 13 candidate coordinate files:
- **Container & Coordinate Precision**: All $N$ sphere centers in each `claim/scu{N}.txt` lie inside the centered unit cube $[-1/2, 1/2]^3$ and have $36$ decimal places per coordinate (at least $30$ decimal places).
- **Exact 65-Digit Decimal Feasible Radius**:
  For each file, the exact feasible radius
  $$r^*(c) = \min\left(\min_{1 \le i \ne j \le N} \frac{\|c_i - c_j\|_2}{2},\; \frac{1}{2} - \max_{1 \le i \le N} \max(|x_i|, |y_i|, |z_i|)\right)$$
  was evaluated in 65-digit `decimal.Decimal` arithmetic with zero tolerance, confirming $r_{\text{pair}}(c) = r_{\text{bound}}(c) = r^*(c)$ to 30+ decimal places and $r^*(c) - r_{\text{table}}(N) \ge 10^{-11}$ (from $10.38\times$ up to $48,794,888\times$ the $10^{-11}$ threshold).
- **Seed Calibration & Non-Isometry Check**:
  - For every $N$ with a posted coordinate file, recomputing $r_{\text{seed}}$ in 65-digit arithmetic reproduced $r_{\text{table}}(N)$ to within $8.213 \times 10^{-32} \dots 9.098 \times 10^{-31}$ (well within the $10^{-20}$ calibration requirement).
  - Comparing sorted pairwise-distance multisets between `claim/scu{N}.txt` and the posted `scu{N}.txt` gave maximum absolute differences between $2.837 \times 10^{-3}$ and $8.378 \times 10^{-2}$, proving non-isometry for all 13 packings.
- **Partial Win `p1` (`N = 1596`)**: In `author.txt`, $N = 1596$ is attributed to `Michael Goldberg`. `claim/scu1596.txt` improves $r_{\text{table}}(1596)$ from $0.045385736359615385798733074995$ to $0.045873685240229747068212434815$ (`+4.879489e-04`), simultaneously satisfying the Full Win criterion and Partial Win `p1`.
- **Update-Log & Pending-Queue Compliance**:
  - Re-fetched `scu/txt/radius.txt` (`Last-Modified: Wed, 07 Oct 2026 19:04:28 GMT`) and `pending-requests.html` (`Last-Modified: Thu, 08 Oct 2026 07:39:03 GMT`) at `2026-10-14T11:07:40Z`.
  - None of the 13 claimed $N$ values appear in recent `scu.html` History-of-updates entries (`01-Oct-2026` through `07-Oct-2026`), and `pending-requests.html` has zero explicit entries under category `scu`. As required by `claim/target.md`, the caveat regarding the category-unspecified `26-Sep-2026 Moki & Julio *many* 4666 candidates` bundle is explicitly stated.

### 1.2 Verified Artifact Table

| $N$ | Artifact (`claim/`) | Bytes | SHA-256 | Author | Live $r_{\text{table}}(N)$ | Certified 65-Digit $r^*(c)$ (30 decimals) | Gain $\Delta r$ | Max Dist Diff vs Posted |
| ---: | :--- | ---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1596** | `claim/scu1596.txt` | `201,096` | `17ad9561bd7a7f216eac6525ed3ed67de13668b78707c2187c5421ae4f40d589` | Michael Goldberg | `0.045385736359615385798733074995` | `0.045873685240229747068212434815` | **`+4.879489e-04`** | `4.792e-02` |
| **812** | `claim/scu812.txt` | `102,312` | `b4ef136473f35c336af549b452ceb08996ed207204969e68c194e2cbdbea700c` | Eckard Specht | `0.056959450361781703936323533204` | `0.056962823157162590720289755717` | **`+3.372795e-06`** | `7.254e-02` |
| **101** | `claim/scu101.txt` | `12,726` | `605bc0591017c7a2eec3f7a37ec33b16936a3664a312bcde00b2bdf46e6538c6` | Eckard Specht | `0.110240604605984488395300868556` | `0.110240606233695265468856021377` | **`+1.627711e-09`** | `3.555e-02` |
| **793** | `claim/scu793.txt` | `99,918` | `1c017482412f0f9653595e9735da2ebbb6a270defb8cbca9d5c57c0c838167ad` | Eckard Specht | `0.057356312222008810279000968621` | `0.057356313101938118309456188665` | **`+8.799293e-10`** | `4.330e-02` |
| **630** | `claim/scu630.txt` | `79,380` | `6d1b8f3299eaf5e0b15af9d921eeb470326b168ce651e3d13588e931498384b8` | Eckard Specht | `0.061949671549650065797038760848` | `0.061949671758532088700924620370` | **`+2.088820e-10`** | `2.830e-02` |
| **632** | `claim/scu632.txt` | `79,632` | `277bfc6a2364e3872f20f42731ccc6e4c5de4cd564814081cf7a3f6398c4b320` | Eckard Specht | `0.061949671549647706846377765805` | `0.061949671758524842833475299750` | **`+2.088771e-10`** | `2.953e-02` |
| **631** | `claim/scu631.txt` | `79,506` | `ab0e5bdcb3875d14645a826e6fcdb65ed580b92640951785e72e3d33a6c5607f` | Eckard Specht | `0.061949671549657821193834961183` | `0.061949671758498235727065581655` | **`+2.088404e-10`** | `2.627e-02` |
| **467** | `claim/scu467.txt` | `58,842` | `66125d4a47294cc7f8c660b9d3b7fb2816badb205eea8f7ec1ab95cbc984e096` | Eckard Specht | `0.067898240894769256234850175248` | `0.067898241051356988413398240298` | **`+1.565877e-10`** | `2.837e-03` |
| **468** | `claim/scu468.txt` | `58,968` | `2ea8af5d391598dc221e4917930da4d42f17f9e541168d1fceed500b11975b89` | Eckard Specht | `0.067898240894769256234850175248` | `0.067898241051356515264205650656` | **`+1.565873e-10`** | `8.378e-02` |
| **466** | `claim/scu466.txt` | `58,716` | `6be37ca99afd5dd53f5719e2a5be83c417c385742c2696ed4187ec9cfe334105` | Eckard Specht | `0.067898240894769256234850176022` | `0.067898241051355201396095879180` | **`+1.565859e-10`** | `4.059e-02` |
| **470** | `claim/scu470.txt` | `59,220` | `d31613aa605c97184a2a8650cd9c6141671d413cb35a6802838201698e3091eb` | Eckard Specht | `0.067898240894670536184764825826` | `0.067898241049419029535261829608` | **`+1.547485e-10`** | `1.961e-02` |
| **471** | `claim/scu471.txt` | `59,346` | `71702210656fae6819da996508da9b9d6383404d274e8405df0a85de342f90b8` | Eckard Specht | `0.067898240894670536184764825826` | `0.067898241042897910706805143111` | **`+1.482274e-10`** | `3.079e-02` |
| **472** | `claim/scu472.txt` | `59,472` | `ca6a9077d3d117cabe44cb177bfe495846e3e4208c782799631ce082c05d2df7` | Eckard Specht | `0.067898240894670536184764825826` | `0.067898240998505114761175793623` | **`+1.038346e-10`** | `4.215e-02` |

### 1.3 Partial Win `p3` (Data-Integrity Audit Findings on Posted `scu469.txt` and `scu629.txt`)
Direct 65-digit `decimal.Decimal` evaluation of the newly posted October 2026 coordinate files confirmed two 12th-decimal upward-rounding discrepancies in `scu/txt/radius.txt`:
- Posted `scu469.txt` achieves exact feasible radius $r^* = 0.067898241050927994885858599319$, whereas `radius.txt` lists `0.067898241051000000000000000000` (deficit $-7.201 \times 10^{-14}$).
- Posted `scu629.txt` achieves exact feasible radius $r^* = 0.061949671761730316605613408051$, whereas `radius.txt` lists `0.061949671762000000000000000000` (deficit $-2.697 \times 10^{-13}$).

## 2. Verdict
All literal clauses of the Full Win criterion across all 13 claimed rows, Partial Win `p1` (`N = 1596`), and Partial Win `p3` in `claim/target.md` are satisfied.

pass: true
