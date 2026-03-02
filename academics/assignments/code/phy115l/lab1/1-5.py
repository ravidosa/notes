import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as integrate
import scipy.special as special

# m\omega / \hbar = 1
N = 10
herms = [special.hermite(i) for i in range(N)]
for i in range(N):
    for j in range(i, N):
        integ, err = integrate.quad(lambda x: 1/np.sqrt(math.pi) * herms[i](x) / np.sqrt(2 ** i * math.factorial(i)) * herms[j](x) / np.sqrt(2 ** j * math.factorial(j)) * np.exp(-x ** 2), -np.inf, np.inf)
        expp = int(i == j)
        print("[" + str(abs(integ - expp) < 1e-10) + "]: i = " + str(i) + ", j = " + str(j) + ", exp: " + str(expp) + ", calculated = " + str(integ))