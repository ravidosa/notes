import numpy as np
import matplotlib.pyplot as plt
import os
import time
from utils import Charge, launch

charge_list = [Charge(0, 7, 1), Charge(0, -7, -1)]

for i, h in enumerate([0.5, 0.1]):
    print("h =", h)
    print("euler\t\trk-2")
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    x0, y0 = 0, 6.9
    xt, yt = 0, -7
    t_eul_i = time.time()
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax, 25, "gray", "euler")
    t_eul_f = time.time()
    t_rk2_i = time.time()
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax, 25, "black", "rk2")
    t_rk2_f = time.time()
    print(str(round(t_eul_f - t_eul_i, 3)) + "\t\t" + str(round(t_rk2_f - t_rk2_i, 3)))

    x0, y0 = 0, -6.9
    xt, yt = 0, 7
    t_eul_i = time.time()
    launch((x0, y0), (xt, yt), 1, h, charge_list, ax, 25, "gray", "euler")
    t_eul_f = time.time()
    t_rk2_i = time.time()
    launch((x0, y0), (xt, yt), 1, h, charge_list, ax, 25, "black", "rk2")
    t_rk2_f = time.time()
    print(str(round(t_eul_f - t_eul_i, 3)) + "\t\t" + str(round(t_rk2_f - t_rk2_i, 3)))

    x0, y0 = 0.1, 7
    xt, yt = 0, -7
    t_eul_i = time.time()
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax, 25, "gray", "euler")
    t_eul_f = time.time()
    t_rk2_i = time.time()
    launch((x0, y0), (xt, yt), 0, h, charge_list, ax, 25, "black", "rk2")
    t_rk2_f = time.time()
    print(str(round(t_eul_f - t_eul_i, 3)) + "\t\t" + str(round(t_rk2_f - t_rk2_i, 3)))

    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Field Lines (h = " + str(h) + ")")
    plt.gca().set_aspect("equal")
    plt.savefig(os.path.join(os.path.dirname(__file__), "3-1" + chr(97 + i) + ".png"))
    plt.show()

# using the runge-kutta method improves significantly on the error
# the field lines for rk-2 with h = 0.5 is fairly close to that of euler with h = 0.1
# the runtime for rk-2 is also siginificantly faster than that of euler
# the computation for rk-2 is more complex and require multiple (2) calls to the field function