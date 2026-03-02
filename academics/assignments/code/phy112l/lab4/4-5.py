import numpy as np
import matplotlib.pyplot as plt
import os
from utils import C_r

J = 1
N = 10
T_arr = np.array([0.5, 1.0, 1.5])
states = 2 ** N
E_n = np.zeros(states)

for s in range(states):
    anti = ((((s >> 1) ^ s) & (2 ** (N - 1) - 1))).bit_count()
    E = np.sum(-1 * J * (N - 1 - 2 * anti))
    E_n[s] = E

r_arr = np.arange(N)
cols = ["r", "g", "b"]
for i, T in enumerate(T_arr):
    C_arr = np.zeros(N)
    for r in range(N):
        C_arr[r] = C_r(states, N, E_n, T, r)
    plt.plot(r_arr, np.log(C_arr), cols[i] + "o", label="T = " + str(T))
plt.xlabel("r")
plt.ylabel("ln C(r)")
plt.title("Log of Spin-spin correlation vs. Separation")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "4-5.png"))
plt.show()