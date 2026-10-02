import matplotlib.pyplot as plt
from sympy import symbols
from utils import plot_2d_vfield, Phase_Portrait

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 8.2.3

x, y, mu = symbols("x, y, mu")
x_dot = -y + mu * x + x * y ** 2
y_dot = x + mu * y - x ** 2

MU = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]

fig, ax = plt.subplots(3, 3)
for ind, mu_ in enumerate(MU):
    def ODE_8_2_3(state, t):
        x, y = state
        return [-y + mu_ * x + x * y ** 2, x + mu_ * y - x ** 2]
    
    Phase_Portrait(ODE_8_2_3, (-0.5, 0.5), (-0.5, 0.5), ax[ind // 3, ind % 3], 200, 1)

    ax[ind // 3, ind % 3].set_xlabel("x")
    ax[ind // 3, ind % 3].set_ylabel("y")
    ax[ind // 3, ind % 3].set_title("mu = " + str(mu_))
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(2, 1)
plot_2d_vfield(lambda x, y: -y + 0 * x + x * y ** 2, lambda x, y: x + 0 * y - x ** 2, (-1, 1), (-1, 1), ax[0])
plot_2d_vfield(lambda x, y: -y + 0.5 * x + x * y ** 2, lambda x, y: x + 0.5 * y - x ** 2, (-1, 1), (-1, 1), ax[1])
plt.tight_layout()
plt.show()

# subcritical hopf bifurcation at mu = 0