import numpy as np
import matplotlib.pyplot as plt
import os
from utils import E_avg_ising

T_min = 0.3
T_max = 8.0
M = 10000
T_arr = np.linspace(T_min, T_max, M)
E_arr = np.zeros(M)
C_arr = np.zeros(M)
S_arr = np.zeros(M)
F_arr = np.zeros(M)

f = open(os.path.join(os.path.dirname(__file__), "mod_ising.txt"), "r")
inp = f.read().split("\n")
E_n = np.array([[int(x) for x in i.split(" ")] for i in inp[:-1]], dtype=int)
for i, T in enumerate(T_arr):
    E_arr[i] = E_avg_ising(E_n, T)

plt.plot(T_arr, E_arr, "ro")
plt.xlabel("T")
plt.ylabel("<E>")
plt.title("Average Energy vs. Temperature")
plt.savefig(os.path.join(os.path.dirname(__file__), "5-5.png"))
plt.show()