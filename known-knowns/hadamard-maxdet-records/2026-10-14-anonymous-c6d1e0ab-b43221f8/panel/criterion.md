# CRITERION Skeptic Report: `hadamard-maxdet-records` — Order `n = 117` Full Win

context: subagent
confirmed_scope: Verified that claim/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt (33,517 bytes, SHA-256 b43221f8bfb6744869262c930cb7e1845f3a285b7f636cac39cca47844a3a3bb) is an explicit 117x117 {-1,+1} matrix with exact normalized determinant |det X| / 2^116 = 324 * 29^57 = 73659860230620869930312403886045415232575930948902221537499019577403834332848324440116, strictly improving by 1.018597x upon the standing Orrick/Rokicki and Math-AI-Caltech record 72314994254613394470813334860641212637154205430658679584420251275641935854599391452615 while remaining below the Barba bound.

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Order & Matrix Entry Compliance
- **Order check**: $n = 117 \equiv 1 \pmod 4$, so $n$ is not divisible by $4$.
- **Matrix entries**: Parsed `claim/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt` (`33,517` bytes, SHA-256 `b43221f8bfb6744869262c930cb7e1845f3a285b7f636cac39cca47844a3a3bb`); confirmed $117$ rows of $117$ entries ($13,689$ entries total), all in $\{-1, +1\}$.

### 1.2 Exact Integer Determinant & Independent Cross-Checks
- **Fraction-free Bareiss elimination** on Python arbitrary-precision integers, **27-prime Chinese Remainder Theorem (CRT)** modular Gaussian elimination, and **exact `fractions.Fraction` Gaussian elimination** all produce the identical integer determinant:
  $$D(X_{117}) = \frac{|\det X_{117}|}{2^{116}} = 324 \cdot 29^{57} = 73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.$$
- **Divisibility by $2^{n-1}$**: Confirmed $|\det X_{117}|$ is divisible by $2^{116}$ with zero remainder.

### 1.3 Standing Record & Barba Upper Bound Comparison
- **Standing record**: Across the archived Orrick/Rokicki MaxDet database (`rokicki_best116.html`), `Math-AI-Caltech/hadamard-maxdet`, and `arXiv:2608.22518` (which only improved $n = 51$ and $n \equiv 3 \pmod 4$ in $103..119$), the best known normalized determinant at $n = 117$ was:
  $$D_{\text{rec}}(117) = 72314994254613394470813334860641212637154205430658679584420251275641935854599391452615.$$
- **Strict improvement**: $D(X_{117})$ exceeds $D_{\text{rec}}(117)$ by a factor of $1.0185973323\times$.
- **Residue-class upper bound (Barba bound for $n \equiv 1 \pmod 4$)**:
  $$B_{\text{norm}}(117) = \left\lfloor \sqrt{233} \cdot 29^{58} \right\rfloor = 100637963222637963009859920958577753795295722943327423237910285617343105697857847003583.$$
  Since $2n - 1 = 233$ is prime (not a square), the Barba bound was not previously attained ($D_{\text{rec}}(117)$ had ratio $0.718566$ to the Barba bound), and $D(X_{117})$ does not exceed $B_{\text{norm}}(117)$ (new ratio $R = 0.731929$).

## 2. Verdict
All clauses of the full success criterion in `claim/target.md` are satisfied.

pass: true
