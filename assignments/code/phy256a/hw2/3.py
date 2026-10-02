import matplotlib.pyplot as plt
from sympy import symbols, solve
from utils import plot_1d_vfield, fixed_points_1DODE

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 3.4.1

x, r = symbols("x, r")
f = r * x + 4 * x ** 3

R = [-8, -6, -4, -2, 0, 2, 4, 6, 8]

fig, ax = plt.subplots(3, 3)
for ind, r_ in enumerate(R):
    plot_1d_vfield(lambda x_: r_ * x_ + 4 * x_ ** 3, (-2 - r_ / 2, 2 - r_ / 2), ax[ind // 3, ind % 3])

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

# r > 0 -> 1 unstable fp at x* = 0
# r = 0 -> 1 half-stable fp at x* = 0
# r < 0 -> 2 unstable fp at x* = sqrt(-r)/2, -sqrt(-r)/2, 1 stable fp at x* = 0