import numpy as np
import matplotlib.pyplot as plt
import os
from utils import E_avg, E2_avg

N = 2
E_n_arr = [np.array([-3.4, -3.0]), np.array([-3.4, 5.0])]
T_min = 0.01
T_max = 100
M = 10000
T_arr = np.linspace(T_min, T_max, M)

for i, E_n in enumerate(E_n_arr):
    plt.figure(i)
    print(E_n)
    E_der = np.zeros(M)
    E_FDT = np.zeros(M)

    dT = (T_max - T_min) / M
    for i, T in enumerate(T_arr):
        E_der[i] = (E_avg(N, E_n, T + dT) - E_avg(N, E_n, T)) / dT
        E_FDT[i] = 1/T ** 2 * (E2_avg(N, E_n, T) - E_avg(N, E_n, T) ** 2)
    plt.semilogx(T_arr, E_der, "ro", label="derivative")
    plt.semilogx(T_arr, E_FDT, "bo", label="FDT")
    plt.xlabel("T")
    plt.ylabel("C")
    plt.title("Specific Heat vs. Temperature")
    plt.legend()
    plt.savefig(os.path.join(os.path.dirname(__file__), "1-12" + chr(97 + i) + ".png"))
    plt.show()