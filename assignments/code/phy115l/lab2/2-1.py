import numpy as np
import matplotlib.pyplot as plt
import os
from utils import tise_rk1, tise_rk4, V_inf_pot

plt.figure(1)
for n in [0.7, 1, 1.3]:
    X,PSI = tise_rk1(E = (np.pi * n) ** 2, V = V_inf_pot, psi0 = 1, phi0 = 0, a = 0, b = 0.5, h = 0.01)
    print("n =", str(n) + ", psi(b) = ", PSI[-1])
    plt.plot(X, PSI, label = "n = " + str(n))

plt.axhline(c = "k")
plt.axvline(x = 0.5, c = "k")
plt.ylim(-1.5, 1.5)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Infinite Potential Well TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-1a.png"))
plt.show()

plt.figure(2)
for n in [1, 3, 5]:
    X,PSI = tise_rk1(E = (np.pi * n) ** 2, V = V_inf_pot, psi0 = 1, phi0 = 0, a = 0, b = 0.5, h = 0.01)
    print("n =", str(n) + ", psi(b) = ", PSI[-1])
    plt.plot(X, PSI, label = "n = " + str(n))

plt.axhline(c = "k")
plt.axvline(x = 0.5, c = "k")
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Infinite Potential Well TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-1b.png"))
plt.show()

plt.figure(3)
for n in [5]:
    X1,PSI1 = tise_rk1(E = (np.pi * n) ** 2, V = V_inf_pot, psi0 = 1, phi0 = 0, a = 0, b = 0.5, h = 0.01)
    print("n =", str(n) + ", psi(b) = ", PSI1[-1])
    plt.plot(X1, PSI1, label = "RK-1, n = " + str(n))
    X4,PSI4 = tise_rk4(E = (np.pi * n) ** 2, V = V_inf_pot, psi0 = 1, phi0 = 0, a = 0, b = 0.5, h = 0.01)
    print("n =", str(n) + ", psi(b) = ", PSI4[-1])
    plt.plot(X4, PSI4, label = "RK-4, n = " + str(n))

plt.axhline(c = "k")
plt.axvline(x = 0.5, c = "k")
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Infinite Potential Well TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-1c.png"))
plt.show()

plt.figure(4)
for n in range(1, 7):
    X,PSI = tise_rk4(E = (np.pi * n) ** 2, V = V_inf_pot, psi0 = 1 if (n % 2 == 1) else 0, phi0 = 0 if (n % 2 == 1) else 1, a = 0, b = 0.5, h = 0.01)
    PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
    print("n =", str(n) + ", psi(b) = ", PSI[-1])
    plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate(((2 * (n % 2) - 1) * np.flip(PSI), PSI)), label = "n = " + str(n))

plt.axhline(c = "k")
plt.axvline(x = 0.5, c = "k")
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Infinite Potential Well TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-1d.png"))
plt.show()