import numpy as np
import itertools
from utils import E_avg, C, S, F

J = 1
N = 10
T = 2.3
E_n = np.zeros(2 ** N)

i = 0
for s in itertools.product([-1, 1], repeat=N):
    s = np.array(s)
    E = np.sum(-1 * J * s[:-1] * s[1:])
    E_n[i] = E
    i = i + 1

print("E_avg = ", E_avg(2 ** N, E_n, T))
print("C = ", C(2 ** N, E_n, T))
print("S = ", S(2 ** N, E_n, T))
print("F = ", F(2 ** N, E_n, T))