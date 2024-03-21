import numpy as np
import itertools

J = 1
N = 10
T = 2.3
E_n = np.zeros(2 ** N)

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def E2_avg(N, E_n, T):
    return np.sum(np.dot(E_n ** 2, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def C(N, E_n, T):
    return 1/T ** 2 * (E2_avg(N, E_n, T) - E_avg(N, E_n, T) ** 2)
def S(N, E_n, T):
    return 1 / T * (E_avg(N, E_n, T) - F(N, E_n, T))
def F(N, E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))

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