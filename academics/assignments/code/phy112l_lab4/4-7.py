import numpy as np
import matplotlib.pyplot as plt

J = 1
N_1 = 4 #set to 1 for 1D
N_2 = 4
N = N_1 * N_2
T_min = 0.3
T_max = 8.0
M = 10000
states = 2 ** (N)
E_n = np.zeros(states)
T_arr = np.linspace(T_min, T_max, M)
E_arr = np.zeros(M)
C_arr = np.zeros(M)
S_arr = np.zeros(M)
F_arr = np.zeros(M)

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
    anti_1 = ((((s >> 1) ^ s) & ((2 ** (N_1 - 1) - 1)) * np.sum(2 ** (N_1 * np.arange(N_2))))).bit_count() #spins within row
    anti_2 = ((((s >> N_1) ^ s) & ((2 ** (N_1 * (N_2 - 1)) - 1)))).bit_count() #spins within column
    E = np.sum(-1 * J * ((N_2 * (N_1 - 1) - 2 * anti_1) + (N_1 * (N_2 - 1) - 2 * anti_2)))
    E_n[s] = E

for i, T in enumerate(T_arr):
    E_arr[i] = E_avg(E_n, T)
    C_arr[i] = C(E_n, T)
    S_arr[i] = S(E_n, T)
    F_arr[i] = F(E_n, T)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(T_arr, E_arr, "ro")
axs[0, 0].set_xlabel("T")
axs[0, 0].set_ylabel("<E>")
axs[0, 0].set_title("Average Energy vs. Temperature")
axs[0, 1].plot(T_arr, C_arr, "bo")
axs[0, 1].set_xlabel("T")
axs[0, 1].set_ylabel("C")
axs[0, 1].set_title("Specific Heat vs. Temperature")
axs[1, 0].plot(T_arr, S_arr, "go")
axs[1, 0].set_xlabel("T")
axs[1, 0].set_ylabel("S")
axs[1, 0].set_title("Entropy vs. Temperature")
axs[1, 1].plot(T_arr, F_arr, "ko")
axs[1, 1].set_xlabel("T")
axs[1, 1].set_ylabel("F")
axs[1, 1].set_title("Free Energy vs. Temperature")
fig.tight_layout()
plt.show()