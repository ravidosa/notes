import matplotlib.pyplot as plt
from sympy import symbols
from utils import Phase_Portrait

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 8.1.1

x, y = symbols("x, y")

MU = [-0.25, 0, 0.25]

fig, ax = plt.subplots(3, 1)
for ind, mu_ in enumerate(MU):
    def ODE_8_1_1(state, t):
        x, y = state
        return [mu_ * x - x ** 2, -y]
    
    Phase_Portrait(ODE_8_1_1, (-0.5, 0.5), (-0.5, 0.5), ax[ind], 200, 1)

    ax[ind].set_xlabel("x")
    ax[ind].set_ylabel("y")
    ax[ind].set_title("mu = " + str(mu_))
plt.tight_layout()
plt.show()

# mu > 0 -> 1 unstable node at (mu, 0), 1 saddle point at (0, 0)
# mu = 0 -> 1 saddle point at (0, 0)
# mu < 0 -> 1 unstable node at (0, 0), 1 saddle point at (mu, 0)