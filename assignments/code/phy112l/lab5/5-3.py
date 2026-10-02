import numpy as np
import matplotlib.pyplot as plt
import os
from utils import E_avg, ternary

J = 1
N_1 = 2 #set to 1 for 1D
N_2 = 2
N = N_1 * N_2
T_min = 0.3
T_max = 8.0
M = 10000
states = 3 ** (N)
E_n = np.zeros(states)
T_arr = np.linspace(T_min, T_max, M)
E_arr = np.zeros(M)
C_arr = np.zeros(M)
S_arr = np.zeros(M)
F_arr = np.zeros(M)

for i in range(states):
    s = ternary(i, N)
    anti_1 = ((((s >> 1) * s) * ternary(int((3 ** (N_1 - 1) - 1) // 2 * np.sum(3 ** (N_1 * np.arange(N_2)))), N))) #spins within row
    anti_2 = ((((s >> N_1) * s) * ternary((3 ** (N_1 * (N_2 - 1)) - 1) // 2, N))) #spins within column
    print(i, anti_1, anti_2)
    E = -1 * J * (anti_1.counts[1] + anti_2.counts[1] - anti_1.counts[2] - anti_2.counts[2])
    E_n[i] = E

for i, T in enumerate(T_arr):
    E_arr[i] = E_avg(E_n, T)

plt.plot(T_arr, E_arr, "ro")
plt.xlabel("T")
plt.ylabel("<E>")
plt.title("Average Energy vs. Temperature")
plt.savefig(os.path.join(os.path.dirname(__file__), "5-3.png"))
plt.show()