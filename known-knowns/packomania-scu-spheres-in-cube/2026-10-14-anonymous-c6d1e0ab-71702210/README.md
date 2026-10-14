# `2026-10-14-anonymous-c6d1e0ab-71702210` — `packomania-scu-spheres-in-cube` (`N = 471`)

## What
Verified in 65-digit decimal arithmetic that object/scu471.txt (59,346 bytes, SHA-256 71702210656fae6819da996508da9b9d6383404d274e8405df0a85de342f90b8) defines a valid non-isometric packing of N = 471 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.067898241042897910706805143111, strictly exceeding the live Packomania scu record 0.067898240894670536184764825826 (Eckard Specht) by +1.482274e-10.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.067898240894670536184764825826`
  - Our certificate (`object/scu471.txt`): `r* = 0.067898241042897910706805143111` (`+1.482274e-10`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 471`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
