# Covering Design Record: `C(38, 16, 3) <= 25`

## What

Verified that claim/C_38_16_3_b25.json (1,412 bytes, SHA-256 fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643) defines a valid plain covering design for C(38, 16, 3) with b = 25 blocks of size 16 over {1, ..., 38} that covers all C(38, 3) = 8,436 3-element subsets, strictly improving by 1 block upon the standing best known upper bound of 26 blocks on both live coveringrepository.com and the La Jolla Covering Repository Zenodo v1.2 archive (and 27 in the dmgordo/LJCR GitHub snapshot).

In this package, the explicit block list is stored at `object/C_38_16_3_b25.json` (identical bytes, SHA-256 `fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643`, 1,412 bytes, `25` blocks of size `16` covering all `8,436` `3`-subsets of `1..38`).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-fd586040/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: < 1 second.
- **Expected last line**: `ALL CHECKS PASS`

## Compared To

All criterion sources were fetched live on `2026-10-14` (`08:01:00Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T08-01-00Z.json`):

| Source | Cell | Listed Upper Bound | Our Block Count `b` | Gain | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|
| `coveringrepository.com` (`m=t=3`) | `C(38, 16, 3)` | `26` | **`25`** | **`-1`** | `https://coveringrepository.com/systems.aspx` | `2026-10-14T08:01:00Z` |
| La Jolla / Gordon (`Zenodo 10.5281/zenodo.10779736` v1.2) | `C(38, 16, 3)` | `26` | **`25`** | **`-1`** | `https://zenodo.org/api/records/19735294/files/coverdata.json/content` | `2026-10-14T08:01:00Z` |
| `dmgordo/LJCR` GitHub (`coverdata.json`) | `C(38, 16, 3)` | `27` | **`25`** | **`-2`** | `https://raw.githubusercontent.com/dmgordo/LJCR/main/coverings/coverdata.json` | `2026-10-14T08:01:00Z` |
| `thebrockchain/covering-designs` | `C(38, 16, 3)` | unlisted | **`25`** | — | `https://raw.githubusercontent.com/thebrockchain/covering-designs/main/README.md` | `2026-10-14T08:01:00Z` |
| `TROPHY_CASE.md` | `C(38, 16, 3)` | unlisted | **`25`** | — | `TROPHY_CASE.md` | `2026-10-14T08:01:00Z` |

## Not Claimed

- Scope: Constructive upper bound `C(38, 16, 3) <= 25` (Schönheim lower bound `L(38, 16, 3) = 19`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive `8,436`-subset checker shipped here; not peer reviewed.

## Credits

- **D. M. Gordon**, *La Jolla Covering Repository* (`https://dmgordon.org/covering-designs/`, Zenodo `10.5281/zenodo.10779736` v1.2).
- **G. Acerbi**, *Covering Repository* (`https://coveringrepository.com/systems.aspx`).
- Contributor credit: `anonymous-c6d1e0ab`.
