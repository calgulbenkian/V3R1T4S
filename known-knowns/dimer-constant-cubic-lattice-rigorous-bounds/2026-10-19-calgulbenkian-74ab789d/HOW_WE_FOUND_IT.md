contributor text, unverified

# How it was found

He's argument bounds the dimer count by the spectral radius of a diagonal-layer matrix. The contributor's team asked whether the same inequality works for all matchings (monomers allowed) at unit activity, since the 2-lift inequality used by He has a version for matching polynomials. They wrote the extension down, built the 512 by 512 layer matrix for the (3,3) cross-section, and found a positive integer vector whose Collatz-Wielandt ratio gives h3 <= 0.7860441. Larger cross-sections gave smaller numbers in the author's notes but were not part of the claim that was checked. The package builder rebuilt the matrix from the definition, checked it against brute-force matching counts on small cases, and recomputed the ratio exactly.
