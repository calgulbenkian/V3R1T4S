# Receipts (real output)

Full run_checks.sh.

```
RESULT trace dims=2,2 l=4 vertices=16 perfect_matchings=4752 tr(T^l)=4752 all_matchings=306305 tr(TMD^l)=306305 EQUAL
RESULT trace dims=3,2 l=4 vertices=24 perfect_matchings=194244 tr(T^l)=194244 all_matchings=162589284 tr(TMD^l)=162589284 EQUAL
RESULT trace dims=2,2 l=6 vertices=24 perfect_matchings=190992 tr(T^l)=190992 all_matchings=162465104 tr(TMD^l)=162465104 EQUAL
PASS trace identity: tr(TMD^l) = number of ALL matchings of the quotient graph, (2,2,4) (3,2,4) (2,2,6) 
RESULT propc dims=3,3 |G|=54 HOLDS (dimer and monomer-dimer)
PASS property C (dimer and monomer-dimer) on the full (3,3) matrices 
RESULT mdcert dims=3,3 states=512 orbits=44 u=255 ratio=731051554747087/618837374495 bound=0.7860440830 ceil10=0.7860440831
PASS exact ratio 731051554747087/618837374495 
PASS h3 <= 0.7860441 (unrounded 0.786044083039) is below FKLM 0.7862023450 by 0.0001582450 (needed: at least 1e-6) 
ALL CHECKS PASS
sh cubic-dimer-h3-ub-33/claim/verify-it-yourself/run_checks.sh  0.43s user 0.03s system 63% cpu 0.724 total

```
