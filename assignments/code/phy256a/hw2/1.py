import matplotlib.pyplot as plt
from sympy import symbols, solve
from utils import plot_1d_vfield, fixed_points_1DODE

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 3.1.1

x, r = symbols("x, r")
f = 1 + r * x + x ** 2

R = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

fig, ax = plt.subplots(3, 3)
for ind, r_ in enumerate(R):
    plot_1d_vfield(lambda x_: 1 + r_ * x_ + x_ ** 2, (-2 - r_ / 2, 2 - r_ / 2), ax[ind // 3, ind % 3])

    ax[ind // 3, ind % 3].set_xlabel("x")
    ax[ind // 3, ind % 3].set_ylabel("y")
    ax[ind // 3, ind % 3].set_title("r = " + str(r_))
plt.tight_layout()
plt.show()

print(r)
fig = fixed_points_1DODE(f, r, x, -5, 5)
plt.show()

fps = solve(f, x)
dfdx = f.diff(x)
print("# FIXED POINT -> df/dx")
for fp in fps:
    print(f"x* = {fp} -> {dfdx.subs({x: fp})}")

# |r| > 2 -> 1 unstable fp at x* = (-r + sqrt(r^2 - 4))/2, 1 stable fp at x* = (-r - sqrt(r^2 - 4))/2
# |r| = 2 -> 1 half-stable fp at x* = -1
# |r| < 2 -> no fp