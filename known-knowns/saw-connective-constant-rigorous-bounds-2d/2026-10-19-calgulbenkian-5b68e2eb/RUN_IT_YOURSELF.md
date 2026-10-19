# Run it yourself

From this package folder, in a fresh shell (python3 3.8 or later, standard library only; about 770 MB of memory, 45 MB of temporary disk). The checker run takes about 7 to 15 minutes, depending on the machine and its load (6 minutes for the full check on an idle Apple-silicon Mac, 11 to 13 minutes for the whole script on a busy one).

```sh
sh verify-it-yourself/run_checks.sh
```

The last line should be `ALL CHECKS PASS`. The steps it runs:

1. Concatenate object/states_part_00.bin to states_part_41.bin and check the sha256 of the whole (5b68e2eb7517096965e583cc68cddb13978e8959b8a0a7a218d08ad10a2dfee7), then of each part against object/SHA256_PARTS.txt.
2. Two negative controls on the first 3000 states (a vector entry set to 1; a seed state removed); both must be rejected.
3. The full check, which can also be run alone on a reassembled file (use a folder of your own for the temporary file):

```sh
mkdir -p work && cat object/states_part_*.bin > work/states.bin
python3 -I verify-it-yourself/check_saw482.py work/states.bin 30 2750336
```

Expected output of the full check ends with:

```
transitions rebuilt 4420718, with more than one candidate 1510053, using a candidate other than the plain suffix 643304, max candidates 10
ok   every candidate target is in the state list (missing: 0)
ok   subset-inclusion invariant holds on all 4420718 chosen transitions (failures: 0)
exact max (P x)_i / x_i = 6792410744 / 3715467520 = 849051343/464433440 = 1.828144293400  (state index 2618199)
ok   bound 849051343/464433440 < 1.82926 - 2e-6 (exact rational comparison)
ok   state count 2750336
ok   loop length K = 30 and 2,750,336 states, as claimed (K = 30, N = 2750336)
ok   bound equals the claimed 849051343/464433440 exactly (got 849051343/464433440)
elapsed (seconds, varies)
PASS
```

(The comparison line uses the rounded 1.82926 minus 2e-6; the stricter bar used in README.md is Alm's published 1.829254, which the bound also beats: 1.8281442934 < 1.829254.)

## How the object was built

The object is the state list and the positive integer test vector from the certificate written by the author's generator, how-we-built-it/saw_bounds_2d.c, run for loop length 30. The compile line is not recorded in the author's snapshot; the source uses only the C standard library and 128-bit integers, so a plain C compiler with optimisation and the math library should build it. The run is documented in how-we-built-it/README.md. The conversion of the 471,147,580-byte text certificate into the 42 binary parts is described in object/AUTOMATON.md (file format); the conversion script itself is not shipped, and the checker needs only the binary parts.
