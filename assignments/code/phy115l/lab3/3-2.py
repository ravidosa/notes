import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.optimize
from utils import tise_rk4, feven, fodd, V_fin_pot

b = 8
tol = 1e-3
plt.axvline(x = 1, c = "k")
plt.axvline(x = -1, c = "k")
plt.ylim(-1, 1)
z0 = np.pi
E = scipy.optimize.bisect(feven, (np.pi * (0 + tol)) ** 2 - z0 ** 2, (np.pi * (1/2 - tol)) ** 2 - z0 ** 2, args = (V_fin_pot, (z0), b))
print("even E:", E)
X,PSI = tise_rk4(E = E, V = V_fin_pot, par = (z0), psi0 = 1, phi0 = 0, a = 0, b = 2, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((np.flip(PSI), PSI)), label = "n = 1")
E = scipy.optimize.bisect(fodd, (np.pi * (1/2 + tol)) ** 2 - z0 ** 2, (np.pi * (1 - tol)) ** 2 - z0 ** 2, args = (V_fin_pot, (z0), b))
print("odd E:", E)
X,PSI = tise_rk4(E = E, V = V_fin_pot, par = (z0), psi0 = 0, phi0 = 1, a = 0, b = 2, h = 0.01)
PSI = PSI / np.sqrt(2 * (np.sum(np.square(np.abs(PSI))) * 0.01))
plt.plot(np.concatenate((-np.flip(X), X)), np.concatenate((-np.flip(PSI), PSI)), label = "n = 2")
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.title("Finite Square Well TISE")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "3-2.png"))
plt.show()