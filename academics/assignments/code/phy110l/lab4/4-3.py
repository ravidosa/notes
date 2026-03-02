import numpy as np
import matplotlib.pyplot as plt
import os
from utils import relaxation, V_boundary_infinity

eps = 1e-8
R = 100
coords = np.mgrid[-R:R + 1,-R:R + 1]
xgrid, ygrid = coords[1,:,:], coords[0,:,:]
boundary_mask, V_orig = V_boundary_infinity((0, 0), R * 10 / 25, 1, xgrid, ygrid)

V = V_orig.copy()
V, iter = relaxation(V, boundary_mask, eps)

fig = plt.figure()

gs = fig.add_gridspec(2,2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[:, 1])

i1 = ax1.imshow(V_orig)
fig.colorbar(i1, ax=ax1,orientation='vertical')
i2 = ax2.imshow(V)
fig.colorbar(i2, ax=ax2,orientation='vertical')
ax3.plot(xgrid[26,:], V[26,:])
ax3.set_xlabel("x")
ax3.set_ylabel("V")
ax3.set_title("Central cut")
fig.suptitle("$\infty$ Shape")
fig.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "4-3.png"))
plt.show()