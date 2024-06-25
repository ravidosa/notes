import numpy as np
from utils import S

N = 3
E_n = np.array([2.6, 3.8, 4.2])
T_arr = [0.3, 2.0, 15.0]

for T in T_arr:
    print("T =", T, ", S =", S(N, E_n, T))