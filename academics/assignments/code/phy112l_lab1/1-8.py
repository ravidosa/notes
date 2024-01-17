import numpy as np
import matplotlib.pyplot as plt

N = 3
E_n = np.array([0.7, 1.3, 5.0])
T_min = 0.01
T_max = 100
M = 10000
T_arr = np.linspace(T_min, T_max, M)
E = np.array([])

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

for T in T_arr:
    E = np.append(E, E_avg(N, E_n, T))
plt.semilogx(T_arr, E, "ro")
plt.xlabel("T")
plt.ylabel("<E>")
plt.title("Average Energy vs. Temperature")
plt.show()