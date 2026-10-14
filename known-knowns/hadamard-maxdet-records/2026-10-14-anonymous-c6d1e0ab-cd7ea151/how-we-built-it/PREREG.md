# Preregistration: Lens 2 — Representation-Absorber (`p2` Frozen Gram Targets & Rational Congruence Absorber)

## 1. Hypothesis and Algebraic Architecture
For an unclosed order $n \equiv 1 \pmod 4$ where $2n - 1$ is not an integer square, Barba's upper bound $\sqrt{2n - 1}(n-1)^{(n-1)/2}$ cannot be attained by an integer matrix. Under the **Partial Win `p2` (Frozen Gram Target)** specification in `target.md`, we seek an explicit $n \times n$ symmetric positive-definite integer matrix $G$ satisfying:
1. $G_{ii} = n$ for all $i$, $G_{ij} \equiv 1 \pmod 2$ for all $i \ne j$, and $G_{ij} + G_{jk} + G_{ki} \equiv n \pmod 4$ for all $i, j, k$.
2. $\det(G) > (\det R_{\text{rec}}(n))^2$ (strictly exceeding the square of the standing record determinant).
3. Exact rational equivalence of $G$ to $n I_n$ (and $I_n$), certified both by Hasse-Minkowski local Hilbert symbols at all prime places $p \mid 2 n \det(G)$ and by an explicit invertible $n \times n$ rational matrix $Q \in GL_n(\mathbb{Q})$ satisfying $Q Q^T = G$ (and $P = \frac{1}{\sqrt{n}} Q \in GL_n(\mathbb{Q})$ satisfying $P (n I_n) P^T = G$ for odd square orders $n = 49 = 7^2$ and $n = 81 = 9^2$).
4. An explicit $k \times n$ $\{\pm 1\}$ matrix $M_0$ of $k = n - 1 \ge n - 2$ rows realizing the leading $(n-1) \times (n-1)$ principal block of $G$: $M_0 M_0^T = G[:n-1, :n-1]$.

### Exact Rank-1 Kernel Absorber Construction
Let $H_{n-1}$ be a $(n-1) \times (n-1)$ Hadamard matrix of order $n - 1 = 4k$, and define the $(n-1) \times n$ $\{\pm 1\}$ matrix
$$M_0 = \begin{pmatrix} \mathbf{1}_{n-1} & H_{n-1} \end{pmatrix} \in \{\pm 1\}^{(n-1) \times n}.$$
Then its Gram matrix is $G_0 = M_0 M_0^T = (n - 1) I_{n-1} + J_{n-1}$, which has determinant $\det(G_0) = 2 (n - 1)^{n-2}$ and exact inverse $G_0^{-1} = \frac{1}{n-1}\left(I_{n-1} - \frac{1}{2(n-1)} J_{n-1}\right)$.
Crucially, the 1-dimensional right kernel $\ker(M_0) \subset \mathbb{Q}^n$ is spanned by the explicit integer vector
$$u = \begin{pmatrix} -(n - 1) \\ H_{n-1}^T \mathbf{1}_{n-1} \end{pmatrix} \in \mathbb{Z}^n, \qquad M_0 u = 0, \qquad u^T u = 2 (n - 1)^2.$$
Extending $G_0$ by an $n$-th row/column vector $g \in \{9, 5, 1, -3, -7\}^{n-1}$ (which automatically obeys $g_i + g_j + 1 \equiv 3 \equiv 1 + 4 \equiv n \pmod 4$ because $g_i \equiv 1 \pmod 4$) gives a candidate $n \times n$ Gram matrix
$$G = \begin{pmatrix} G_0 & g \\ g^T & n \end{pmatrix}$$
with exact Schur-complement determinant
$$\det(G) = (n - 1)^{n - 3} \cdot \text{val}(g), \qquad \text{val}(g) = 2 n (n - 1)^2 - 2 (n - 1) \sum_{i=1}^{n-1} g_i^2 + \left(\sum_{i=1}^{n-1} g_i\right)^2.$$
Whenever $\text{val}(g) = r^2$ is a perfect integer square exceeding $16 (n - 1)^2 c_{\text{rec}}(n)^2$, the kernel absorber vector $u \in \ker(M_0)$ allows us to complete $M_0$ to an explicit $n \times n$ rational matrix
$$Q = \begin{pmatrix} M_0 \\ q_n \end{pmatrix}, \qquad q_n = (G_0^{-1} g)^T M_0 + \frac{r}{2(n - 1)^2} u^T \in \mathbb{Q}^{1 \times n}$$
satisfying $M_0 q_n^T = g$ and $q_n q_n^T = g^T G_0^{-1} g + \frac{r^2}{2(n - 1)^2} = n$, so $Q Q^T = G$ identically!

## 2. Target Orders and Diophantine Square Search
- **Primary odd-square orders $n = 49 = 7^2$ and $n = 81 = 9^2$**:
  Because $\sqrt{n} \in \mathbb{Z}$, setting $P = \frac{1}{\sqrt{n}} Q \in GL_n(\mathbb{Q})$ satisfies $P (n I_n) P^T = Q I_n Q^T = G$ constructively over $\mathbb{Q}$, proving rational equivalence to both $I_n$ and $n I_n$ simultaneously.
- **All 15 unclosed $n \equiv 1 \pmod 4$ orders in $29 \le n \le 97$**:
  Enumerate 3-level step vectors $g \in \{5, 1, -3\}^{n-1}$ (with multiplicity counts $(a, b, c)$, $a + b + c = n - 1$) such that $\text{val}(g) = r^2$ is a perfect square with $r / (4(n-1)) > c_{\text{rec}}(n)$.
- **Audit of Two-Circulant $n \equiv 3 \pmod 4$ PAF Targets ($55 \le n \le 99$)**:
  Evaluate whether two-circulant Gram targets can improve on the Caltech `arXiv:2608.22518` borders without full multi-row completion.
null_test: not needed because hadamard-maxdet-records is an exact deterministic integer determinant problem
