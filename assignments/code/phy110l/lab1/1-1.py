import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge

coords = np.mgrid[-25:26,-25:26]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
charge_list = [Charge(0, 7, -1), Charge(0, -7, -1)]
V = charge_list[0].potential(xgrid, ygrid) + charge_list[1].potential(xgrid, ygrid)
plt.imshow(V)
plt.colorbar()
plt.contour(V, np.linspace(-1, 0, 10), colors="k")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Two Negative Charges")
plt.savefig(os.path.join(os.path.dirname(__file__), "1-1.png"))
plt.show()

plt.gca().set_aspect("equal")