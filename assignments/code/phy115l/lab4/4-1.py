import numpy as np
import matplotlib.pyplot as plt
import os
from utils import central_2nd

a = 0
b = 2 * np.pi
N = 1000
h = (b - a) / N
x = np.arange(a, b, h)
plt.axhline(c = "k")
plt.plot(x, np.sin(x), "g-", label="$f(x) = \sin(x)$")
plt.plot(x, -np.sin(x), "r-", label="$f''(x) = -\sin(x)$")
plt.plot(x, central_2nd(np.sin(x), h), "b--", label="$f''(x)$ (computed)")
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Second Order Finite Differences")
plt.legend()
plt.savefig(os.path.join(os.path.dirname(__file__), "4-1.png"))
plt.show()