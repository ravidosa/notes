import math
import matplotlib.pyplot as plt

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 10.3.13

import cmpy.dm as dm
import cmpy.dm.drawing as dmd
import matplotlib.pyplot as plt
import numpy as np
tm = dm.LogisticMap()

# Parameter range
pmin = 2.95
pmax = 4

dmd.bifurcation_plot_1d1p(tm, (-0.1,1.0), (pmin,pmax), pBins=2048)

# The map's maximum
Xmax = 0.5
# Plot up to and including Nth iterate of map's maximum
N = 6
# The number of increments in the parameter
rSteps = 1000

rvals = np.linspace(pmin,pmax, rSteps)
                                             # Make 2D array of (parameter values, number of iterate)
iterates = np.zeros( (len(rvals), N) )     # N-1 => Skip 0th iterate
for i,r in enumerate(rvals):   # 1D Map method returns sequence of iterates: orbit(X_0,number of iterates,parameter)
    iterates[i] = tm.orbit(Xmax, N+1, params=[r])[1:] # Indexing '[1:]' => Skip 0th iterate

iterates = iterates.transpose()             # Make horizontal plot coordinate be parameter 'r'
for i in range(N):
    plt.plot(rvals, iterates[i], 'b-')
plt.show()