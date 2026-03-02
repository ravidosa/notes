import numpy as np
import matplotlib.pyplot as plt
import os
from utils import relaxation, V_boundary_infplates, V_boundary_infplates_corr

eps = 1e-5
R = 25
coords = np.mgrid[-R:R + 1,-R:R + 1]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
boundary_mask, V_orig = V_boundary_infplates((0, 0), 0.4 * R, 1, xgrid, ygrid)

V = V_orig.copy()
V, iter = relaxation(V, boundary_mask, eps, cond="periodicx")

fig = plt.figure()

gs = fig.add_gridspec(2,2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[:, 1])

i1 = ax1.imshow(V_orig)
fig.colorbar(i1, ax=ax1,orientation='vertical')
i2 = ax2.imshow(V)
fig.colorbar(i2, ax=ax2,orientation='vertical')
ax3.plot(ygrid[:,26], V[:,26])
ax3.set_xlabel("y")
ax3.set_ylabel("V")
ax3.set_title("Central cut")
fig.suptitle("Infinite Plates")
fig.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "4-4a.png"))
plt.show()

boundary_mask, V_orig = V_boundary_infplates_corr((0, 0), 0.4 * R, 1, xgrid, ygrid)

V = V_orig.copy()
V, iter = relaxation(V, boundary_mask, eps, cond="periodicx")

fig = plt.figure()

gs = fig.add_gridspec(2,2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[:, 1])

i1 = ax1.imshow(V_orig)
fig.colorbar(i1, ax=ax1,orientation='vertical')
i2 = ax2.imshow(V)
fig.colorbar(i2, ax=ax2,orientation='vertical')
ax3.plot(ygrid[:,26], V[:,26])
ax3.set_xlabel("y")
ax3.set_ylabel("V")
ax3.set_title("Central cut")
fig.suptitle("Infinite Plates (with correction)")
fig.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "4-4b.png"))
plt.show()

# the potential has not converged to 0 everywhere outside the plate because due to the nature of the relaxation technique, it becomes a linear gradient from the potential at V = +-0.2R to the top and bottom edges
# to correct for this, we can set V = 0 right above/below the plates instead