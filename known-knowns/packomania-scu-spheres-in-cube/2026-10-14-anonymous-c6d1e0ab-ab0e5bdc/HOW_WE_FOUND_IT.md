# How We Found It — `scu` (`N = 631`)

*Note: contributor text, unverified (narrative explanation of how the packing was constructed; the machine-verified certificate is in `object/scu631.txt`).*

## Method Summary
1. **Lens 1 (`how-we-built-it/cavity_splice.c`)**: Vacancy deletion from higher-$N$ lattice/near-lattice packings (`scu1688 -> N=1596`, `scu102 -> N=101`, `scu796 -> N=793`, `scu469 -> N=466..468`) and Voronoi cavity / odd-FCC vacancy insertion (`scu811 -> N=812`, `scu629 -> N=630..632`, `scu469 -> N=470..472`).
2. **Lens 2 (`how-we-built-it/scu_lbfgs_optimizer.c`)**: Smooth log-sum-exp L-BFGS continuation and 36-decimal exact boundary/pair equilibration.
