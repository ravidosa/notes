import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.optimize
from utils import tise_rk4, feven, fodd, feven_t, V_fin_pot_sym

z0 = np.pi / 2
tol = 1e-3
delta = 3
b = 8
plt.figure(1)
plt.axvline(x = delta, c = "k")
plt.axvline(x = -delta, c = "k")
plt.axvline(x = delta + 2, c = "k")
plt.axvline(x = -delta - 2, c = "k")
plt.ylim(-1, 1)
E = scipy.optimize.bisect(feven, -np.pi * (0 + tol), -np.pi * (1 - tol), xtol=1e-4, args=(V_fin_pot_sym, (z0, delta), b))
print(E)
X,PSI = tise_rk4(E = E, V = V_fin_pot_sym, par = (z0, delta), psi0 = 1, phi0 = 0, a = 0, b = b, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((np.flip(PSI), PSI)))
plt.axhline(c = "k")
plt.ylim(-1, 1)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Symmetric Finite Square Well TISE (even)")
plt.savefig(os.path.join(os.path.dirname(__file__), "3-3a.png"))
plt.show()

plt.figure(2)
plt.axvline(x = delta, c = "k")
plt.axvline(x = -delta, c = "k")
plt.axvline(x = delta + 2, c = "k")
plt.axvline(x = -delta - 2, c = "k")
plt.ylim(-1, 1)
E = scipy.optimize.bisect(fodd, -np.pi * (0 + tol), -np.pi * (1 - tol), xtol=1e-4, args=(V_fin_pot_sym, (z0, delta), b))
print(E)
X,PSI = tise_rk4(E = E, V = V_fin_pot_sym, par = (z0, delta), psi0 = 0, phi0 = 1, a = 0, b = b, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((-np.flip(PSI), PSI)))
plt.axhline(c = "k")
plt.ylim(-1, 1)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Symmetric Finite Square Well TISE (odd)")
plt.savefig(os.path.join(os.path.dirname(__file__), "3-3b.png"))
plt.show()

plt.figure(3)
delta_min = 0
delta_max = 3
M = 50
E = np.zeros(M)
E_ = np.zeros(M)
delta_arr = np.linspace(delta_min, delta_max, M)
for i, delta in enumerate(delta_arr):
    b = delta + 3
    E[i] = scipy.optimize.bisect(feven, -np.pi * (0 + tol), -np.pi * (1 - tol), xtol=1e-4, args=(V_fin_pot_sym, (z0, delta), b))
    z = scipy.optimize.bisect(feven_t, np.pi * (0 + tol), np.pi * (1/2 - tol), args = (z0))
    E_[i] = z ** 2 - z0 ** 2
plt.plot(delta_arr, E - E_)
plt.xlabel("$\delta$")
plt.ylabel("$Bonding Energy$")
plt.title("Bonding Energy vs $\delta$")
plt.savefig(os.path.join(os.path.dirname(__file__), "3-3c.png"))
plt.show()

plt.figure(4)
z0 = np.pi / 2
tol = 1e-3
delta = 3
b = 8
plt.axvline(x = delta, c = "k")
plt.axvline(x = -delta, c = "k")
plt.axvline(x = delta + 2, c = "k")
plt.axvline(x = -delta - 2, c = "k")
plt.ylim(-1, 1)
E = scipy.optimize.bisect(feven, -np.pi * (0 + tol), -np.pi * (1 - tol), xtol=1e-4, args=(V_fin_pot_sym, (z0, delta), b))
X,PSI = tise_rk4(E = E, V = V_fin_pot_sym,par = (z0, delta), psi0 = 1, phi0 = 0, a = 0, b = b, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((np.flip(PSI), PSI)), label="delta = 3")
delta = 0.5
b = 5
plt.axvline(x = delta, c = "r")
plt.axvline(x = -delta, c = "r")
plt.axvline(x = delta + 2, c = "r")
plt.axvline(x = -delta - 2, c = "r")
plt.ylim(-1, 1)
E = scipy.optimize.bisect(feven, -np.pi * (0 + tol), -np.pi * (1 - tol), xtol=1e-4, args=(V_fin_pot_sym, (z0, delta), b))
X,PSI = tise_rk4(E = E, V = V_fin_pot_sym, par = (z0, delta), psi0 = 1, phi0 = 0, a = 0, b = b, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((np.flip(PSI), PSI)), label="delta = 0.5")
plt.axhline(c = "k")
plt.ylim(-1, 1)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Symmetric Finite Square Well TISE (even)")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "3-3d.png"))
plt.show()

plt.figure(5)
z0 = np.pi / 2
tol = 1e-3
delta = 3
b = 8
plt.axvline(x = delta, c = "k")
plt.axvline(x = -delta, c = "k")
plt.axvline(x = delta + 2, c = "k")
plt.axvline(x = -delta - 2, c = "k")
plt.ylim(-1, 1)
E = scipy.optimize.bisect(fodd, -np.pi * (0 + tol), -np.pi * (1 - tol), xtol=1e-4, args=(V_fin_pot_sym, (z0, delta), b))
print(E)
X,PSI = tise_rk4(E = E, V = V_fin_pot_sym, par = (z0, delta), psi0 = 0, phi0 = 1, a = 0, b = b, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((-np.flip(PSI), PSI)), label="delta = 3")
delta = 0.5
b = 5
plt.axvline(x = delta, c = "r")
plt.axvline(x = -delta, c = "r")
plt.axvline(x = delta + 2, c = "r")
plt.axvline(x = -delta - 2, c = "r")
plt.ylim(-1, 1)
E = scipy.optimize.bisect(fodd, -np.pi * (0 + tol), -np.pi * (1 - tol), xtol=1e-4, args=(V_fin_pot_sym, (z0, delta), b))
print(E)
X,PSI = tise_rk4(E = E, V = V_fin_pot_sym, par = (z0, delta), psi0 = 0, phi0 = 1, a = 0, b = b, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((-np.flip(PSI), PSI)), label="delta = 0.5")
plt.axhline(c = "k")
plt.ylim(-1, 1)
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Symmetric Finite Square Well TISE (odd)")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "3-3e.png"))
plt.show()