# The record we beat (metadata and short excerpts only)

No third-party page is copied here. Every row is one honest GET (curl or equivalent, user agent naming the research client) made on 2026-10-19 (UTC) by the panel's or the contributor's agents; the times, statuses and hashes are copied from their fetch logs, from LITERATURE_ADDENDUM.md and from the panel's novelty report. LITERATURE_SEARCH.md and LITERATURE_ADDENDUM.md in this folder are the search records written for the loop length 30 claim and copied unchanged (see README.md, section Not claimed, for why they were not repeated in full for loop length 32).

## The bar

Alm's published rigorous upper bound for the connective constant of the 4.8^2 lattice is mu < 1.829254 (J. Phys. A 38 (2005), section 5.1.3: "The matrix G(19, 42), with dimension 125 094, gives the bound mu < 1.829 254"). Jensen's 2004 Table 3 lists the same value rounded as 1.82926. Extracted cell used for comparison: 1.829254.

| Source | URL | UTC fetch time | HTTP | sha256 of the fetched bytes |
|---|---|---|---|---|
| Alm 2005 manuscript copy (Internet Archive copy of the link on Alm's page) | https://web.archive.org/web/2010id_/http://www2.math.uu.se/research/pub/Alm3.pdf | 2026-10-19T06:32:57Z | 200 | a3ddda13eac714eaa6c051dd6a6d57412c1f7b34c79fee86491be6736eb6d7aa |
| Alm's page for the paper | https://www2.math.uu.se/~sveralm/boundsabstr.html | 2026-10-19T06:32:08Z | 200 | 042b7c5e111f9d8669b58dc2d4dc9f32d23948903f1e6d3136348f92ce811143 |
| Parviainen thesis, full text (Internet Archive copy) | https://web.archive.org/web/2020id_/http://uu.diva-portal.org/smash/get/diva2:164546/FULLTEXT01.pdf | 2026-10-19T06:37:18Z | 200 | 161459735e1fc657a940bdc1dcea85fb6d3137c475f9b5a15c04d1be5620b5f1 |
| Jensen 2004, arXiv pdf (Table 3) | https://arxiv.org/pdf/cond-mat/0409381 | 2026-10-19T05:38:12Z | 200 | f25e7dc5d6310c8e7450a8ac217818c99df66fecc1309b14945e2cf7ce3db417 |
| Jensen 2004, arXiv abstract page | https://arxiv.org/abs/cond-mat/0409381 | 2026-10-19T05:20:01Z | 200 | 78be1d882fd9d7fae5178b3b59871d23adeec8cf3999730209a22ea4b6a0582a |
| He 2025, arXiv abstract page | https://arxiv.org/abs/2508.01993 | 2026-10-19T05:20:02Z | 200 | 3a3d51f77fc08a5c007ed73b070556b13cea56ea980be401f255b44e211197bc |
| Couronne 2022, arXiv abstract page | https://arxiv.org/abs/2211.16146 | 2026-10-19T05:20:02Z | 200 | 4675536f3843ca111409d86f7448f72dffaf4063b1acc379de2a57bbf1d729b1 |

Fetches made for the loop length 32 panel (novelty skeptic), all HTTP 200 on the first attempt:

| Source | URL | UTC fetch time | HTTP | sha256 of the fetched bytes |
|---|---|---|---|---|
| He 2025, arXiv pdf (searched for 4.8^2 text; none) | https://arxiv.org/pdf/2508.01993 | 2026-10-19T14:34:48Z | 200 | 38bf4354ac1d72b878897bbac04e3b2176c2451780057368b23bc426d7cf8af3 |
| He's software repository page (no 4.8^2 numbers) | https://github.com/qidong-he/weighted_connective_constant | 2026-10-19T14:34:50Z | 200 | 91a99ba323648c1a325ac8acf2adb3b3e68725e5116a15b436560759744cee38 |
| OpenAlex cited-by list for Alm 2005 (12 citing works; none a 4.8^2 bound) | https://api.openalex.org/works?filter=cites:W2040632682 | 2026-10-19T14:35:30Z | 200 | e08c303bea96bbd88f6c00106a39423e6b8b81cac5e96f7d28ad63bfcb1fb0b0 |

The four arXiv API queries of the same panel run (sorted by date; first query 2026-10-19T14:34:34Z, hash 0b4dad9a481a4361f884c338e2b1ee11a5681ee7f067a421a2985b589bea9bf2; the others at 14:34:37Z, 14:34:41Z and 14:34:44Z) found no 4.8^2 bound; their exact queries are in panel/novelty.md.

Other fetches of the k = 30 search (Alm's other pages, a failed Alm3.pdf link with HTTP 404, the DiVA host that did not connect) are listed with their statuses in LITERATURE_ADDENDUM.md.

## Short quotations

Jensen 2004, Table 3 row, as read by the novelty skeptic: "(4.82 )   1.804596   1.80883001(6) [15]   1.82926 [3]". Reference [3]: "Alm S E 2004 in preparation. Courtesy of a private communication from R Parviainen and contained in his PhD Thesis ... Uppsala dissertations in mathematics 34".

Alm 2005, summary table row: "(4.82)  3  3  1.804 596 [9]  1.808 830 [12]  1.829 254".

## This claim against the bar

18108999119/9912056861 = 1.826966831703. Difference from 1.829254: 2.287e-3. Difference from 1.82926: 2.293e-3.

## Limits of the search

No rigorous 4.8^2 upper bound below 1.829254 was found in Crossref, OpenAlex cited-by lists for Jensen 2004 and Alm 2005, arXiv, or the documents above. Google Scholar, MathSciNet and zbMATH were not searched. See README.md, section Not claimed.
