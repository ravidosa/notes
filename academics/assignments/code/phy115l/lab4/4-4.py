import numpy as np
import matplotlib.pyplot as plt
import os
from utils import norm, energy, V_inf_pot

B = 100000
a = -1.2
b = 1.2
N = 50
x = np.linspace(a, b, N)
y = np.piecewise(x, [x < -0.8, (-0.8 <= x) & (x < 0.8), 0.8 <= x], [0, 1, 0])
y = norm(x, y)
E = energy(x, y, V_inf_pot, (B))
print(E)
plt.ylim((0, 1.5))
plt.plot(x, V_inf_pot(x, (B)), "k:")
plt.plot(x, y, label="original $\psi^0$")
ann = [(1, 10000), (0.1, 100000), (0.01, 200000), (0.001, 500000)]
for j, (delta_y, M) in enumerate(ann):
    E__ = E
    for _ in range(M):
        i = np.random.randint(1, N - 1)
        y_ = np.copy(y)
        y_[i] += np.random.uniform(0, delta_y)
        y_ = norm(x, y_)
        E_ = energy(x, y_, V_inf_pot, (B))
        if E_ < E:
            y, E = y_, E_
    print(E, round(abs(E__ - E) / E * 100, 2), "% error")
    if j < len(ann) - 1 and j in [0, 1]:
        plt.plot(x, y, label="$\psi^" + str(j + 1) + "$")
    elif j == len(ann) - 1:
        plt.plot(x, y, label="final $\psi^" + str(j + 1) + "$")
exp = np.pi ** 2 / 4
print("expected E:", exp, round(abs(exp - E) / E * 100, 2), "% error")
plt.plot(x, np.piecewise(x, [x < -1, (-1 <= x) & (x < 1), 1 <= x], [0, lambda x: np.cos(np.pi * x / 2), 0]), label="$\psi_0(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Variational Method (infinite square well)")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "4-4.png"))
plt.show()
# wavefunction and energy approach expected ground state values with more iterations of simulated annealing
# numerical uncertainty of h = (1.2 - -1.2)/50 = 0.048