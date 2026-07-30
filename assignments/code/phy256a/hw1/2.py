from sympy import symbols, integrate
from sympy.plotting import plot
from utils import fixed_points, PlotStatesVParameter

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 2.7.6

x, r = symbols("x, r")
f = r + x - x ** 3

fps = fixed_points(f, r, x, -5, 5, 0.05)

fig = PlotStatesVParameter(fps, -5, 5, "r", "x")
fig.show()

R_IND = [86, 100, 114, 128, 142]

p = [None] * len(R_IND)
for ind, i in enumerate(R_IND):
    p[ind] = plot(f.subs({r: fps[i][0]}), (x, -2, 2), ylabel="f", label="r = " + str(round(fps[i][0], 2)), show=False)

combined = plot(xlabel="x", ylabel="f(x)", show=False)
for ind in range(len(p)):
    combined.extend(p[ind])
combined.legend = True
combined.show()

ip = [None] * len(R_IND)
for ind, i in enumerate(R_IND):
    ip[ind] = plot(-integrate(f, x).subs({r: fps[i][0]}), (x, -2, 2), ylabel="f", label="r = " + str(round(fps[i][0], 2)), show=False)

integ = plot(xlabel="x", ylabel="V(x)", show=False)
for ind in range(len(p)):
    integ.extend(ip[ind])
integ.show()

# |r| > r* -> 1 unstable fp
# |r| < r* -> 2 unstable, 1 stable fp