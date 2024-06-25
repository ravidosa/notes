import numpy as np
import matplotlib.pyplot as plt
import os
from utils import S

N = 3
E_n = np.array([-3.7, -3.5, 0.5])
T_min = 0.01
T_max = 100
M = 10000
T_arr = np.linspace(T_min, T_max, M)
S_arr = np.zeros(M)

for i, T in enumerate(T_arr):
    S_arr[i] = S(N, E_n, T)
plt.semilogx(T_arr, S_arr, "ro")
plt.xlabel("T")
plt.ylabel("S")
plt.title("Entropy vs. Temperature")
plt.savefig(os.path.join(os.path.dirname(__file__), "2-4.png"))
plt.show()