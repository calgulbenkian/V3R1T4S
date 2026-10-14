# How We Found It — `hsp4` (`d = 4, N = 170`)

*Note: contributor text, unverified (narrative explanation of how the packing was constructed; the machine-verified certificate is in `object/WIN_hsp4_170_polished.txt`).*

## Method Summary
1. **Lens 1 (`how-we-built-it/transplant_scan.c`)**: Two-stage frozen-shell inner-core transplantation (`N_in = 20` inner spheres from `N = 166` rotated in `O(4)` inside the frozen `N_out = 150` outer shell of `N = 169`), followed by unfrozen full-system soft-sphere L-BFGS jamming (`WIN_transplant_hsp4_170.txt`, `r* = 0.2156371457737953995400180`).
2. **Lens 2 (`how-we-built-it/hsp_basin_opt.c`)**: 80-bit `long double` log-sum-exp L-BFGS continuation up to `beta = 2,000,000` with annealing micro-jitter, polishing `N = 170` to `r* = 0.2156450594683900081281903` (`+5.536430e-05` over `0.215589695168`) and generating the `N = 301` extension row (`r* = 0.1875249820010892044888787`, `+1.888510e-03` over single-cavity insertion).
