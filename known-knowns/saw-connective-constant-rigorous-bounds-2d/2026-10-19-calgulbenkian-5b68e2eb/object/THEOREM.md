# Subset-Inclusion Theorem and its proof

Setting. G is a connected, locally finite, vertex-transitive graph (as the 4.8^2 lattice is), Aut(G) its automorphism group, c_n the number of n-step self-avoiding walks (SAWs) on G from a fixed vertex o, and mu(G) = lim c_n^(1/n) (the limit exists because c_(n+m) <= c_n c_m, which holds for vertex-transitive graphs; for a general connected graph that inequality can fail, and the argument below then bounds limsup c_n^(1/n)).

A walk state is a finite sequence S = (u_0, ..., u_(L-1)) of distinct vertices with consecutive vertices adjacent; head(S) = u_(L-1); V(S) is its vertex set. (Only the vertex set and head are used below.)

**Theorem (Subset-Inclusion automaton bound).** Let S_0, ..., S_(N-1) be walk states. Suppose that for every state S_i and every neighbour A of head(S_i) with A not in V(S_i), one target index t(i, A) in {0, ..., N-1} is chosen such that

  (SI) there is sigma in Aut(G) with sigma(A) = head(S_t) and V(S_t) contained in sigma(V(S_i) union {A}).

Let M be the N x N matrix with M[i][j] = number of neighbours A (not in V(S_i)) with t(i, A) = j. Suppose a 1-edge walk (w_0, w_1) from o is equivalent under Aut(G) to the 2-vertex state S_s (that is, some automorphism sends w_0, w_1 to the two vertices of S_s in order). Then the number of n-step SAWs starting with the edge (w_0, w_1) is at most (M^(n-1) 1)_s, where 1 is the all-ones vector. Hence, if x is any vector of positive numbers with (M x)_i <= lambda x_i for all i, then the number of such walks is at most lambda^(n-1) x_s / min(x), and if the first edges of walks from o fall into r equivalence classes of seed states, c_n <= (number of first edges) lambda^(n-1) max(x)/min(x), so mu(G) <= lambda.

**Proof.** Fix an n-step SAW W = (w_0, ..., w_n) whose first edge is equivalent to S_s. We build, by induction on m = 1, ..., n, a state index i_m and an automorphism tau_m with

  (a) tau_m(w_m) = head(S_(i_m)),
  (b) V(S_(i_m)) is contained in tau_m({w_0, ..., w_m}),

and i_1 = s. For m = 1, take tau_1 the automorphism from the equivalence; V(S_s) = {tau_1(w_0), tau_1(w_1)}, so (a) and (b) hold.

Step m to m+1 (m < n). Put A = tau_m(w_(m+1)). It is a neighbour of tau_m(w_m) = head(S_(i_m)). Because W is self-avoiding, w_(m+1) is not in {w_0, ..., w_m}, so A is not in tau_m({w_0, ..., w_m}), which contains V(S_(i_m)) by (b). So A is not in V(S_(i_m)), the transition (i_m, A) exists, and the chosen target t = t(i_m, A) has an automorphism sigma with sigma(A) = head(S_t) and V(S_t) contained in sigma(V(S_(i_m)) union {A}). Set i_(m+1) = t and tau_(m+1) = sigma composed with tau_m. Then (a): tau_(m+1)(w_(m+1)) = sigma(A) = head(S_t). And (b): V(S_t) is contained in sigma(V(S_(i_m)) union {A}), which is contained in sigma(tau_m({w_0..w_m}) union {tau_m(w_(m+1))}) = tau_(m+1)({w_0, ..., w_(m+1)}).

The walk W is thereby sent to the sequence of transitions (i_1, A_1), ..., (i_(n-1), A_(n-1)), a path of n-1 steps in the transition multigraph of M starting at s, where A_m = tau_m(w_(m+1)). The map from walks to such paths is injective: given the path, the neighbour A_m is recovered at each step, and w_(m+1) = tau_m^(-1)(A_m), where tau_m is determined by the earlier steps (each tau_(m+1) is determined by tau_m and the chosen sigma, which we fix as a function of (i_m, A_m)). Therefore the number of such walks is at most the number of (n-1)-step paths in M's multigraph from s, which is (M^(n-1) 1)_s. 

Collatz-Wielandt step. If x > 0 and M x <= lambda x componentwise, then M^k x <= lambda^k x (M has non-negative entries), hence (M^k 1)_s <= (M^k x)_s / min(x) <= lambda^k x_s / min(x). The number of first edges of a SAW from o is the vertex degree d (here d = 3), and each first edge is equivalent to a seed state, so c_n <= d lambda^(n-1) max(x)/min(x). Taking n-th roots and n to infinity gives mu(G) <= lambda. With x an integer vector, lambda = max_i (M x)_i / x_i is computed exactly as a rational number. QED.

## Application to the (4.8^2) lattice

G is the 4.8^2 lattice (squares and octagons; vertex set and neighbour rule in AUTOMATON.md). The automorphisms used are the 8 symmetries about the origin composed with translations by multiples of 3 in each coordinate; the checker verifies that these are automorphisms (on a window) and that all vertices are equivalent and all directed edges fall into two classes (square edge, octagon edge), the two seed states.

The states are canonical forms of walks of bounded loop length: a walk (u_0, ..., u_(L-1)) is kept only while (number of edges) + dist(u_0, u_(L-1)) <= k, where dist is graph distance; older vertices are forgotten from the oldest end (Ponitz and Tittmann style finite memory). A state is not required to be a whole walk history. The target of a transition is a state whose vertex set is a subset of the image of the extended walk's vertex set under an automorphism. This is exactly (SI). Which of several allowed targets is used does not matter for the theorem; the checker takes, for each transition, the allowed target with the smallest test-vector entry among the candidates listed in AUTOMATON.md, and verifies (SI) for that target against the decoded target state.

Chord shortcuts (dropping the part of a walk between two non-consecutive but adjacent vertices) also satisfy (SI), since the shortcut walk uses a subset of the vertices of the extended walk. The checker verifies (SI) directly for each chosen target, so the theorem does not depend on how the candidate lists were built. The bound rests only on (SI); once chord shortcuts are used, no claim is made that every loop of length at most k is excluded from the automaton (forgetting more vertices only admits extra walks, which is safe for an upper bound).
