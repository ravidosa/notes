import math
import matplotlib.pyplot as plt

print(plt)

# Nonlinear Dynamics and Chaos (Strogatz, 2e) Exercise 10.3.10

for theta_0 in [0.1, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 3.5, 4]:
    x_n = [theta_0]
    for _ in range(9):
        x_n.append(math.sin(math.pi * x_n[-1]) ** 2)
    plt.plot(range(1, 11), x_n, label="$\\theta_0 = " + str(theta_0) + "$")
plt.xlabel("$n$")
plt.ylabel("$x_n$")
plt.legend()
plt.show()

# x_n+1 = sin^2(pi * theta_n+1)
#       = sin^2(2pi * theta_n)
#       = (2 * sin(pi * theta_n) * cos(pi * theta_n))^2
#       = 4 * sin^2(pi * theta_n) * cos^2(pi * theta_n)
#       = 4 * x_n * (1 - x_n)
# chaotic, similar to logistic map at r = 4