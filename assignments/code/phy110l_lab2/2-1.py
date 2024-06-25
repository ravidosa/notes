import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge, central_2nd

coords = np.mgrid[-25:26,-25:26]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
charge_list = [Charge(0, 7, 1), Charge(0, -7, -1)]
V = charge_list[0].potential_grid(xgrid, ygrid) + charge_list[1].potential_grid(xgrid, ygrid)
dy_cen, dx_cen = central_2nd(V, 1)
dy_gr, dx_gr = np.gradient(V)
E_theta_gr = np.degrees(np.arctan2(-dy_gr, -dx_gr))
E_theta_cen = np.degrees(np.arctan2(-dy_cen, -dx_cen))

fig, ax = plt.subplots(1, 3, gridspec_kw={"width_ratios": [3, 3, 2]})
plt.gca().set_aspect("equal")
ax[0].imshow(E_theta_gr, cmap="hsv")
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
ax[0].set_title("Dipole (gradient)")
plt.sca(ax[1])
i = ax[1].imshow(E_theta_cen, cmap="hsv")
ax[1].set_xlabel("x")
ax[1].set_title("Dipole (central diff.)")
fig.delaxes(ax[2])
fig.subplots_adjust(right=0.8)
fig.colorbar(i, ax=ax.ravel().tolist(), orientation='vertical')
fig.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-1.png"))
plt.show()
