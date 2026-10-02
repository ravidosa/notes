import numpy as np
import matplotlib.pyplot as plt
import os
from utils import Charge, launch

charge_list = [Charge(0, 7, 1), Charge(0, -7, -1)]

fig = plt.figure(1)
ax = fig.add_subplot(111)
x0, y0 = 0, 6.9
xt, yt = 0, -7
h = 0.1
launch((x0, y0), (xt, yt), 0, h, charge_list, ax)
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Line (+ to -)")
plt.gca().set_aspect("equal")
plt.savefig(os.path.join(os.path.dirname(__file__), "2-3a.png"))
plt.show()

fig = plt.figure(2)
ax = fig.add_subplot(111)
x0, y0 = 0, -6.9
xt, yt = 0, 7
h = 0.1
launch((x0, y0), (xt, yt), 1, h, charge_list, ax)
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Line (- to +)")
plt.gca().set_aspect("equal")
plt.savefig(os.path.join(os.path.dirname(__file__), "2-3b.png"))
plt.show()

fig = plt.figure(3)
ax = fig.add_subplot(111)
x0, y0 = 0.1, 7
xt, yt = 0, -7
h = 0.1
launch((x0, y0), (xt, yt), 0, h, charge_list, ax)
plt.xlim(-25, 25)
plt.ylim(-25, 25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Line (+ to -, perp.)")
plt.gca().set_aspect("equal")
plt.savefig(os.path.join(os.path.dirname(__file__), "2-3c.png"))
plt.show()

# drawing field lines is not physically identical to plotting the trajectories of charged particles
# the trajectory is additionally dependent on the charge and mass of the particle
# drawing field lines treats these quantities as 1, which primarily affects the distance between successive iterations