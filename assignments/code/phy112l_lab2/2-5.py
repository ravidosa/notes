import numpy as np
import matplotlib.pyplot as plt
import os
from utils import S

N = 7
E_n = np.array([0.3, 0.4, 0.5, 5.0, 6.0, 300.0, 400.0])
T_min = 0.01
T_max = 10000
M = 100000
T_arr = np.linspace(T_min, T_max, M)
S_arr = np.zeros(M)

for i, T in enumerate(T_arr):
    S_arr[i] = S(N, E_n, T)
plt.semilogx(T_arr, S_arr, "ro")
plt.xlabel("T")
plt.ylabel("S")
plt.title("Entropy vs. Temperature")
plt.savefig(os.path.join(os.path.dirname(__file__), "2-5.png"))
plt.show()