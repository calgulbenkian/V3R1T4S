# CRITERION Skeptic Report: `hadamard-maxdet-records` — Order `n = 109` Full Win

context: subagent
confirmed_scope: Verified that claim/M109_2119202655125403624550373680790052808829003860176536932438843923020304438454497.txt (29,067 bytes, SHA-256 0108345c2f3cbffdd58f23eef8aba73546583f02062a013a5b64ab95e198faa6) is an explicit 109x109 {-1,+1} matrix with exact normalized determinant |det X| / 2^108 = 291 * 27^53 = 2119202655125403624550373680790052808829003860176536932438843923020304438454497, strictly improving by 1.128746x upon the standing Orrick/Rokicki and Math-AI-Caltech record 1877483841834222713683125485573890072927341503771574105042244268774869908324352 while remaining below the Barba bound.

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Order & Matrix Entry Compliance
- **Order check**: $n = 109 \equiv 1 \pmod 4$, so $n$ is not divisible by $4$.
- **Matrix entries**: Parsed `claim/M109_2119202655125403624550373680790052808829003860176536932438843923020304438454497.txt` (`29,067` bytes, SHA-256 `0108345c2f3cbffdd58f23eef8aba73546583f02062a013a5b64ab95e198faa6`); confirmed $109$ rows of $109$ entries ($11,881$ entries total), all in $\{-1, +1\}$.

### 1.2 Exact Integer Determinant & Independent Cross-Checks
- **Fraction-free Bareiss elimination** on Python arbitrary-precision integers, **25-prime Chinese Remainder Theorem (CRT)** modular Gaussian elimination, and **exact `fractions.Fraction` Gaussian elimination** all produce the identical integer determinant:
  $$D(X_{109}) = \frac{|\det X_{109}|}{2^{108}} = 291 \cdot 27^{53} = 2119202655125403624550373680790052808829003860176536932438843923020304438454497.$$
- **Divisibility by $2^{n-1}$**: Confirmed $|\det X_{109}|$ is divisible by $2^{108}$ with zero remainder.

### 1.3 Standing Record & Barba Upper Bound Comparison
- **Standing record**: Across the archived Orrick/Rokicki MaxDet database (`rokicki_best108.html`), `Math-AI-Caltech/hadamard-maxdet`, and `arXiv:2608.22518` (which only improved $n = 51$ and $n \equiv 3 \pmod 4$ in $103..119$), the best known normalized determinant at $n = 109$ was:
  $$D_{\text{rec}}(109) = 1877483841834222713683125485573890072927341503771574105042244268774869908324352.$$
- **Strict improvement**: $D(X_{109})$ exceeds $D_{\text{rec}}(109)$ by a factor of $1.1287461487\times$.
- **Residue-class upper bound (Barba bound for $n \equiv 1 \pmod 4$)**:
  $$B_{\text{norm}}(109) = \left\lfloor \sqrt{217} \cdot 27^{54} \right\rfloor = 2896497323385832583622927428277996632836928103583147613858951575196511441468179.$$
  Since $2n - 1 = 217 = 7 \cdot 31$ is not a square, the Barba bound was not previously attained ($D_{\text{rec}}(109)$ had ratio $0.648191$ to the Barba bound), and $D(X_{109})$ does not exceed $B_{\text{norm}}(109)$ (new ratio $R = 0.731643$).

## 2. Verdict
All clauses of the full success criterion in `claim/target.md` are satisfied.

pass: true
