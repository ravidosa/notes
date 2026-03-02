import numpy as np
import matplotlib.pyplot as plt
import os
from utils import E_avg, E2_avg, S

N = 3
E_n = np.array([-3.7, -3.5, 0.5])
T_min = 0.01
T_max = 100
M = 1000
T_arr = np.linspace(T_min, T_max, M)
S_EF = np.zeros(M)
S_C = np.zeros(M)

for i, T in enumerate(T_arr):
    S_EF[i] = S(N, E_n, T)
    C = np.zeros(M)
    for j, TT in enumerate(np.linspace(T_min, T, M)):
        C[j] = 1/TT ** 3 * (E2_avg(N, E_n, TT) - E_avg(N, E_n, TT) ** 2)
    S_C[i] = 1/2 * T / M * np.sum(C[:-1] + C[1:])

plt.semilogx(T_arr, S_EF, "ro", label="free energy")
plt.semilogx(T_arr, S_C, "bo", label="specific heat")
plt.xlabel("T")
plt.ylabel("S")
plt.title("Entropy vs. Temperature")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "2-6.png"))
plt.show()