import numpy as np
import matplotlib.pyplot as plt
J = 1
N_1 = 3 #set to 1 for 1D
N_2 = 3
N = N_1 * N_2
vac = 3
T_min = 0.3
T_max = 8.0
M = 10000
states = 3 ** (N)
E_n = np.zeros(states)
T_arr = np.linspace(T_min, T_max, M)
E_arr = np.zeros(M)
C_arr = np.zeros(M)
S_arr = np.zeros(M)
F_arr = np.zeros(M)
class ternary():
    def __init__(self, dec):
        self.dec = dec
        self.tern = self.dec_to_tern()
        self.counts = self.trit_counter()
    def __repr__(self):
        return self.tern
    def dec_to_tern(self):
        dec = self.dec
        if dec == 0:
            tern = "0"
        else:
            tern = ""
            while dec:
                dec, rem = divmod(dec, 3)
                tern = str(rem) + tern
        return tern.zfill(N)
    def trit_counter(self):
        return [self.tern.count(str(i)) for i in range(3)]
    def trit_count(self, tr):
        return self.counts[tr]
    def __mul__(self, t):
        return ternary(sum([self.trit_mul(self.tern[ind], t.tern[ind]) * 3 ** (N - 1 - ind) for ind in range(N)]))
    def __lshift__(self, s):
        return ternary(self.dec * 3 ** s)
    def __rshift__(self, s):
        return ternary(self.dec // 3 ** s)
    @staticmethod
    def trit_mul(tr1, tr2):
        return (int(tr1) * int(tr2)) % 3
def E_avg(E_n, T):
    return np.sum(np.dot(E_n, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def E2_avg(E_n, T):
    return np.sum(np.dot(E_n ** 2, np.exp(-1 / T * E_n))) / np.sum(np.exp(-1 / T * E_n))
def C(E_n, T):
    return 1/T ** 2 * (E2_avg(E_n, T) - E_avg(E_n, T) ** 2)
def S(E_n, T):
    return 1 / T * (E_avg(E_n, T) - F(E_n, T))
def F(E_n, T):
    return -1 * T * np.log(np.sum(np.exp(-1 / T * E_n)))

m1 = ternary(int((3 ** (N_1 - 1) - 1) // 2 * np.sum(3 ** (N_1 * np.arange(N_2)))))
m2 = ternary((3 ** (N_1 * (N_2 - 1)) - 1) // 2)
for i in range(states):
    s = ternary(i)
    if s.counts[0] == vac:
        anti_1 = ((((s >> 1) * s) * m1)).counts #spins within row
        anti_2 = ((((s >> N_1) * s) * m2)).counts #spins within column
        E = -1 * J * (anti_1[1] + anti_2[1] - anti_1[2] - anti_2[2])
    else:
        E = None
    E_n[i] = E
for i, T in enumerate(T_arr):
    E_arr[i] = E_avg(E_n[~np.isnan(E_n)], T)

plt.plot(T_arr, E_arr, "ro")
plt.xlabel("T")
plt.ylabel("<E>")
plt.title("Average Energy vs. Temperature")
plt.show()