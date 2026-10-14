# `2026-10-14-anonymous-c6d1e0ab-605bc059` — `packomania-scu-spheres-in-cube` (`N = 101`)

## What
Verified in 65-digit decimal arithmetic that object/scu101.txt (12,726 bytes, SHA-256 605bc0591017c7a2eec3f7a37ec33b16936a3664a312bcde00b2bdf46e6538c6) defines a valid non-isometric packing of N = 101 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.110240606233695265468856021377, strictly exceeding the live Packomania scu record 0.110240604605984488395300868556 (Eckard Specht) by +1.627711e-09.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.110240604605984488395300868556`
  - Our certificate (`object/scu101.txt`): `r* = 0.110240606233695265468856021377` (`+1.627711e-09`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 101`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
