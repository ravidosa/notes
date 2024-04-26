import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.optimize
from utils import tise_rk4, feven, fodd, V_sawtooth

b = 8

E = np.zeros(6)
for n in range(6):
    eneg = scipy.optimize.bisect(feven if n % 2 == 0 else fodd, n, n + 1.5, xtol=1e-4, args=(V_sawtooth, b))
    print("n =", str(n) + ", E =", eneg)
    E[n] = eneg

for n in range(6):
    X,PSI = tise_rk4(E = E[n], V = V_sawtooth, psi0 = 0 if (n % 2 == 1) else (-1) ** (n // 2), phi0 = (-1) ** (n // 2) if (n % 2 == 1) else 0, a = 0, b = 7.5, h = 0.01)
    PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
    print("n =", str(n) + ", psi(b) = ", PSI[-1])
    plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate(((2 * ((n + 1) % 2) - 1) * np.flip(PSI), PSI)), label = "n = " + str(n))

plt.axhline(c = "k")
plt.ylim(-1, 1)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Sawtooth Potential TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-4.png"))
plt.show()