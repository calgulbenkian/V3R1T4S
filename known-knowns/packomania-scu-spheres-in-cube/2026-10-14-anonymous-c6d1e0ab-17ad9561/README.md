# `2026-10-14-anonymous-c6d1e0ab-17ad9561` — `packomania-scu-spheres-in-cube` (`N = 1596`)

## What
Verified in 65-digit decimal arithmetic that object/scu1596.txt (201,096 bytes, SHA-256 17ad9561bd7a7f216eac6525ed3ed67de13668b78707c2187c5421ae4f40d589) defines a valid non-isometric packing of N = 1596 equal spheres in the unit cube [-1/2, 1/2]^3 with exact radius r* = 0.045873685240229747068212434815, strictly exceeding the live Packomania scu record 0.045385736359615385798733074995 (Michael Goldberg) by +4.879489e-04 (also satisfying Partial Win p1 for a non-Specht row).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/scu/txt/radius.txt`, fetched `2026-10-14T12:06:05Z`, SHA-256 `7c7e549a82bf9f6f8d877fcf4da9529d5ec1e8e9a10365c2a53e6ef7364cd9fa`)**:
  - Standing bound (`Michael Goldberg`): `r_table = 0.045385736359615385798733074995`
  - Our certificate (`object/scu1596.txt`): `r* = 0.045873685240229747068212434815` (`+4.879489e-04`)

## Not Claimed
- Does not claim a proof of global optimality for `N = 1596`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` explicit entries naming `scu`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`) and Michael Goldberg (1971).
