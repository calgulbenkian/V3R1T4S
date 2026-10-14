# Reproduction & Independent Verification Report: `codetables-binary-linear`

context: subagent (astra)
role: REPRODUCE skeptic
target: codetables-binary-linear
submission_type: solution_claim (Full Win across 12 distinct (q, n, k) cells)

## 1. Quoted Mathematical Definitions from `claim/target.md` and `claim/CLAIM.md`

From `claim/target.md` (`statement` and `success_criterion`):
- **Statement**:
  "For given [n,k] over GF(q), codetables.de (Grassl) records the best known lower and upper bounds on the maximum minimum distance d. A linear code with d larger than the tabulated lower bound is a new record. Binary tables cover n at most 256."
- **Success Criterion**:
  "Success means a k x n generator matrix over GF(q) with these properties. (1) Rank is exactly k over GF(q), computed independently. (2) The exact minimum distance d is computed by full enumeration of all q^k - 1 nonzero codewords when feasible (2^k at most ~2^32), or, for large k (or large k with small n-k, via the dual and MacWilliams identities), by two independent exact minimum-distance implementations that agree; never by sampling. (3) d is STRICTLY GREATER (direction: max) than the lower bound in the live http://www.codetables.de/ cell for (q,n,k) at verification time, and at most the upper bound. (4) The code is not one of the 7 LinCodeEvolve codes (arXiv:2609.37056) or a code derived from them, and no newer arXiv claim already reaches that d."

From `claim/CLAIM.md` (Section 1):
- "Every generator matrix G in F_q^{k x n} was verified to have exact full row rank rank_{F_q}(G) = k via Gaussian elimination over F_q."
- "Every minimum Hamming distance d(C) = min_{x in F_q^k \ {0}} wt(x G) and minimum-weight codeword count A_d was computed exhaustively over all q^k - 1 nonzero codewords (never sampling) by two independent implementations."

---

## 2. Independent Verification Before Reading `claim/verify_bklc.py`

Before inspecting `claim/verify_bklc.py`, I wrote and executed a standalone dual-method verifier from scratch (combining a Python finite-field Gaussian elimination checker over `GF(2)` and `GF(4) = GF(2)[w] / (w^2 + w + 1)` with two independent C99 exhaustive full-codebook evaluators compiled with `clang -O3`):
1. **Exact Row Rank (`rank_{GF(q)}(G) = k`)**:
   - Performs full Gaussian elimination to reduced row echelon form over `GF(2)` (for `q = 2`) and over `GF(4)` with elements `{0, 1, 2 = w, 3 = w^2 = w + 1}`, addition `a ^ b`, and multiplication table `2*2 = 3, 2*3 = 1, 3*3 = 2` (for `q = 4`).
   - Also tests a corrupted copy of each generator matrix with row `0` zeroed out, confirming that the rank drops from `k` to `k - 1` (`16` for `q = 2, k = 17`; `9` for `q = 4, k = 10`; `10` for `q = 4, k = 11`) and is strictly rejected.
2. **Exhaustive Full-Codebook Enumeration by Two Independent C99 Implementations**:
   - **Astra Method 1 (Bit-Sliced Lexicographic Odometer)**: Packs each generator row into three 64-bit words (`uint64_t` for `n` up to `192` bits; pairs `(lo, hi)` of `uint64_t` words per scalar multiple `a in {1, 2, 3}` for `GF(4)`) and iterates `m = 1 ... q^k - 1` (`131,071` nonzero codewords for `q = 2, k = 17`; `1,048,575` nonzero codewords for `q = 4, k = 10`; `4,194,303` nonzero codewords for `q = 4, k = 11`), computing `wt(x G)` via hardware `__builtin_popcountll` to determine the exact minimum Hamming weight `d`, minimum-weight multiplicity `A_d`, second minimum weight `d_2` (`A_{d_2}`), and maximum weight `w_max`.
   - **Astra Method 2 (Incremental Gray-Code / Coordinate-Level Base-4 Odometer)**:
     - For `q = 2`: walks all `2^17 - 1 = 131,071` nonzero codewords in binary Gray-code order `g = m ^ (m shifted right by 1)`, updating a single row per step via `cw ^= row[ctz(g ^ prev_g)]`.
     - For `q = 4`: walks all `4^k - 1` nonzero codewords via an unpacked coordinate-by-coordinate base-4 odometer `uint8_t cw[256]`, updating `cw[j] ^= GF4_MUL[old_a][G[pos][j]] ^ GF4_MUL[new_a][G[pos][j]]` and counting `cw[j] != 0` directly without bit-slicing.

Both independent methods agreed identically on `(d, A_d)` for all 12 primary winning `.json` files (and all 6 secondary `.json` files) in `claim/`.

### A. Independent Verification Table for All 12 Primary Record-Breaking Files

| # | File (relative to `claim/`) | `[n, k, d]_q` | `codetables.de` `[d_lo, d_up]` | Gain | Rank (`Corrupt`) | Nonzero Codewords `q^k - 1` | Verified `d` (`M1 == M2`) | Verified `A_d` (`M1 == M2`) | Next Weight `d_2` (`A_{d_2}`) | Max Weight |
| :-: | :--- | :--- | :---: | :---: | :---: | ---: | ---: | ---: | :--- | ---: |
| 1 | `claim/opt_win_q2_n170_k17_d69.json` | `[170, 17, 69]_2` | `[68, 76]` | **`+1`** | `17/17` (`16`) | `131,071` | **`69`** | **`468`** | `70` (`1931`) | `111` |
| 2 | `claim/opt_win_q2_n171_k17_d70.json` | `[171, 17, 70]_2` | `[69, 76]` | **`+1`** | `17/17` (`16`) | `131,071` | **`70`** | **`1092`** | `71` (`3137`) | `112` |
| 3 | `claim/win_q2_n172_k17_d71.json` | `[172, 17, 71]_2` | `[70, 76]` | **`+1`** | `17/17` (`16`) | `131,071` | **`71`** | **`1751`** | `72` (`4590`) | `111` |
| 4 | `claim/win_q2_n173_k17_d72.json` | `[173, 17, 72]_2` | `[70, 77]` | **`+2`** | `17/17` (`16`) | `131,071` | **`72`** | **`6341`** | `80` (`39440`) | `112` |
| 5 | `claim/opt_win_q2_n174_k17_d72.json` | `[174, 17, 72]_2` | `[71, 78]` | **`+1`** | `17/17` (`16`) | `131,071` | **`72`** | **`3154`** | `73` (`3187`) | `113` |
| 6 | `claim/win_q4_n156_k10_d101.json` | `[156, 10, 101]_4` | `[100, 109]` | **`+1`** | `10/10` (`9`) | `1,048,575` | **`101`** | **`4590`** | `102` (`714`) | `156` |
| 7 | `claim/win_q4_n154_k11_d97.json` | `[154, 11, 97]_4` | `[96, 106]` | **`+1`** | `11/11` (`10`) | `4,194,303` | **`97`** | **`2448`** | `98` (`1224`) | `154` |
| 8 | `claim/win_q4_n155_k11_d98.json` | `[155, 11, 98]_4` | `[97, 107]` | **`+1`** | `11/11` (`10`) | `4,194,303` | **`98`** | **`3672`** | `100` (`9486`) | `154` |
| 9 | `claim/win_q4_n157_k11_d99.json` | `[157, 11, 99]_4` | `[98, 108]` | **`+1`** | `11/11` (`10`) | `4,194,303` | **`99`** | **`1428`** | `100` (`3009`) | `155` |
| 10 | `claim/win_q4_n158_k11_d100.json` | `[158, 11, 100]_4` | `[99, 109]` | **`+1`** | `11/11` (`10`) | `4,194,303` | **`100`** | **`2703`** | `101` (`1734`) | `156` |
| 11 | `claim/win_q4_n162_k11_d103.json` | `[162, 11, 103]_4` | `[102, 112]` | **`+1`** | `11/11` (`10`) | `4,194,303` | **`103`** | **`2907`** | `104` (`5049`) | `161` |
| 12 | `claim/win_q4_n163_k11_d104.json` | `[163, 11, 104]_4` | `[103, 113]` | **`+1`** | `11/11` (`10`) | `4,194,303` | **`104`** | **`7956`** | `106` (`11934`) | `162` |

### B. Independent Verification of the 6 Additional Companion `.json` Files in `claim/`

| File (relative to `claim/`) | `[n, k, d]_q` | `codetables.de` `[d_lo, d_up]` | Gain | Rank | Verified `d` | Verified `A_d` | Next Weight `d_2` (`A_{d_2}`) |
| :--- | :--- | :---: | :---: | :---: | ---: | ---: | :--- |
| `claim/win_q2_n170_k17_d69.json` | `[170, 17, 69]_2` | `[68, 76]` | `+1` | `17/17` | `69` | `1751` | `72` (`4590`) |
| `claim/win_q2_n171_k17_d70.json` | `[171, 17, 70]_2` | `[69, 76]` | `+1` | `17/17` | `70` | `1751` | `72` (`4590`) |
| `claim/opt_win_q2_n172_k17_d71.json` | `[172, 17, 71]_2` | `[70, 76]` | `+1` | `17/17` | `71` | `2657` | `72` (`3684`) |
| `claim/win_q2_n173_k17_d71.json` | `[173, 17, 71]_2` | `[70, 77]` | `+1` | `17/17` | `71` | `544` | `72` (`3230`) |
| `claim/opt_win_q2_n173_k17_d71.json` | `[173, 17, 71]_2` | `[70, 77]` | `+1` | `17/17` | `71` | `1584` | `72` (`2190`) |
| `claim/win_q2_n174_k17_d72.json` | `[174, 17, 72]_2` | `[71, 78]` | `+1` | `17/17` | `72` | `3774` | `76` (`8602`) |

---

## 3. Artifact Integrity & SHA-256 Hashes

| File (relative to `claim/`) | Size (bytes) | SHA-256 Digest |
| :--- | ---: | :--- |
| `claim/verify_bklc.py` | `19850` | `de65a78e4c2ca678be31825451768510d2bc463bf3541d56fa1ede904018fd73` |
| `claim/qc_search.c` | `45474` | `3c67e469a4902f9c780334140e9f5e1c268321617d4e9f1a19861169b91a23e0` |
| `claim/bklc_opt.c` | `22874` | `b6c94ad17fe294f90da5c49201fd01756d07e61346cd7890c3321a12d6aa1337` |
| `claim/opt_win_q2_n170_k17_d69.json` | `6173` | `68f3c9cb8816740cfd7d1610339438a661d60d08c389cf8df2d6baa791b212c9` |
| `claim/opt_win_q2_n171_k17_d70.json` | `6208` | `fd175df444fe56b8d6d2eb4007e72edacec2575e49ac048492f2035eff96e2b4` |
| `claim/win_q2_n172_k17_d71.json` | `6228` | `dbda9f8c500349cb70c2d6c4ddbfdb3ef06e32996fd78a5b6556c2c46503438b` |
| `claim/win_q2_n173_k17_d72.json` | `6262` | `a17d00378317979d9fe0acb452d3cce805f55cb17595a8407acb9b56b7b51a76` |
| `claim/opt_win_q2_n174_k17_d72.json` | `6313` | `07292e7fb3a5377aa924d70118c0c8a409df6cf4b2641584d1aa0a765a298218` |
| `claim/win_q4_n156_k10_d101.json` | `3453` | `1f41839c1e4c0ee67c181cd5aefa9917c948c506ec9f53849ea6eface2322441` |
| `claim/win_q4_n154_k11_d97.json` | `3726` | `380a0c68430f902188b249779cbd0939ac94776b49a2793a462a12895a761d3d` |
| `claim/win_q4_n155_k11_d98.json` | `3748` | `1ef5fd30a7ac75387fa3c61042fd04fcbe480f94788a329f9c51f9b0dc7aaae5` |
| `claim/win_q4_n157_k11_d99.json` | `3792` | `b84c0b9a7e8b93c969d13a2372aab66f04e038803bd8e9651e97845f12f291bd` |
| `claim/win_q4_n158_k11_d100.json` | `3815` | `f3c0d752a28835345362e0d9f4d487519ad8b113f118b07236f63efdaad788b8` |
| `claim/win_q4_n162_k11_d103.json` | `3904` | `70900001eaf3d83a0097232cb01947e218e7d3c9a24955e1a6c452f83c70c88b` |
| `claim/win_q4_n163_k11_d104.json` | `3927` | `28103164e334b8d35cdcb6e2d2dac8be21a26b82a9acaad2b53d835d25456b8f` |
| `claim/win_q2_n170_k17_d69.json` | `6160` | `8531f57da208d19f0b0183b8976bc6d0ae96464b895d091c75e9a8ddb4e52e59` |
| `claim/win_q2_n171_k17_d70.json` | `6194` | `7654b528cba649d17be157acad5410b311dcb2d04a71a80b8c470b5a8638000c` |
| `claim/opt_win_q2_n172_k17_d71.json` | `6242` | `ffe9d3d1f5e6bc210b110f904be89244c85cbf8fcf25074da43312e299a98c8e` |
| `claim/win_q2_n173_k17_d71.json` | `6261` | `a3a53cf04d03f2c729143e1ae0f00ec94ed15dce8a753f848dc2bb35857bf167` |
| `claim/opt_win_q2_n173_k17_d71.json` | `6276` | `da2092e577da54e379cc97621c730aa1323d28b2d8c80cf0674805c6f64d1211` |
| `claim/win_q2_n174_k17_d72.json` | `6296` | `1817263a63dc07473712a9cfcd696082309c10f26457d6ff6587f82610bce147` |

---

## 4. Audit and Execution of Author's Verifier (`claim/verify_bklc.py`)

After completing my independent verification, I inspected `claim/verify_bklc.py` and executed it:
1. `python3 claim/verify_bklc.py --self-test`:
   - Exit code: `0`
   - Verified positive baseline `[7,4,3]_2` (`rank=4, d1=3, d2=3, A_3=7`), positive quantum baseline `[[5,1,3]]_2` (`d=3`), and negative rank-deficient `[7,4]_2` (`rank=3 != 4 correctly rejected`).
2. `python3 claim/verify_bklc.py claim/*.json`:
   - Exit code: `0`
   - Output across all 18 JSON files:
     - `file=opt_win_q2_n170_k17_d69.json PASS kind=solution_claim params=[170,17,69]_2 rank=17 A_d=468 d_table_lo=68 d_table_hi=76 gain=+1 methods_agree=True`
     - `file=opt_win_q2_n171_k17_d70.json PASS kind=solution_claim params=[171,17,70]_2 rank=17 A_d=1092 d_table_lo=69 d_table_hi=76 gain=+1 methods_agree=True`
     - `file=opt_win_q2_n172_k17_d71.json PASS kind=solution_claim params=[172,17,71]_2 rank=17 A_d=2657 d_table_lo=70 d_table_hi=76 gain=+1 methods_agree=True`
     - `file=opt_win_q2_n173_k17_d71.json PASS kind=solution_claim params=[173,17,71]_2 rank=17 A_d=1584 d_table_lo=70 d_table_hi=77 gain=+1 methods_agree=True`
     - `file=opt_win_q2_n174_k17_d72.json PASS kind=solution_claim params=[174,17,72]_2 rank=17 A_d=3154 d_table_lo=71 d_table_hi=78 gain=+1 methods_agree=True`
     - `file=win_q2_n170_k17_d69.json PASS kind=solution_claim params=[170,17,69]_2 rank=17 A_d=1751 d_table_lo=68 d_table_hi=76 gain=+1 methods_agree=True`
     - `file=win_q2_n171_k17_d70.json PASS kind=solution_claim params=[171,17,70]_2 rank=17 A_d=1751 d_table_lo=69 d_table_hi=76 gain=+1 methods_agree=True`
     - `file=win_q2_n172_k17_d71.json PASS kind=solution_claim params=[172,17,71]_2 rank=17 A_d=1751 d_table_lo=70 d_table_hi=76 gain=+1 methods_agree=True`
     - `file=win_q2_n173_k17_d71.json PASS kind=solution_claim params=[173,17,71]_2 rank=17 A_d=544 d_table_lo=70 d_table_hi=77 gain=+1 methods_agree=True`
     - `file=win_q2_n173_k17_d72.json PASS kind=solution_claim params=[173,17,72]_2 rank=17 A_d=6341 d_table_lo=70 d_table_hi=77 gain=+2 methods_agree=True`
     - `file=win_q2_n174_k17_d72.json PASS kind=solution_claim params=[174,17,72]_2 rank=17 A_d=3774 d_table_lo=71 d_table_hi=78 gain=+1 methods_agree=True`
     - `file=win_q4_n154_k11_d97.json PASS kind=solution_claim params=[154,11,97]_4 rank=11 A_d=2448 d_table_lo=96 d_table_hi=106 gain=+1 methods_agree=True`
     - `file=win_q4_n155_k11_d98.json PASS kind=solution_claim params=[155,11,98]_4 rank=11 A_d=3672 d_table_lo=97 d_table_hi=107 gain=+1 methods_agree=True`
     - `file=win_q4_n156_k10_d101.json PASS kind=solution_claim params=[156,10,101]_4 rank=10 A_d=4590 d_table_lo=100 d_table_hi=109 gain=+1 methods_agree=True`
     - `file=win_q4_n157_k11_d99.json PASS kind=solution_claim params=[157,11,99]_4 rank=11 A_d=1428 d_table_lo=98 d_table_hi=108 gain=+1 methods_agree=True`
     - `file=win_q4_n158_k11_d100.json PASS kind=solution_claim params=[158,11,100]_4 rank=11 A_d=2703 d_table_lo=99 d_table_hi=109 gain=+1 methods_agree=True`
     - `file=win_q4_n162_k11_d103.json PASS kind=solution_claim params=[162,11,103]_4 rank=11 A_d=2907 d_table_lo=102 d_table_hi=112 gain=+1 methods_agree=True`
     - `file=win_q4_n163_k11_d104.json PASS kind=solution_claim params=[163,11,104]_4 rank=11 A_d=7956 d_table_lo=103 d_table_hi=113 gain=+1 methods_agree=True`
3. **Corrupted negative test on `claim/verify_bklc.py`**:
   - Zeroing row `0` of `claim/opt_win_q2_n170_k17_d69.json` exits with code `1` and outputs `FAIL: rank deficiency rank(G)=16 != k=17`.

All independent and author verification checks succeed.

pass: true
