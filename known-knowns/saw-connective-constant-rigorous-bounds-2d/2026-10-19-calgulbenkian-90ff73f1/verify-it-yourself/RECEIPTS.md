# Receipts

Output of sh verify-it-yourself/run_checks.sh on 2026-10-19 by the builder (python3.9, standard library only, one process). Wall 1,206 s (full check 1,193 s), 1.57 GB peak resident, user CPU 1,127 s. An earlier standalone run of the full check: 1,258 s wall, 1.58 GB.

```
== reassemble object/vector_part_*.bin and check the whole first
whole object sha256 matches (90ff73f1cfa9702a47f15e59a2fcdbd02c28185f75c1bd309a4e44790c93390b)
== each part against object/SHA256_PARTS.txt
all parts match
== known-answer test: loop length 22 (39367 states, bound 138688915658/75566571101 = 1.835321010829), a few seconds
ok   lattice: adjacency symmetric and 3-regular; the 8 symmetries about the origin and translations by 3Z^2 are automorphisms (window +-9)
vector entries read: 39367, bytes 169792, decode 0s
ok   all test-vector entries are positive integers (min 1000000, max 10000000000000)
ok   all directed edges in window +-12 reduce to the two seed states (2 classes)
ok   all vertices in the window are equivalent under the symmetry group (vertex-transitive): 1 class
ok   regenerated state count 39367 equals the vector length 39367
transitions rebuilt 63787, with more than one candidate 20412, using a candidate other than the plain suffix 7782, max candidates 7
ok   subset-inclusion invariant holds on all 63787 chosen transitions (failures: 0)
exact max (P x)_i / x_i = 693444578290 / 377832855505 = 138688915658/75566571101 = 1.835321010829  (state index 18789)
ok   state count 39367 equals the claimed 39367
ok   bound equals the claimed 138688915658/75566571101 exactly (got 138688915658/75566571101)
known-answer test only (K = 22): not the claimed loop length
elapsed 5 s
PASS
== negative controls (known-answer vector with state 0 set to 1)
negative control (a vector entry changed to 1) rejected as expected
== full check at the claimed loop length K = 32: regenerate 8,135,148 states, rebuild all transitions, subset-inclusion on each, exact ratio (see REPRODUCE.md for time)
ok   lattice: adjacency symmetric and 3-regular; the 8 symmetries about the origin and translations by 3Z^2 are automorphisms (window +-9)
vector entries read: 8135148, bytes 27851812, decode 4s
ok   all test-vector entries are positive integers (min 1000000, max 10000000000000)
ok   all directed edges in window +-12 reduce to the two seed states (2 classes)
ok   all vertices in the window are equivalent under the symmetry group (vertex-transitive): 1 class
ok   regenerated state count 8135148 equals the vector length 8135148
transitions rebuilt 13072399, with more than one candidate 4549424, using a candidate other than the plain suffix 1986536, max candidates 11
ok   subset-inclusion invariant holds on all 13072399 chosen transitions (failures: 0)
exact max (P x)_i / x_i = 18108999119 / 9912056861 = 18108999119/9912056861 = 1.826966831703  (state index 5898119)
ok   state count 8135148 equals the claimed 8135148
ok   bound equals the claimed 18108999119/9912056861 exactly (got 18108999119/9912056861)
ok   bound 18108999119/9912056861 < 1.82926 - 2e-6 (exact rational comparison)
ok   bound 18108999119/9912056861 < the loop-length-30 bound 849051343/464433440 (exact rational comparison)
elapsed 1193 s
PASS
ALL CHECKS PASS
```
