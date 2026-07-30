import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve
from utils import fixed_points_1DMap

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 10.3.4

x, c = symbols("x, c")
f = x ** 2 + c

fps = solve(f - x, x)
print("# FIXED POINTS")
print(fps)

ff = f.subs({x: f})
p2_orb = solve(ff - x, x)
print("# PERIOD-2 ORBITS")
print(p2_orb)

fig = fixed_points_1DMap(ff, c, x, -5, 5)
plt.show()

# subcritical pitchfork bifucation, superstable at c = -1