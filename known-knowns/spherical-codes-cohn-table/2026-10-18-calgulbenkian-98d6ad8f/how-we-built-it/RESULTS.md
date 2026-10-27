# Results for (d=29, N=60)

Contributor text. This is the row for (d=29, N=60) from the search agent's results table, trimmed on 2026-10-27 to
this row. The agent's other rows are not part of this claim and are not shown. The minimal angle is corrected: the
agent's table gave 88.150016797797149449 degrees, and arccos of the c* below is 88.150016722088 degrees.

| (d, N) | `/plain` cos (12 decimals) | Our c* (12 decimals) | Our c* (30 digits) | Improvement | Minimal angle (degrees) | Contacts within 1e-9 | Table attribution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (29, 60) | 0.032282791684 | 0.032282689322 | 0.032282689322403249986273377213 | 1.023616e-07 | 88.150016722088 | 1345 | Ilmari Vahteristo, annealing solver |

The search code is `sc_opt.c` (Riemannian L-BFGS on a log-sum-exp smoothing of the largest inner product, with
basin-hopping kicks). The candidate was normalised and polished to 30 significant digits by a separate 50-digit script,
which is not shipped. The contact count is the agent's and is not checked by `../verify-it-yourself/`.
