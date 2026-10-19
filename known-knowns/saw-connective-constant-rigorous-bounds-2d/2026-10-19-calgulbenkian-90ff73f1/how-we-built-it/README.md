# How we built it

Contributor material, unverified. Source copied from Argon's newer generator snapshot of 2026-10-19 (read-only), file saw_bounds_2d.c (sha256 e49aab1197d5f061dbfff1c190b0b2a4bf1733f240c74c548627c8dc67cbf7fd before the edit below; byte-identical to the file in the earlier snapshot), with one sanitising edit: the usage message printed by the program had angle-bracket placeholders, which were replaced by braces. Nothing else in the source was changed. The generator's sibling programs for other targets are not included.

## Provenance of the certificate

The author's run for loop length 32 wrote a certificate file named cert_482_k32.txt (1,484,783,810 bytes, sha256 e6a346bd0a25d7ce1fb2e65df43854a7a07fa3499ce2fe47684d91e231e291ed). Our triage regenerated it by compiling and running saw_bounds_2d.c; the regenerated file is byte-identical (same sha256) to the one on the author's laptop. The object in object/ is that certificate reduced to its integer vector (verify-it-yourself/make_vector.py is the provenance tool that does the reduction and checks the state order against the checker's).

## Commands

The snapshot documents the program's interface and the run it reports, but not the compile line or the shell history. As far as it is documented:

- Interface (from the program): saw_bounds_2d takes a lattice name (482, kagome, triangular or square), the maximum loop length k, an optional certificate file name, and an optional use_bridges mode (default 1; mode 2 adds finite-pocket pruning).
- The run for this claim, in shell form: saw_bounds_2d 482 32 cert_482_k32.txt 1 (the author reported 8,135,148 states in 37.19 s).
- The compile command is not recorded. The source includes only stdio, stdlib, stdint, string, math and time, and uses 128-bit integer arithmetic for the exact comparison, so a plain C compiler with optimisation and the math library should build it.
- The author's snapshot holds no PREREG.md for this target (the run was a direct construction, not a measurement against a null), so none is shipped. A null test is not required for this category.

## Reported results (excerpt of the author's results notes, local paths removed)

The best published rigorous upper bound the author compared with was 1.82926 (Jensen 2004 Table 3).

| Max loop k | Mode | States | Exact fraction max (MV)_i / V_i | Bound |
|---:|---|---:|---|---:|
| 22 | use_bridges=1 | 39,367 | 693444578290/377832855505 | 1.835321010829 |
| 28 | use_bridges=1 | 940,974 | 15540968660/8494170644 | 1.829604008601 |
| 30 | use_bridges=1 | 2,750,336 | 6792410744/3715467520 | 1.828144293400 |
| 32 | use_bridges=1 | 8,135,148 | 18108999119/9912056861 | 1.826966831703 |
| 32 | use_bridges=2 | 5,787,106 | 14988071382/8205358318 | 1.826619972113 |
| 34 | use_bridges=2 | 16,873,086 | 19360805483/10605620094 | 1.825523195381 |

Only the loop length 32, use_bridges=1 row is claimed in this package. The pocket-pruned rows (use_bridges=2) are not covered by the theorem in object/THEOREM.md and are not claimed.
