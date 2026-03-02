import numpy as np
import matplotlib.pyplot as plt
import os
import math
import scipy.special as special

n = 3
fig, axs = plt.subplots(n + 1)
fig.suptitle('Harmonic Oscillator')
fig.tight_layout()
x = np.linspace(-5, 5, 1000)
for i in range(n + 1):
    y = 1/(math.pi ** (1/4) * np.sqrt(2 ** i * math.factorial(i)) ) * (special.hermite(i))(x) * np.exp(-x ** 2/2)
    axs[n - i].set_title("$n = " + str(i) + "$")
    axs[n - i].plot(x, y, "b", label="\psi_n(x)")
    axs[n - i].plot(x, y ** 2, "r", label="|\psi_n(x)|^2")
handles, labels = plt.gca().get_legend_handles_labels()
fig.legend(handles, labels, loc="upper right")

plt.savefig(os.path.join(os.path.dirname(__file__), "1-5.png"))
plt.show()