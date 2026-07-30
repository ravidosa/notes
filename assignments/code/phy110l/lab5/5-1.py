import numpy as np
import matplotlib.pyplot as plt
import os
from utils import V

N = 10
V0 = 1
L = 100
coeffs = (lambda n : n * np.pi / L, lambda n : 0, lambda n : 0, lambda n : 4 * V0 / (n * np.pi) * (n % 2), lambda n : 0)

coords = np.mgrid[0:2 * L + 1, 0:L + 1]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
for i, N in enumerate([1, 5, 10, 50, 100]):
    Vgrid = V(xgrid, ygrid, coeffs, N)
    fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
    ax.plot_surface(xgrid,ygrid,Vgrid)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("V")
    ax.set_title("Potential in Semi-Infinite Open Box (" + str(N) + " terms)")
    plt.savefig(os.path.join(os.path.dirname(__file__), "5-1" + chr(97 + i) + ".png"))
    plt.show()
# as N increases, the boundary condition that V = V0 at x = 0 becomes better
# this is because the V = 0 at y = 0, L boundary condition is already met by each of the sine functions
# using more terms in the fourier series better approximates the V = V0 condition since we need to approximate the plateau using only sines and cosines