# `2026-10-14-anonymous-c6d1e0ab-1c017482` — `packomania-scu-spheres-in-cube` (`N = 793`)

## What
Verified in 65-digit decimal arithmetic that object/scu793.txt (99,918 bytes, SHA-256 1c017482412f0f9653595e9735da2ebbb6a270defb8cbca9d5c57c0c838167ad) defines a valid non-isometric packing of N = 793 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.057356313101938118309456188665, strictly exceeding the live Packomania scu record 0.057356312222008810279000968621 (Eckard Specht) by +8.799293e-10.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.057356312222008810279000968621`
  - Our certificate (`object/scu793.txt`): `r* = 0.057356313101938118309456188665` (`+8.799293e-10`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 793`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
