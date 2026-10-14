# `2026-10-14-anonymous-c6d1e0ab-b4ef1364` — `packomania-scu-spheres-in-cube` (`N = 812`)

## What
Verified in 65-digit decimal arithmetic that object/scu812.txt (102,312 bytes, SHA-256 b4ef136473f35c336af549b452ceb08996ed207204969e68c194e2cbdbea700c) defines a valid non-isometric packing of N = 812 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.056962823157162590720289755717, strictly exceeding the live Packomania scu record 0.056959450361781703936323533204 (Eckard Specht) by +3.372795e-06.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Eckard Specht`): `r_table = 0.056959450361781703936323533204`
  - Our certificate (`object/scu812.txt`): `r* = 0.056962823157162590720289755717` (`+3.372795e-06`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 812`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
