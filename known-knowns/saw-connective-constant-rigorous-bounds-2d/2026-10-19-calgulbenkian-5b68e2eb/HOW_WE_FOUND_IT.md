contributor text, unverified

# How we found it

The contributor's team (an AI search agent, Gemini, called Argon, working for calgulbenkian) set out to improve rigorous upper bounds for the connective constant of two-dimensional lattices. On 2026-10-18/19 it proved a subset-inclusion statement for finite-memory loop-avoiding-walk automata: if every transition of a finite state list can be matched to a target state whose vertex set lies inside the image of the extended walk under a lattice symmetry, then a positive integer test vector gives an upper bound through the Collatz-Wielandt ratio. It combined that with small-bridge (chord) shortcuts and let a C program (how-we-built-it/saw_bounds_2d.c) iterate on the choice of targets and the test vector, for growing maximum loop length k.

On the 4.8^2 lattice the exact ratio fell as k grew: 1.8376 at k = 20, 1.8296 at k = 28, and 1.828144293400 at k = 30 (2,750,336 states), which is the first length below the target. Loop lengths 28 and 29 give the same automaton and miss. The team also ran k = 32 and a pocket-pruned k = 34 variant; those are not claimed here.

The author's snapshot recorded the k = 30 certificate as saved but did not contain it (files over 100 MB were skipped in our copy). Our triage regenerated it by compiling and running the author's generator; two regenerations agree byte for byte. The object here is that certificate reduced to the state list and the integer vector. A checker written from the definition, not from the author's code, rebuilds every transition and verifies the condition; three panel skeptics did the same with their own code, and a read-only review by a model of a different family asked for four wording and checker fixes (see README.md).
