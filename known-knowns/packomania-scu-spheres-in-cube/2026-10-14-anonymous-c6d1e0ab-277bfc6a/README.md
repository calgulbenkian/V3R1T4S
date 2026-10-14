# `2026-10-14-anonymous-c6d1e0ab-277bfc6a` — `packomania-scu-spheres-in-cube` (`N = 632`)

## What
Verified in 65-digit decimal arithmetic that object/scu632.txt (79,632 bytes, SHA-256 277bfc6a2364e3872f20f42731ccc6e4c5de4cd564814081cf7a3f6398c4b320) defines a valid non-isometric packing of N = 632 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.061949671758524842833475299750, strictly exceeding the live Packomania scu record 0.061949671549647706846377765805 (Eckard Specht) by +2.088771e-10.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.061949671549647706846377765805`
  - Our certificate (`object/scu632.txt`): `r* = 0.061949671758524842833475299750` (`+2.088771e-10`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 632`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
