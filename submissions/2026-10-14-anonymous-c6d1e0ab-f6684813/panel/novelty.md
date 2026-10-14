# Novelty Skeptic Report — `ghr-sum-difference-c3a` (`Partial Win p1`)

context: subagent
context: subagent (fable)

## 1. Executive Summary

I independently audited the novelty of the three claimed finite-certified lower bounds on the Gyarmati–Hennecart–Ruzsa sum-difference constant `C_{3a}` (`Partial Win p1` in `claim/CLAIM.md`, `claim/target.md`, and `claim/REPRODUCE.md`):
- `claim/best_k2_m2_finite_cert.json` (`SHA-256: a4be363d511abedbd64b9d99599e6d72572fe7423b96b63cce20e9e1b431e71b`): `C_{3a} ge 1.19299096527644796779957337201144650183761204467324` (`k = 2, m = 2, ell = 10^{16}, B = 21700, q = 25879, |M| = 6641`)
- `claim/best_k2_finite_cert.json` (`SHA-256: 88a8597a3f644e9ea00bdd76269ce69e5c367e9eeaddab9c1a8d3594d8750b1d`): `C_{3a} ge 1.19298973462186362590382529754753993070825527359705` (`k = 2, m = 1, ell = 10^{16}, B = 21700, q = 25879, |M| = 6641`)
- `claim/deep_k1_cert.json` (`SHA-256: f66848137f7f749bc2305b5fcca464507273d02a515a0e1174050714adf0da17`): `C_{3a} ge 1.19229311147308833018077611662264204140088149782869` (`k = 1, m = 1, ell = 10^{13}, B = 19572, q = 30295, |M| = 3889`)

All three certificates are novel, genuine finite-depth improvements over the standing published finite-certified record `1.19102809` (Kleinwaks 2026b), exceeding it by `+0.001962875...`, `+0.001961644...`, and `+0.001265021...` respectively (more than `12,650x` the `1e-7` threshold required for `Partial Win p1`).

---

## 2. Honest Live Scoreboard & Primary Source Fetches (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`)

Each primary source was fetched via a single `curl -sS -A "V3R1T4S-novelty-panel/1.0"` GET request at `2026-10-14T12:09:16Z` (and `2026-10-14T12:09:28Z` for Kleinwaks's repository README):

| Source URL | UTC Timestamp | HTTP Status | Byte Size | SHA-256 Hash | Extracted Standing Record / Status |
|---|---|---|---|---|---|
| `https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/3a.md` | `2026-10-14T12:09:16Z` | `200` | `8479` | `2ebc3954e674a94481435e422e5c0b82f53581a537e8d8e85ffae1684826641a` | Top row `[K2026b]`: `1.19102809 (1.19519192*)` — explicit finite construction of `1.19102809` (`B=17032`, base `34065`, `10^{13}` digits) alongside limit bound `1.19519192*` (`B=26972`, base `27022`) |
| `https://teorth.github.io/optimizationproblems/constants/3a.html` | `2026-10-14T12:09:16Z` | `200` | `10932` | `cdb3974928fbc6c12f0b60b4a783bbe292e513e3cb68ff6ad41119e8fe484faa` | Identical rendered table: top row `[K2026b]` is `1.19102809 (1.19519192*)` |
| `https://raw.githubusercontent.com/kleinwaks/masked-digit-sum-difference-bound/main/README.md` | `2026-10-14T12:09:28Z` | `200` | `6675` | `6ced037cefc460651c2f92f73b89a0023b76c2ba442dbc2dea4bdc9c02c72f19` | States `C_{3a} gt 1.19519192` in the controlled-carry limit and `C_{3a} gt 1.19102809` in the finite construction (`B=17032`, base `34065`, up to `10^{13}` digits) |
| `https://raw.githubusercontent.com/skyline-23/MSTD-search/main/README.md` | `2026-10-14T12:09:16Z` | `404` | `14` | `d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed` | `404: Not Found` (historical URL; active package is `kleinwaks/masked-digit-sum-difference-bound` audited above) |
| `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T12:09:16Z` | `200` | `1863362` | `38d410bab7edd7154c7e4a0033bbf3d1b65b28f836cc568ca08cb450ddb8a8c4` | `100` open PRs inspected; `0` PRs target `ghr-sum-difference-c3a`, `C_{3a}`, Ruzsa, or Kleinwaks |

---

## 3. Comparison Against Standing Published Bounds

In `constants/3a.md` (`SHA-256: 2ebc3954e674a94481435e422e5c0b82f53581a537e8d8e85ffae1684826641a`), the table distinguishes between:
1. **Limit lower bounds (marked with `*`)**: Best is `1.19519192*` (`[K2026b]`, Logan Kleinwaks 2026b, controlled-carry limit construction in base `27022`), preceded by `1.19102809*` (`[K2026]`) and `1.187326127925948*` (`[Num2026]`).
2. **Finite-certified lower bounds (without `*`, certified from a single explicit finite integer set)**:
   - Best published finite-certified bound is **`1.19102809`** (`[K2026b]`, Logan Kleinwaks 2026b, carry-free masked-digit construction in base `34065` with `10^{13}` digits; also `1.19102809427254...` in Zenodo 19363795), preceded by `1.1835129324` (`[MI2026]`, base-33 exact counting certificate).

Running `python3 claim/verify_c3a.py claim/best_k2_m2_finite_cert.json claim/best_k2_finite_cert.json claim/deep_k1_cert.json` confirms that all three claimed certificates are explicit finite-set constructions (`nh = 0`, `methods_agree = true`) that strictly beat `1.19102809427254`:

| Certificate File | Parameters `(k, m, ell, B, q, |M|)` | Certified 50-Digit Finite Lower Bound | Standing Finite Record (`[K2026b]`) | Net Gain over `1.19102809427254` | Margin Ratio vs. `1e-7` (`p1`) |
|---|---|---|---|---|---|
| `claim/best_k2_m2_finite_cert.json` | `(2, 2, 10^{16}, 21700, 25879, 6641)` | `1.19299096527644796779957337201144650183761204467324` | `1.19102809427254...` | **`+0.00196287100390...`** | **`19,628x`** |
| `claim/best_k2_finite_cert.json` | `(2, 1, 10^{16}, 21700, 25879, 6641)` | `1.19298973462186362590382529754753993070825527359705` | `1.19102809427254...` | **`+0.00196164034932...`** | **`19,616x`** |
| `claim/deep_k1_cert.json` | `(1, 1, 10^{13}, 19572, 30295, 3889)` | `1.19229311147308833018077611662264204140088149782869` | `1.19102809427254...` | **`+0.00126501720054...`** | **`12,650x`** |

 Furthermore, the mathematical mechanism—Controlled-Carry Block Reduction Modulo `q^k` (`k in {1, 2}`) with odd base `q in (B, 2B+1)` (`nh = 0`) combined with **Non-Semigroup Modulo-`q` Shadow Pruning** (pruning `7` top elements in `claim/best_k2_m2_finite_cert.json` and `371` elements in `claim/deep_k1_cert.json` from the truncated multiplicative semigroup)—is genuinely new: both `[K2026]` and `[K2026b]` use unpruned truncated multiplicative semigroups (`M = semigroup cap [0, B]`) and only certify finite sets in the carry-free (`q ge 2B+1`) regime.

---

## 4. Internal Duplicate Check (`TROPHY_CASE.md` & Open PRs)

1. **`TROPHY_CASE.md`**: Holds 53 rows across 7 families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`). Zero entries involve `ghr-sum-difference-c3a` or sum-difference exponents.
2. **Open PRs (`elder-plinius/V3R1T4S`)**: Across all 100 open PRs (`SHA-256: 38d410bab7edd7154c7e4a0033bbf3d1b65b28f836cc568ca08cb450ddb8a8c4`), zero PRs target `ghr-sum-difference-c3a`.

pass: true
