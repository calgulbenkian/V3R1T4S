# Preregistration: Lens 1 — C Evaluator-Optimizer (Bordered High-Excess Hadamard & Sherman-Morrison Search)

## 1. Hypothesis and Attack Architecture
For unclosed orders $n \equiv 1 \pmod 4$ with $n = 4k + 1$, Orrick and Solomon (2003, `arXiv:math/0311292`) established that bordering a $4k \times 4k$ Hadamard matrix $H_{4k}$ whose row/column signs have been switched to attain excess $\Sigma(H_{4k}) = \mathbf{1}_{4k}^T H_{4k} \mathbf{1}_{4k}$ yields an explicit $n \times n$ $\{\pm 1\}$ matrix
$$R = \begin{pmatrix} -1 & \mathbf{1}_{4k}^T \\ \mathbf{1}_{4k} & H_{4k} \end{pmatrix}$$
with exact integer normalized determinant
$$D(R) = \frac{|\det R|}{2^{n-1}} = \left(k + \frac{\Sigma(H_{4k})}{4}\right) k^{2k-1}.$$
In the reference MaxDet catalog (`orrick_fullPage.html`, `Math-AI-Caltech/hadamard-maxdet`, and `tomas.rokicki.com/newrec.html`), the bordered-Hadamard construction was only carried up to $n - 1 = 100$ ($n = 101$); for $n = 105$ ($k = 26$), $n = 109$ ($k = 27$), and $n = 117$ ($k = 29$), the standing baseline records are Tomas Rokicki's April 2005 double-circulant matrices (`best104.html`, `best108.html`, `best116.html`) with ratios $R \in [0.65, 0.72]$.

Furthermore, starting from a bordered high-excess Hadamard matrix $R$, flipping interior entries $R_{ij} \gets -R_{ij}$ changes $\det(R)$ by the exact rank-1 Sherman-Morrison factor $|1 - 2 R_{ij} (R^{-1})_{ji}|$, which can break out of the rigid $(n-1) I_{n-1} + J_{n-1}$ Gram spectrum when a single or paired interior flip increases $|\det R|$ (as occurred historically at $n = 57$).

## 2. Target Orders & Baseline Records
1. **$n = 105$ ($k = 26$, $n - 1 = 104 = 103 + 1$, $p = 103 \equiv 3 \pmod 4$ prime)**:
   - Standing baseline record: `384743747284587846942188483608583600735563257274079045682562818122226665625` ($\approx 263.955566 \times 26^{51}$, $R = 0.70$, Rokicki 2005).
   - Required excess to beat baseline via Paley Class I $H_{104}$: $\Sigma(H_{104}) \ge 952$ ($D \ge 264 \times 26^{51}$).
2. **$n = 109$ ($k = 27$, $n - 1 = 108 = 107 + 1$, $p = 107 \equiv 3 \pmod 4$ prime)**:
   - Standing baseline record: `1877483841834222713683125485573890072927341503771574105042244268774869908324352` ($\approx 257.808189 \times 27^{53}$, $R = 0.65$, Rokicki 2005).
   - Required excess to beat baseline via Paley Class I $H_{108}$: $\Sigma(H_{108}) \ge 924$ ($D \ge 258 \times 27^{53}$).
3. **$n = 117$ ($k = 29$, $n - 1 = 116 = 4 \times 29$, Williamson quadruple $m = 29$)**:
   - Standing baseline record: `72314994254613394470813334860641212637154205430658679584420251275641935854599391452615` ($\approx 318.084477 \times 29^{57}$, $R = 0.72$, Rokicki 2005).
   - Required excess to beat baseline via Williamson $H_{116}$: $\Sigma(H_{116}) \ge 1160$ ($D \ge 319 \times 29^{57}$).
4. **Smaller unclosed $n \equiv 1 \pmod 4$ orders ($n \in \{37, 45, 49, 53, 65, 69, 73, 77, 81, 89, 93, 97\}$)**:
   - Audit whether multi-start excess maximization + rank-1/rank-2 Sherman-Morrison coordinate ascent from Paley I, Paley II, and Williamson Hadamard cores improves on the Orrick-Solomon records.

## 3. Implementation & Verification Protocol
- Compile `code/maxdet_search.c` (`clang -O3 -march=native -pthread`) implementing fast multi-start taboo/simulated-annealing sign-switching for Hadamard excess $\Sigma(H_{4k})$ followed by Sherman-Morrison rank-1 and rank-2 determinant coordinate ascent.
- Verify every candidate matrix independently via `verify_maxdet.py` using both exact fraction-free Bareiss elimination and multi-prime CRT modular determinants.
null_test: not needed because hadamard-maxdet-records is an exact deterministic integer determinant problem
