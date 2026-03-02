import numpy as np
import matplotlib.pyplot as plt
import os
from utils import tise_rk4, V_qho

plt.figure(1)
for n in range(4):
    X,PSI = tise_rk4(E = 2 * n + 1, V = V_qho, psi0 = 0 if (n % 2 == 1) else (-1) ** (n // 2), phi0 = (-1) ** (n // 2) if (n % 2 == 1) else 0, a = 0, b = 5, h = 0.01)
    PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
    print("n =", str(n) + ", psi(b) = ", PSI[-1])
    plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate(((2 * ((n + 1) % 2) - 1) * np.flip(PSI), PSI)), label = "n = " + str(n))

plt.axhline(c = "k")
plt.ylim(-1, 1)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Quantum Harmonic Oscillator TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-2a.png"))
plt.show()

plt.figure(2)
for n in range(4):
    X,PSI = tise_rk4(E = 2 * n + 1, V = V_qho, psi0 = 0 if (n % 2 == 1) else (-1) ** (n // 2), phi0 = (-1) ** (n // 2) if (n % 2 == 1) else 0, a = 0, b = 10, h = 0.01)
    #PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01)) can't normalize if diverges
    print("n =", str(n) + ", psi(b) = ", PSI[-1])
    plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate(((2 * ((n + 1) % 2) - 1) * np.flip(PSI), PSI)), label = "n = " + str(n))

plt.axhline(c = "k")
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Quantum Harmonic Oscillator TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-2b.png"))
plt.show()