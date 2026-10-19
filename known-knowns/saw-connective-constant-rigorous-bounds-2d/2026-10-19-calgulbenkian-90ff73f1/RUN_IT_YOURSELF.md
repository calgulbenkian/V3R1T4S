# Run it yourself

From this package folder, in a fresh shell (python3 3.8 or later, standard library only; no network). Needs about 1.6 GB of memory, about 28 MB of temporary disk, and about 21 minutes on an Apple-silicon Mac (a slower machine may need much longer; a driver that enforces a timeout should allow at least 3000 s, and 5400 s on a slow machine):

```sh
sh verify-it-yourself/run_checks.sh
```

The last line should be `ALL CHECKS PASS`. The steps it runs:

1. Check every file under object/ against SHA256SUMS (stops with FAIL on any mismatch).
2. Concatenate object/vector_part_00.bin to vector_part_30.bin and check the sha256 of the whole (90ff73f1cfa9702a47f15e59a2fcdbd02c28185f75c1bd309a4e44790c93390b), then of each part against object/SHA256_PARTS.txt.
3. The known-answer test (loop length 22, a few seconds): the same checker on known-answer/vector_k22.bin must print PASS with the bound 138688915658/75566571101.
4. A negative control (state 0 of the known-answer vector set to 1) that must be rejected.
5. The full check, which can also be run alone on a reassembled file (use a folder of your own for the temporary file):

```sh
mkdir -p work && cat object/vector_part_*.bin > work/vector.bin
python3 -I verify-it-yourself/check_saw482.py work/vector.bin 32
```

Expected output of the full check ends with:

```
ok   regenerated state count 8135148 equals the vector length 8135148
transitions rebuilt 13072399, with more than one candidate 4549424, using a candidate other than the plain suffix 1986536, max candidates 11
ok   subset-inclusion invariant holds on all 13072399 chosen transitions (failures: 0)
exact max (P x)_i / x_i = 18108999119 / 9912056861 = 18108999119/9912056861 = 1.826966831703  (state index 5898119)
ok   state count 8135148 equals the claimed 8135148
ok   bound equals the claimed 18108999119/9912056861 exactly (got 18108999119/9912056861)
ok   bound 18108999119/9912056861 < 1.82926 - 2e-6 (exact rational comparison)
ok   bound 18108999119/9912056861 < the loop-length-30 bound 849051343/464433440 (exact rational comparison)
elapsed (seconds, varies)
PASS
```

(The comparison line uses the rounded 1.82926 minus 2e-6; the stricter bar used in README.md is Alm's published 1.829254, which the bound also beats: 1.826966831703 < 1.829254.)

## How the object was built

The object is the integer test vector of the certificate written by the author's generator, how-we-built-it/saw_bounds_2d.c, run for loop length 32 (command and provenance in how-we-built-it/README.md). verify-it-yourself/make_vector.py turns the 1.48 GB text certificate into the 31 binary parts (not needed to check). The file format and the definition of the automaton, including the clarifications added after the panel, are in object/AUTOMATON.md; the checker needs only the binary parts.
