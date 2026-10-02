import numpy as np

def crout_tridiagonal(A, b):
    N = np.size(b)
    L, U = np.zeros((N, N)), np.eye(N)
    z, x = np.zeros(N), np.zeros(N)

    L[0, 0] = A[0, 0]
    U[0, 1] = A[0, 1] / L[0, 0]
    z[0] = b[0] / L[0, 0]

    for i in range(1, N - 1):
        L[i, i - 1] = A[i, i - 1]
        L[i, i] = A[i, i] - L[i, i - 1] * U[i - 1, i]
        U[i, i + 1] = A[i, i + 1] / L[i, i]
        z[i] = (b[i] - L[i, i - 1] * z[i - 1]) / L[i, i]
    
    L[N - 1, N - 2] = A[N - 1, N - 2]
    L[N - 1, N - 1] = A[N - 1, N - 1] - L[N - 1, N - 2] * U[N - 2, N - 1]
    z[N - 1] = (b[N - 1] - L[N - 1, N - 2] * z[N - 2]) / L[N - 1, N - 1]

    x[N - 1] = z[N - 1]
    for i in range(N - 2, -1, -1):
        x[i] = z[i] - U[i, i + 1] * x[i + 1]

    return x

def linear_ode_bvp_center_diff(p, q, r, a, b, alf, bet, N):
    h = (b - a) / (N + 1)
    A = np.zeros((N, N))
    d = np.zeros(N)
    w = np.zeros(N + 2)

    x = a + h
    A[0, 0] = 2 + h ** 2 * q(x)
    A[0, 1] = -1 + h / 2 * p(x)
    d[0] = -h ** 2 * r(x) + (1 + h / 2 * p(x)) * alf

    for i in range(1, N - 1):
        x = a + i * h
        A[i, i] = 2 + h ** 2 * q(x)
        A[i, i + 1] = -1 + h / 2 * p(x)
        A[i, i - 1] = -1 - h / 2 * p(x)
        d[i] = -h ** 2 * r(x)
    
    x = b - h
    A[N - 1, N - 1] = 2 + h ** 2 * q(x)
    A[N - 1, N - 2] = -1 - h / 2 * p(x)
    d[N - 1] = -h ** 2 * r(x) + (1 - h / 2 * p(x)) * bet

    w[0], w[N + 1] = alf, bet
    w[1:N + 1] = crout_tridiagonal(A, d)

    return w

def rayleigh_ritz(p, q, f, x, N):
    h = x[1:] - x[:-1]
    Q = np.zeros((6, N + 1))
    A, b = np.zeros((N, N)), np.zeros(N)
    c = np.zeros(N + 2)

    for i in range(N):
        Q[0, i] = h[i] / 12 * (q(x[i + 1]) + q(x[i + 2]))
        Q[1, i] = h[i - 1] / 12 * (3 * q(x[i + 1]) + q(x[i]))
        Q[2, i] = h[i] / 12 * (3 * q(x[i + 1]) + q(x[i + 2]))
        Q[3, i] = 1 / (2 * h[i - 1]) * (p(x[i + 1]) + p(x[i]))
        Q[4, i] = h[i - 1] / 6 * (2 * f(x[i + 1]) + f(x[i]))
        Q[5, i] = h[i] / 6 * (2 * f(x[i + 1]) + f(x[i + 2]))
    Q[3, N] = 1 / (2 * h[N - 1]) * (p(x[N + 1]) + p(x[N]))

    for i in range(N - 1):
        A[i, i] = Q[3, i] + Q[3, i + 1] + Q[1, i] + Q[2, i]
        A[i, i + 1] = -Q[3, i + 1] + Q[0, i]
        A[i, i - 1] = -Q[3, i] + Q[0, i - 1]
        b[i] = Q[4, i] + Q[5, i]
    A[N - 1, N - 1] = Q[3, N - 1] + Q[3, N] + Q[1, N - 1] + Q[2, N - 1]
    A[N - 1, N - 2] = -Q[3, N - 1] + Q[0, N - 2]
    b[N - 1] = Q[4, N - 1] + Q[5, N - 1]

    c = crout_tridiagonal(A, b)

    phi = np.vectorize(lambda x_ : sum([c[i - 1] * ((x_ - x[i - 1]) / h[i - 1] if x[i - 1] < x_ and x_ <= x[i] else (x[i + 1] - x_) / h[i] if x[i] < x_ and x_ <= x[i + 1] else 0) for i in range(1, N + 1)]))
    w = np.zeros(N + 2)
    w = phi(x)

    return w

def SOR(A, b, omega, x_0, epsilon=1e-8):
    x = x_0
    n = len(b)
    x_t = 1 + x_0
    x_arr = np.array([np.linalg.norm(np.matmul(A, x) - b)])
    i = 0
    while True:
        i += 1
        x_t = x.copy()
        for j in range(n):
            x_t[j] = (1 - omega) * x[j] + omega/A[j][j] * (-1 * (np.dot(A[j, :j], x_t[:j]) + np.dot(A[j, j+1:], x[j+1:])) + b[j])
        if np.abs(np.linalg.norm(x - x_t)/np.linalg.norm(x)) <= epsilon:
            x = x_t.copy()
            x_arr = np.append(x_arr, np.linalg.norm(np.matmul(A, x) - b))
            break
        x = x_t.copy()
        x_arr = np.append(x_arr, np.linalg.norm(np.matmul(A, x) - b))
    return x, i, x_arr

def elliptical_pde_bvp_center_diff(f, g, a, b, c, d, M, N, epsilon=1e-8):
    h, k = (b - a) / N, (d - c) / M
    x, y = np.linspace(a, b, N + 1), np.linspace(c, d, M + 1)
    size = (N - 1) * (M - 1)

    lam = h ** 2 / k ** 2
    mu = 2 * (1 + lam)
    l = 1
    A = np.zeros((size, size))
    b_ = np.zeros(size)

    for k in range(size):
        i, j = k % (M - 1), k // (N - 1)
        A[k, k] = mu
        if i > 0:
            A[k, k - 1] = -l
        if i < (M - 1) - 1:
            A[k, k + 1] = -l
        if j > 0:
            A[k - (N - 1), k] = -lam
        if j < (N - 1) - 1:
            A[k + (N - 1), k] = -lam
        b_[k] = -h ** 2 * f(x[i + 1], y[j + 1])
        if i == 0:
            b_[k] += g(a, y[j + 1])
        if i == (N - 1) - 1:
            b_[k] += g(b, y[j + 1])
        if j == 0:
            b_[k] += g(x[i + 1], c)
        if j == (M - 1) - 1:
            b_[k] += g(x[i + 1], d)
    
    w, _, _ = SOR(A, b_, 4 / (2 + np.sqrt(4 - (np.cos(np.pi / M) + np.cos(np.pi / N)) ** 2)), np.zeros_like(b_), epsilon)
    return w