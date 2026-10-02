import numpy as np

def hermite_power(n):
    coeffs = np.zeros(n + 1)
    coeffs[n] = 2 ** n
    i = n
    while i - 2 >= 0:
        i = i - 2
        coeffs[i] = coeffs[i + 2] * ((i + 1) * (i + 2)) / (-2 * (n - i))
    return coeffs

def hermite_generating(n):
    coeffs = np.zeros(n + 1)
    coeffs[0] = 1
    for i in range(n):
        coeffs = np.roll(coeffs, 1) + np.roll(-2 * np.multiply(coeffs, np.arange(0, n + 1)), -1) # chain ruling
    coeffs = np.multiply(2 ** np.arange(0, len(coeffs)), coeffs)
    return coeffs

def hermite_recursion(n, u):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * u
    else:
        return 2 * u * hermite_recursion(n - 1, u) - 2 * (n - 1) * hermite_recursion(n - 2, u)