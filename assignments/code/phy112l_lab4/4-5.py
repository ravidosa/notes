import numpy as np
import matplotlib.pyplot as plt

J = 1
N = 10
T_arr = np.array([0.5, 1.0, 1.5])
states = 2 ** N
E_n = np.zeros(states)

def E_avg(E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def E2_avg(E_n, T):
    return np.sum(np.dot(E_n ** 2, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def C(E_n, T):
    return 1/T ** 2 * (E2_avg(E_n, T) - E_avg(E_n, T) ** 2)
def S(E_n, T):
    return 1 / T * (E_avg(N, E_n, T) - F(N, E_n, T))
def F(E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))
def S_n_avg(E_n, T, n):
    nth_site = 2 * np.bitwise_and(np.right_shift(np.arange(0, states), N - n - 1),  1) - 1
    return np.sum(np.dot(nth_site, np.exp(-1 / T * E_n)) / np.sum(np.exp(-1 / T * E_n)))
def C_r(E_n, T, r):
    zeroth_site = 2 * np.bitwise_and(np.right_shift(np.arange(0, states), N - 1),  1) - 1
    rth_site = 2 * np.bitwise_and(np.right_shift(np.arange(0, states), N - r - 1),  1) - 1
    return np.sum(np.dot(np.multiply(zeroth_site, rth_site), np.exp(-1 / T * E_n)) / np.sum(np.exp(-1 / T * E_n)))

for s in range(states):
    anti = ((((s >> 1) ^ s) & (2 ** (N - 1) - 1))).bit_count()
    E = np.sum(-1 * J * (N - 1 - 2 * anti))
    E_n[s] = E

r_arr = np.arange(N)
cols = ["r", "g", "b"]
for i, T in enumerate(T_arr):
    C_arr = np.zeros(N)
    for r in range(N):
        C_arr[r] = C_r(E_n, T, r)
    plt.plot(r_arr, np.log(C_arr), cols[i] + "o", label="T = " + str(T))
plt.xlabel("r")
plt.ylabel("ln C(r)")
plt.title("Log of Spin-spin correlation vs. Separation")
plt.legend()
plt.show()