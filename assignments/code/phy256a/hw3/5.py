import matplotlib.pyplot as plt
from utils import TimeSeries3DODE, Phase_Portrait_3DODE, Lorenz_ODE

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 9.3.3

time_step = 0.01     # Integration time step
n_transients = 0     # Number of time steps to throw away
n_iterations = 1000  # Number of time steps
parameters = (10.0, 126.52, 8/3) # sigma, R, b

IC_INT = [((5,5,5),15), ((1,0,0),10), ((-1,0,0),10), ((0,-1,0),20)]

fig, ax = plt.subplots(len(IC_INT), 4)
for ind, i in enumerate(IC_INT):
    initial_condition, integration_time = i
    TimeSeries3DODE(Lorenz_ODE, parameters, initial_condition, n_transients, n_iterations, time_step, 0, "$t$", "$x(t)$", "Lorenz time series $x(t)$", ax[ind, 0])
    TimeSeries3DODE(Lorenz_ODE, parameters, initial_condition, n_transients, n_iterations, time_step, 1, "$t$", "$y(t)$", "Lorenz time series $y(t)$", ax[ind, 1])
    TimeSeries3DODE(Lorenz_ODE, parameters, initial_condition, n_transients, n_iterations, time_step, 2, "$t$", "$z(t)$", "Lorenz time series $z(t)$", ax[ind, 2])

    Phase_Portrait_3DODE(Lorenz_ODE, "Lorenz", parameters, initial_condition, ax[ind, 3], integration_time, 2, 0) # x(t) versus z(t)
fig.suptitle(f"Lorenz Attractor (sigma = {parameters[0]}, r = {parameters[1]}, b = {parameters[2]})")
fig.tight_layout()
plt.show()

# chaotic, tarjectories enter two stable limit cycles