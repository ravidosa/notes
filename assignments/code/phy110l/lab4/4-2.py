import numpy as np
import matplotlib.pyplot as plt
import os
from utils import relaxation, V_boundary_hollowsquare

eps = 1e-8
print("Grid radius\tIterations")
for R in [25, 50, 100]:
    coords = np.mgrid[-R:R + 1,-R:R + 1]
    xgrid, ygrid = coords[1,:,:], coords[0,:,:]
    boundary_mask, V_orig = V_boundary_hollowsquare((0, 0), R / 25 * 10, 1, xgrid, ygrid)

    V = V_orig.copy()
    V, iter = relaxation(V, boundary_mask, eps)
    print(str(R) + "\t\t" + str(iter))

# N seems to increase linearly with R, and as the square root of grid size
# the number of computations is linearly dependent on the grid radius