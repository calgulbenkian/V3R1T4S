#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

typedef struct { double x, y, z; } Vec3;

static int load_scu(const char *path, Vec3 *c, int max_n) {
    FILE *f = fopen(path, "r");
    if (!f) return 0;
    int idx, n = 0;
    double x, y, z;
    while (n < max_n && fscanf(f, "%d %lf %lf %lf", &idx, &x, &y, &z) == 4) {
        c[n].x = x; c[n].y = y; c[n].z = z;
        n++;
    }
    fclose(f);
    return n;
}

static double load_r_table(int N_target) {
    FILE *f = fopen("data/radius.txt", "r");
    if (!f) return 0.0;
    int n;
    double r;
    while (fscanf(f, "%d %lf", &n, &r) == 2) {
        if (n == N_target) { fclose(f); return r; }
    }
    fclose(f);
    return 0.0;
}

static double exact_r_from_c(int n, Vec3 *c) {
    double min_x = 1e9, max_x = -1e9;
    double min_y = 1e9, max_y = -1e9;
    double min_z = 1e9, max_z = -1e9;
    for (int i = 0; i < n; i++) {
        if (c[i].x < min_x) min_x = c[i].x;
        if (c[i].x > max_x) max_x = c[i].x;
        if (c[i].y < min_y) min_y = c[i].y;
        if (c[i].y > max_y) max_y = c[i].y;
        if (c[i].z < min_z) min_z = c[i].z;
        if (c[i].z > max_z) max_z = c[i].z;
    }
    double cx = 0.5 * (min_x + max_x);
    double cy = 0.5 * (min_y + max_y);
    double cz = 0.5 * (min_z + max_z);
    double M = 0.5 * (max_x - min_x);
    if (0.5 * (max_y - min_y) > M) M = 0.5 * (max_y - min_y);
    if (0.5 * (max_z - min_z) > M) M = 0.5 * (max_z - min_z);
    double min_d2 = 1e18;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double dx = (c[i].x - c[j].x) / M;
            double dy = (c[i].y - c[j].y) / M;
            double dz = (c[i].z - c[j].z) / M;
            double d2 = dx*dx + dy*dy + dz*dz;
            if (d2 < min_d2) min_d2 = d2;
        }
    }
    double d_min = sqrt(min_d2);
    double r = d_min / (2.0 * (2.0 + d_min));
    double scale = (0.5 - r) / M;
    for (int i = 0; i < n; i++) {
        c[i].x = (c[i].x - cx) * scale;
        c[i].y = (c[i].y - cy) * scale;
        c[i].z = (c[i].z - cz) * scale;
    }
    return r;
}

static double eval_wall_pair(int n, const double *x, double R, double *g) {
    int dim = 3 * n;
    for (int i = 0; i < dim; i++) g[i] = 0.0;
    double E = 0.0;
    double D = 2.0 * R;
    double D2 = D * D;
    double wall = 0.5 - R;
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < 3; k++) {
            double v = x[3*i+k];
            if (v > wall) {
                double pen = v - wall;
                E += 0.5 * pen * pen;
                g[3*i+k] += pen;
            } else if (v < -wall) {
                double pen = -wall - v;
                E += 0.5 * pen * pen;
                g[3*i+k] -= pen;
            }
        }
        double xi = x[3*i], yi = x[3*i+1], zi = x[3*i+2];
        for (int j = i + 1; j < n; j++) {
            double dx = xi - x[3*j], dy = yi - x[3*j+1], dz = zi - x[3*j+2];
            double d2 = dx*dx + dy*dy + dz*dz;
            if (d2 < D2) {
                double d = sqrt(d2);
                if (d < 1e-15) d = 1e-15;
                double pen = D - d;
                E += 0.5 * pen * pen;
                double f = -pen / d;
                g[3*i]   += f * dx; g[3*i+1] += f * dy; g[3*i+2] += f * dz;
                g[3*j]   -= f * dx; g[3*j+1] -= f * dy; g[3*j+2] -= f * dz;
            }
        }
    }
    return E;
}

static double lbfgs_wall_pair(int n, Vec3 *c, double R, int max_iter) {
    int dim = 3 * n;
    int m = 15;
    double *x = calloc(dim, sizeof(double));
    double *g = calloc(dim, sizeof(double));
    double *x_old = calloc(dim, sizeof(double));
    double *g_old = calloc(dim, sizeof(double));
    double *d = calloc(dim, sizeof(double));
    double *q = calloc(dim, sizeof(double));
    double *s = calloc(m * dim, sizeof(double));
    double *y = calloc(m * dim, sizeof(double));
    double rho[15], alpha[15];

    for (int i = 0; i < n; i++) {
        x[3*i] = c[i].x; x[3*i+1] = c[i].y; x[3*i+2] = c[i].z;
    }

    double E = eval_wall_pair(n, x, R, g);
    int hist = 0;
    for (int iter = 0; iter < max_iter; iter++) {
        double gnorm2 = 0.0;
        for (int i = 0; i < dim; i++) gnorm2 += g[i] * g[i];
        if (gnorm2 < 1e-32 || E < 1e-33) break;

        for (int i = 0; i < dim; i++) q[i] = g[i];
        int bound = hist < m ? hist : m;
        for (int k = bound - 1; k >= 0; k--) {
            int idx = (hist - 1 - (bound - 1 - k)) % m;
            double dot = 0.0;
            for (int i = 0; i < dim; i++) dot += s[idx*dim + i] * q[i];
            alpha[k] = rho[idx] * dot;
            for (int i = 0; i < dim; i++) q[i] -= alpha[k] * y[idx*dim + i];
        }
        double gamma = 1.0;
        if (hist > 0) {
            int last = (hist - 1) % m;
            double sy = 0.0, yy = 0.0;
            for (int i = 0; i < dim; i++) {
                sy += s[last*dim + i] * y[last*dim + i];
                yy += y[last*dim + i] * y[last*dim + i];
            }
            if (yy > 1e-30 && sy > 1e-30) gamma = sy / yy;
        }
        for (int i = 0; i < dim; i++) d[i] = gamma * q[i];
        for (int k = 0; k < bound; k++) {
            int idx = (hist - bound + k) % m;
            double dot = 0.0;
            for (int i = 0; i < dim; i++) dot += y[idx*dim + i] * d[i];
            double beta = rho[idx] * dot;
            for (int i = 0; i < dim; i++) d[i] += s[idx*dim + i] * (alpha[k] - beta);
        }
        for (int i = 0; i < dim; i++) d[i] = -d[i];

        for (int i = 0; i < dim; i++) { x_old[i] = x[i]; g_old[i] = g[i]; }
        double step = 0.5;
        double E_new = E;
        int accepted = 0;
        for (int ls = 0; ls < 25; ls++) {
            for (int i = 0; i < dim; i++) x[i] = x_old[i] + step * d[i];
            E_new = eval_wall_pair(n, x, R, g);
            if (E_new <= E + 1e-32) { accepted = 1; break; }
            step *= 0.5;
        }
        if (!accepted) {
            step = 0.05;
            for (int i = 0; i < dim; i++) x[i] = x_old[i] - step * g_old[i];
            E_new = eval_wall_pair(n, x, R, g);
            hist = 0;
        } else {
            int slot = hist % m;
            double sy = 0.0;
            for (int i = 0; i < dim; i++) {
                s[slot*dim + i] = x[i] - x_old[i];
                y[slot*dim + i] = g[i] - g_old[i];
                sy += s[slot*dim + i] * y[slot*dim + i];
            }
            if (sy > 1e-32) { rho[slot] = 1.0 / sy; hist++; }
            else hist = 0;
        }
        E = E_new;
    }
    for (int i = 0; i < n; i++) {
        c[i].x = x[3*i]; c[i].y = x[3*i+1]; c[i].z = x[3*i+2];
    }
    free(x); free(g); free(x_old); free(g_old); free(d); free(q); free(s); free(y);
    return E;
}

static double inflate_packing(int n, Vec3 *c, double R_start, double step_init, int stages, int iter_per_stage) {
    Vec3 *best = calloc(n, sizeof(Vec3));
    Vec3 *work = calloc(n, sizeof(Vec3));
    double best_r = exact_r_from_c(n, c);
    memcpy(best, c, n * sizeof(Vec3));
    double R_target = (R_start > best_r) ? R_start : best_r + step_init;
    double step = step_init;
    for (int st = 0; st < stages; st++) {
        memcpy(work, best, n * sizeof(Vec3));
        lbfgs_wall_pair(n, work, R_target, iter_per_stage);
        double r_now = exact_r_from_c(n, work);
        if (r_now > best_r) {
            best_r = r_now;
            memcpy(best, work, n * sizeof(Vec3));
            R_target = best_r + step;
        } else {
            step *= 0.5;
            R_target = best_r + step;
        }
    }
    memcpy(c, best, n * sizeof(Vec3));
    free(best); free(work);
    return best_r;
}

static void save_raw(int n, const Vec3 *c) {
    char path[256];
    snprintf(path, sizeof(path), "attempts/c-evaluator-optimizer/results/raw_scu%d.txt", n);
    FILE *f = fopen(path, "w");
    for (int i = 0; i < n; i++) {
        fprintf(f, "%d %.17g %.17g %.17g\n", i + 1, c[i].x, c[i].y, c[i].z);
    }
    fclose(f);
}

int main(void) {
    printf("=== Lens 2 (c-evaluator-optimizer): Unconstrained Smooth Wall+Pair L-BFGS & Cavity Insertion ===\n");
    Vec3 *c = calloc(2000, sizeof(Vec3));
    Vec3 *c2 = calloc(2000, sizeof(Vec3));

    /* 1. Polish the 6 rows from Lens 1 (N = 101, 466, 467, 468, 793, 1596) */
    int lens1_rows[6] = {101, 466, 467, 468, 793, 1596};
    for (int k = 0; k < 6; k++) {
        int N = lens1_rows[k];
        char path[256];
        snprintf(path, sizeof(path), "attempts/far-import-cavity-splice/results/scu%d.txt", N);
        load_scu(path, c, N);
        double r_table = load_r_table(N);
        double r_init = exact_r_from_c(N, c);
        double r_opt = inflate_packing(N, c, r_init + 1e-10, 5e-11, 14, (N > 1000) ? 1500 : 2500);
        save_raw(N, c);
        printf("[Lens 2 Polish] N=%4d: r_table=%.18f -> r_opt=%.18f (gain=%+.6e)\n",
               N, r_table, r_opt, r_opt - r_table);
        fflush(stdout);
    }

    /* 2. N = 812: Voronoi cavity insertion [0.36385, -0.04032, 0.04041] into scu811.txt */
    {
        load_scu("data/seeds/scu811.txt", c, 811);
        c[811].x = 0.36385; c[811].y = -0.04032; c[811].z = 0.04041;
        double r_table = load_r_table(812);
        lbfgs_wall_pair(812, c, 0.056960, 2500);
        double r_opt = inflate_packing(812, c, 0.05696285, 2e-7, 16, 2500);
        save_raw(812, c);
        printf("[Lens 2 Voronoi Insertion] N= 812: r_table=%.18f -> r_opt=%.18f (gain=%+.6e)\n",
               r_table, r_opt, r_opt - r_table);
        fflush(stdout);
    }

    /* 3. N = 630, 631, 632: 11x11x11 odd-parity FCC vacancies into scu629.txt + L-BFGS */
    {
        load_scu("data/seeds/scu629.txt", c, 629);
        double R = 0.061949671761730317;
        double step = (1.0 - 2.0 * R) / 10.0;
        Vec3 vacs[10];
        int nv = 0;
        for (int ix = 0; ix < 11; ix++) {
            for (int iy = 0; iy < 11; iy++) {
                for (int iz = 0; iz < 11; iz++) {
                    if ((ix + iy + iz) % 2 == 1) {
                        Vec3 pt = {(-5 + ix) * step, (-5 + iy) * step, (-5 + iz) * step};
                        double dmin = 1e9;
                        for (int i = 0; i < 629; i++) {
                            double d = hypot(hypot(pt.x - c[i].x, pt.y - c[i].y), pt.z - c[i].z);
                            if (d < dmin) dmin = d;
                        }
                        for (int i = 0; i < nv; i++) {
                            double d = hypot(hypot(pt.x - vacs[i].x, pt.y - vacs[i].y), pt.z - vacs[i].z);
                            if (d < dmin) dmin = d;
                        }
                        if (dmin > 0.12) vacs[nv++] = pt;
                    }
                }
            }
        }
        for (int add = 1; add <= 3; add++) {
            int N = 629 + add;
            load_scu("data/seeds/scu629.txt", c, 629);
            for (int a = 0; a < add; a++) c[629 + a] = vacs[a];
            double r_table = load_r_table(N);
            lbfgs_wall_pair(N, c, 0.061949671762, 3000);
            save_raw(N, c);
            double r_opt = exact_r_from_c(N, c);
            printf("[Lens 2 FCC Vacancy Insertion] N=%4d: r_table=%.18f -> r_opt=%.18f (gain=%+.6e)\n",
                   N, r_table, r_opt, r_opt - r_table);
            fflush(stdout);
        }
    }

    /* 4. N = 470, 471, 472: Vacancy insertions c500[245, 115, 92] into raw scu469.txt */
    {
        load_scu("data/seeds/scu469.txt", c, 469);
        load_scu("data/seeds/scu500.txt", c2, 500);
        c[469] = c2[245];
        double r_table470 = load_r_table(470);
        lbfgs_wall_pair(470, c, 0.067898241051, 3500);
        double r_opt470 = inflate_packing(470, c, 0.067898241047, 5e-12, 10, 2000);
        save_raw(470, c);
        printf("[Lens 2 Vacancy Insertion] N= 470: r_table=%.18f -> r_opt=%.18f (gain=%+.6e)\n",
               r_table470, r_opt470, r_opt470 - r_table470);
        fflush(stdout);

        load_scu("data/seeds/scu469.txt", c, 469);
        c[469] = c2[245];
        c[470] = c2[115];
        double r_table471 = load_r_table(471);
        lbfgs_wall_pair(471, c, 0.067898241051, 5000);
        save_raw(471, c);
        double r_opt471 = exact_r_from_c(471, c);
        printf("[Lens 2 Vacancy Insertion] N= 471: r_table=%.18f -> r_opt=%.18f (gain=%+.6e)\n",
               r_table471, r_opt471, r_opt471 - r_table471);
        fflush(stdout);

        load_scu("data/seeds/scu469.txt", c, 469);
        c[469] = c2[245];
        c[470] = c2[115];
        c[471] = c2[92];
        double r_table472 = load_r_table(472);
        lbfgs_wall_pair(472, c, 0.067898241051, 5000);
        save_raw(472, c);
        double r_opt472 = exact_r_from_c(472, c);
        printf("[Lens 2 Vacancy Insertion] N= 472: r_table=%.18f -> r_opt=%.18f (gain=%+.6e)\n",
               r_table472, r_opt472, r_opt472 - r_table472);
        fflush(stdout);
    }

    free(c); free(c2);
    return 0;
}
