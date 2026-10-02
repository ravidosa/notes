import numpy as np

def E_avg(E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

def E2_avg(E_n, T):
    return np.sum(np.dot(E_n ** 2, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))

def C(E_n, T):
    return 1/T ** 2 * (E2_avg(E_n, T) - E_avg(E_n, T) ** 2)

def F(E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))

def S(E_n, T):
    return 1 / T * (E_avg(E_n, T) - F(E_n, T))

def S_n_avg(states, N, E_n, T, n):
    nth_site = 2 * np.bitwise_and(np.right_shift(np.arange(0, states), N - n - 1),  1) - 1
    return np.sum(np.dot(nth_site, np.exp(-1 / T * E_n)) / np.sum(np.exp(-1 / T * E_n)))

def C_r(states, N, E_n, T, r):
    zeroth_site = 2 * np.bitwise_and(np.right_shift(np.arange(0, states), N - 1),  1) - 1
    rth_site = 2 * np.bitwise_and(np.right_shift(np.arange(0, states), N - r - 1),  1) - 1
    return np.sum(np.dot(np.multiply(zeroth_site, rth_site), np.exp(-1 / T * E_n)) / np.sum(np.exp(-1 / T * E_n)))