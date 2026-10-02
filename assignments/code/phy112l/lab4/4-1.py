import numpy as np
from utils import S_n_avg

J = 1
N = 10
T = 2.3
states = 2 ** N
E_n = np.zeros(states)

for s in range(states):
    anti = ((((s >> 1) ^ s) & (2 ** (N - 1) - 1))).bit_count()
    E = np.sum(-1 * J * (N - 1 - 2 * anti))
    E_n[s] = E

for n in range(N):
    print("<S_" + str(n) + "> = ", S_n_avg(states, N, E_n, T, n))