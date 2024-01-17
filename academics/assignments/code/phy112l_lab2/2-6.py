import numpy as np
import matplotlib.pyplot as plt

N = 3
E_n = np.array([-3.7, -3.5, 0.5])
T_min = 0.01
T_max = 100
M = 10000
T_arr = np.linspace(T_min, T_max, M)
C = np.array([])
S_EF = np.array([])
S_C = np.array([])

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def E2_avg(N, E_n, T):
    return np.sum(np.dot(E_n ** 2, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def F(N, E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))
def S(N, E_n, T):
    return 1 / T * (E_avg(N, E_n, T) - F(N, E_n, T))

for T in T_arr:
    S_EF = np.append(S_EF, S(N, E_n, T))
    C = np.array([])
    for TT in np.linspace(T_min, T, M):
        C = np.append(C, 1/TT ** 3 * (E2_avg(N, E_n, TT) - E_avg(N, E_n, TT) ** 2))
    S_C = np.append(S_C, 1/2 * T / M * np.sum(C[:-1] + C[1:]))
plt.semilogx(T_arr, S_EF, "ro", label="free energy")
plt.semilogx(T_arr, S_C, "bo", label="specific heat")
plt.xlabel("T")
plt.ylabel("S")
plt.title("Entropy vs. Temperature")
plt.legend()
plt.show()