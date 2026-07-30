import numpy as np
import matplotlib.pyplot as plt
import os
from utils import launch

N = 100
V0 = 1
L = 100
M = 50
coeffs = (lambda n : n * np.pi / L, lambda n : 0, lambda n : 0, lambda n : 4 * V0 / (n * np.pi) * (n % 2), lambda n : 0)
h = 0.1

fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.xlim(0, L)
plt.ylim(0, 2 * L)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Field Lines")
for x in np.linspace(0, L, M + 1):
    launch((x, h), (np.inf, np.inf), 0, h, (coeffs, N), ax, (0, L, 0, 2 * L), "black")
plt.savefig(os.path.join(os.path.dirname(__file__), "5-2.png"))
plt.show()
# symmetric about x = 50, curves strongly to either side
# matches gradient of V