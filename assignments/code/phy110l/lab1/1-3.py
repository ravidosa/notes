import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge

coords = np.mgrid[-25:26,-25:26]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
charge_list = [Charge(-7, 7, 1), Charge(7, -7, 1), Charge(-7, -7, -1), Charge(7, 7, -1)]
V = charge_list[0].potential(xgrid, ygrid) + charge_list[1].potential(xgrid, ygrid) + charge_list[2].potential(xgrid, ygrid) + charge_list[3].potential(xgrid, ygrid)
plt.figure(figsize=(6,6))
plt.imshow(V)
plt.colorbar()
plt.contour(V, np.linspace(-0.05, 0.05, 10), colors="k")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadrupole")
plt.figtext(0.125, 0.02, "For an electric quadrupole, the potential falls off as $1/r^3$.\nAs this charge distribution has zero net charge and dipole moment,\nthe quadrupole moment is the most significant term.\nIt can be used to model nuclei.", wrap=True, fontsize=8)
plt.savefig(os.path.join(os.path.dirname(__file__), "1-3.png"))
plt.show()

plt.gca().set_aspect("equal")