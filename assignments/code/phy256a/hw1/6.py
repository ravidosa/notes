import matplotlib.pyplot as plt
from math import sin
from utils import Phase_Portrait

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 7.1.4

def ODE_7_1_4(state, t):
	r, theta = state
	return [r * sin(r), 1]

nICs = 200
IntegrationTime = 1
fig = Phase_Portrait(ODE_7_1_4, (-10, 10), (-10, 10), nICs,IntegrationTime, polar=True)
plt.show()

# J =   sin(r) + r cos(r)   0
#       0                   0
# tr(J) = sin(r) + r cos(r)
# det(J) = 0
# (0, 0) -> unstable fp
# (n pi, theta) -> unstable is (even n) / stable is (odd n)