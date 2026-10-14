# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/C_38_16_3_b25.json` and `verify-it-yourself/verify_covering.py`.*

## Minimum-Unique-Coverage Block Deletion + 64-Bit Bitmask WalkSAT/Tabu/DCW (`how-we-built-it/covering_sa.c`)

We extracted the standing `26`-block `(v=38, k=16, t=3)` covering design from the La Jolla Covering Repository (`Zenodo 10.5281/zenodo.19735294`), computed the exact coverage multiplicity of all `8,436` triples, removed the block with the fewest uniquely covered triples, and repaired all uncovered triples using our multi-threaded 64-bit bitmask WalkSAT + Tabu + Dynamic Constraint Weighting solver (`how-we-built-it/covering_sa.c`), reaching `b = 25` blocks (`-1` below all live sources).
