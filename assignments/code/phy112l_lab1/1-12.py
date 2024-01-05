import numpy as np
import matplotlib.pyplot as plt

N = 2
E_n = np.array([-3.4, 5.0])
T_min = 0.01
T_max = 100
M = 10000
E_der = np.array([])
E_FDT = np.array([])

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def E2_avg(N, E_n, T):
    return np.sum(np.dot(E_n ** 2, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

dT = (T_max - T_min) / M
for T in np.linspace(T_min, T_max, M):
    E_der = np.append(E_der, (E_avg(N, E_n, T + dT) - E_avg(N, E_n, T)) / dT)
    E_FDT = np.append(E_FDT, 1/T ** 2 * (E2_avg(N, E_n, T) - E_avg(N, E_n, T) ** 2))
plt.semilogx(np.linspace(T_min, T_max, M), E_der, "ro", label="derivative")
plt.semilogx(np.linspace(T_min, T_max, M), E_FDT, "bo", label="FDT")
plt.xlabel("T")
plt.ylabel("C")
plt.title("Specific Heat vs. Temperature")
plt.legend()
plt.show()