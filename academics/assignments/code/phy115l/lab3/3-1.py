import numpy as np
import scipy.optimize
from utils import feven_t, fodd_t

tol = 1e-3
z0 = np.pi / 2
print("z_0 =", z0)
z = scipy.optimize.bisect(feven_t, np.pi * (0 + tol), np.pi * (1/2 - tol), args = (z0))
E = z ** 2 - z0 ** 2
print("E =", E)

print("")
z0 = np.pi
print("z_0 =", z0)
z = scipy.optimize.bisect(feven_t, np.pi * (0 + tol), np.pi * (1/2 - tol), args = (z0))
E = z ** 2 - z0 ** 2
print("E_even =", E)
z = scipy.optimize.bisect(fodd_t, np.pi * (1/2 + tol), np.pi * (1 - tol), args = (z0))
E = z ** 2 - z0 ** 2
print("E_odd =", E)

print("")
z0 = 3 * np.pi
print("z_0 =", z0)
for i in range(int(np.ceil(z0 / np.pi))):
    z = scipy.optimize.bisect(feven_t, np.pi * (i + tol), np.pi * (i + 1/2 - tol), args = (z0))
    E = z ** 2 - z0 ** 2
    print("E_" + str(2 * i + 2) + " =", E)
    z = scipy.optimize.bisect(fodd_t, np.pi * (i + 1/2 + tol), np.pi * (i + 1 - tol), args = (z0))
    E = z ** 2 - z0 ** 2
    print("E_" + str(2 * i + 1) + " =", E)

print("")
z0 = 100 * np.pi
print("z_0 =", z0)
for i in range(2):
    z = scipy.optimize.bisect(feven_t, np.pi * (i + tol), np.pi * (i + 1/2 - tol), args = (z0))
    E = z ** 2 - z0 ** 2
    K = E + z0 ** 2
    print("[finite well]\tK_" + str(2 * i + 2) + " =", K)
    print("[infinite well]\tE_" + str(2 * i + 1) + " =", ((2 * i + 1) * np.pi / 2) ** 2)
    z = scipy.optimize.bisect(fodd_t, np.pi * (i + 1/2 + tol), np.pi * (i + 1 - tol), args = (z0))
    E = z ** 2 - z0 ** 2
    K = E + z0 ** 2
    print("[finite well]\tK_" + str(2 * i + 1) + " =", K)
    print("[infinite well]\tE_" + str(2 * i + 2) + " =", ((2 * i + 2) * np.pi / 2) ** 2)