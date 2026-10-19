# reproduce report: saw-482-k32 (GROUP phys)

context: Claude Code subagent, fresh context [Sonnet 5.5]

## Integrity
claim.SHA256SUMS verified from inside claim/: 45 entries, all OK, 0 failures. Claim copied to rep_ws/claim; all work in rep_ws/. No network used.

## Definition (quoted from object/AUTOMATON.md)
"Vertices: integer points (x, y) with (x mod 3, y mod 3) one of (1,0) E, (2,0) W, (0,1) N, (0,2) S" with a fixed 3-neighbour offset list per type; states are canonical walks (head moved to (-1,0), lexicographically smallest of 8 symmetries); "prune(walk): drop oldest vertices ... while start < len - 2 and (len - 1 - start) + dist(walk[start], head) > k"; candidate targets c0 (prune), chord shortcuts (cap 64, depth 3), intermediate suffixes already in the final list (cap 32); "The target is the candidate with the smallest test-vector entry"; vector = tag SAW482V2 + xz stream of six byte planes (big-endian 48-bit).

## Theorem (object/THEOREM.md): re-derived, PROVED as applied at k = 32
My own derivation, step by step:
1. Given an n-step SAW W whose first edge is equivalent (by an automorphism tau_1) to seed S_s, induct: (a) tau_m(w_m) = head(S_{i_m}), (b) V(S_{i_m}) is contained in tau_m({w_0..w_m}). Base case holds by choice of tau_1.
2. Step: A = tau_m(w_{m+1}) is a neighbour of head(S_{i_m}). Self-avoidance of W gives w_{m+1} not in {w_0..w_m}, so A is not in tau_m({w_0..w_m}), which contains V(S_{i_m}); hence A is not in V(S_{i_m}), and the transition (i_m, A) exists in M. The chosen target t has sigma with sigma(A) = head(S_t) and V(S_t) contained in sigma(V(S_{i_m}) u {A}); with tau_{m+1} = sigma o tau_m, (a) holds, and (b) holds because sigma(V(S_{i_m}) u {A}) is contained in sigma(tau_m({w_0..w_m}) u {tau_m(w_{m+1})}) = tau_{m+1}({w_0..w_{m+1}}).
3. Injectivity: sigma is fixed as a function of (i_m, A_m), so tau_m is a function of the first edge and the transition path (A_1..A_{m-1}); w_{m+1} = tau_m^{-1}(A_m). So distinct walks with the same first edge give distinct (n-1)-step paths in the multigraph of M, giving at most (M^{n-1} 1)_s walks. No extra care is needed beyond this (this answers the open question on injectivity); M counts each free neighbour A separately, so multiplicity is right.
4. Collatz-Wielandt: x > 0, Mx <= lambda x, M >= 0 gives M^k 1 <= M^k x / min x <= lambda^k x / min x; c_n <= 3 lambda^{n-1} max x / min x (3 first edges, each in a seed class); n-th roots give mu <= lambda. Vertex-transitivity/submultiplicativity is not even needed, since the bound is direct on c_n.
5. Hypotheses at k = 32, checked by me (rep_ws/skeptic/lattice.py, output in lattice_output.txt): adjacency is symmetric and 3-regular; the 8 symmetries and translations by 3 are automorphisms (window +-9; the relation is 3-periodic, so a window of one period suffices exactly); face tracing gives only sizes 4 and 8 (it is 4.8^2); the directed edges form exactly 2 classes under the group used, with canonical keys equal to the two seeds. States need not be full histories (only head and vertex set are used), and my C program checked (SI) itself for the chosen target of every transition (and every candidate).
Conclusion: the theorem is proved; the bound follows from (SI) on every transition plus the exact ratio. The candidate-list rules and caps only choose among valid targets and are not needed for validity.

## Own checker (written from AUTOMATON.md before reading anything in verify-it-yourself/)
rep_ws/skeptic/saw.c (C, single thread, about 1 GB) and dec.py (Python, numpy, decodes the vector from the documented format). It:
- regenerates the state set breadth-first from the two seeds in the documented order (own canonicalisation, own distance tables by BFS, own hash store), validating walks (distinct, adjacent);
- in a second pass rebuilds every candidate list (suffix prune, chord shortcuts, intermediate suffixes in the final list), picks the smallest vector entry, checks (SI) for every candidate by trying all 8 symmetries with a translation by multiples of 3 sending A to (-1,0);
- computes max (Mx)_i / x_i by unsigned 128-bit integer cross-multiplication.
Calibration on the shipped known-answer vector (k = 22, 39,367 states): my program gives 693444578290/377832855505, which equals the generator ratio quoted in CLAIM.md for k = 22. One ambiguity in the definition (rule 2 "walk" could mean the extended walk or the pre-extension state) was resolved by this test: the extended walk reproduces the ratio and satisfies (SI) everywhere; the other reading fails (SI) on 11,430 chosen transitions. Rule 3 offset (start vs start+1) is ambiguous in the text but gives identical results at k = 22 and k = 32 (both run).

Command: ./saw 32 k32.u64 0 0 (and 0 1); output (rep_ws/skeptic/output_r30.txt, output_r31.txt, identical):
states 8135148
vector entries 8135148
transitions 13072399
nonc0_chosen 1986536
SI_fail_chosen 0
SI_fail_any_candidate 0
MAX 18108999119/9912056861 at state 5898119

Vector decode: 8135148 entries, min 1000000, max 10000000000000, all positive integers. gcd(18108999119, 9912056861) = 1. Decimal 1.82696683170288363. Margin below 1.82926: 0.00229317 (exact comparison: at least 1e-6 holds; also below 1.829254 by 0.002287).

## Shipped checker
Command: sh verify-it-yourself/run_checks.sh (in rep_ws/claim, under nice), 1188 s. Its output agrees with mine: state count 8135148; 13072399 transitions, 1986536 not the plain suffix; subset-inclusion failures 0; exact max 18108999119/9912056861 at state index 5898119; bound equals claimed exactly; below 1.82926 - 2e-6 and below the k = 30 bound. Known-answer test and negative control also passed. Last line of run_checks.sh output: `ALL CHECKS PASS` (the checker's own last line: PASS). Full output saved in rep_ws/skeptic/author_run_checks.txt. No disagreement.

## Open questions concerning reproduction
- Theorem correct and complete? Yes, see above; injectivity is fine with sigma fixed per (state, neighbour).
- Vector-only certificate acceptable? Reproduction works: I regenerated the states and transitions from the written text and my result is exact. Caveat: the text has two ambiguities (rule 2's "walk", rule 3's suffix offset). The first needed a test against the known-answer vector to resolve; the author should state it explicitly (rule 2 acts on the extended walk, whose last vertex is A). They do not affect validity, only which ratio results.
- Is AUTOMATON.md clear enough to regenerate the order? Almost: the state count and order were reproduced exactly (count equals the vector length, ratio equal), after the one ambiguity above.
- Smallest-entry candidate within the theorem? Yes: (SI) holds for all candidates (0 failures over every candidate of every transition), so any choice is valid.
- Checking only through ratio and invariants, not the author's transition lists? Sufficient: validity needs only (SI) and the exact ratio, both recomputed independently here.
- Finite window for lattice checks: sufficient, because the neighbour rule is 3-periodic and symmetry/translation properties reduce to one period; the window +-9 covers it exactly.
- Candidate caps and depth cap as definition: acceptable; they do not affect validity (all candidates satisfy SI), only the value.
- Novelty and k = 34 variant: not a reproduction matter; not judged.

pass: true
