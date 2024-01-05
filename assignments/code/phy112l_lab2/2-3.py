import numpy as np

N = 3
E_n = np.array([2.6, 3.8, 4.2])

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def F(N, E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))
def S(N, E_n, T):
    return 1 / T * (E_avg(N, E_n, T) - F(N, E_n, T))

for T in [0.3, 2.0, 15.0]:
    print("T =", T, ", S =", S(N, E_n, T))