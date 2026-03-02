import numpy as np
import matplotlib.pyplot as plt
import os
from utils import V

N = 100
V0 = 1
L = 100
coeffs = (lambda n : n * np.pi / L, lambda n : 0, lambda n : 0, lambda n : 4 * V0 / (n * np.pi) * (n % 2), lambda n : 0)

coords = np.mgrid[0:2 * L + 1, 0:L + 1]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
Vgrid = V(xgrid, ygrid, coeffs, N)
V_anal = 2 * V0 / np.pi * np.arctan2(np.sin(np.pi / L * xgrid), np.sinh(np.pi / L * ygrid))
plt.imshow(np.abs((Vgrid - V_anal) / V_anal))
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Series Approximation Fractional Error")
plt.savefig(os.path.join(os.path.dirname(__file__), "5-3.png"))
plt.show()

# the biggest fractional errors are near the y = 2L boundary at either x = 0, L boundary
# this makes sense, as at small y, the exponential term dominates, and the largest error comes from the approximation of V = V0 at y = 0 using a fourier series, so when the sines dominate at large y, more error is visible