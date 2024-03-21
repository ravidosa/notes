import numpy as np
import matplotlib.pyplot as plt

N = 7
E_n = np.array([0.3, 0.4, 0.5, 5.0, 6.0, 300.0, 400.0])
T_min = 0.01
T_max = 10000
M = 100000
T_arr = np.linspace(T_min, T_max, M)
S_arr = np.array([])

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def F(N, E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))
def S(N, E_n, T):
    return 1 / T * (E_avg(N, E_n, T) - F(N, E_n, T))

for T in T_arr:
    S_arr = np.append(S_arr, S(N, E_n, T))
plt.semilogx(T_arr, S_arr, "ro")
plt.xlabel("T")
plt.ylabel("S")
plt.title("Entropy vs. Temperature")
plt.show()