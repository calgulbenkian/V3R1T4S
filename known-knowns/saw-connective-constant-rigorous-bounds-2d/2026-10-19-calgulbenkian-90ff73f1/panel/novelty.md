# Novelty report: saw-482-k32 (4.8^2 lattice, rigorous upper bound 18108999119/9912056861 = 1.826966831703)

context: Claude Code subagent, fresh context [claude-sonnet-5-5]

Claim folder verified from inside claim/ against ../claim.SHA256SUMS: every line OK. Fetches are logged in nov_ws/FETCHLOG.txt (UTC time, HTTP status, sha256; all 200 on first attempt, one plain request per URL, honest client). The k = 30 panel's novelty report was read (its nov_ws folder does not exist, so only the report was available); I re-fetched rather than relying on it.

## Baseline
- Jensen 2004 Table 3 (4.8^2): lower 1.804596, estimate 1.80883001(6), upper 1.82926 [3] (Alm/Parviainen private communication). Confirmed by the k = 30 panel's verbatim quote from arXiv cond-mat/0409381 and by the claim's own table-record/LITERATURE_ADDENDUM.md, which quotes Alm, J. Phys. A 38 (2005) 2055, section 5.1.3: "The matrix G(19, 42), with dimension 125 094, gives the bound mu < 1.829 254". The best published rigorous upper bound is therefore 1.829254 (Alm 2005; the 1.82926 is its rounding). I did not re-read Alm 2005 itself (paywalled); I rely on the addendum's Internet Archive extraction and Jensen's table, which agree.
- Claimed 1.826966831703 is lower than 1.829254 by 2.287e-3 (and than 1.82926 by 2.293e-3). Margin far above 1e-6.

## Literature re-run (2026-10-19, arXiv API over https, 4 queries; results sorted by date)
- q1 "connective constant" AND (Archimedean OR truncated square OR 4.8 OR octagon): 1 hit, Jensen 2004 (cond-mat/0409381).
- q2 "connective constant" AND "upper bound": 7 hits: 2509.04568 (restricted walks, surfaces; read: square/triangular-type growth constants, no 4.8^2 text hits), 2508.01993 He, 2211.16146 Couronne (square only), 1809.00760, 1808.09032, 1709.09223, cond-mat/0409381. None gives a 4.8^2 bound.
- q3 self-avoiding AND (Alm OR Ponitz OR Tittmann OR Parviainen): 3 hits (2509.04568, 2508.01993, cond-mat/0410241 on the 3.12 lattice). None on 4.8^2.
- q4 self-avoiding walk AND (Laves OR honeycomb OR kagome OR hexagonal) AND bound: 9 hits, all hexagonal/other-lattice or off-topic; none 4.8^2.
- He, arXiv 2508.01993 v3, full PDF fetched and text-searched: lattices treated are square, triangular, hexagonal (2D) and simple, BCC, FCC cubic (3D). No 4.8^2, truncated-square, Archimedean or 1.82 figure appears. His software repository page (github.com/qidong-he/weighted_connective_constant, fetched; the HTML is page chrome, no table of results) gives no 4.8^2 numbers; the paper reports none. Ponitz-Tittmann (2000) is the square-lattice automaton predecessor; no 4.8^2 result is known from it.
- OpenAlex cited-by list for Alm 2005 (W2040632682, 12 citing works, fetched): the most recent are a 2024 comb-polymer growth-rate paper, a 2022 weighted-graph spanning-tree paper, and 2014-2016 spatial-mixing / regular-graph connective-constant papers. None is a 4.8^2 upper bound; the regular-graph bounds are general and far weaker than 1.83.
- Result: no rigorous 4.8^2 upper bound below 1.829254 found, so none below 1.826967. This is a search result, not proof of absence.

## This repo
- prs_all.json (473 PRs, fetched 2026-10-19T04:30:31Z, used in place of the api.github.com pulls pages as the batch note allows): the only PR on the target saw-connective-constant-rigorous-bounds-2d is #534 (calgulbenkian, open), the author's own k = 30 filing, which this claim is meant to replace; it is not a competing value. No other PR on SAW, connective constants or Archimedean lattices.
- Read-only `gh pr list --repo elder-plinius/V3R1T4S --state all --search "4.8"` (2026-10-19T14:34Z, once): one result, #534. So no PR filed after the snapshot on this target.
- TROPHY_CASE.md (200, sha256 b946f68e...71a1): no connective-constant entry. known-knowns listing (200, sha256 8a2927f7...36d011): 20 folders, no SAW or connective-constant folder.
- Closed calgulbenkian bulk-close PRs (#65-#120): none concerns this target.

## PR #350 propagation test
- Nothing merged or open gives a 4.8^2 value that implies this one. Bounds on other lattices (square 2.662342, triangular, kagome) do not constrain the 4.8^2 constant downward; the only monotone relation is subgraph inclusion (mu of a subgraph is at most mu of a supergraph), and every supergraph of 4.8^2 has a larger constant, so no table value yields 1.8270.
- Relation to #534: the k = 32 value is the same construction at a larger loop length, replacing the k = 30 value in the same PR. It is not a separate record from #534; the record would be this value in place of that one. It follows from no table value; it comes from a new automaton run.

## Open questions concerning novelty, answered
- "Has any rigorous 4.8^2 upper bound below 1.826967 been published since?" Not found, by the searches above (arXiv, OpenAlex cited-by for Alm 2005, He's paper and code page, this repo). Caveat: search only.
- Baseline attribution: 1.82926 is Jensen 2004 Table 3 quoting Alm/Parviainen; Alm 2005 gives 1.829254. Both are above the claim by more than 2.28e-3. Confirmed by quotation in the addendum and by the k = 30 panel's quote of Jensen.
- The k = 34 pocket variant (1.825523) is not claimed; nothing to judge. Whether p1's "claimant must show by search" clause is met belongs to criterion; the folder carries the search records (LITERATURE_SEARCH.md and LITERATURE_ADDENDUM.md, made for k = 30) and, as the CLAIM says, they were not repeated for k = 32. This report repeats the search for the later window and found nothing new.

unresolved: Alm 2005 full text and Parviainen's thesis were not read by me (the addendum reports reading Internet Archive copies); Google Scholar not searchable. A non-arXiv bound hiding in a journal could plausibly exist but nothing in the citing-works list, Jensen's table, He's paper or the repo points to one.

Verdict: strictly better than the confirmed baseline 1.829254 (and 1.82926) by about 2.29e-3 and than all later work found; not propagation-implied; not a competing value to #534.

pass: true
