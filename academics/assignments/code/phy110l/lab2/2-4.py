import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge, launch

charge_list = [Charge(0, 7, 1), Charge(0, -7, -1)]

fig = plt.figure(1)
ax = fig.add_subplot(111)

par_arr = [(0, 6.9, 0, -7),
           (0.1, 7, 0, -7),
           (-0.1, 7, 0, -7),
           (0, 7.1, 0, 25),
           (0, -25, 0, -7),
           (-0.07, 6.92, 0, -7),
           (0.07, 6.92, 0, -7),
           (-0.07, 7.07, 0, -7),
           (0.07, 7.07, 0, -7),
           (-0.04, 6.91, 0, -7),
           (0.04, 6.91, 0, -7),
           (-0.09, 6.96, 0, -7),
           (0.09, 6.96, 0, -7),
           (-0.04, 7.09, 0, -7),
           (0.04, 7.09, 0, -7),
           (-0.09, 7.05, 0, -7),
           (0.09, 7.05, 0, -7)]
h = 0.1

ax.plot(0, 7, "ro", markersize="10", zorder=9999999)
ax.plot(0, -7, "bo", markersize="10", zorder=9999999)
for x0, y0, xt, yt in par_arr:
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax)
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Lines")
plt.gca().set_aspect("equal")
plt.savefig(os.path.join(os.path.dirname(__file__), "2-4.png"))
plt.show()