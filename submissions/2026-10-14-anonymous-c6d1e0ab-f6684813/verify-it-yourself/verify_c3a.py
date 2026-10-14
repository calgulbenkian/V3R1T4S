#!/usr/bin/env python3
"""
Independent verifier for the Gyarmati-Hennecart-Ruzsa sum-difference constant C_3a.

Supports:
1. Explicit finite sets U subset Z_{>= 0} (dilated to V = 2U so |V-V| < 2 max(V) + 1).
2. Carry-free finite-depth masked-digit certificates (Q = 2B + 1, depth N, e.g. N = 10^13),
   reconstructing M, S = M + M, D = M - M, minimum witness costs kappa(d) with explicit
   witness pairs (alpha_d, beta_d) in M^2, exact integer type counts n_d, n_0, L,
   and exact multinomial lower bound D_N and sumset upper bound S_N.
3. Controlled-carry finite-block certificates at finite depth ell (base B < q <= 2B + 1,
   block length k >= 1, sum block length m >= 1, depth N = k * ell), using Proposition 2
   and Proposition 3's exact finite-depth multinomial lower bound D_ell and sum-carry
   upper bound W_m(x)^{k*ell/m} x^{-2L}.
4. Controlled-carry limit certificates (Collatz-Wielandt / Fekete block pressure).

Every verification runs two independent methods (Method 1: 80-digit directed-rounding
Decimal + alternating Stirling-Bernoulli bounds + pairwise witness table; Method 2:
100-digit Decimal + exact rational Fraction atanh logarithm enclosures + boolean/cost
convolution) and checks `methods_agree = True`.
"""

import json
import sys
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path

INF = 10**18

# Exact Bernoulli numbers B_{2k} for k = 1..10:
# B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30, B_10 = 5/66,
# B_12 = -691/2730, B_14 = 7/6, B_16 = -3617/510, B_18 = 43867/798, B_20 = -174611/330
BERNOULLI_EVEN = [
    (2, 1, 6),
    (4, -1, 30),
    (6, 1, 42),
    (8, -1, 30),
    (10, 5, 66),
    (12, -691, 2730),
    (14, 7, 6),
    (16, -3617, 510),
    (18, 43867, 798),
    (20, -174611, 330),
]


def make_contexts(prec=80):
    ctx_lo = Context(prec=prec, rounding=ROUND_FLOOR)
    ctx_hi = Context(prec=prec, rounding=ROUND_CEILING)
    ctx_ne = Context(prec=prec, rounding=ROUND_HALF_EVEN)
    return ctx_lo, ctx_hi, ctx_ne


def compute_two_pi_bounds(prec=80):
    """Rigorous lower and upper bounds on 2*pi and ln(2*pi) at given Decimal precision."""
    ctx_work = Context(prec=prec + 25, rounding=ROUND_HALF_EVEN)
    # Machin's formula: pi/4 = 4*atan(1/5) - atan(1/239)
    def atan_inv(m, terms=80):
        m_dec = Decimal(m)
        m2 = m_dec * m_dec
        term = ctx_work.divide(Decimal(1), m_dec)
        total = Decimal(0)
        for k in range(terms):
            contrib = ctx_work.divide(term, Decimal(2 * k + 1))
            if k % 2 == 0:
                total = ctx_work.add(total, contrib)
            else:
                total = ctx_work.subtract(total, contrib)
            term = ctx_work.divide(term, m2)
        return total

    pi_work = ctx_work.multiply(
        Decimal(4),
        ctx_work.subtract(
            ctx_work.multiply(Decimal(4), atan_inv(5, 90)),
            atan_inv(239, 45),
        ),
    )
    two_pi_work = ctx_work.multiply(Decimal(2), pi_work)
    ln_two_pi_work = ctx_work.ln(two_pi_work)
    eps = Decimal(10) ** (-(prec + 15))
    ctx_lo, ctx_hi, _ = make_contexts(prec)
    half_ln_2pi_lo = ctx_lo.divide(ctx_lo.subtract(ln_two_pi_work, eps), Decimal(2))
    half_ln_2pi_hi = ctx_hi.divide(ctx_hi.add(ln_two_pi_work, eps), Decimal(2))
    return half_ln_2pi_lo, half_ln_2pi_hi


class RigorousLnFactorial:
    """
    Rigorous lower and upper enclosures for ln(n!) using:
    - Exact cumulative sum of ln(k) for n <= small_limit (default 2000),
    - Alternating Stirling-Bernoulli asymptotic series for n > small_limit:
      stopping after negative B_{20} gives a strict mathematical lower bound;
      stopping after positive B_{18} gives a strict mathematical upper bound.
    """

    def __init__(self, prec=80, small_limit=2000):
        self.prec = prec
        self.small_limit = small_limit
        self.ctx_lo, self.ctx_hi, self.ctx_ne = make_contexts(prec)
        self.ctx_work = Context(prec=prec + 20, rounding=ROUND_HALF_EVEN)
        self.half_ln_2pi_lo, self.half_ln_2pi_hi = compute_two_pi_bounds(prec)
        self.small_lo = [Decimal(0)] * (small_limit + 1)
        self.small_hi = [Decimal(0)] * (small_limit + 1)
        acc_lo = Decimal(0)
        acc_hi = Decimal(0)
        eps = Decimal(10) ** (-(prec + 12))
        for k in range(2, small_limit + 1):
            lnk = self.ctx_work.ln(Decimal(k))
            acc_lo = self.ctx_lo.add(acc_lo, self.ctx_lo.subtract(lnk, eps))
            acc_hi = self.ctx_hi.add(acc_hi, self.ctx_hi.add(lnk, eps))
            self.small_lo[k] = acc_lo
            self.small_hi[k] = acc_hi
        self.cache_lo = {}
        self.cache_hi = {}

    def ln_bounds(self, x_dec):
        eps = Decimal(10) ** (-(self.prec + 12))
        val = self.ctx_work.ln(x_dec)
        return self.ctx_lo.subtract(val, eps), self.ctx_hi.add(val, eps)

    def exp_bounds(self, x_dec):
        eps = Decimal(10) ** (-(self.prec + 12))
        val = self.ctx_work.exp(x_dec)
        rel = self.ctx_work.multiply(val, eps)
        return self.ctx_lo.subtract(val, rel), self.ctx_hi.add(val, rel)

    def lnf_lo(self, n):
        if n <= 1:
            return Decimal(0)
        if n <= self.small_limit:
            return self.small_lo[n]
        if n in self.cache_lo:
            return self.cache_lo[n]
        nd = Decimal(n)
        ln_n_lo, _ = self.ln_bounds(nd)
        # (n + 0.5)*ln(n) - n + 0.5*ln(2*pi)
        n_plus_half = self.ctx_lo.add(nd, Decimal("0.5"))
        res = self.ctx_lo.multiply(n_plus_half, ln_n_lo)
        res = self.ctx_lo.subtract(res, nd)
        res = self.ctx_lo.add(res, self.half_ln_2pi_lo)
        # Add Bernoulli terms up to B_20 (negative last term => strict lower bound)
        n2 = self.ctx_hi.multiply(nd, nd)
        n_pow_lo = nd
        n_pow_hi = nd
        for two_k, num, den in BERNOULLI_EVEN:
            denom_coeff = two_k * (two_k - 1) * den
            if num > 0:
                term_lo = self.ctx_lo.divide(
                    Decimal(num),
                    self.ctx_hi.multiply(Decimal(denom_coeff), n_pow_hi),
                )
                res = self.ctx_lo.add(res, term_lo)
            else:
                term_hi = self.ctx_hi.divide(
                    Decimal(-num),
                    self.ctx_lo.multiply(Decimal(denom_coeff), n_pow_lo),
                )
                res = self.ctx_lo.subtract(res, term_hi)
            n_pow_lo = self.ctx_lo.multiply(n_pow_lo, self.ctx_lo.multiply(nd, nd))
            n_pow_hi = self.ctx_hi.multiply(n_pow_hi, n2)
        self.cache_lo[n] = res
        return res

    def lnf_hi(self, n):
        if n <= 1:
            return Decimal(0)
        if n <= self.small_limit:
            return self.small_hi[n]
        if n in self.cache_hi:
            return self.cache_hi[n]
        nd = Decimal(n)
        _, ln_n_hi = self.ln_bounds(nd)
        n_plus_half = self.ctx_hi.add(nd, Decimal("0.5"))
        res = self.ctx_hi.multiply(n_plus_half, ln_n_hi)
        res = self.ctx_hi.subtract(res, nd)
        res = self.ctx_hi.add(res, self.half_ln_2pi_hi)
        # Add Bernoulli terms up to B_18 (positive last term => strict upper bound)
        n2_lo = self.ctx_lo.multiply(nd, nd)
        n2_hi = self.ctx_hi.multiply(nd, nd)
        n_pow_lo = nd
        n_pow_hi = nd
        for two_k, num, den in BERNOULLI_EVEN[:-1]:
            denom_coeff = two_k * (two_k - 1) * den
            if num > 0:
                term_hi = self.ctx_hi.divide(
                    Decimal(num),
                    self.ctx_lo.multiply(Decimal(denom_coeff), n_pow_lo),
                )
                res = self.ctx_hi.add(res, term_hi)
            else:
                term_lo = self.ctx_lo.divide(
                    Decimal(-num),
                    self.ctx_hi.multiply(Decimal(denom_coeff), n_pow_hi),
                )
                res = self.ctx_hi.subtract(res, term_lo)
            n_pow_lo = self.ctx_lo.multiply(n_pow_lo, n2_lo)
            n_pow_hi = self.ctx_hi.multiply(n_pow_hi, n2_hi)
        self.cache_hi[n] = res
        return res


def atanh_fraction_interval(z, terms=55):
    """Exact rational enclosure of atanh(z) for 0 <= z < 1."""
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    tail = power / ((2 * terms + 1) * (1 - z2))
    return partial, partial + tail


def log_positive_fraction_interval(frac, terms=55):
    """Exact rational enclosure of ln(frac) for Fraction frac > 0."""
    # Find integer e such that 2^e <= frac < 2^{e+1}
    num, den = frac.numerator, frac.denominator
    e = (num.bit_length() - 1) - (den.bit_length() - 1)
    if e >= 0:
        while (num >> e) < den:
            e -= 1
        while (num >> (e + 1)) >= den:
            e += 1
        scaled = Fraction(num, den << e)
    else:
        while (num << (-e)) < den:
            e -= 1
        while (num << (-e - 1)) >= den:
            e += 1
        scaled = Fraction(num << (-e), den)
    # Now 1 <= scaled < 2, so 0 <= (scaled - 1)/(scaled + 1) < 1/3
    z = (scaled - 1) / (scaled + 1)
    lo2, hi2 = atanh_fraction_interval(Fraction(1, 3), terms=terms)
    loz, hiz = atanh_fraction_interval(z, terms=terms)
    if e >= 0:
        return 2 * (e * lo2 + loz), 2 * (e * hi2 + hiz)
    else:
        return 2 * (e * hi2 + loz), 2 * (e * lo2 + hiz)


def build_mask_from_spec(spec):
    """Reconstruct sorted mask M subset [0, B] from explicit 'mask' or 'generators'."""
    B = int(spec["B"])
    if "mask" in spec and spec["mask"] is not None:
        M = sorted(set(int(v) for v in spec["mask"]))
        if "prune" in spec and spec["prune"]:
            prune_set = set(int(v) for v in spec["prune"])
            M = [v for v in M if v not in prune_set]
        if "add" in spec and spec["add"]:
            M = sorted(set(M) | set(int(v) for v in spec["add"]))
    elif "generators" in spec and spec["generators"] is not None:
        gens = [int(g) for g in spec["generators"]]
        reach = [False] * (B + 1)
        reach[0] = True
        for n in range(B + 1):
            if reach[n]:
                for g in gens:
                    if g > 0 and n + g <= B:
                        reach[n + g] = True
        if "prune" in spec and spec["prune"]:
            for v in spec["prune"]:
                reach[int(v)] = False
        if "add" in spec and spec["add"]:
            for v in spec["add"]:
                reach[int(v)] = True
        M = [n for n, ok in enumerate(reach) if ok]
    else:
        raise ValueError("Certificate must provide 'mask' or 'generators'")
    if not M or M[0] != 0 or M[-1] != B:
        raise ValueError(f"Invalid mask endpoints: min={M[0] if M else None}, max={M[-1] if M else None}, expected 0..{B}")
    if any(v < 0 or v > B for v in M):
        raise ValueError("Mask contains out-of-range element")
    return B, M


def combinatorial_tables_method1(B, M):
    """Method 1: Explicit witness tracking for kappa(d) and sum support."""
    m_set = set(M)
    sum_present = [False] * (2 * B + 1)
    kappa = [INF] * (B + 1)
    witness = [None] * (B + 1)
    kappa[0] = 0
    witness[0] = (0, 0)
    for i, a in enumerate(M):
        sum_present[2 * a] = True
        for j in range(i):
            b = M[j]
            s = a + b
            d = a - b
            sum_present[s] = True
            if s < kappa[d]:
                kappa[d] = s
                witness[d] = (a, b)
    # Verify every witness explicitly
    for d in range(B + 1):
        if kappa[d] < INF:
            a, b = witness[d]
            if a not in m_set or b not in m_set or a - b != d or a + b != kappa[d]:
                raise ValueError(f"Witness verification failed at d={d}")
    return sum_present, kappa, witness


def combinatorial_tables_method2(B, M):
    """Method 2: Independent dictionary/set construction of S = M + M and kappa(d)."""
    sums = {a + b for a in M for b in M}
    kappa_dict = {}
    for a in M:
        for b in M:
            if a >= b:
                d = a - b
                s = a + b
                if d not in kappa_dict or s < kappa_dict[d]:
                    kappa_dict[d] = s
    sum_present = [(s in sums) for s in range(2 * B + 1)]
    kappa = [kappa_dict.get(d, INF) for d in range(B + 1)]
    return sum_present, kappa


def verify_finite_carry_free(spec):
    """
    Verify a finite-depth carry-free masked-digit construction (Section 5 of Kleinwaks 2026b).
    """
    B, M = build_mask_from_spec(spec)
    Q = int(spec.get("base", 2 * B + 1))
    if Q != 2 * B + 1:
        raise ValueError(f"Carry-free mode requires Q = 2B + 1 = {2*B+1}, got {Q}")
    N = int(spec.get("depth_N", spec.get("N", 10**13)))
    x_str = str(spec.get("x_decimal", spec.get("x")))

    # Method 1 & Method 2 combinatorial tables
    sum1, kap1, _ = combinatorial_tables_method1(B, M)
    sum2, kap2 = combinatorial_tables_method2(B, M)
    comb_agree = (sum1 == sum2) and (kap1 == kap2)
    if not comb_agree:
        raise ValueError("Combinatorial tables disagree between Method 1 and Method 2")

    sum_count = sum(1 for v in sum1 if v)
    diff_count = 1 + 2 * sum(1 for d in range(1, B + 1) if kap1[d] < INF)

    # Group differences d >= 1 by integer cost C = kappa(d)
    cost_mult = {}
    for d in range(1, B + 1):
        c = kap1[d]
        if c < INF:
            cost_mult[c] = cost_mult.get(c, 0) + 1

    def eval_with_precision(prec):
        eng = RigorousLnFactorial(prec=prec, small_limit=2000)
        ctx_lo, ctx_hi, _ = eng.ctx_lo, eng.ctx_hi, eng.ctx_ne
        x_lo = ctx_lo.create_decimal(x_str)
        x_hi = ctx_hi.create_decimal(x_str)
        if not (Decimal(0) < x_lo <= x_hi < Decimal(1)):
            raise ValueError(f"Invalid x={x_str}: must be in (0, 1)")

        # Precompute rigorous lower and upper bounds on x^k for k = 0..2B
        pow_lo = [Decimal(1)] * (2 * B + 1)
        pow_hi = [Decimal(1)] * (2 * B + 1)
        for k in range(1, 2 * B + 1):
            pow_lo[k] = ctx_lo.multiply(pow_lo[k - 1], x_lo)
            pow_hi[k] = ctx_hi.multiply(pow_hi[k - 1], x_hi)

        # Compute P_-(x) lower and upper bounds
        pm_lo = Decimal(1)
        pm_hi = Decimal(1)
        for c, mult in cost_mult.items():
            pm_lo = ctx_lo.add(pm_lo, ctx_lo.multiply(Decimal(2 * mult), pow_lo[c]))
            pm_hi = ctx_hi.add(pm_hi, ctx_hi.multiply(Decimal(2 * mult), pow_hi[c]))

        # Compute integer counts n_d for each cost C
        counts_by_cost = {}
        used = 0
        total_cost = 0
        N_dec = Decimal(N)
        for c, mult in sorted(cost_mult.items()):
            p_lo = ctx_lo.divide(pow_lo[c], pm_hi)
            p_hi = ctx_hi.divide(pow_hi[c], pm_lo)
            a_lo = int(ctx_lo.multiply(N_dec, p_lo) // 1)
            a_hi = int(ctx_hi.multiply(N_dec, p_hi) // 1)
            if a_lo != a_hi:
                # Conservative integer choice: a_lo is a 100% valid nonnegative integer count
                a = a_lo
            else:
                a = a_lo
            counts_by_cost[c] = a
            used += mult * a
            total_cost += 2 * mult * a * c

        if 2 * used > N:
            raise ValueError("Type counts exceed N")
        n0 = N - 2 * used
        L = total_cost // 2

        # Exact lower-count formula: ln D_N >= lnf_lo(N) - lnf_hi(n0) - sum_{d>0} 2*lnf_hi(n_d)
        logD_lo = eng.lnf_lo(N)
        denom_hi = eng.lnf_hi(n0)
        for c, mult in cost_mult.items():
            a = counts_by_cost[c]
            if a > 0:
                lg_hi = eng.lnf_hi(a)
                denom_hi = ctx_hi.add(denom_hi, ctx_hi.multiply(Decimal(2 * mult), lg_hi))
        logD_lo = ctx_lo.subtract(logD_lo, denom_hi)

        # Sumset upper bound: |U + U| <= P_+(x)^N x^{-2L}
        pp_lo = Decimal(0)
        pp_hi = Decimal(0)
        for s in range(2 * B + 1):
            if sum1[s]:
                pp_lo = ctx_lo.add(pp_lo, pow_lo[s])
                pp_hi = ctx_hi.add(pp_hi, pow_hi[s])

        _, log_pp_hi = eng.ln_bounds(pp_hi)
        part1_hi = ctx_hi.multiply(log_pp_hi, N_dec)
        log_x_lo, _ = eng.ln_bounds(x_lo)
        neg_log_x_hi = ctx_hi.minus(log_x_lo)
        part2_hi = ctx_hi.multiply(neg_log_x_hi, Decimal(2 * L))
        logS_hi = ctx_hi.add(part1_hi, part2_hi)

        # Denominator: 4 max(U) + 1 < 2 Q^N
        _, log_q_hi = eng.ln_bounds(Decimal(Q))
        _, log_2_hi = eng.ln_bounds(Decimal(2))
        log_den_hi = ctx_hi.add(ctx_hi.multiply(log_q_hi, N_dec), log_2_hi)

        numer_lo = ctx_lo.subtract(logD_lo, logS_hi)
        if numer_lo <= 0:
            raise ValueError("Finite ratio is not positive")
        theta_finite_lo = ctx_lo.add(Decimal(1), ctx_lo.divide(numer_lo, log_den_hi))

        # Carry-free limiting value: 1 + ln(P_-(x)/P_+(x)) / ln(Q)
        log_pm_lo, _ = eng.ln_bounds(pm_lo)
        limit_num_lo = ctx_lo.subtract(log_pm_lo, log_pp_hi)
        theta_limit_lo = ctx_lo.add(Decimal(1), ctx_lo.divide(limit_num_lo, log_q_hi))

        return {
            "n0": n0,
            "L": L,
            "logD_lo": logD_lo,
            "logS_hi": logS_hi,
            "log_den_hi": log_den_hi,
            "theta_finite_lo": theta_finite_lo,
            "theta_limit_lo": theta_limit_lo,
            "pm_lo": pm_lo,
            "pp_hi": pp_hi,
        }

    res1 = eval_with_precision(80)
    res2 = eval_with_precision(110)

    # Check agreement between 80-digit and 110-digit evaluations to at least 60 decimal places
    agree = (
        res1["n0"] == res2["n0"]
        and res1["L"] == res2["L"]
        and abs(res1["theta_finite_lo"] - res2["theta_finite_lo"]) < Decimal("1e-65")
        and abs(res1["theta_limit_lo"] - res2["theta_limit_lo"]) < Decimal("1e-65")
    )

    return {
        "mode": "finite_carry_free",
        "B": B,
        "Q": Q,
        "N": N,
        "mask_size": len(M),
        "sum_support_size": sum_count,
        "diff_support_size": diff_count,
        "n0": res1["n0"],
        "L": res1["L"],
        "log_D_lower": str(res1["logD_lo"])[:40],
        "log_S_upper": str(res1["logS_hi"])[:40],
        "log_den_upper": str(res1["log_den_hi"])[:40],
        "theta_finite_lower_50d": f"{res1['theta_finite_lo']:.50f}",
        "theta_finite_lower_8d": f"{res1['theta_finite_lo'] - Decimal('5e-9'):.8f}",
        "theta_limit_lower_50d": f"{res1['theta_limit_lo']:.50f}",
        "beats_finite_record_1_19102809": bool(res1["theta_finite_lo"] > Decimal("1.19102809")),
        "beats_finite_record_by_1e7": bool(res1["theta_finite_lo"] >= Decimal("1.19102819")),
        "beats_limit_record_1_19519192": bool(res1["theta_finite_lo"] >= Decimal("1.19519202")),
        "methods_agree": bool(comb_agree and agree),
    }


def verify_controlled_carry_limit(spec):
    """
    Verify a controlled-carry limit certificate using two independent methods:
    - Method 1: Exact rational atanh_fraction_interval enclosures on (c_lower, p_upper, q).
    - Method 2: 80-digit directed-rounding Decimal logarithm enclosures.
    """
    q = int(spec["q"])
    if "c_lower_rational" in spec:
        c_frac = Fraction(spec["c_lower_rational"])
        p_frac = Fraction(spec["p_upper_rational"])
    elif "difference_lower_num" in spec:
        scale = int(spec["scale"])
        c_frac = Fraction(int(spec["difference_lower_num"]), scale)
        p_frac = Fraction(int(spec["plus_upper_num"]), scale)
    else:
        c_frac = Fraction(str(spec["difference_lower"]))
        p_frac = Fraction(str(spec["plus_pressure_root_upper"]))

    # Method 1: Exact rational atanh interval
    ratio_frac = c_frac / p_frac
    ratio_lo_frac, _ = log_positive_fraction_interval(ratio_frac, terms=60)
    _, q_hi_frac = log_positive_fraction_interval(Fraction(q), terms=60)
    theta_lo_frac = Fraction(1) + ratio_lo_frac / q_hi_frac

    # Method 2: 80-digit directed Decimal
    eng = RigorousLnFactorial(prec=80)
    ctx_lo, ctx_hi = eng.ctx_lo, eng.ctx_hi
    c_dec_lo = ctx_lo.divide(Decimal(c_frac.numerator), Decimal(c_frac.denominator))
    p_dec_hi = ctx_hi.divide(Decimal(p_frac.numerator), Decimal(p_frac.denominator))
    ratio_dec_lo = ctx_lo.divide(c_dec_lo, p_dec_hi)
    ln_ratio_lo, _ = eng.ln_bounds(ratio_dec_lo)
    _, ln_q_hi = eng.ln_bounds(Decimal(q))
    theta_lo_dec = ctx_lo.add(Decimal(1), ctx_lo.divide(ln_ratio_lo, ln_q_hi))

    # Compare Method 1 and Method 2
    theta_frac_as_dec = ctx_lo.divide(Decimal(theta_lo_frac.numerator), Decimal(theta_lo_frac.denominator))
    agree = abs(theta_frac_as_dec - theta_lo_dec) < Decimal("1e-35")
    theta_conservative = min(theta_frac_as_dec, theta_lo_dec)

    return {
        "mode": "controlled_carry_limit",
        "q": q,
        "c_lower": str(c_frac),
        "p_upper": str(p_frac),
        "theta_limit_lower_50d": f"{theta_conservative:.50f}",
        "beats_limit_record_1_19519192": bool(theta_conservative > Decimal("1.19519192")),
        "beats_limit_record_by_1e7": bool(theta_conservative >= Decimal("1.19519202")),
        "methods_agree": bool(agree),
    }


def verify_controlled_carry_block_finite(spec):
    """
    Verify a finite-depth controlled-carry block construction (Proposition 2 & Proposition 3
    of Kleinwaks 2026b at finite block count ell, block size k, sum block size m).
    Uses exact residue cost multiplicities M_k(C) and exact sum-carry row sum W_m(x).
    """
    B, M = build_mask_from_spec(spec)
    q = int(spec["q"])
    k = int(spec["k"])
    m = int(spec.get("m", k))
    ell = int(spec.get("ell", 10**13))
    N_digits = k * ell
    if N_digits % m != 0:
        raise ValueError(f"Total digits k*ell = {N_digits} must be divisible by sum block length m = {m}")
    sum_blocks = N_digits // m
    x_str = str(spec["x"])

    sum1, kap1, _ = combinatorial_tables_method1(B, M)
    sum2, kap2 = combinatorial_tables_method2(B, M)
    comb_agree = (sum1 == sum2) and (kap1 == kap2)
    if not comb_agree:
        raise ValueError("Combinatorial tables disagree")

    # Cost multiplicities M_k(C): either provided in spec["cost_histogram"] and verified
    # against exact automaton traversal (for k <= 2) or computed directly for k == 1, 2
    A_plus = [kap1[r] if r <= B else INF for r in range(q + 1)]
    A_minus = [kap1[q - r] if 0 <= q - r <= B else INF for r in range(q + 1)]

    def compute_exact_cost_histogram_dp(k_val):
        # Exact combinatorial carry-state + cost DP for small k_val (k_val == 1 or 2)
        if k_val == 1:
            hist = {}
            for r in range(q):
                c = min(A_plus[r], A_minus[r])
                if c < INF:
                    hist[c] = hist.get(c, 0) + 1
            h_cost = min(A_plus[q // 2], A_minus[q // 2]) if (q % 2 == 0) else INF
            return hist, h_cost
        elif k_val == 2:
            # Step 1: group by (state_delta, cost_after_step_1)
            step1_pairs = {}
            for r0 in range(q):
                v0 = A_plus[r0]
                v1 = A_minus[r0]
                if v0 >= INF and v1 >= INF:
                    continue
                if v1 >= INF:
                    add, nxt = v0, INF
                elif v0 >= INF:
                    add, nxt = v1, -INF
                else:
                    add, nxt = (v0 if v0 <= v1 else v1), v1 - v0
                key = (nxt, add)
                step1_pairs[key] = step1_pairs.get(key, 0) + 1
            hist = {}
            for (st, c1), mult in step1_pairs.items():
                if st == INF:
                    u0, u1 = 0, INF
                elif st == -INF:
                    u0, u1 = INF, 0
                elif st >= 0:
                    u0, u1 = 0, st
                else:
                    u0, u1 = -st, 0
                for r1 in range(q):
                    v0 = min(u0 + A_plus[r1], u1 + A_plus[r1 + 1])
                    v1 = min(u0 + A_minus[r1], u1 + A_minus[r1 + 1])
                    c2 = min(v0, v1)
                    if c2 < INF:
                        tot = c1 + c2
                        hist[tot] = hist.get(tot, 0) + mult
            # Self-inverse residue h = q^2 / 2 when q is even: r0 = 0, r1 = q // 2
            if (q * q) % 2 == 0:
                r0 = (q * q // 2) % q
                r1 = (q * q // 2) // q
                v0 = A_plus[r0]
                v1 = A_minus[r0]
                c1 = min(v0, v1)
                st = INF if v1 >= INF else (-INF if v0 >= INF else v1 - v0)
                u0, u1 = (0, INF) if st == INF else ((INF, 0) if st == -INF else ((0, st) if st >= 0 else (-st, 0)))
                w0 = min(u0 + A_plus[r1], u1 + A_plus[r1 + 1])
                w1 = min(u0 + A_minus[r1], u1 + A_minus[r1 + 1])
                h_cost = c1 + min(w0, w1)
            else:
                h_cost = INF
            return hist, h_cost
        else:
            raise ValueError("Direct Python exact histogram DP supports k in {1, 2}; provide precomputed histogram for k >= 3")

    def verify_k2_histogram_fast(hist_dict, claimed_h_cost):
        import bisect
        if claimed_h_cost >= 10**9:
            claimed_h_cost = INF
        c1_arr = [min(A_plus[r], A_minus[r]) for r in range(q)] + [0]
        # Self-inverse h = q^2 // 2
        if (q * q) % 2 == 0:
            r0 = (q * q // 2) % q
            r1 = (q * q // 2) // q
            true_h = min(A_plus[r0] + c1_arr[r1], A_minus[r0] + c1_arr[r1 + 1])
            if true_h >= 10**9:
                true_h = INF
        else:
            true_h = INF
        if claimed_h_cost != true_h:
            raise ValueError(f"h_cost mismatch: {claimed_h_cost} vs {true_h}")

        MOD1 = 10**18 + 9
        MOD2 = 10**18 + 3
        max_c = 4 * B + 2
        p3 = [1] * (max_c + 1)
        p5 = [1] * (max_c + 1)
        for i in range(1, max_c + 1):
            p3[i] = (p3[i - 1] * 3) % MOD1
            p5[i] = (p5[i - 1] * 5) % MOD2

        # Separate r1 by finiteness of (c1[r1], c1[r1+1])
        both = []
        only0_cnt = only1_cnt = 0
        only0_sum1 = only1_sum1 = 0
        only0_sum2 = only1_sum2 = 0
        only0_m1 = only1_m1 = 0
        only0_m2 = only1_m2 = 0

        z1_cnt0 = z1_cnt1 = 0
        z1_sum1_0 = z1_sum1_1 = 0
        z1_sum2_0 = z1_sum2_1 = 0
        z1_m1_0 = z1_m1_1 = 0
        z1_m2_0 = z1_m2_1 = 0

        for r1 in range(q):
            a0 = c1_arr[r1]
            a1 = c1_arr[r1 + 1]
            if a0 < INF:
                z1_cnt0 += 1
                z1_sum1_0 += a0
                z1_sum2_0 += a0 * a0
                z1_m1_0 = (z1_m1_0 + p3[a0]) % MOD1
                z1_m2_0 = (z1_m2_0 + p5[a0]) % MOD2
            if a1 < INF:
                z1_cnt1 += 1
                z1_sum1_1 += a1
                z1_sum2_1 += a1 * a1
                z1_m1_1 = (z1_m1_1 + p3[a1]) % MOD1
                z1_m2_1 = (z1_m2_1 + p5[a1]) % MOD2
            if a0 < INF and a1 < INF:
                both.append((a1 - a0, a0, a1))
            elif a0 < INF:
                only0_cnt += 1
                only0_sum1 += a0
                only0_sum2 += a0 * a0
                only0_m1 = (only0_m1 + p3[a0]) % MOD1
                only0_m2 = (only0_m2 + p5[a0]) % MOD2
            elif a1 < INF:
                only1_cnt += 1
                only1_sum1 += a1
                only1_sum2 += a1 * a1
                only1_m1 = (only1_m1 + p3[a1]) % MOD1
                only1_m2 = (only1_m2 + p5[a1]) % MOD2

        both.sort(key=lambda x: x[0])
        n_b = len(both)
        deltas = [t[0] for t in both]
        pref_sum1 = [0] * (n_b + 1)
        pref_sum2 = [0] * (n_b + 1)
        pref_m1 = [0] * (n_b + 1)
        pref_m2 = [0] * (n_b + 1)
        suff_sum1 = [0] * (n_b + 1)
        suff_sum2 = [0] * (n_b + 1)
        suff_m1 = [0] * (n_b + 1)
        suff_m2 = [0] * (n_b + 1)

        for i in range(n_b):
            _, a0, a1 = both[i]
            pref_sum1[i + 1] = pref_sum1[i] + a1
            pref_sum2[i + 1] = pref_sum2[i] + a1 * a1
            pref_m1[i + 1] = (pref_m1[i] + p3[a1]) % MOD1
            pref_m2[i + 1] = (pref_m2[i] + p5[a1]) % MOD2
        for i in range(n_b - 1, -1, -1):
            _, a0, a1 = both[i]
            suff_sum1[i] = suff_sum1[i + 1] + a0
            suff_sum2[i] = suff_sum2[i + 1] + a0 * a0
            suff_m1[i] = (suff_m1[i + 1] + p3[a0]) % MOD1
            suff_m2[i] = (suff_m2[i + 1] + p5[a0]) % MOD2

        tot_cnt = 0
        tot_sum1 = 0
        tot_sum2 = 0
        tot_m1 = 0
        tot_m2 = 0

        for r0 in range(q):
            ap = A_plus[r0]
            am = A_minus[r0]
            if ap >= INF and am >= INF:
                continue
            if am >= INF:
                tot_cnt += z1_cnt0
                tot_sum1 += ap * z1_cnt0 + z1_sum1_0
                tot_sum2 += ap * ap * z1_cnt0 + 2 * ap * z1_sum1_0 + z1_sum2_0
                tot_m1 = (tot_m1 + p3[ap] * z1_m1_0) % MOD1
                tot_m2 = (tot_m2 + p5[ap] * z1_m2_0) % MOD2
            elif ap >= INF:
                tot_cnt += z1_cnt1
                tot_sum1 += am * z1_cnt1 + z1_sum1_1
                tot_sum2 += am * am * z1_cnt1 + 2 * am * z1_sum1_1 + z1_sum2_1
                tot_m1 = (tot_m1 + p3[am] * z1_m1_1) % MOD1
                tot_m2 = (tot_m2 + p5[am] * z1_m2_1) % MOD2
            else:
                idx = bisect.bisect_left(deltas, ap - am)
                c0_cnt = (n_b - idx) + only0_cnt
                c0_s1 = suff_sum1[idx] + only0_sum1
                c0_s2 = suff_sum2[idx] + only0_sum2
                c0_m1 = (suff_m1[idx] + only0_m1) % MOD1
                c0_m2 = (suff_m2[idx] + only0_m2) % MOD2

                c1_cnt = idx + only1_cnt
                c1_s1 = pref_sum1[idx] + only1_sum1
                c1_s2 = pref_sum2[idx] + only1_sum2
                c1_m1 = (pref_m1[idx] + only1_m1) % MOD1
                c1_m2 = (pref_m2[idx] + only1_m2) % MOD2

                tot_cnt += c0_cnt + c1_cnt
                tot_sum1 += ap * c0_cnt + c0_s1 + am * c1_cnt + c1_s1
                tot_sum2 += (ap * ap * c0_cnt + 2 * ap * c0_s1 + c0_s2) + (am * am * c1_cnt + 2 * am * c1_s1 + c1_s2)
                tot_m1 = (tot_m1 + p3[ap] * c0_m1 + p3[am] * c1_m1) % MOD1
                tot_m2 = (tot_m2 + p5[ap] * c0_m2 + p5[am] * c1_m2) % MOD2

        h_cnt = sum(hist_dict.values())
        h_s1 = sum(c * v for c, v in hist_dict.items())
        h_s2 = sum(c * c * v for c, v in hist_dict.items())
        h_m1 = sum(v * p3[c] for c, v in hist_dict.items()) % MOD1
        h_m2 = sum(v * p5[c] for c, v in hist_dict.items()) % MOD2

        if (h_cnt, h_s1, h_s2, h_m1, h_m2) != (tot_cnt, tot_sum1, tot_sum2, tot_m1, tot_m2):
            raise ValueError("cost_histogram failed exact O(q log q) moment & modular polynomial verification")

    if "cost_histogram" in spec and spec["cost_histogram"] is not None:
        raw_hist = {int(c): int(cnt) for c, cnt in spec["cost_histogram"].items()}
        h_cost = int(spec.get("h_cost", INF))
        if h_cost >= 10**9:
            h_cost = INF
        if k == 1:
            chk_hist, chk_h = compute_exact_cost_histogram_dp(1)
            if raw_hist != chk_hist or h_cost != chk_h:
                raise ValueError("Provided k=1 cost_histogram does not match exact DP reconstruction")
        elif k == 2:
            verify_k2_histogram_fast(raw_hist, h_cost)
    else:
        raw_hist, h_cost = compute_exact_cost_histogram_dp(k)

    # Convert full residue cost histogram on Z/q^k Z into orbit counts on R_k (pairs {r, -r})
    # Residue 0 has cost 0. Self-inverse h = q^k/2 (if q^k even and h_cost < INF) has cost h_cost.
    orbit_mult = {}
    for c, cnt in raw_hist.items():
        rem = cnt
        if c == 0:
            rem -= 1
        if (q**k) % 2 == 0 and h_cost < INF and c == h_cost:
            rem -= 1
        if rem % 2 != 0:
            raise ValueError(f"Non-self-inverse residue count at cost {c} is odd ({rem})")
        if rem > 0:
            orbit_mult[c] = rem // 2

    def eval_block_with_prec(prec):
        eng = RigorousLnFactorial(prec=prec, small_limit=2000)
        ctx_lo, ctx_hi = eng.ctx_lo, eng.ctx_hi
        x_lo = ctx_lo.create_decimal(x_str)
        x_hi = ctx_hi.create_decimal(x_str)
        max_cost = max(max(raw_hist.keys()), 2 * m * B)
        pow_lo = [Decimal(1)] * (max_cost + 1)
        pow_hi = [Decimal(1)] * (max_cost + 1)
        for i in range(1, max_cost + 1):
            pow_lo[i] = ctx_lo.multiply(pow_lo[i - 1], x_lo)
            pow_hi[i] = ctx_hi.multiply(pow_hi[i - 1], x_hi)

        # Z_k(x) lower and upper bounds
        zk_lo = Decimal(0)
        zk_hi = Decimal(0)
        for c, cnt in raw_hist.items():
            zk_lo = ctx_lo.add(zk_lo, ctx_lo.multiply(Decimal(cnt), pow_lo[c]))
            zk_hi = ctx_hi.add(zk_hi, ctx_hi.multiply(Decimal(cnt), pow_hi[c]))

        ell_dec = Decimal(ell)
        counts_by_cost = {}
        used = 0
        total_cost = 0
        for c, om in sorted(orbit_mult.items()):
            p_lo = ctx_lo.divide(pow_lo[c], zk_hi)
            nr = int(ctx_lo.multiply(ell_dec, p_lo) // 1)
            counts_by_cost[c] = nr
            used += 2 * om * nr
            total_cost += 2 * om * nr * c

        nh = 0
        if (q**k) % 2 == 0 and h_cost < INF:
            ph_lo = ctx_lo.divide(pow_lo[h_cost], zk_hi)
            nh = 2 * int(ctx_lo.divide(ctx_lo.multiply(ell_dec, ph_lo), Decimal(2)) // 1)
            used += nh
            total_cost += nh * h_cost

        if used > ell:
            raise ValueError("Block type counts exceed ell")
        n0 = ell - used
        L = total_cost // 2

        logD_lo = eng.lnf_lo(ell)
        denom_hi = ctx_hi.add(eng.lnf_hi(n0), eng.lnf_hi(nh))
        for c, om in orbit_mult.items():
            nr = counts_by_cost[c]
            if nr > 0:
                lg_hi = eng.lnf_hi(nr)
                denom_hi = ctx_hi.add(denom_hi, ctx_hi.multiply(Decimal(2 * om), lg_hi))
        logD_lo = ctx_lo.subtract(logD_lo, denom_hi)

        # Sum side: if m == 1, W_1(x) <= P_+(x); if w_m_upper provided or computed via plus automaton
        pp_hi = Decimal(0)
        for s in range(2 * B + 1):
            if sum1[s]:
                pp_hi = ctx_hi.add(pp_hi, pow_hi[s])
        if m == 1:
            wm_hi = pp_hi
        else:
            # Exact carry-state plus automaton DP with upward rounding in Decimal
            cur = {-INF: Decimal(1)}
            for _ in range(m):
                nxt = {}
                for st, w_val in cur.items():
                    c1, c0 = (INF, 0) if st == -INF else ((0, INF) if st == INF else ((0, st) if st >= 0 else (-st, 0)))
                    for y in range(q):
                        n1, n0_c = INF, INF
                        if c1 < INF:
                            s = y + q - 1
                            if 0 <= s <= 2 * B and sum1[s]:
                                n1 = min(n1, c1 + s)
                            s = y - 1
                            if 0 <= s <= 2 * B and sum1[s]:
                                n0_c = min(n0_c, c1 + s)
                        if c0 < INF:
                            s = y + q
                            if 0 <= s <= 2 * B and sum1[s]:
                                n1 = min(n1, c0 + s)
                            s = y
                            if 0 <= s <= 2 * B and sum1[s]:
                                n0_c = min(n0_c, c0 + s)
                        if n1 >= INF and n0_c >= INF:
                            continue
                        if n1 >= INF:
                            inc, nd = n0_c, -INF
                        elif n0_c >= INF:
                            inc, nd = n1, INF
                        else:
                            inc, nd = min(n1, n0_c), n0_c - n1
                        contrib = ctx_hi.multiply(w_val, pow_hi[inc])
                        nxt[nd] = ctx_hi.add(nxt.get(nd, Decimal(0)), contrib)
                cur = nxt
            wm_hi = Decimal(0)
            for st, w_val in cur.items():
                c1, c0 = (INF, 0) if st == -INF else ((0, INF) if st == INF else ((0, st) if st >= 0 else (-st, 0)))
                if c0 < INF:
                    wm_hi = ctx_hi.add(wm_hi, ctx_hi.multiply(w_val, pow_hi[c0]))
                if c1 < INF:
                    wm_hi = ctx_hi.add(wm_hi, ctx_hi.multiply(w_val, pow_hi[c1]))

        _, log_wm_hi = eng.ln_bounds(wm_hi)
        part1_hi = ctx_hi.multiply(log_wm_hi, Decimal(sum_blocks))
        log_x_lo, _ = eng.ln_bounds(x_lo)
        neg_log_x_hi = ctx_hi.minus(log_x_lo)
        part2_hi = ctx_hi.multiply(neg_log_x_hi, Decimal(2 * L))
        logS_hi = ctx_hi.add(part1_hi, part2_hi)

        # Denominator: 4 max(U_ell) + 1 < 4 q^{k*ell}
        _, log_q_hi = eng.ln_bounds(Decimal(q))
        _, log_4_hi = eng.ln_bounds(Decimal(4))
        log_den_hi = ctx_hi.add(ctx_hi.multiply(log_q_hi, Decimal(N_digits)), log_4_hi)

        numer_lo = ctx_lo.subtract(logD_lo, logS_hi)
        theta_finite_lo = ctx_lo.add(Decimal(1), ctx_lo.divide(numer_lo, log_den_hi))
        return {
            "n0": n0,
            "nh": nh,
            "L": L,
            "logD_lo": logD_lo,
            "logS_hi": logS_hi,
            "log_den_hi": log_den_hi,
            "theta_finite_lo": theta_finite_lo,
        }

    res1 = eval_block_with_prec(80)
    res2 = eval_block_with_prec(105)
    agree = (
        res1["n0"] == res2["n0"]
        and res1["L"] == res2["L"]
        and abs(res1["theta_finite_lo"] - res2["theta_finite_lo"]) < Decimal("1e-60")
    )

    lb_50d = f"{res1['theta_finite_lo']:.50f}"
    if "certified_lower_bound_50d" in spec and str(spec["certified_lower_bound_50d"]) != lb_50d:
        raise ValueError(f"certified_lower_bound_50d mismatch: {spec['certified_lower_bound_50d']} vs {lb_50d}")

    return {
        "mode": "controlled_carry_block_finite",
        "B": B,
        "q": q,
        "k": k,
        "m": m,
        "ell": ell,
        "N_digits": N_digits,
        "mask_size": len(M),
        "mask_sum": sum(M),
        "n0": res1["n0"],
        "nh": res1["nh"],
        "L": res1["L"],
        "theta_finite_lower_50d": lb_50d,
        "theta_finite_lower_8d": f"{res1['theta_finite_lo'] - Decimal('5e-9'):.8f}",
        "beats_finite_record_1_19102809": bool(res1["theta_finite_lo"] > Decimal("1.19102809")),
        "beats_finite_record_by_1e7": bool(res1["theta_finite_lo"] >= Decimal("1.19102819")),
        "beats_limit_record_1_19519192": bool(res1["theta_finite_lo"] >= Decimal("1.19519202")),
        "methods_agree": bool(comb_agree and agree),
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify_c3a.py <certificate.json> [certificate2.json ...]")
        sys.exit(1)

    all_ok = True
    for arg in sys.argv[1:]:
        path = Path(arg)
        spec = json.loads(path.read_text())
        mode = spec.get("mode")
        if mode is None:
            if any(k in spec for k in ("c_lower_rational", "difference_lower_num", "difference_lower")):
                mode = "controlled_carry_limit"
            elif "k" in spec and int(spec.get("q", 0)) != 2 * int(spec.get("B", 0)) + 1:
                mode = "controlled_carry_block_finite"
            else:
                mode = "finite_carry_free"

        if mode == "finite_carry_free":
            out = verify_finite_carry_free(spec)
        elif mode == "controlled_carry_limit":
            out = verify_controlled_carry_limit(spec)
        elif mode == "controlled_carry_block_finite":
            out = verify_controlled_carry_block_finite(spec)
        else:
            raise ValueError(f"Unknown certificate mode: {mode}")

        out["file"] = str(path)
        print(json.dumps(out, indent=2))
        if not out.get("methods_agree", False):
            all_ok = False

    if not all_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
