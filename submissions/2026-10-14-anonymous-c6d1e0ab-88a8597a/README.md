# `2026-10-14-anonymous-c6d1e0ab-88a8597a` — `ghr-sum-difference-c3a` (`best_k2_finite_cert.json`)

## What
Verified in 80-digit and 105-digit directed-rounding decimal arithmetic that object/best_k2_finite_cert.json (438,438 bytes, SHA-256 88a8597a3f644e9ea00bdd76269ce69e5c367e9eeaddab9c1a8d3594d8750b1d) certifies an explicit finite-set lower bound C_3a >= 1.19298973462186362590382529754753993070825527359705 (k=2, m=1, ell=10000000000000000, B=21700, q=25879, |M|=6641), strictly beating the published finite-certified record 1.19102809 by +1.961645e-03 >= 1e-7 (Partial Win p1).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/3a.md`, fetched `2026-10-14T10:55:24Z`, SHA-256 `2ebc3954e674a94481435e422e5c0b82f53581a537e8d8e85ffae1684826641a`)**:
  - Standing finite-certified lower bound (Kleinwaks 2026b): `C_3a >= 1.19102809`
  - Standing asymptotic limit lower bound (Kleinwaks 2026b): `C_3a >= 1.19519192*`
  - Our finite-depth certificate (`object/best_k2_finite_cert.json`): `C_3a >= 1.19298973462186362590382529754753993070825527359705` (`+1.961645e-03` over `1.19102809`)

## Not Claimed
- Does not exceed the asymptotic $N \to \infty$ block-limit lower bound `1.19519192*` (`beats_limit_record_1_19519192: false`); this submission is scoped strictly to Partial Win `p1` (explicit finite-set lower bound strictly beating `1.19102809` by at least `1e-7`).

## Credits
- Problem formulation and benchmark maintenance by Terence Tao (`teorth/optimizationproblems`), Gyarmati–Hennecart–Ruzsa (2003), Boyer–Li (2024), and Kleinwaks (2026a/b).
