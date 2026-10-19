# Run it yourself

In a fresh shell, from this package folder:

```sh
sh verify-it-yourself/run_checks.sh
```

Requirements: python3 3.8 or later, standard library only. No network.

Time: under one second to a few seconds.

Expected last line: `ALL CHECKS PASS`. Real output of an earlier run is in verify-it-yourself/RECEIPTS.md.

## Rebuilding the object

The object was produced by the contributor's C programs in how-we-built-it/. No command lines were recorded in the snapshot (see how-we-built-it/README.md). The derivation of why the ratio bounds the constant is in object/DERIVATION.md.
