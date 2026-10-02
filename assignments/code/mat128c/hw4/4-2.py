import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from utils import rayleigh_ritz

a, b = 0, 1
alf, bet = 0, 1
p = lambda x : x ** 2 + 1
q = lambda x : x
f = lambda x : x ** 6 - 30 * x ** 5 - 20 * x ** 3
F = lambda x : f(x) + (bet - alf) * 2 * x - (bet * x + alf * (1 - x)) * q(x)
u_x = lambda x : x ** 5

N_min, N_max = 2, 128
h = (b - a) / np.arange(N_min, N_max + 1)
e_N = np.zeros(N_max - N_min + 1)

for N in range(N_min, N_max + 1):
    x = np.linspace(a, b, N + 2)
    w_ = rayleigh_ritz(p, q, F, x, N)
    w = w_ + bet * x + alf * (1 - x)

    u = u_x(x)
    e = np.abs(w - u)
    e_N[N - N_min] = np.max(e)

popt, pcov = sp.optimize.curve_fit(lambda x, a, b : a * x + b, np.log10(h[5:]), np.log10(e_N[5:]))
print(popt)
h_ = np.linspace(np.min(h), np.max(h))
plt.plot(np.log10(h), np.log10(e_N), label="error")
plt.plot(np.log10(h_), popt[0] * np.log10(h_) + popt[1], label="fit")
plt.xlabel("$\log\Delta t$")
plt.ylabel("$\log\hat{e}^N$")
plt.title("Error vs. step size (Rayleigh-Ritz)")
plt.legend()
plt.show()