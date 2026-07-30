import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge, launch

fig = plt.figure(1)
ax = fig.add_subplot(111)

charge_list = [Charge(0, 0, 1)]

par_arr = [(0, -0.1, 0, -np.inf),
           (0.1, 0, np.inf, 0),
           (-0.1, 0, -np.inf, 0),
           (0, 0.1, 0, np.inf),
           (-0.07, -0.08, -np.inf, -np.inf),
           (0.07, -0.08, np.inf, -np.inf),
           (-0.07, 0.07, -np.inf, np.inf),
           (0.07, 0.07, np.inf, np.inf),
           (-0.04, -0.09, -np.inf, -np.inf),
           (0.04, -0.09, np.inf, -np.inf),
           (-0.09, -0.04, -np.inf, -np.inf),
           (0.09, -0.04, np.inf, -np.inf),
           (-0.04, 0.09, -np.inf, np.inf),
           (0.04, 0.09, np.inf, np.inf),
           (-0.09, 0.05, -np.inf, np.inf),
           (0.09, 0.05, np.inf, np.inf)]
h = 0.1

ax.plot(0, 0, "ro", markersize="10", zorder=9999999)
for x0, y0, xt, yt in par_arr:
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax, 25, "black", "rk2")
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Lines")
plt.gca().set_aspect("equal")
plt.savefig(os.path.join(os.path.dirname(__file__), "3-2a.png"))
plt.show()

fig = plt.figure(2)
ax = fig.add_subplot(111)

charge_list = [Charge(0, 7, 1), Charge(0, -7, 1)]

par_arr = [(0.1, 7, np.inf, 0),
           (-0.1, 7, -np.inf, 0),
           (0, 7.1, 0, np.inf),
           (-0.07, 6.92, -np.inf, -np.inf),
           (0.07, 6.92, np.inf, -np.inf),
           (-0.07, 7.07, -np.inf, np.inf),
           (0.07, 7.07, np.inf, np.inf),
           (-0.04, 6.91, -np.inf, -np.inf),
           (0.04, 6.91, np.inf, -np.inf),
           (-0.09, 6.96, -np.inf, -np.inf),
           (0.09, 6.96, np.inf, -np.inf),
           (-0.04, 7.09, -np.inf, np.inf),
           (0.04, 7.09, np.inf, np.inf),
           (-0.09, 7.05, -np.inf, np.inf),
           (0.09, 7.05, np.inf, np.inf),
           (0.1, -7, np.inf, 0),
           (-0.1, -7, -np.inf, 0),
           (0, -7.1, 0, np.inf),
           (-0.07, -6.92, -np.inf, -np.inf),
           (0.07, -6.92, np.inf, -np.inf),
           (-0.07, -7.07, -np.inf, np.inf),
           (0.07, -7.07, np.inf, np.inf),
           (-0.04, -6.91, -np.inf, -np.inf),
           (0.04, -6.91, np.inf, -np.inf),
           (-0.09, -6.96, -np.inf, -np.inf),
           (0.09, -6.96, np.inf, -np.inf),
           (-0.04, -7.09, -np.inf, np.inf),
           (0.04, -7.09, np.inf, np.inf),
           (-0.09, -7.05, -np.inf, np.inf),
           (0.09, -7.05, np.inf, np.inf)]
h = 0.1

ax.plot(0, 7, "ro", markersize="10", zorder=9999999)
ax.plot(0, -7, "ro", markersize="10", zorder=9999999)
for x0, y0, xt, yt in par_arr:
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax, 25, "black", "rk2")
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Lines")
plt.gca().set_aspect("equal")
plt.savefig(os.path.join(os.path.dirname(__file__), "3-2b.png"))
plt.show()

fig = plt.figure(3)
ax = fig.add_subplot(111)

charge_list = [Charge(6, -8, 1), Charge(-6, -8, 1), Charge(0, 10, -1)]

par_arr = [(6, -7.9, 0, 10),
           (6.05, -7.91, 0, 10),
           (6.07, -7.93, 0, 10),
           (6.09, -7.96, 0, 10),
           (5.96, -7.91, 0, 10),
           (5.93, -7.93, 0, 10),
           (5.91, -7.96, 0, 10),
           (6.09, -7.96, 0, 10),
           (6.1, -8, np.inf, -8),
           (6.09, -8.04, np.inf, -np.inf),
           (6.07, -8.05, np.inf, -np.inf),
           (6.05, -8.09, np.inf, -np.inf),
           (6, -8.1, 3, -np.inf),
           (5.96, -8.09, 0, -np.inf),
           (5.93, -8.07, 0, -np.inf),
           (5.92, -8.05, 0, -np.inf),
           (-6, -7.9, 0, 10),
           (-6.05, -7.91, 0, 10),
           (-6.07, -7.93, 0, 10),
           (-6.09, -7.96, 0, 10),
           (-5.96, -7.91, 0, 10),
           (-5.93, -7.93, 0, 10),
           (-5.91, -7.96, 0, 10),
           (-6.09, -7.96, 0, 10),
           (-6.1, -8, -np.inf, -8),
           (-6.09, -8.04, -np.inf, -np.inf),
           (-6.07, -8.05, -np.inf, -np.inf),
           (-6.05, -8.09, -np.inf, -np.inf),
           (-6, -8.1, -3, -np.inf),
           (-5.96, -8.09, 0, -np.inf),
           (-5.93, -8.07, 0, -np.inf),
           (-5.92, -8.05, 0, -np.inf),
           (0, 25, 0, 10)]
h = 0.1

ax.plot(6, -8, "ro", markersize="10", zorder=9999999)
ax.plot(-6, -8, "ro", markersize="10", zorder=9999999)
ax.plot(0, 10, "bo", markersize="10", zorder=9999999)
for x0, y0, xt, yt in par_arr:
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax, 25, "black", "rk2")
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Lines")
plt.gca().set_aspect("equal")
plt.savefig(os.path.join(os.path.dirname(__file__), "3-2c.png"))
plt.show()