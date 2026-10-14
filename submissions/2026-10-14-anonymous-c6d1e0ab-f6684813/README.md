# `2026-10-14-anonymous-c6d1e0ab-f6684813` — `ghr-sum-difference-c3a` (`deep_k1_cert.json`)

## What
Verified in 80-digit and 105-digit directed-rounding decimal arithmetic that object/deep_k1_cert.json (26,995 bytes, SHA-256 f66848137f7f749bc2305b5fcca464507273d02a515a0e1174050714adf0da17) certifies an explicit finite-set lower bound C_3a >= 1.19229311147308833018077611662264204140088149782869 (k=1, m=1, ell=10000000000000, B=19572, q=30295, |M|=3889), strictly beating the published finite-certified record 1.19102809 by +1.265021e-03 >= 1e-7 (Partial Win p1).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/3a.md`, fetched `2026-10-14T10:55:24Z`, SHA-256 `2ebc3954e674a94481435e422e5c0b82f53581a537e8d8e85ffae1684826641a`)**:
  - Standing finite-certified lower bound (Kleinwaks 2026b): `C_3a >= 1.19102809`
  - Standing asymptotic limit lower bound (Kleinwaks 2026b): `C_3a >= 1.19519192*`
  - Our finite-depth certificate (`object/deep_k1_cert.json`): `C_3a >= 1.19229311147308833018077611662264204140088149782869` (`+1.265021e-03` over `1.19102809`)

## Not Claimed
- Does not exceed the asymptotic $N \to \infty$ block-limit lower bound `1.19519192*` (`beats_limit_record_1_19519192: false`); this submission is scoped strictly to Partial Win `p1` (explicit finite-set lower bound strictly beating `1.19102809` by at least `1e-7`).

## Credits
- Problem formulation and benchmark maintenance by Terence Tao (`teorth/optimizationproblems`), Gyarmati–Hennecart–Ruzsa (2003), Boyer–Li (2024), and Kleinwaks (2026a/b).
