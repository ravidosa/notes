import numpy as np
from utils import E_avg

N = 3
E_n = np.array([2.6, 3.8, 4.2])
T_arr = [0.3, 2.0, 15.0]

for T in T_arr:
    print("T =", T, ", <E> =", E_avg(N, E_n, T))