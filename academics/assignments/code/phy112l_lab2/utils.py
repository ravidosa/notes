import numpy as np

def E_avg(N, E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

def E2_avg(N, E_n, T):
    return np.sum(np.dot(E_n ** 2, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

def F(N, E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))

def S(N, E_n, T):
    return 1 / T * (E_avg(N, E_n, T) - F(N, E_n, T))