// Multi-threaded Riemannian L-BFGS + Log-Sum-Exp Minimax Optimizer for Spherical Codes
// Compiles with: clang -O3 -march=native -pthread spherical_opt.c -lm -o spherical_opt
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <pthread.h>
#include <stdint.h>
#include <time.h>

static int D = 0;
static int N = 0;
static double *init_coords = NULL;
static double best_global_c = 2.0;
static double *best_global_coords = NULL;
static pthread_mutex_t best_mutex = PTHREAD_MUTEX_INITIALIZER;

static inline uint64_t xorshift64(uint64_t *s) {
    uint64_t x = *s;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    return *s = x;
}

static inline double rand_normal(uint64_t *rng) {
    double u1 = ((xorshift64(rng) >> 11) + 0.5) * (1.0 / 9007199254740992.0);
    double u2 = ((xorshift64(rng) >> 11) + 0.5) * (1.0 / 9007199254740992.0);
    return sqrt(-2.0 * log(u1)) * cos(6.28318530717958647692 * u2);
}

static void normalize_all(double *X) {
    for (int i = 0; i < N; i++) {
        double *xi = X + i * D;
        double s = 0.0;
        for (int k = 0; k < D; k++) s += xi[k] * xi[k];
        double inv = 1.0 / sqrt(s);
        for (int k = 0; k < D; k++) xi[k] *= inv;
    }
}

static void project_tangent(const double *X, double *G) {
    for (int i = 0; i < N; i++) {
        const double *xi = X + i * D;
        double *gi = G + i * D;
        double dot = 0.0;
        for (int k = 0; k < D; k++) dot += xi[k] * gi[k];
        for (int k = 0; k < D; k++) gi[k] -= dot * xi[k];
    }
}

static double compute_max_dot(const double *X) {
    double cmax = -2.0;
    for (int i = 0; i < N; i++) {
        const double *xi = X + i * D;
        for (int j = i + 1; j < N; j++) {
            const double *xj = X + j * D;
            double dot = 0.0;
            for (int k = 0; k < D; k++) dot += xi[k] * xj[k];
            if (dot > cmax) cmax = dot;
        }
    }
    return cmax;
}

// Compute log-sum-exp objective and Riemannian gradient for active pairs (dot >= cmax - cutoff)
static double eval_lse_grad(const double *X, double beta, double *G, double *out_cmax) {
    int dim = N * D;
    for (int i = 0; i < dim; i++) G[i] = 0.0;

    double cmax = -2.0;
    for (int i = 0; i < N; i++) {
        const double *xi = X + i * D;
        for (int j = i + 1; j < N; j++) {
            const double *xj = X + j * D;
            double dot = 0.0;
            for (int k = 0; k < D; k++) dot += xi[k] * xj[k];
            if (dot > cmax) cmax = dot;
        }
    }
    if (out_cmax) *out_cmax = cmax;

    double cutoff = 40.0 / beta;
    double thresh = cmax - cutoff;
    double sum_exp = 0.0;

    for (int i = 0; i < N; i++) {
        const double *xi = X + i * D;
        double *gi = G + i * D;
        for (int j = i + 1; j < N; j++) {
            const double *xj = X + j * D;
            double dot = 0.0;
            for (int k = 0; k < D; k++) dot += xi[k] * xj[k];
            if (dot >= thresh) {
                double w = exp(beta * (dot - cmax));
                sum_exp += w;
                double *gj = G + j * D;
                for (int k = 0; k < D; k++) {
                    gi[k] += w * xj[k];
                    gj[k] += w * xi[k];
                }
            }
        }
    }

    double inv_sum = 1.0 / sum_exp;
    for (int i = 0; i < dim; i++) G[i] *= inv_sum;
    project_tangent(X, G);
    return cmax + log(sum_exp) / beta;
}

static void run_lbfgs_stage(double *X, double beta, int max_iters, double *best_X, double *best_c) {
    int dim = N * D;
    const int M = 12;
    double *S = calloc((size_t)M * dim, sizeof(double));
    double *Y = calloc((size_t)M * dim, sizeof(double));
    double rho[12] = {0};
    double alpha_hist[12] = {0};

    double *G = malloc(dim * sizeof(double));
    double *G_new = malloc(dim * sizeof(double));
    double *X_new = malloc(dim * sizeof(double));
    double *P = malloc(dim * sizeof(double));
    double *Q = malloc(dim * sizeof(double));

    double cmax = 0.0;
    double f = eval_lse_grad(X, beta, G, &cmax);
    if (cmax < *best_c) {
        *best_c = cmax;
        memcpy(best_X, X, dim * sizeof(double));
    }

    int hist_len = 0;
    int hist_head = 0;
    double step_guess = 1.0 / (beta > 100.0 ? sqrt(beta) : 10.0);

    for (int iter = 0; iter < max_iters; iter++) {
        // Two-loop L-BFGS recursion
        memcpy(Q, G, dim * sizeof(double));
        for (int h = hist_len - 1; h >= 0; h--) {
            int idx = (hist_head - 1 - (hist_len - 1 - h) + M * 100) % M;
            const double * si = S + (size_t)idx * dim;
            const double * yi = Y + (size_t)idx * dim;
            double dot = 0.0;
            for (int k = 0; k < dim; k++) dot += si[k] * Q[k];
            alpha_hist[h] = rho[idx] * dot;
            for (int k = 0; k < dim; k++) Q[k] -= alpha_hist[h] * yi[k];
        }
        double gamma = 1.0;
        if (hist_len > 0) {
            int last = (hist_head - 1 + M) % M;
            const double *sl = S + (size_t)last * dim;
            const double *yl = Y + (size_t)last * dim;
            double sy = 0.0, yy = 0.0;
            for (int k = 0; k < dim; k++) { sy += sl[k] * yl[k]; yy += yl[k] * yl[k]; }
            if (yy > 1e-30 && sy > 1e-30) gamma = sy / yy;
        }
        for (int k = 0; k < dim; k++) P[k] = gamma * Q[k];
        for (int h = 0; h < hist_len; h++) {
            int idx = (hist_head - hist_len + h + M * 100) % M;
            const double *si = S + (size_t)idx * dim;
            const double *yi = Y + (size_t)idx * dim;
            double dot = 0.0;
            for (int k = 0; k < dim; k++) dot += yi[k] * P[k];
            double b = rho[idx] * dot;
            for (int k = 0; k < dim; k++) P[k] += si[k] * (alpha_hist[h] - b);
        }
        for (int k = 0; k < dim; k++) P[k] = -P[k];
        project_tangent(X, P);

        double g_dot_p = 0.0, p_norm_sq = 0.0;
        for (int k = 0; k < dim; k++) {
            g_dot_p += G[k] * P[k];
            p_norm_sq += P[k] * P[k];
        }
        if (g_dot_p >= 0.0 || p_norm_sq < 1e-32) {
            for (int k = 0; k < dim; k++) P[k] = -G[k];
            g_dot_p = 0.0;
            for (int k = 0; k < dim; k++) g_dot_p -= G[k] * G[k];
            hist_len = 0;
            step_guess = 1.0 / (beta > 100.0 ? beta : 100.0);
        }
        if (g_dot_p > -1e-28) break;

        double step = (hist_len > 0) ? 1.0 : step_guess;
        double f_new = f;
        double cmax_new = cmax;
        int accepted = 0;
        for (int ls = 0; ls < 25; ls++) {
            for (int k = 0; k < dim; k++) X_new[k] = X[k] + step * P[k];
            normalize_all(X_new);
            f_new = eval_lse_grad(X_new, beta, G_new, &cmax_new);
            if (cmax_new < *best_c) {
                *best_c = cmax_new;
                memcpy(best_X, X_new, dim * sizeof(double));
            }
            if (f_new <= f + 1e-4 * step * g_dot_p) {
                accepted = 1;
                break;
            }
            step *= 0.5;
        }
        if (!accepted) {
            hist_len = 0;
            step_guess *= 0.25;
            if (step_guess < 1e-15) break;
            continue;
        }

        double *si = S + (size_t)hist_head * dim;
        double *yi = Y + (size_t)hist_head * dim;
        double sy = 0.0;
        for (int k = 0; k < dim; k++) {
            si[k] = X_new[k] - X[k];
            yi[k] = G_new[k] - G[k];
            sy += si[k] * yi[k];
        }
        if (sy > 1e-28) {
            rho[hist_head] = 1.0 / sy;
            hist_head = (hist_head + 1) % M;
            if (hist_len < M) hist_len++;
        }

        memcpy(X, X_new, dim * sizeof(double));
        memcpy(G, G_new, dim * sizeof(double));
        f = f_new;
        cmax = cmax_new;
    }

    free(S); free(Y); free(G); free(G_new); free(X_new); free(P); free(Q);
}

typedef struct {
    int tid;
    int n_restarts;
    double noise_scale;
    int stages_iters;
} worker_arg_t;

static void *worker(void *arg_ptr) {
    worker_arg_t *arg = (worker_arg_t *)arg_ptr;
    int dim = N * D;
    uint64_t rng = 0x9E3779B97F4A7C15ULL ^ ((uint64_t)(arg->tid + 1) * 0xBF58476D1CE4E5B9ULL) ^ (uint64_t)time(NULL);

    double *X = malloc(dim * sizeof(double));
    double *best_X = malloc(dim * sizeof(double));
    double best_c = 2.0;

    static const double betas[] = {
        80.0, 250.0, 800.0, 2500.0, 8000.0, 25000.0,
        80000.0, 250000.0, 1000000.0, 5000000.0, 25000000.0, 100000000.0
    };
    int n_betas = (int)(sizeof(betas) / sizeof(betas[0]));

    for (int r = 0; r < arg->n_restarts; r++) {
        int is_pure_polish = (init_coords != NULL && arg->tid == 0 && r == 0);
        if (init_coords != NULL) {
            double ns = is_pure_polish ? 0.0 : arg->noise_scale * pow(0.35, (double)(r % 4));
            for (int k = 0; k < dim; k++) {
                X[k] = init_coords[k] + ns * rand_normal(&rng);
            }
        } else {
            for (int k = 0; k < dim; k++) {
                X[k] = rand_normal(&rng);
            }
        }
        normalize_all(X);

        double cur_best_c = compute_max_dot(X);
        memcpy(best_X, X, dim * sizeof(double));

        int start_b = is_pure_polish ? 5 : (init_coords != NULL && arg->noise_scale <= 0.005 ? 3 : 0);
        for (int b = start_b; b < n_betas; b++) {
            run_lbfgs_stage(X, betas[b], arg->stages_iters, best_X, &cur_best_c);
            if (b >= 7) {
                memcpy(X, best_X, dim * sizeof(double));
            }
        }

        pthread_mutex_lock(&best_mutex);
        if (cur_best_c < best_global_c) {
            best_global_c = cur_best_c;
            memcpy(best_global_coords, best_X, dim * sizeof(double));
            printf("[T%d r=%d] NEW BEST (d=%d, N=%d): c* = %.16f\n", arg->tid, r, D, N, best_global_c);
            fflush(stdout);
        }
        pthread_mutex_unlock(&best_mutex);
    }

    free(X);
    free(best_X);
    return NULL;
}

int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, "Usage: %s d N out.txt [in.txt|-] [restarts_per_thread] [threads] [noise_scale] [iters_per_stage]\n", argv[0]);
        return 1;
    }
    D = atoi(argv[1]);
    N = atoi(argv[2]);
    const char *out_path = argv[3];
    const char *in_path = (argc > 4) ? argv[4] : "-";
    int restarts = (argc > 5) ? atoi(argv[5]) : 2;
    int threads = (argc > 6) ? atoi(argv[6]) : 8;
    double noise = (argc > 7) ? atof(argv[7]) : 0.01;
    int iters = (argc > 8) ? atoi(argv[8]) : 180;

    int dim = N * D;
    best_global_coords = calloc(dim, sizeof(double));

    if (strcmp(in_path, "-") != 0) {
        FILE *fp = fopen(in_path, "r");
        if (fp) {
            init_coords = calloc(dim, sizeof(double));
            char line[16384];
            int row = 0;
            while (fgets(line, sizeof(line), fp) && row < N) {
                char *p = line;
                for (int col = 0; col < D; col++) {
                    init_coords[row * D + col] = strtod(p, &p);
                    while (*p == ',' || *p == ' ' || *p == '\t') p++;
                }
                row++;
            }
            fclose(fp);
            normalize_all(init_coords);
            best_global_c = compute_max_dot(init_coords);
            memcpy(best_global_coords, init_coords, dim * sizeof(double));
            printf("Loaded (%d, %d) from %s: initial c* = %.16f\n", D, N, in_path, best_global_c);
        }
    }

    pthread_t th[32];
    worker_arg_t args[32];
    for (int t = 0; t < threads; t++) {
        args[t].tid = t;
        args[t].n_restarts = restarts;
        args[t].noise_scale = noise;
        args[t].stages_iters = iters;
        pthread_create(&th[t], NULL, worker, &args[t]);
    }
    for (int t = 0; t < threads; t++) pthread_join(th[t], NULL);

    FILE *out = fopen(out_path, "w");
    if (out) {
        for (int i = 0; i < N; i++) {
            for (int k = 0; k < D; k++) {
                fprintf(out, "%s%.17g", (k == 0) ? "" : ",", best_global_coords[i * D + k]);
            }
            fprintf(out, "\n");
        }
        fclose(out);
    }
    printf("FINAL (%d, %d): best c* = %.16f -> %s\n", D, N, best_global_c, out_path);
    return 0;
}
