import numpy as np
import matplotlib.pyplot as plt
import os
import itertools
from utils import E_avg, C, S, F

J = 1
N = 10
T_min = 0.3
T_max = 8.0
M = 10000
E_n = np.zeros(2 ** N)
T_arr = np.linspace(T_min, T_max, M)
E_arr = np.zeros(M)
C_arr = np.zeros(M)
S_arr = np.zeros(M)
F_arr = np.zeros(M)

i = 0
for s in itertools.product([-1, 1], repeat=N):
    s = np.array(s)
    E = np.sum(-1 * J * s[:-1] * s[1:])
    E_n[i] = E
    i = i + 1

i = 0
for T in T_arr:
    E_arr[i] = E_avg(2 ** N, E_n, T)
    C_arr[i] = C(2 ** N, E_n, T)
    S_arr[i] = S(2 ** N, E_n, T)
    F_arr[i] = F(2 ** N, E_n, T)
    i = i + 1

print(min(S_arr))

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(T_arr, E_arr, "ro")
axs[0, 0].set_xlabel("T")
axs[0, 0].set_ylabel("<E>")
axs[0, 0].set_title("Average Energy vs. Temperature")
axs[0, 1].plot(T_arr, C_arr, "bo")
axs[0, 1].set_xlabel("T")
axs[0, 1].set_ylabel("C")
axs[0, 1].set_title("Specific Heat vs. Temperature")
axs[1, 0].plot(T_arr, S_arr, "go")
axs[1, 0].set_xlabel("T")
axs[1, 0].set_ylabel("S")
axs[1, 0].set_title("Entropy vs. Temperature")
axs[1, 1].plot(T_arr, F_arr, "ko")
axs[1, 1].set_xlabel("T")
axs[1, 1].set_ylabel("F")
axs[1, 1].set_title("Free Energy vs. Temperature")
fig.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "3-4.png"))
plt.show()