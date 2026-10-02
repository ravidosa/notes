import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge, central_2nd

coords = np.mgrid[-25:26,-25:26]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
charge_list = [Charge(0, 7, 1), Charge(0, -7, -1)]
V = charge_list[0].potential_grid(xgrid, ygrid) + charge_list[1].potential_grid(xgrid, ygrid)
dy_cen, dx_cen = central_2nd(V, 1)
dy_ch, dx_ch = tuple(map(sum, zip(charge_list[0].field_grid(xgrid, ygrid), charge_list[1].field_grid(xgrid, ygrid))))
fr_y, fr_x = np.abs(dy_ch - -dy_cen) / np.abs(dy_ch), np.abs(dx_ch - -dx_cen) / np.abs(dx_ch)

fig, ax = plt.subplots(1, 3, gridspec_kw={"width_ratios": [3, 3, 2]})
plt.gca().set_aspect("equal")
ax[0].imshow(fr_x)
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
ax[0].set_title("Fractional Error\n($x$-direction)")
plt.sca(ax[1])
i = ax[1].imshow(fr_y)
ax[1].set_xlabel("x")
ax[1].set_title("Fractional Error\n($y$-direction)")
fig.delaxes(ax[2])
fig.subplots_adjust(right=0.8)
fig.colorbar(i, ax=ax.ravel().tolist(), orientation='vertical')
fig.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-2.png"))
plt.show()
print(np.nanmax(fr_x[np.isfinite(fr_x)]), np.nanmax(fr_y[np.isfinite(fr_y)]))
# the fractional error is significantly larger than machine precision (~10^0)
# this is likely because the \Delta x = 1 used in to calculate the electric field is so large
# using the central difference method then results in an O(1^3) = O(1) error in the value of the electric field, which agrees with the fractional errors