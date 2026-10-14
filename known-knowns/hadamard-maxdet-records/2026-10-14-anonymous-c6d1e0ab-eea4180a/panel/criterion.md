# CRITERION Skeptic Report: `hadamard-maxdet-records` — Order `n = 105` Full Win

context: subagent
confirmed_scope: Verified that claim/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt (26,959 bytes, SHA-256 eea4180adc25f6e40db1e7bac9a06f7b63183141abaadbdf7d44c83af403e50b) is an explicit 105x105 {-1,+1} matrix with exact normalized determinant |det X| / 2^104 = 276 * 26^51 = 402299811033982511699641115457655638247621548505385285611140221022215602176, strictly improving by 1.045631x upon the standing Orrick/Rokicki and Math-AI-Caltech record 384743747284587846942188483608583600735563257274079045682562818122226665625 while remaining below the Barba bound.

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Order & Matrix Entry Compliance
- **Order check**: $n = 105 \equiv 1 \pmod 4$, so $n$ is not divisible by $4$.
- **Matrix entries**: Parsed `claim/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt` (`26,959` bytes, SHA-256 `eea4180adc25f6e40db1e7bac9a06f7b63183141abaadbdf7d44c83af403e50b`); confirmed $105$ rows of $105$ entries ($11,025$ entries total), all in $\{-1, +1\}$.

### 1.2 Exact Integer Determinant & Independent Cross-Checks
- **Fraction-free Bareiss elimination** on Python arbitrary-precision integers, **24-prime Chinese Remainder Theorem (CRT)** modular Gaussian elimination, and **exact `fractions.Fraction` Gaussian elimination** all produce the identical integer determinant:
  $$D(X_{105}) = \frac{|\det X_{105}|}{2^{104}} = 276 \cdot 26^{51} = 402299811033982511699641115457655638247621548505385285611140221022215602176.$$
- **Divisibility by $2^{n-1}$**: Confirmed $|\det X_{105}|$ is divisible by $2^{104}$ with zero remainder.

### 1.3 Standing Record & Barba Upper Bound Comparison
- **Standing record**: Across the archived Orrick/Rokicki MaxDet database (`rokicki_best104.html`), `Math-AI-Caltech/hadamard-maxdet`, and `arXiv:2608.22518` (which only improved $n = 51$ and $n \equiv 3 \pmod 4$ in $103..119$), the best known normalized determinant at $n = 105$ was:
  $$D_{\text{rec}}(105) = 384743747284587846942188483608583600735563257274079045682562818122226665625.$$
- **Strict improvement**: $D(X_{105})$ exceeds $D_{\text{rec}}(105)$ by a factor of $1.0456305327\times$.
- **Residue-class upper bound (Barba bound for $n \equiv 1 \pmod 4$)**:
  $$B_{\text{norm}}(105) = \left\lfloor \sqrt{209} \cdot 26^{52} \right\rfloor = 547882258728472660210324664501712688349467880552241675318385825994770342169.$$
  Since $2n - 1 = 209 = 11 \cdot 19$ is not a square, the Barba bound was not previously attained ($D_{\text{rec}}(105)$ had ratio $0.702238$ to the Barba bound), and $D(X_{105})$ does not exceed $B_{\text{norm}}(105)$ (new ratio $R = 0.734282$).

## 2. Verdict
All clauses of the full success criterion in `claim/target.md` are satisfied.

pass: true
