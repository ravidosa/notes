import numpy as np
from utils import C_r

J = 1
N = 10
T_arr = np.array([0.5, 1.0, 1.5])
states = 2 ** N
E_n = np.zeros(states)

for s in range(states):
    anti = ((((s >> 1) ^ s) & (2 ** (N - 1) - 1))).bit_count()
    E = np.sum(-1 * J * (N - 1 - 2 * anti))
    E_n[s] = E

for T in T_arr:
    print("T =", T)
    for r in range(N):
        print("C(" + str(r) + ") = ", C_r(states, N, E_n, T, r))