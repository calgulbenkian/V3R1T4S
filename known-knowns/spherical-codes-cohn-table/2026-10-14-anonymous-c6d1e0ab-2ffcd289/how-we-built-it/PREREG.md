# Preregistration — Lens 1 (`c-evaluator-optimizer`)

frozen_utc: 2026-10-14T08:11:00Z
lens: c-evaluator-optimizer
target_id: spherical-codes-cohn-table
null_test: not needed because spherical-codes-cohn-table is an exact deterministic continuous-geometry optimization problem verified at 60-digit precision by verify_spherical.py.

## Plan
Build a multi-threaded C (`clang -O3 -march=native -pthread`) `long double` / `__float128` Riemannian log-sum-exp L-BFGS + active-set minimax subgradient/LP polish solver (`spherical_opt.c`), followed by 60-digit Decimal normalization and coordinate export ($\ge 25$ digits per coordinate).
1. Attack unstarred, unlabeled rows (Full Win `solution_claim` for $d \ge 4$, plus `p1` for $d = 3$), including:
   - Unlabeled orthogonal-union rows built from unconverged lower-dimensional codes: `(27, 68)`, `(28, 70)`, `(29, 72)`, `(30, 74)`, `(29, 114)`.
   - Unlabeled near-collision cliff rows: `(7, 140)`, `(4, 112)`, `(6, 124)`, `(7, 116)`, `(6, 551)`, `(3, 666)` (`p1` + Full Win).
2. Attack a batch of $\ge 20$ rows labeled `'needs more optimization'` in dimension $d = 4$ (Partial Win `p2`).
