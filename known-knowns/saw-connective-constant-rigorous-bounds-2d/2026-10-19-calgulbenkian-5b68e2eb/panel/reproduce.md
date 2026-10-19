context: Claude Code subagent, fresh context [claude-sonnet-5-5]

# reproduce report: saw-482-k30 (4.8^2 connective constant, loop length 30)

Cell checked against claim.SHA256SUMS from the claim folder: 0 mismatches. Work done in a copy (rep_ws/claim). The network was not used. Novelty of the 1.82926 baseline was not judged (other skeptic).

## Claim and definition quoted
Claim: mu(4.8^2) <= 849051343/464433440 = 1.8281442934, the exact Collatz-Wielandt ratio max_i (Mx)_i / x_i of a loop-length-30 automaton with 2,750,336 states. Partial win p1: "A certified improvement, by at least 1e-6, of the best published rigorous bound for the triangular, kagome or 4.8^2 lattice ... same certificate rules." Certificate rule for upper bounds: "the automaton/transfer matrix definition plus a nonnegative test vector whose Collatz-Wielandt ratio is verified in exact or outward-rounded arithmetic".
Definition used (object/AUTOMATON.md): vertices are integer points whose residues mod 3 are (1,0) E, (2,0) W, (0,1) N, (0,2) S, with the listed three neighbour offsets per type; 8 symmetries about the origin plus translations by multiples of 3; canonical walk key with head at (-1,0); prune rule (edges + graph distance from oldest vertex to head <= k = 30); chord shortcuts (depth <= 3); suffix candidates; target = candidate with smallest vector entry.

## 1. Theorem (object/THEOREM.md): re-derived from scratch, decision: PROVED
I did not read the author's proof before deriving mine. Statement needed: states S_i with vertex sets and heads; for every state and every free neighbour A of its head a chosen target t(i,A) with some sigma in Aut(G), sigma(A) = head(S_t), V(S_t) a subset of sigma(V(S_i) union {A}). Then for any positive x with Mx <= lambda x, mu <= lambda.
Proof (mine). Let W = (w_0..w_n) be an SAW whose first edge is carried by an automorphism tau_1 onto a seed state S_s. Induct: keep an index i_m and automorphism tau_m with tau_m(w_m) = head(S_{i_m}) and V(S_{i_m}) a subset of tau_m({w_0..w_m}). Step: A = tau_m(w_{m+1}) is a neighbour of the head. Because W is self-avoiding, A is not in tau_m({w_0..w_m}), hence not in V(S_{i_m}) (subset), so the transition (i_m, A) exists. Take its chosen sigma and target; put tau_{m+1} = sigma tau_m. Then tau_{m+1}(w_{m+1}) = sigma(A) = head(S_t), and V(S_t) is a subset of sigma(V(S_{i_m}) union {A}) which is a subset of tau_{m+1}({w_0..w_{m+1}}). The walk maps to the sequence of pairs (i_m, A_m), A_m = tau_m(w_{m+1}); this is injective because sigma is fixed as a function of (i,A) and tau_m is rebuilt from earlier pairs, so w_{m+1} = tau_m^{-1}(A_m). So the number of walks with that first edge class is at most (M^{n-1} 1)_s. With Mx <= lambda x and x > 0: (M^k 1)_s <= lambda^k x_s / min x. Three first edges from the origin, each in a seed class (checked below): c_n <= 3 lambda^{n-1} max x / min x, so mu <= lambda. Multiplicity (several neighbours to one target) is counted by M. No gap found. The two points that need a check on the lattice, namely that the 8 symmetries with translations by 3Z^2 are automorphisms and that every directed edge is equivalent to a seed, are checked mechanically below. The theorem needs no reachability and no particular rule for choosing targets, because condition (SI) is verified per transition (below), so the stalk-style worry of an unproved step does not arise here. The "dropped history" is legitimate because only V(S) and the head are used.

## 2. Lattice and automaton definition vs the 4.8^2 lattice (own script rep_ws/skeptic/lattice.py, output in rep_ws/skeptic/output.txt)
- adjacency symmetric and closed (u in nb(v) iff v in nb(u)) on window |x|,|y| <= 14: 0 failures; degree 3 everywhere.
- the 8 symmetries preserve vertex set and adjacency on window: 0 failures. Neighbour offsets depend only on residues mod 3, so translations by 3Z^2 are automorphisms by construction, and the window covers all residue classes many times.
- cycle census through each of the 4 vertex types: exactly one 4-cycle and exactly two 8-cycles, none of length 3,5,6,7,9 (consistent with vertex configuration 4.8.8: one square and two octagons at each vertex).
- all 12 directed edge types (4 vertex types x 3 neighbours) are carried by a symmetry plus translation in 3Z^2 onto exactly one seed: the square edge (1,0)->(0,1) or the octagon edge (1,0)->(2,0); none to both.
(The folder says the checker uses a finite window too; the residue-class argument above makes the window check complete.)

## 3. My own checker (mychk.c, written from AUTOMATON.md and THEOREM.md before opening verify-it-yourself/; C, no code from the author)
Command: cat object/states_part_*.bin > states.bin; ./mychk states.bin 30 2750336 (whole-file sha256 5b68e2eb7517096965e583cc68cddb13978e8959b8a0a7a218d08ad10a2dfee7 matches SHA256_PARTS.txt).
Real output (rep_ws/skeptic/output_run1.txt; a second run is byte-identical apart from the timing line, so deterministic):
records 2750336 (expected 2750336), bytes consumed 37215863 of 37215863, max L 30, duplicates 0, zero vector entries 0
states undecodable 0, repeated vertex pairs 0, non-canonical 0
seed 0 present in list: yes ; seed 1 present in list: yes
transitions 4420718, with more than one candidate 1510053, chosen target differs from plain suffix 643304, max candidates 10, transitions with no candidate in list 0, closure-missing(kinds 1,2) 0
subset-inclusion failures (direct search over 8 symmetries x translations by multiples of 3): 0
max_i (Mx)_i/x_i = 6792410744 / 3715467520 = 849051343 / 464433440 (state index 2618199) = 1.828144293400
below 1.829258 exactly: yes
equals 849051343/464433440: yes
What it does: decodes every state (head fixed at (-1,0), steps back by neighbour index), checks distinct vertices and canonicity; rebuilds all transitions from the definition (prune with exact graph distance from BFS tables, chord shortcuts, suffix candidates), requires closure of the state list; picks the smallest vector entry; verifies (SI) for each chosen target by searching all 8 symmetries and translations in 3Z^2 for sigma with sigma(A) = (-1,0) and V(T) a subset of sigma(V(S) union {A}) (an independent test, not reusing the canonicalising symmetry); sums x over targets and takes the exact maximum ratio in 128-bit integers; compares exactly with 1.82926 - 2e-6 = 914629/500000 (strict, margin about 1.11e-3).
Negative control with my checker: first vector entry set to 1 gives ratio 17353775213218 and "below 1.829258: NO" (rep_ws/skeptic/output_negctl.txt).

## 4. Author's checker, run after mine
sh verify-it-yourself/run_checks.sh: part and whole sha256 match, both negative controls rejected, full check rebuilds 4420718 transitions (1510053 multi-candidate, 643304 non-plain), 0 missing, 0 invariant failures, exact ratio 849051343/464433440 = 1.828144293400, PASS, ALL CHECKS PASS (902 s on a heavily loaded machine; output in rep_ws/skeptic/author_run_checks_output.txt). Every count agrees with my independent checker. No disagreement.

## Mismatches and limits
None found. Limits, stated plainly: the object was regenerated by the triage from the author's generator and the author's own k = 30 certificate is not in the snapshot (folder says so); that does not affect the bound, because the bound is the exact ratio of the shipped state list and vector under the definition, and the theorem makes any state list with a verified (SI) per transition valid. The k = 32 and k = 34 variants are not claimed and not checked. Whether 1.82926 is the current published value is not judged here.

pass: true
