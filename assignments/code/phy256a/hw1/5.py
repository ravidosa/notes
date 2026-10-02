import matplotlib.pyplot as plt
from math import sin
from utils import Phase_Portrait

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 6.3.2, 6.3.7

def ODE_6_3_2(state, t):
	x, y = state
	return [sin(y), x - x ** 3]

nICs = 200
IntegrationTime = 1
fig = Phase_Portrait(ODE_6_3_2, (-2, 2), (-10, 10), nICs,IntegrationTime)
plt.show()

# J =   0           cos(y)
#       1 - 3x^2    0
# tr(J) = 0
# det(J) = cos(y)(3x^2 - 1)
# (-1, n pi) -> center (even n) / saddle point (odd n)
# (0, n pi) -> saddle point (even n) / center (odd n)
# (1, n pi) -> center (even n) / saddle point (odd n)