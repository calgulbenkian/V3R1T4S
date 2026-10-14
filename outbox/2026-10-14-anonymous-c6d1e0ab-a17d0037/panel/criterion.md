# CRITERION Skeptic Report: `codetables-binary-linear` — 12 Record-Breaking `[n, k, d]_q` Linear Codes

context: subagent
confirmed_scope: Verified 12 explicit record-breaking linear code generator matrices in claim/ across 5 binary cells ([170,17,69]_2, [171,17,70]_2, [172,17,71]_2, [173,17,72]_2, [174,17,72]_2) and 7 quaternary cells ([156,10,101]_4, [154,11,97]_4, [155,11,98]_4, [157,11,99]_4, [158,11,100]_4, [162,11,103]_4, [163,11,104]_4), confirming full row rank k over GF(q), exact minimum distance d and multiplicity A_d via two independent full-codebook enumerations over all q^k - 1 nonzero codewords, strict improvement (+1 to +2) over live codetables.de lower bounds while remaining at most the upper bounds, and complete disjointness from the LinCodeEvolve codes (arXiv:2609.37056).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Independent Full-Rank & Dual-Method Exact Minimum-Distance Verification
Executed `claim/verify_bklc.py` (including `--self-test` on `[7,4,3]_2`, `[[5,1,3]]_2`, and rank-deficient negative test) across all 13 `claim/win_*.json` files covering the 12 distinct `(q, n, k)` cells:
- **(1) Full Row Rank**: Every $k \times n$ generator matrix $G$ over $\mathbb{F}_q$ has entries in $\{0, \dots, q-1\}$ and exact rank $\operatorname{rank}_{\mathbb{F}_q}(G) = k$ via Gaussian elimination over $\mathbb{F}_q$.
- **(2) Exact Minimum Distance by Full Enumeration (Two Independent Implementations)**: For every code ($2^{17} - 1 = 131,071$ nonzero codewords for $q=2, k=17$; $4^{10} - 1 = 1,048,575$ for $q=4, k=10$; $4^{11} - 1 = 4,194,303$ for $q=4, k=11$), Method 1 (iterative Gray-code / monic odometer over $G$) and Method 2 (recursive DFS over the RREF matrix $M$) agree identically on both $(d, A_d)$ without sampling.
- **(3) Strict Improvement Over Live `codetables.de` Lower Bounds**: Every cell achieves $d$ strictly greater than $d_{\text{lo}}(q, n, k)$ (by $+1$, and by $+2$ at $[173, 17, 72]_2$) and at most $d_{\text{up}}(q, n, k)$.
- **(4) Disjointness from `LinCodeEvolve` (`arXiv:2609.37056`)**: The 5 binary cells have $k = 17$ (disjoint from `LinCodeEvolve`'s $q=2, k \in \{19, 20, 21, 22\}, n \in [170, 240]$ region), and the 7 quaternary cells are over $\mathbb{F}_4$ (untouched by `LinCodeEvolve`).

### 1.2 Verified Artifact Table

| # | Artifact (`claim/`) | Bytes | SHA-256 | Parameters $[n, k, d]_q$ | Rank | Exact $A_d$ | Live `codetables.de` $[d_{\text{lo}}, d_{\text{up}}]$ | Gain |
| :-: | :--- | ---: | :--- | :--- | :-: | ---: | :---: | :-: |
| 1 | `claim/win_q2_n170_k17_d69.json` | `6,160` | `8531f57da208d19f0b0183b8976bc6d0ae96464b895d091c75e9a8ddb4e52e59` | `[170, 17, 69]_2` | `17` | `1,751` | `68..76` | `+1` |
| 2 | `claim/win_q2_n171_k17_d70.json` | `6,194` | `7654b528cba649d17be157acad5410b311dcb2d04a71a80b8c470b5a8638000c` | `[171, 17, 70]_2` | `17` | `1,751` | `69..76` | `+1` |
| 3 | `claim/win_q2_n172_k17_d71.json` | `6,228` | `dbda9f8c500349cb70c2d6c4ddbfdb3ef06e32996fd78a5b6556c2c46503438b` | `[172, 17, 71]_2` | `17` | `1,751` | `70..76` | `+1` |
| 4 | `claim/win_q2_n173_k17_d72.json` | `6,262` | `a17d00378317979d9fe0acb452d3cce805f55cb17595a8407acb9b56b7b51a76` | `[173, 17, 72]_2` | `17` | `6,341` | `70..77` | `+2` |
| 4b | `claim/win_q2_n173_k17_d71.json` | `6,261` | `a3a53cf04d03f2c729143e1ae0f00ec94ed15dce8a753f848dc2bb35857bf167` | `[173, 17, 71]_2` | `17` | `544` | `70..77` | `+1` |
| 5 | `claim/win_q2_n174_k17_d72.json` | `6,296` | `1817263a63dc07473712a9cfcd696082309c10f26457d6ff6587f82610bce147` | `[174, 17, 72]_2` | `17` | `3,774` | `71..78` | `+1` |
| 6 | `claim/win_q4_n156_k10_d101.json` | `3,453` | `1f41839c1e4c0ee67c181cd5aefa9917c948c506ec9f53849ea6eface2322441` | `[156, 10, 101]_4` | `10` | `4,590` | `100..109` | `+1` |
| 7 | `claim/win_q4_n154_k11_d97.json` | `3,726` | `380a0c68430f902188b249779cbd0939ac94776b49a2793a462a12895a761d3d` | `[154, 11, 97]_4` | `11` | `2,448` | `96..106` | `+1` |
| 8 | `claim/win_q4_n155_k11_d98.json` | `3,748` | `1ef5fd30a7ac75387fa3c61042fd04fcbe480f94788a329f9c51f9b0dc7aaae5` | `[155, 11, 98]_4` | `11` | `3,672` | `97..107` | `+1` |
| 9 | `claim/win_q4_n157_k11_d99.json` | `3,792` | `b84c0b9a7e8b93c969d13a2372aab66f04e038803bd8e9651e97845f12f291bd` | `[157, 11, 99]_4` | `11` | `1,428` | `98..108` | `+1` |
| 10 | `claim/win_q4_n158_k11_d100.json` | `3,815` | `f3c0d752a28835345362e0d9f4d487519ad8b113f118b07236f63efdaad788b8` | `[158, 11, 100]_4` | `11` | `2,703` | `99..109` | `+1` |
| 11 | `claim/win_q4_n162_k11_d103.json` | `3,904` | `70900001eaf3d83a0097232cb01947e218e7d3c9a24955e1a6c452f83c70c88b` | `[162, 11, 103]_4` | `11` | `2,907` | `102..112` | `+1` |
| 12 | `claim/win_q4_n163_k11_d104.json` | `3,927` | `28103164e334b8d35cdcb6e2d2dac8be21a26b82a9acaad2b53d835d25456b8f` | `[163, 11, 104]_4` | `11` | `7,956` | `103..113` | `+1` |

## 2. Verdict
All four clauses of the full success criterion in `claim/target.md` are satisfied across all 12 `(q, n, k)` cells.

pass: true
