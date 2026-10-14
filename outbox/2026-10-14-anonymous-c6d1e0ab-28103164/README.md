# `2026-10-14-anonymous-c6d1e0ab-28103164` — `codetables-binary-linear` (`[163, 11, 104]_4`)

## What
Verified that object/win_q4_n163_k11_d104.json (3,927 bytes, SHA-256 28103164e334b8d35cdcb6e2d2dac8be21a26b82a9acaad2b53d835d25456b8f) defines an explicit 11 x 163 generator matrix G over GF(4) of exact row rank 11 whose linear code [163, 11, 104]_4 has exact minimum Hamming distance d = 104 (with A_104 = 7956 minimum-weight codewords across all 4,194,303 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 103 (upper bound 113) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=4&n=163&k=11`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `a4ff14cada7375b909baa6e23ec895c046fbfbd844d79136996ba17fa444a234`)**:
  - Standing lower bound: `d_lower = 103` (upper bound `d_upper = 113`)
  - Our explicit generator matrix (`object/win_q4_n163_k11_d104.json`): `d = 104` (`+1` improvement, `A_104 = 7956`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 113` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
