import numpy as np
import matplotlib.pyplot as plt

N = 2
E_n = np.array([-3.4, 5.0])
T_min = 0.01
T_max = 100
M = 10000
E = np.array([])

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

dT = (T_max - T_min) / M
for T in np.linspace(T_min, T_max, M)[:-1]:
    E = np.append(E, (E_avg(N, E_n, T + dT) - E_avg(N, E_n, T)) / dT)
plt.semilogx(np.linspace(T_min, T_max, M)[:-1], E, "ro")
plt.xlabel("T")
plt.ylabel("C")
plt.title("Specific Heat vs. Temperature")
plt.show()
print(np.linspace(T_min, T_max, M)[E.argmax()])