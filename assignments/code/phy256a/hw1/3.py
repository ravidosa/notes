from sympy import symbols, solve
from sympy.plotting import plot, plot_parametric
import numpy as np
import matplotlib.pyplot as plt
from utils import Phase_Portrait

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 6.1.2

x, y = symbols("x, y")
x_dot = x - x ** 3
y_dot = -y

x_nullclines = solve(x_dot, x)
y_nullclines = solve(y_dot, y)

t = symbols("t")

n = [None] * (len(x_nullclines) + len(y_nullclines))
for ind, nc in enumerate(x_nullclines):
    n[ind] = plot_parametric((nc, t, (t, -2, 2)), show=False)
for ind, nc in enumerate(y_nullclines):
    n[ind + len(x_nullclines)] = plot_parametric((t, nc, (t, -2, 2)), show=False)

nullc = plot(title="Nullclines", xlabel="x", ylabel="y", show=False)
for ind in range(len(n)):
    nullc.extend(n[ind])
nullc.show()

def ODE_6_1_2(state, t):
	x, y = state
	return [x - x ** 3, -y]

nICs = 200
IntegrationTime = 1
fig = Phase_Portrait(ODE_6_1_2, (-2, 2), (-1, 1), nICs,IntegrationTime)
fig.show()

x, y = np.meshgrid(np.linspace(-1.5, 1.5, 50), np.linspace(-0.5, 0.5, 20))

x_dot = x - x ** 3
y_dot = -y

plt.figure()
plt.quiver(x, y, x_dot, y_dot)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Vector Field")
plt.show()

# (-1, 0) -> stable fp
# (0, 0) -> half-stable fp
# (1, 0) -> stable fp