import numpy as np
import matplotlib.pyplot as plt
T_min = 0.3
T_max = 8.0
M = 10000
T_arr = np.linspace(T_min, T_max, M)
E_arr = np.zeros(M)
C_arr = np.zeros(M)
S_arr = np.zeros(M)
F_arr = np.zeros(M)

def E_avg(E_n, T):
    return np.dot(E_n, np.exp(-1 / T * E_n)) / np.sum(np.exp(-1 / T * E_n))
def E2_avg(E_n, T):
    return np.dot(E_n ** 2, np.exp(-1 / T * E_n)) / np.sum(np.exp(-1 / T * E_n))
def C(E_n, T):
    return 1/T ** 2 * (E2_avg(E_n, T) - E_avg(E_n, T) ** 2)
def S(E_n, T):
    return 1 / T * (E_avg(E_n, T) - F(E_n, T))
def F(E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))
def E_avg_ising(E_n, T):
    return np.dot(E_n[:,1], np.multiply(E_n[:,0], np.exp(-1 / T * E_n[:,0]))) / np.dot(E_n[:,1], np.exp(-1 / T * E_n[:,0]))

f = open("mod_ising.txt", "r")
inp = f.read().split("\n")
E_n = np.array([[int(x) for x in i.split(" ")] for i in inp[:-1]], dtype=int)
for i, T in enumerate(T_arr):
    E_arr[i] = E_avg_ising(E_n, T)

plt.plot(T_arr, E_arr, "ro")
plt.xlabel("T")
plt.ylabel("<E>")
plt.title("Average Energy vs. Temperature")
plt.show()