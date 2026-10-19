# How we built it

Contributor material, unverified. Source copied from Argon's snapshot of 2026-10-19 (read-only), file saw_bounds_2d.c, with one sanitising edit: the usage message printed by the program had angle-bracket placeholders, which were replaced by braces. Nothing else in the source was changed. The generator's sibling programs for other targets are not included.

## Provenance of the certificate (important)

The author's own run for loop length 30 wrote a certificate file named cert_482_k30.txt (about 449 MB; the author's results notes say it was saved). Our snapshot of the author's folder skipped files over 100 MB, so that file is not in our copy; only the loop length 22 certificate (4,977,339 bytes) is. Our triage therefore regenerated the loop length 30 certificate by compiling and running saw_bounds_2d.c, and the builder repeated the run and got a byte-identical 471,147,580-byte text certificate (sha256 dfe6907bafbaea1921d9baa11cdc482ae42e75f110a66c05f263a8d515076a4f). The object in object/ is that certificate reduced to the state list and the integer vector. The author's own copy of the certificate was not compared.

## Commands

The snapshot documents the program's interface and the run it reports, but not the compile line or the shell history. As far as it is documented:

- Interface (from the program): saw_bounds_2d takes a lattice name (482, kagome, triangular or square), the maximum loop length k, an optional certificate file name, and an optional use_bridges mode (default 1; mode 2 adds finite-pocket pruning).
- The reported run for this claim: lattice 482, k = 30, use_bridges = 1, certificate written to a file; reported 2,750,336 states and 8.35 s. In shell form: saw_bounds_2d 482 30 cert_482_k30.txt 1
- The compile command is not recorded. The source includes only stdio, stdlib, stdint, string, math and time, and uses 128-bit integer arithmetic for the exact comparison.
- Reported results for other k (k = 22, 28, 30, 32 with use_bridges = 1; k = 30, 32, 34 with use_bridges = 2) are in the table below.
- PREREG.md: the author's snapshot holds no PREREG.md for this target (the run was a direct construction, not a measurement against a null), so none is shipped. A null test is not required for this category.

## Reported results (excerpt of the author's RESULTS.md, Part 1, with local paths removed)

The best published rigorous upper bound the author compared with was 1.82926 (Jensen 2004 Table 3). The author's table for the 4.8^2 lattice:

| Max loop k | Mode | States | Exact fraction max (MV)_i / V_i | Bound | Reported runtime |
|---:|---|---:|---|---:|---:|
| 22 | use_bridges=1 | 39,367 | 693444578290/377832855505 | 1.835321010829 | 0.45 s |
| 28 | use_bridges=1 | 940,974 | 15540968660/8494170644 | 1.829604008601 | 2.68 s |
| 30 | use_bridges=1 | 2,750,336 | 6792410744/3715467520 | 1.828144293400 | 8.35 s |
| 30 | use_bridges=2 | 1,990,016 | 20081808562/10987138918 | 1.827755952835 | 6.41 s |
| 32 | use_bridges=1 | 8,135,148 | 18108999119/9912056861 | 1.826966831703 | 37.19 s |
| 32 | use_bridges=2 | 5,787,106 | 14988071382/8205358318 | 1.826619972113 | 22.96 s |
| 34 | use_bridges=2 | 16,873,086 | 19360805483/10605620094 | 1.825523195381 | 101.78 s |

Only the loop length 30, use_bridges=1 row is claimed in this package. The pocket-pruned rows (use_bridges=2) are not covered by the theorem in object/THEOREM.md and are not claimed.

The theorem the generator relies on (the subset-inclusion condition and the Collatz-Wielandt step) is proved in object/THEOREM.md, which was written for this package and checked by the panel.
