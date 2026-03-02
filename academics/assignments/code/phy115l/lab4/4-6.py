import numpy as np
import matplotlib.pyplot as plt
import os
from utils import norm, energy, V_qho

a = -3
b = 3
N = 100
x = np.linspace(a, b, N)
y = np.piecewise(x, [x < -0.8, (-0.8 <= x) & (x < 0.8), 0.8 <= x], [0, 1, 0])
y = norm(x, y)
E = energy(x, y, V_qho, ())
print(E)
plt.ylim((0, 1))
plt.plot(x, V_qho(x, ()), "k:")
plt.plot(x, y, label="original $\psi^0$")
ann = [(1, 10000), (0.1, 100000), (0.01, 200000), (0.001, 500000)]
for j, (delta_y, M) in enumerate(ann):
    E__ = E
    for _ in range(M):
        i = np.random.randint(1, N - 1)
        y_ = np.copy(y)
        y_[i] += np.random.uniform(0, delta_y)
        y_ = norm(x, y_)
        E_ = energy(x, y_, V_qho, ())
        if E_ < E:
            y, E = y_, E_
    print(E, round(abs(E__ - E) / E * 100, 2), "% error")
    if j < len(ann) - 1 and j in [0, 3]:
        plt.plot(x, y, label="$\psi^" + str(j + 1) + "$")
    elif j == len(ann) - 1:
        plt.plot(x, y, label="final $\psi^" + str(j + 1) + "$")
exp = 1
print("expected E:", exp, round(abs(exp - E) / E * 100, 2), "% error")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Variational Method (quantum harmonic oscillator)")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "4-6.png"))
plt.show()
# wavefunction and energy approach expected ground state values with more iterations of simulated annealing
# numerical uncertainty of h = (3 - -3)/100 = 0.06