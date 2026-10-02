import numpy as np

# System of Units:
# Position:  a = 1
# Energy:   E0 = hbar^2 / (2 m a^2)

# Potential V(x) in units of E0
def V(x):
    pass

def V_inf_pot(x):
    return 0

def V_qho(x):
    return np.square(x)

def V_sawtooth(x):
    return np.abs(x)

# TISE as two first order diff eqs:
# Y = (psi, phi)
# F = dY/dx = (dpsi/dx, dphi/dx)
# dpsi/dx = phi
# dphi/dx = (V-E) psi
def F(Y, x, E, V):
    psi = Y[0]
    phi = Y[1]
    dpsi_dx = phi
    dphi_dx = (V(x) - E) * psi
    F = np.array([dpsi_dx, dphi_dx], float)
    return F

# Numerical integration (using Runge-Kutta Order 1)
def tise_rk1(E, V, psi0, phi0, a, b, h):
    Y = np.array([psi0, phi0], float)
    X = np.arange(a, b, h, float)
    PSI = np.array([psi0], float)
    for x in X:
        # 1st order Runge-Kutta:
        K1 = h * F(Y, x, E, V)
        Y += K1
        PSI = np.append(PSI, Y[0])
    X = np.append(X, b)
    return X, PSI

# Numerical integration (using Runge-Kutta Order 4)
def tise_rk4(E, V, psi0, phi0, a, b, h):
    Y = np.array([psi0, phi0], float)
    X = np.arange(a, b, h, float)
    PSI = np.array([psi0], float)
    for x in X:
        # 1st order Runge-Kutta:
        K1 = h * F(Y, x, E, V)
        K2 = h * F(Y + K1 / 2, x + h / 2, E, V)
        K3 = h * F(Y + K2 / 2, x + h / 2, E, V)
        K4 = h * F(Y + K3, x + h, E, V)
        Y += (K1 + 2 * K2 + 2 * K3 + K4) / 6
        PSI = np.append(PSI, Y[0])
    X = np.append(X, b)
    return X, PSI

def feven(E, V, b):
    X, PSI = tise_rk4(E = E, V = V, psi0 = 1, phi0 = 0, a = 0, b = b, h = 0.01)
    return PSI[-1]
def fodd(E, V, b):
    X, PSI = tise_rk4(E = E, V = V, psi0 = 0, phi0 = 1, a = 0, b = b, h = 0.01)
    return PSI[-1]