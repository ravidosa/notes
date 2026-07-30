import matplotlib.pyplot as plt
from utils import Phase_Portrait

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 6.1.8

def ODE_6_1_8(state, t):
	x, y = state
	return [y, -x + y * (1 - x ** 2)]

nICs = 200
IntegrationTime = 1
fig = Phase_Portrait(ODE_6_1_8, (-2, 2), (-1, 1), nICs,IntegrationTime)
plt.show()