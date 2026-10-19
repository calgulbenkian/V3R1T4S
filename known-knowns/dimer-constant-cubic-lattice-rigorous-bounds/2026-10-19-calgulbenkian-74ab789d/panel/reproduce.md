context: Claude Code subagent, fresh context [Claude Sonnet 5.5]

# reproduce: cubic-dimer-h3-ub-33 (p2, h3 <= 0.7860441)

Scope: does the saved vector give the stated exact ratio, and is the unpublished monomer-dimer extension a correct proof. Novelty and criterion: other skeptics. No network.

## 0. Integrity
claim.SHA256SUMS verified from the claim folder: all OK. Work in rep_ws/; my code in rep_ws/skeptic/.

## 1. Definition (quoted from object/DERIVATION.md section 3)
"T^MD[U,W] := sum over S subset of (V minus U) of per A[S, W]  (per A[S,W] = 0 unless |S| = |W|)", V = Z/3 x Z/3, D = {(0,0),(1,0),(0,1)}, A[u,v] = 1 iff v-u in D. Claim: h3 <= (1/9) log max_U (T^MD x)_U / x_U for any positive x; "the checker builds [the matrix] entirely (no symmetry reduction is needed for validity)".

## 2. My own checker (written before opening verify-it-yourself/)
rep_ws/skeptic/sk_h3.py (pure Python, exact integers). It builds all 512 x 512 entries by enumerating, for every subset S of the layer, all injective forward maps S -> V and recording the image set, then summing over S contained in V minus U. It computes the orbits of the 512 states under the 18-element group (9 translations x coordinate swap), expands the 44 shipped orbit values to all 512 states by minimum-mask representative, and computes (T^MD x)_U for every one of the 512 states with cross-multiplied comparison. The shipped file was read only for the columns mask and x.
Output (rep_ws/skeptic/sk_h3_output.txt):
  group-invariance of T (sampled): 0 violations
  my orbit count: 44  cert orbits: 44  same canonical masks: True
  max ratio: 731051554747087 / 618837374495 at state mask 255
  claimed 731051554747087/618837374495 equal: True
  bound = 0.786044083039587  ceil7 = 0.7860441  ceil10= 0.7860440831
  below 0.7862023450 by 0.000158262
All 44 entries are positive integers. The exact ratio equals the claimed one; 0.786044083039587 rounded up is 0.7860441 (seven places), consistent with the claim's "unrounded 0.786044083039". The certificate header prints 0.7860440830, which is rounded down at ten places; the claim sentence itself correctly uses 0.7860441.

## 3. Author's script
sh verify-it-yourself/run_checks.sh (CW_PROCS=12), output in rep_ws/author_run_checks_output.txt: "RESULT mdcert dims=3,3 states=512 orbits=44 u=255 ratio=731051554747087/618837374495 bound=0.7860440830 ceil10=0.7860440831" and "ALL CHECKS PASS". Agrees with mine.

## 4. Proof of the extension re-derived (steps E1 to E5)
(E1) Trace identity for all matchings. In the quotient Z^3/<m(e1-e3), n(e2-e3), l e3> (isomorphic to V x Z/l by x -> (x1 mod m, x2 mod n, x1+x2+x3 mod l), whose kernel is exactly the lattice; every edge goes from height k to k+1 with offsets D), a matching is determined by the cyclic sequence of sets U_k of layer-k vertices matched downward. The layer-k vertices outside U_k are each a monomer or matched upward (a set S), and the upper endpoints form U_{k+1}; the number of ways is the sum over S of per A[S, U_{k+1}] = T^MD[U_k, U_{k+1}]. So Phi(quotient) = tr((T^MD)^l). Independent computational check (rep_ws/skeptic/sk_trace2.py: quotient built by triangular reduction of Z^d modulo the lattice, all matchings counted by a bitmask recursion, T^MD built from the definition): (2,2,4): 306305 = 306305; (3,2,4): 162589284 = 162589284; (2,2,6): 162465104 = 162465104; Z^4 (2,2,2,4): 1880275257729 = 1880275257729 (sk_trace2_output.txt).
(E2) Csikvari's inequality M(H,t) <= M(G,t)^2 for a 2-lift H of a bipartite G, valid for all t >= 0, evaluated at t = 1, gives Phi(H) <= Phi(G)^2. It is quoted from He (Csikvari, J. Eur. Math. Soc. 2017); I could not fetch it, so I accept it as a citation and did not re-derive it. Numeric sanity on actual graphs (sk_trace2.py): Phi(T_{4,2,4}) = 87631492737 <= Phi(T_{2,2,4})^2 = 93822753025, and Phi(T_{2,2,8}) = 88091196353 <= 93822753025. The lifts are 2-lifts for the same reason as in the dimer case (index-2 sublattice, simple 6-regular bipartite graphs).
(E3) The box with sides (2^p m, 2^p n, 2^p) is a spanning subgraph of the rectangular torus, which equals T_{2^p m, 2^p n, 2^p}; every matching of the box is a matching of the torus. 2p lifts give Phi(torus) <= Phi(T_{m,n,2^p})^{4^p} = tr((T^MD)^{2^p})^{4^p} <= (2^{mn} rho^{2^p})^{4^p}.
(E4) (1/vol) log Phi(box_p) <= (1/(mn)) log rho + (log 2)/2^p. Phi(box) >= phi(l, box) for every l; FKLM's box limit says (1/vol) log phi(l_n, box_n) -> h3(p0) for 2 l_n/vol -> p0 and box sides -> infinity, so liminf of (1/vol) log Phi(box_p) is at least h3(p0) for every p0, hence at least sup h3(p0) = h3. Only "Phi is at least each term" is used, which is the correct direction. The unit-activity matching entropy named by the p2 text is this quantity.
(E5) Letting p -> infinity: h3 <= (1/(mn)) log rho(T^MD_{m,n}). Collatz-Wielandt for the nonnegative integer matrix T^MD and the positive vector then gives h3 <= (1/9) log(731051554747087/618837374495) = 0.786044083039587.
I find the steps correct. External inputs: Csikvari's lemma (cited), existence of the box limits and the definition h3 = sup h3(p) from FKLM (quoted in the derivation; I read only the saved excerpt). No symmetry claim is used: the check ran on the whole 512 x 512 matrix.

Open question 4 (symmetry expansion of the vector): acceptable. My expansion by minimum mask is independent of the file's and the maximum is the same. Question 3: the (5,4) figure 0.7859680768 in object/RESULTS.md is not part of this claim and I did not check it. Questions 1 and 2 (proved? FKLM identification): answered in section 4.

Mismatch count: 0. Non-determinism: none.
pass: true
