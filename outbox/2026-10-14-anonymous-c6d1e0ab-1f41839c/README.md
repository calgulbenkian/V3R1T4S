# `2026-10-14-anonymous-c6d1e0ab-1f41839c` — `codetables-binary-linear` (`[156, 10, 101]_4`)

## What
Verified that object/win_q4_n156_k10_d101.json (3,453 bytes, SHA-256 1f41839c1e4c0ee67c181cd5aefa9917c948c506ec9f53849ea6eface2322441) defines an explicit 10 x 156 generator matrix G over GF(4) of exact row rank 10 whose linear code [156, 10, 101]_4 has exact minimum Hamming distance d = 101 (with A_101 = 4590 minimum-weight codewords across all 1,048,575 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 100 (upper bound 109) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=4&n=156&k=10`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `a4ff14cada7375b909baa6e23ec895c046fbfbd844d79136996ba17fa444a234`)**:
  - Standing lower bound: `d_lower = 100` (upper bound `d_upper = 109`)
  - Our explicit generator matrix (`object/win_q4_n156_k10_d101.json`): `d = 101` (`+1` improvement, `A_101 = 4590`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 109` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
