import numpy as np

N = 3
E_n = np.array([0.7, 1.3, 5.0])
T_min = 10
T_max = 10.9
M = 10

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

dT = (T_max - T_min) / M
for T in np.linspace(T_min, T_max, M)[:-1]:
    print("T = (" + str(T) + ",", str(T + dT) + "), C =", (E_avg(N, E_n, T + dT) - E_avg(N, E_n, T)) / dT)