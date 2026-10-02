import numpy as np
from utils import norm, energy, V_fp

# free particle energy check
OFFSET = 10
a = -5
b = 5
N = 1000
x = np.linspace(a, b, N)
y = np.cos(np.pi * x / 2)
y = norm(x, y)
print("calculated energy:", energy(x, y, V_fp, (OFFSET)))
print("expected energy:", OFFSET + np.pi ** 2 / 4)