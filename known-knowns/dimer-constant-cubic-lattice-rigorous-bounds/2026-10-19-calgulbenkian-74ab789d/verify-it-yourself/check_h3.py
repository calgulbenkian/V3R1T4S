#!/usr/bin/env python3
"""Monomer-dimer entropy h3 upper bound at (3,3): standard library only, a few seconds.

Builds the full 512 x 512 monomer-dimer layer matrix from the definition
  T[U,W] = sum over S subset of (V minus U) of per A[S,W]       (A[u,v] = 1 iff v-u in {(0,0),(1,0),(0,1)} on Z/3 x Z/3)
expands the shipped vector (44 orbit values) to all 512 states and computes max_U (T x)_U / x_U in exact integers.
"""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import cwcheck as cw
from decimal import Decimal, getcontext

claim = os.path.dirname(here)
ok_all = True


def report(name, ok, extra=''):
    global ok_all
    ok_all = ok_all and ok
    print('%s %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)


report('trace identity: tr(TMD^l) = number of ALL matchings of the quotient graph, (2,2,4) (3,2,4) (2,2,6)',
       all([cw.cmd_trace(d, l) for d, l in (([2, 2], 4), ([3, 2], 4), ([2, 2], 6))]))
report('property C (dimer and monomer-dimer) on the full (3,3) matrices', cw.cmd_propc([3, 3]))
res = cw.cmd_mdcert([3, 3], os.path.join(claim, 'object', 'cert_md_h3_33.txt'))
if res is None:
    report('certificate', False)
else:
    num, den, b = res
    report('exact ratio 731051554747087/618837374495', num * 618837374495 == 731051554747087 * den)
    getcontext().prec = 40
    up7 = (b * 10 ** 7).to_integral_value(rounding='ROUND_CEILING') / 10 ** 7
    report('h3 <= %s (unrounded %s) is below FKLM 0.7862023450 by %s (needed: at least 1e-6)' % (up7, str(b)[:14], Decimal('0.7862023450') - up7),
           up7 == Decimal('0.7860441') and Decimal('0.7862023450') - up7 >= Decimal('0.000001'))
print('ALL CHECKS PASS' if ok_all else 'SOME CHECK FAILED')
sys.exit(0 if ok_all else 1)
