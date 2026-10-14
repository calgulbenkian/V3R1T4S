#include < algorithm >
#include < atomic >
#include < cmath >
#include < cstdint >
#include < fstream >
#include < iomanip >
#include < iostream >
#include < map >
#include < mutex >
#include < numeric >
#include < string >
#include < thread >
#include < vector >

constexpr int INF = 1000000000;

double eval_Z2_fast(int B, int q, const std::vector< int >& kap, const std::vector< double >& xp) {
    std::vector< int > c1(q + 1, INF);
    c1[q] = 0;
    for (int r = 0; r < q; ++r) {
        int ap = (r <= B) ? kap[r] : INF;
        int am = (q - r <= B) ? kap[q - r] : INF;
        c1[r] = std::min(ap, am);
    }

    double z1_r1 = 0.0, z1_r1_plus = 0.0, only_c0_sum = 0.0, only_c1_sum = 0.0;
    struct PairDelta { int delta; double w0, w1; };
    std::vector< PairDelta > both;
    both.reserve(q);

    for (int r1 = 0; r1 < q; ++r1) {
        int a0 = c1[r1], a1 = c1[r1 + 1];
        if (a0 < INF) z1_r1 += xp[a0];
        if (a1 < INF) z1_r1_plus += xp[a1];
        if (a0 < INF && a1 < INF) both.push_back({a1 - a0, xp[a0], xp[a1]});
        else if (a0 < INF) only_c0_sum += xp[a0];
        else if (a1 < INF) only_c1_sum += xp[a1];
    }

    std::sort(both.begin(), both.end(), [](const PairDelta& a, const PairDelta& b) {
        return a.delta < b.delta;
    });

    size_t n = both.size();
    std::vector< int > deltas(n);
    std::vector< double > pref_w1(n + 1, 0.0), suff_w0(n + 1, 0.0);
    for (size_t i = 0; i < n; ++i) {
        deltas[i] = both[i].delta;
        pref_w1[i + 1] = pref_w1[i] + both[i].w1;
    }
    for (size_t i = n; i > 0; --i) {
        suff_w0[i - 1] = suff_w0[i] + both[i - 1].w0;
    }

    double z2 = 0.0;
    for (int r0 = 0; r0 < q; ++r0) {
        int ap = (r0 <= B) ? kap[r0] : INF;
        int am = (q - r0 <= B) ? kap[q - r0] : INF;
        if (ap >= INF && am >= INF) continue;
        if (am >= INF) z2 += xp[ap] * z1_r1;
        else if (ap >= INF) z2 += xp[am] * z1_r1_plus;
        else {
            int thresh = ap - am;
            auto it = std::lower_bound(deltas.begin(), deltas.end(), thresh);
            size_t idx = (size_t)(it - deltas.begin());
            z2 += xp[ap] * (suff_w0[idx] + only_c0_sum) + xp[am] * (pref_w1[idx] + only_c1_sum);
        }
    }
    return z2;
}

void write_k2_certificate_from_mask(int B, int q, double x, int m_sum, const std::vector< int >& M, const std::string& path) {
    std::vector< int > kap(B + 1, INF);
    kap[0] = 0;
    for (int a : M) for (int b : M) {
        int d = std::abs(a - b);
        if (a + b < kap[d]) kap[d] = a + b;
    }

    std::vector< int > A_plus(q + 1, INF), A_minus(q + 1, INF);
    for (int r = 0; r <= q; ++r) {
        if (r <= B) A_plus[r] = kap[r];
        if (q - r >= 0 && q - r <= B) A_minus[r] = kap[q - r];
    }

    std::map<std::pair<int, int>, int64_t> step1;
    for (int r0 = 0; r0 < q; ++r0) {
        int v0 = A_plus[r0], v1 = A_minus[r0];
        if (v0 >= INF && v1 >= INF) continue;
        int add = std::min(v0, v1);
        int nxt = (v1 >= INF) ? INF : ((v0 >= INF) ? -INF : (v1 - v0));
        step1[{nxt, add}] += 1;
    }
    std::vector<std::pair<std::pair<int, int>, int64_t>> pairs(step1.begin(), step1.end());
    int max_c = 4 * B + 2;
    unsigned int nthreads = std::max(1u, std::thread::hardware_concurrency());
    std::vector<std::vector< int64_t >> local_hist(nthreads, std::vector< int64_t >(max_c, 0));
    std::atomic< size_t > next_i{0};
    std::vector<std::thread> pool;
    for (unsigned int t = 0; t < nthreads; ++t) {
        pool.emplace_back([&, t]() {
            auto& h = local_hist[t];
            while (true) {
                size_t i = next_i.fetch_add(1);
                if (i >= pairs.size()) break;
                int st = pairs[i].first.first;
                int c1 = pairs[i].first.second;
                int64_t mult = pairs[i].second;
                int u0 = (st == INF) ? 0 : ((st == -INF) ? INF : (st >= 0 ? 0 : -st));
                int u1 = (st == INF) ? INF : ((st == -INF) ? 0 : (st >= 0 ? st : 0));
                for (int r1 = 0; r1 < q; ++r1) {
                    int v0 = std::min(u0 >= INF || A_plus[r1] >= INF ? INF : u0 + A_plus[r1],
                                      u1 >= INF || A_plus[r1 + 1] >= INF ? INF : u1 + A_plus[r1 + 1]);
                    int v1 = std::min(u0 >= INF || A_minus[r1] >= INF ? INF : u0 + A_minus[r1],
                                      u1 >= INF || A_minus[r1 + 1] >= INF ? INF : u1 + A_minus[r1 + 1]);
                    int c2 = std::min(v0, v1);
                    if (c2 < INF) h[c1 + c2] += mult;
                }
            }
        });
    }
    for (auto& th : pool) th.join();

    std::vector< int64_t > hist(max_c, 0);
    for (unsigned int t = 0; t < nthreads; ++t) for (int c = 0; c < max_c; ++c) hist[c] += local_hist[t][c];

    int h_cost = INF;
    int64_t q2 = (int64_t)q * q;
    if (q2 % 2 == 0) {
        int r0 = (int)((q2 / 2) % q), r1 = (int)((q2 / 2) / q);
        int v0 = A_plus[r0], v1 = A_minus[r0];
        int c1 = std::min(v0, v1);
        int st = (v1 >= INF) ? INF : ((v0 >= INF) ? -INF : (v1 - v0));
        int u0 = (st == INF) ? 0 : ((st == -INF) ? INF : (st >= 0 ? 0 : -st));
        int u1 = (st == INF) ? INF : ((st == -INF) ? 0 : (st >= 0 ? st : 0));
        int w0 = std::min(u0 >= INF || A_plus[r1] >= INF ? INF : u0 + A_plus[r1],
                          u1 >= INF || A_plus[r1 + 1] >= INF ? INF : u1 + A_plus[r1 + 1]);
        int w1 = std::min(u0 >= INF || A_minus[r1] >= INF ? INF : u0 + A_minus[r1],
                          u1 >= INF || A_minus[r1 + 1] >= INF ? INF : u1 + A_minus[r1 + 1]);
        h_cost = c1 + std::min(w0, w1);
    }

    std::ofstream f(path);
    f << "{\n";
    f << "  \"mode\": \"controlled_carry_block_finite\",\n";
    f << "  \"B\": " << B << ",\n";
    f << "  \"q\": " << q << ",\n";
    f << "  \"k\": 2,\n";
    f << "  \"m\": " << m_sum << ",\n";
    f << "  \"ell\": 10000000000000000,\n";
    f << std::setprecision(16) << "  \"x\": \"" << x << "\",\n";
    f << "  \"h_cost\": " << h_cost << ",\n";
    f << "  \"mask\": [";
    for (size_t i = 0; i < M.size(); ++i) {
        if (i > 0) f << ", ";
        f << M[i];
    }
    f << "],\n";
    f << "  \"cost_histogram\": {\n";
    bool first = true;
    for (int c = 0; c < max_c; ++c) {
        if (hist[c] > 0) {
            if (!first) f << ",\n";
            f << "    \"" << c << "\": " << hist[c];
            first = false;
        }
    }
    f << "\n  }\n}\n";
}

int main() {
    std::cout << std::setprecision(13);
    std::vector< int > gens = {1518, 1524, 1587, 2024, 2032, 2116};
    int B_max = 24000;
    std::vector<unsigned char> reach(B_max + 1, 0);
    reach[0] = 1;
    for (int n = 0; n <= B_max; ++n) if (reach[n]) for (int g : gens) if (n + g <= B_max) reach[n + g] = 1;
    std::vector< int > all_M;
    for (int n = 0; n <= B_max; ++n) if (reach[n]) all_M.push_back(n);

    double best_th = 0.0, best_x = 0.0;
    int best_B = 0, best_q = 0;

    int last_B = -1;
    for (int B_target = 20000; B_target <= 23500; B_target += 100) {
        auto it = std::lower_bound(all_M.begin(), all_M.end(), B_target);
        if (it == all_M.end()) continue;
        int B = *it;
        if (B == last_B) continue;
        last_B = B;
        std::vector<unsigned char> sum_present(2 * B + 1, 0);
        std::vector< int > kap(B + 1, INF);
        kap[0] = 0;
        for (int a : all_M) {
            if (a > B) break;
            for (int b : all_M) {
                if (b > a) break;
                sum_present[a + b] = 1;
                if (a + b < kap[a - b]) kap[a - b] = a + b;
            }
        }
        for (double lam : {6.70, 6.85, 7.00, 7.15, 7.30}) {
            double x = std::exp(-lam / B);
            std::vector< double > xp(4 * B + 5, 1.0);
            for (int i = 1; i < (int)xp.size(); ++i) xp[i] = xp[i - 1] * x;
            double pp = 0.0;
            for (int s = 0; s <= 2 * B; ++s) if (sum_present[s]) pp += xp[s];

            for (int q = std::max(B + 10, 24800); q <= 26000; q += 20) {
                double z2 = eval_Z2_fast(B, q, kap, xp);
                double th = 1.0 + (0.5 * std::log(z2) - std::log(pp)) / std::log((double)q);
                if (th > best_th) {
                    best_th = th;
                    best_B = B;
                    best_q = q;
                    best_x = x;
                }
            }
        }
    }
    // Fine scan around best_q
    {
        int B = best_B;
        std::vector<unsigned char> sum_present(2 * B + 1, 0);
        std::vector< int > kap(B + 1, INF);
        kap[0] = 0;
        for (int a : all_M) {
            if (a > B) break;
            for (int b : all_M) {
                if (b > a) break;
                sum_present[a + b] = 1;
                if (a + b < kap[a - b]) kap[a - b] = a + b;
            }
        }
        std::vector< double > xp(4 * B + 5, 1.0);
        for (int i = 1; i < (int)xp.size(); ++i) xp[i] = xp[i - 1] * best_x;
        double pp = 0.0;
        for (int s = 0; s <= 2 * B; ++s) if (sum_present[s]) pp += xp[s];
        int q_c = best_q;
        for (int q = std::max(B + 1, q_c - 40); q <= q_c + 40; ++q) {
            double z2 = eval_Z2_fast(B, q, kap, xp);
            double th = 1.0 + (0.5 * std::log(z2) - std::log(pp)) / std::log((double)q);
            if (th > best_th) {
                best_th = th;
                best_q = q;
            }
        }
    }

    // Optimize x at (best_B, best_q)
    std::vector< int > M;
    for (int a : all_M) if (a <= best_B) M.push_back(a);
    std::vector<unsigned char> sum_present(2 * best_B + 1, 0);
    std::vector< int > kap(best_B + 1, INF);
    kap[0] = 0;
    for (int a : M) for (int b : M) {
        if (b > a) break;
        sum_present[a + b] = 1;
        if (a + b < kap[a - b]) kap[a - b] = a + b;
    }
    auto eval_x = [&](double x) {
        std::vector< double > xp(4 * best_B + 5, 1.0);
        for (int i = 1; i < (int)xp.size(); ++i) xp[i] = xp[i - 1] * x;
        double pp = 0.0;
        for (int s = 0; s <= 2 * best_B; ++s) if (sum_present[s]) pp += xp[s];
        double z2 = eval_Z2_fast(best_B, best_q, kap, xp);
        return 1.0 + (0.5 * std::log(z2) - std::log(pp)) / std::log((double)best_q);
    };
    double lo = std::exp(-7.3 / best_B), hi = std::exp(-6.3 / best_B);
    for (int iter = 0; iter < 40; ++iter) {
        double m1 = lo + (hi - lo) / 3.0;
        double m2 = hi - (hi - lo) / 3.0;
        if (eval_x(m1) < eval_x(m2)) lo = m1;
        else hi = m2;
    }
    best_x = 0.5 * (lo + hi);
    best_th = eval_x(best_x);
    std::cout << "Best semigroup k=2: B=" << best_B << " odd_q=" << best_q
              << " |M|=" << M.size() << " x=" << best_x << " theta(P+)=" << best_th << "\n";

    // Now test pruning top elements of M (elements near best_B that have unique sums in M+M and are shadowed in k=2!)
    std::vector<unsigned char> in_mask(best_B + 1, 0);
    for (int a : M) in_mask[a] = 1;
    std::vector< double > xp(4 * best_B + 5, 1.0);
    for (int i = 1; i < (int)xp.size(); ++i) xp[i] = xp[i - 1] * best_x;

    // Test top 150 elements of M for greedy removal
    for (int pass = 1; pass <= 3; ++pass) {
        int removed_in_pass = 0;
        for (int idx = (int)M.size() - 2; idx >= std::max(1, (int)M.size() - 250); --idx) {
            int cand = M[idx];
            if (!in_mask[cand]) continue;
            in_mask[cand] = 0;
            std::fill(sum_present.begin(), sum_present.end(), 0);
            std::fill(kap.begin(), kap.end(), INF);
            kap[0] = 0;
            std::vector< int > cur_M;
            for (int n = 0; n <= best_B; ++n) if (in_mask[n]) cur_M.push_back(n);
            for (int a : cur_M) for (int b : cur_M) {
                if (b > a) break;
                sum_present[a + b] = 1;
                if (a + b < kap[a - b]) kap[a - b] = a + b;
            }
            double pp = 0.0;
            for (int s = 0; s <= 2 * best_B; ++s) if (sum_present[s]) pp += xp[s];
            double z2 = eval_Z2_fast(best_B, best_q, kap, xp);
            double th = 1.0 + (0.5 * std::log(z2) - std::log(pp)) / std::log((double)best_q);
            if (th > best_th + 1e-12) {
                best_th = th;
                removed_in_pass++;
            } else {
                in_mask[cand] = 1;
            }
        }
        M.clear();
        for (int n = 0; n <= best_B; ++n) if (in_mask[n]) M.push_back(n);
        std::cout << "Pass " << pass << ": removed=" << removed_in_pass << " |M|=" << M.size()
                  << " theta(P+)=" << best_th << "\n";
        if (removed_in_pass == 0) break;
    }

    write_k2_certificate_from_mask(best_B, best_q, best_x, 1, M, "attempts/c-evaluator-optimizer/best_k2_finite_cert.json");
    return 0;
}
