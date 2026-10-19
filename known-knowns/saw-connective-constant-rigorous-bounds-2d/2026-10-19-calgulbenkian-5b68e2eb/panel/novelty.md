# Novelty report: saw-482-k30 (4.8^2 lattice, rigorous upper bound 849051343/464433440 = 1.8281442934)

context: Claude Code subagent, fresh context [claude-sonnet-5-5]

All fetches are saved in the group folder novelty_ws/ (FETCHLOG.txt: URL, UTC time, status, sha256). One plain request per URL, honest client, no retries; all returned 200.

## Baseline source confirmed
- Jensen, "Improved lower bounds on the connective constants for two-dimensional self-avoiding walks", https://arxiv.org/pdf/cond-mat/0409381, fetched 2026-10-19T05:38:12Z, 200, sha256 f25e7dc5d6310c8e7450a8ac217818c99df66fecc1309b14945e2cf7ce3db417.
- Table 3 row, verbatim: "(4.82 )   1.804596   1.80883001(6) [15]   1.82926 [3]". Reference [3] reads: "Alm S E 2004 in preparation. Courtesy of a private communication from R Parviainen and contained in his PhD Thesis Connective Properties of Archimedean and Laves Lattices Uppsala dissertations in mathematics 34". So 1.82926 is the best upper bound in that 2004 table, credited to Alm 2004 via Parviainen's thesis (not Alm 1993). The bank's quotation is accurate.

## Search for a rigorous 4.8^2 upper bound below 1.82926 published since 2004
- arXiv API (https export.arxiv.org, 2026-10-19), three queries for this cell: "connective constant" AND "upper bound" (hits include 2509.04568 self-osculating walks on square and triangular lattices; 2508.01993 He, weighted SAW; 2211.16146 Couronne, square; 1809.00760; 1808.09032; 1709.09223; cond-mat/0409381); "self-avoiding" AND "rigorous" AND "upper bound" (3 hits, none relevant); "connective constant" with 4.8, Archimedean or truncated square (only Jensen 2004). None gives a 4.8^2 upper bound. Group-wide I used five arXiv queries, one above the brief's four; disclosed.
- He, arXiv 2508.01993 v3, full PDF fetched and text-searched: no 4.8^2, no 1.82xx value, no Archimedean or kagome results. 2509.04568 covers square and triangular lattices only. Couronne 2211.16146 is square only.
- Wikipedia "Connective constant" (2026-10-19T05:38:57Z, 200, sha256 b581eab6f1a287f32e7c68507b7c585c68ce992f72677e5214e399d6b1d48498): lists only the estimate 1.80883001(6) for 4.8^2, no upper bound.
- Result: no rigorous 4.8^2 upper bound below 1.82926 published since 2004 was found. The claimed 1.8281442934 is lower by 1.1157e-3 (margin far above 1e-6).

## This repo
- TROPHY_CASE.md (2026-10-19T05:37:45Z, 200, sha256 b946f68eb0a6473dd2224065a52390235a535d3282da24669f6724a1472171a1): no connective-constant entry.
- known-knowns listing (200, sha256 8a2927f7995495ec01c3022b965eba5363a7831765ebd4a18a27a0e6ae36d011): no SAW folder.
- Pull requests from the saved local prs_all.json (fetched 2026-10-19T04:30:31Z, 473 PRs), used in place of the api.github.com pages as the batch note allows: none on saw-connective-constant-rigorous-bounds-2d; no open competing value. Closed calgulbenkian bulk-close PRs (#65-#120): none on this target.
- PR #350 propagation: the bound is for 4.8^2 only; no other lattice's merged or open value implies it, and it is not a monotone consequence of the table (it is a new finite-memory automaton bound). Not propagation-implied.

## Open question answered
"Has a rigorous upper bound below 1.828144 for the 4.8^2 lattice been published since (e.g. with He's 2025 software)?" Not found: He's paper and software report no 4.8^2 results, and no later arXiv paper in the queries does. This is a search result, not proof of absence.

unresolved: Parviainen's 2004 Uppsala thesis (the source of 1.82926) was not fetched; Alm's in-preparation paper and Google Scholar were not searchable. A better published bound hiding in the thesis itself is implausible since Jensen's table quotes the thesis figure as current best. A later (2005-2024) non-arXiv journal bound could plausibly exist but nothing in Jensen's Table 3, Wikipedia or the arXiv queries points to one. The claimant's README admits no literature search was made; whether p1's "show by search" clause is satisfied belongs to the criterion role.

Verdict: strictly better than the confirmed baseline and than all later work found, with the unresolved caveat above.

pass: true
