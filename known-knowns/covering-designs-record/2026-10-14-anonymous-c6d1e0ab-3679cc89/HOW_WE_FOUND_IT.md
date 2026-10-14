# How We Found It (contributor text, unverified)

*Note: This file is contributor text, unverified. The claim rests solely on `object/C_45_14_3_b58.json` and `verify-it-yourself/verify_covering.py`.*

## Minimum-Unique-Coverage Block Deletion + 64-Bit Bitmask WalkSAT/Tabu/DCW (`how-we-built-it/covering_sa.c`)

We extracted the standing `59`-block `(v=45, k=14, t=3)` covering design from the La Jolla Covering Repository (`Zenodo 10.5281/zenodo.19735294`), computed the exact coverage multiplicity of all `14,190` triples, removed the block with the fewest uniquely covered triples, and repaired all uncovered triples using our multi-threaded 64-bit bitmask WalkSAT + Tabu + Dynamic Constraint Weighting solver (`how-we-built-it/covering_sa.c`), reaching `b = 58` blocks (`-1` below all live sources).
