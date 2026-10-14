# `2026-10-14-anonymous-c6d1e0ab-ab0e5bdc` — `packomania-scu-spheres-in-cube` (`N = 631`)

## What
Verified in 65-digit decimal arithmetic that object/scu631.txt (79,506 bytes, SHA-256 ab0e5bdcb3875d14645a826e6fcdb65ed580b92640951785e72e3d33a6c5607f) defines a valid non-isometric packing of N = 631 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.061949671758498235727065581655, strictly exceeding the live Packomania scu record 0.061949671549657821193834961183 (Eckard Specht) by +2.088404e-10.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.061949671549657821193834961183`
  - Our certificate (`object/scu631.txt`): `r* = 0.061949671758498235727065581655` (`+2.088404e-10`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 631`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
