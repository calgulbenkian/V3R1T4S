# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/C_55_14_3_b97.json` and `verify-it-yourself/verify_covering.py`.*

## Minimum-Unique-Coverage Block Deletion + 64-Bit Bitmask WalkSAT/Tabu/DCW (`how-we-built-it/covering_sa.c`)

We extracted the standing `99`-block `(v=55, k=14, t=3)` covering design from the La Jolla Covering Repository (`Zenodo 10.5281/zenodo.19735294`), computed the exact coverage multiplicity of all `26,235` triples, removed the block with the fewest uniquely covered triples, and repaired all uncovered triples using our multi-threaded 64-bit bitmask WalkSAT + Tabu + Dynamic Constraint Weighting solver (`how-we-built-it/covering_sa.c`), reaching `b = 97` blocks (`-2` below all live sources).
