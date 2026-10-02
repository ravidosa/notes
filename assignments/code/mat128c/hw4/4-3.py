import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from utils import elliptical_pde_bvp_center_diff

f = lambda x, y : -8 * np.pi ** 2 * np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y)
g = lambda x, y : 0
a, b, c, d = 0, 1, 0, 1
u_xy = lambda x, y : np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y)

N_min, N_max = 2, 128
h = (b - a) / np.arange(N_min, N_max + 1)
e_N = np.zeros(N_max - N_min + 1)

for N in range(N_min, N_max + 1):
    print(N)
    w = elliptical_pde_bvp_center_diff(f, g, a, b, c, d, N, N, 1e-4)

    y, x = np.meshgrid(np.linspace(a, b, N + 1)[1:-1], np.linspace(c, d, N + 1)[1:-1])
    
    u = np.reshape(u_xy(x, y), (N - 1) ** 2)
    e = np.abs(w - u)
    e_N[N - N_min] = np.max(e)

popt, pcov = sp.optimize.curve_fit(lambda x, a, b : a * x + b, np.log10(h[1:]), np.log10(e_N[1:]))
print(popt)
h_ = np.linspace(np.min(h), np.max(h))
plt.plot(np.log10(h), np.log10(e_N), label="error")
plt.plot(np.log10(h_), popt[0] * np.log10(h_) + popt[1], label="fit")
plt.xlabel("$\log\Delta t$")
plt.ylabel("$\log\hat{e}^N$")
plt.title("Error vs. step size (Centered difference)")
plt.legend()
plt.show()