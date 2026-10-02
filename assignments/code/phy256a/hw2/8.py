import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from utils import cobweb

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 10.4.6

x = symbols("x")
r = 3.7389149
f = r * x * (1 - x)

fig = cobweb(f, x, 0.5)
plt.xlabel("$x_n$")
plt.ylabel("$x_{n+1}$")
plt.title(f"Logistic Map (r = {r})")
plt.show()

# period 5 orbit