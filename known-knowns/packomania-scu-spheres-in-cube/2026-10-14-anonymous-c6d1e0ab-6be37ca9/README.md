# `2026-10-14-anonymous-c6d1e0ab-6be37ca9` — `packomania-scu-spheres-in-cube` (`N = 466`)

## What
Verified in 65-digit decimal arithmetic that object/scu466.txt (58,716 bytes, SHA-256 6be37ca99afd5dd53f5719e2a5be83c417c385742c2696ed4187ec9cfe334105) defines a valid non-isometric packing of N = 466 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.067898241051355201396095879180, strictly exceeding the live Packomania scu record 0.067898240894769256234850176022 (Eckard Specht) by +1.565859e-10.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.067898240894769256234850176022`
  - Our certificate (`object/scu466.txt`): `r* = 0.067898241051355201396095879180` (`+1.565859e-10`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 466`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
