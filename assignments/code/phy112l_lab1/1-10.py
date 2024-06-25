import numpy as np
import matplotlib.pyplot as plt
import os
from utils import E_avg

N = 2
E_n_arr = [np.array([-3.4, -3.0]), np.array([-3.4, 5.0])]
T_min = 0.01
T_max = 100
M = 10000
T_arr = np.linspace(T_min, T_max, M)

for i, E_n in enumerate(E_n_arr):
    plt.figure(i)
    print(E_n)
    E = np.zeros(M - 1)

    dT = (T_max - T_min) / M
    for i, T in enumerate(T_arr[:-1]):
        E[i] = (E_avg(N, E_n, T + dT) - E_avg(N, E_n, T)) / dT
    plt.semilogx(T_arr[:-1], E, "ro")
    plt.xlabel("T")
    plt.ylabel("C")
    plt.title("Specific Heat vs. Temperature")
    plt.savefig(os.path.join(os.path.dirname(__file__), "1-10" + chr(97 + i) + ".png"))
    print(T_arr[E.argmax()])
    plt.show()