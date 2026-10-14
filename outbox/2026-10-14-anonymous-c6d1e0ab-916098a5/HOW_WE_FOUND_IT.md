# How We Found It — `Q_13` `symmetric_coil` (`L = 2870`)

*Note: contributor text, unverified (narrative explanation of how the certificate was constructed; the machine-verified certificate is in `object/sym_coil_Q13_2870.txt`).*

## Method Summary
1. **Lens 1 (`how-we-built-it/lift_all_dims.c`)**: Single-coordinate reflection avoidance and antipodal splicing of symmetric coils from $Q_{n-1}$ to $Q_n$, followed by paired $+2$ half-period window augmentations using 512-bit SIMD BFS and parity-pruned DFS.
2. **Lens 2 (`how-we-built-it/snake_coil_opt.c`)**: Two-stage cascaded unrestricted coil lifting (`Q12 -> Q13 -> Q14`), $Q_9$-subcube automorphism splicing on `toner_q14_5850.txt`, and neutral pocket drift (`drift_opt`) generating strictly inequivalent equal-record snakes and coils across $Q_{10}..Q_{13}$.
