import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import special
from utils import hermite_recursion

M = 10000
chk = 0
res = np.zeros(M)
for i in range(M):
    n = np.random.randint(0, 10)
    u = np.random.random() * 10
    corr = (special.hermite(n))(u)
    test = hermite_recursion(n, u)
    res[i] = abs(corr - test) / u
    if abs(corr - test) / u > 1e-6:
        chk += 1
print(str(M - chk) + "/" + str(M), "tests passed")
plt.hist(res)
plt.savefig(os.path.join(os.path.dirname(__file__), "1-3.png"))
plt.show()