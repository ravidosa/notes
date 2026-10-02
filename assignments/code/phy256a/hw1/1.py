from sympy import symbols, solve, diff, ln
from sympy.plotting import plot

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 2.4.6

x = symbols("x")
f = ln(x)

fps = solve(f, x)
dfdx = diff(f, x)
print("# FIXED POINT -> df/dx")
for fp in fps:
    print(f"x* = {fp} -> {dfdx.subs({x: fp})}")

plot(f, (x, 0.1, 2), xlabel="x", ylabel="f(x)")

# x* = 1 -> unstable fp