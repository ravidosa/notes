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

def E_avg_ising(E_n, T):
    return np.dot(E_n[:,1], np.multiply(E_n[:,0], np.exp(-1 / T * E_n[:,0]))) / np.dot(E_n[:,1], np.exp(-1 / T * E_n[:,0]))

class ternary():
    def __init__(self, dec, N):
        self.dec = dec
        self.N = N
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
        return tern.zfill(self.N)
    def trit_counter(self):
        return [self.tern.count(str(i)) for i in range(3)]
    def trit_count(self, tr):
        return self.counts[tr]
    def __mul__(self, t):
        return ternary(sum([self.trit_mul(self.tern[ind], t.tern[ind]) * 3 ** (self.N - 1 - ind) for ind in range(self.N)]), self.N)
    def __lshift__(self, s):
        return ternary(self.dec * 3 ** s, self.N)
    def __rshift__(self, s):
        return ternary(self.dec // 3 ** s, self.N)
    @staticmethod
    def trit_mul(tr1, tr2):
        return (int(tr1) * int(tr2)) % 3