# `2026-10-14-anonymous-c6d1e0ab-1ef5fd30` — `codetables-binary-linear` (`[155, 11, 98]_4`)

## What
Verified that object/win_q4_n155_k11_d98.json (3,748 bytes, SHA-256 1ef5fd30a7ac75387fa3c61042fd04fcbe480f94788a329f9c51f9b0dc7aaae5) defines an explicit 11 x 155 generator matrix G over GF(4) of exact row rank 11 whose linear code [155, 11, 98]_4 has exact minimum Hamming distance d = 98 (with A_98 = 3672 minimum-weight codewords across all 4,194,303 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 97 (upper bound 107) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=4&n=155&k=11`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `a4ff14cada7375b909baa6e23ec895c046fbfbd844d79136996ba17fa444a234`)**:
  - Standing lower bound: `d_lower = 97` (upper bound `d_upper = 107`)
  - Our explicit generator matrix (`object/win_q4_n155_k11_d98.json`): `d = 98` (`+1` improvement, `A_98 = 3672`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 107` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
