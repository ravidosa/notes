import numpy as np
import matplotlib.pyplot as plt
import os
from utils import E_avg

N = 3
E_n = np.array([0.7, 1.3, 5.0])
T_min = 0.01
T_max = 100
M = 10000
T_arr = np.linspace(T_min, T_max, M)
E = np.zeros(M)

for i, T in enumerate(T_arr):
    E[i] = E_avg(N, E_n, T)
plt.semilogx(T_arr, E, "ro")
plt.xlabel("T")
plt.ylabel("<E>")
plt.title("Average Energy vs. Temperature")
plt.savefig(os.path.join(os.path.dirname(__file__), "1-8.png"))
plt.show()