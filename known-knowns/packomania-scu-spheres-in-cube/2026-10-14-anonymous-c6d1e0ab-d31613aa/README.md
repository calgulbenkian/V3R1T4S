# `2026-10-14-anonymous-c6d1e0ab-d31613aa` — `packomania-scu-spheres-in-cube` (`N = 470`)

## What
Verified in 65-digit decimal arithmetic that object/scu470.txt (59,220 bytes, SHA-256 d31613aa605c97184a2a8650cd9c6141671d413cb35a6802838201698e3091eb) defines a valid non-isometric packing of N = 470 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.067898241049419029535261829608, strictly exceeding the live Packomania scu record 0.067898240894670536184764825826 (Eckard Specht) by +1.547485e-10.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.067898240894670536184764825826`
  - Our certificate (`object/scu470.txt`): `r* = 0.067898241049419029535261829608` (`+1.547485e-10`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 470`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
