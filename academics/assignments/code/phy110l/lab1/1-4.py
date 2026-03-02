import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge

coords = np.mgrid[-25:26,-25:26]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
charge_list = [Charge(0, 7, 1), Charge(0, -7, -1)]
V = charge_list[0].potential(xgrid, ygrid) + charge_list[1].potential(xgrid, ygrid)
dy, dx = np.gradient(V)
E_theta = np.degrees(np.arctan2(-dy, -dx))
plt.imshow(E_theta, cmap="hsv")
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Dipole")
plt.savefig(os.path.join(os.path.dirname(__file__), "1-4.png"))
plt.show()

plt.gca().set_aspect("equal")