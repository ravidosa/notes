import numpy as np
import matplotlib.pyplot as plt

def V(x, y, coeffs, N):
    k, sin_plus, cos_plus, sin_min, cos_min = coeffs
    V = np.zeros_like(x, dtype=float)
    for n in range(1, N + 1):
        k_n, sin_plus_n, cos_plus_n, sin_min_n, cos_min_n = k(n), sin_plus(n), cos_plus(n), sin_min(n), cos_min(n)
        V += (sin_plus_n * np.sin(k_n * x) * np.exp(k_n * y) + cos_plus_n * np.cos(k_n * x) * np.exp(k_n * y) + sin_min_n * np.sin(k_n * x) * np.exp(-k_n * y) + cos_min_n * np.cos(k_n * x) * np.exp(-k_n * y))
    return V

def E_x(x, y, coeffs, N):
    k, sin_plus, cos_plus, sin_min, cos_min = coeffs
    E_x_ = np.zeros_like(x, dtype=float)
    for n in range(1, N + 1):
        k_n, sin_plus_n, cos_plus_n, sin_min_n, cos_min_n = k(n), sin_plus(n), cos_plus(n), sin_min(n), cos_min(n)
        E_x_ -= (sin_plus_n * k_n * np.cos(k_n * x) * np.exp(k_n * y) + cos_plus_n * k_n * -np.sin(k_n * x) * np.exp(k_n * y) + sin_min_n * k_n * np.cos(k_n * x) * np.exp(-k_n * y) + cos_min_n * k_n *np.sin(k_n * x) * np.exp(-k_n * y))
    return E_x_

def E_y(x, y, coeffs, N):
    k, sin_plus, cos_plus, sin_min, cos_min = coeffs
    E_y_ = np.zeros_like(x, dtype=float)
    for n in range(1, N + 1):
        k_n, sin_plus_n, cos_plus_n, sin_min_n, cos_min_n = k(n), sin_plus(n), cos_plus(n), sin_min(n), cos_min(n)
        E_y_ -= (sin_plus_n * k_n * np.sin(k_n * x) * np.exp(k_n * y) + cos_plus_n * k_n * np.cos(k_n * x) * np.exp(k_n * y) + sin_min_n * -k_n * np.sin(k_n * x) * np.exp(-k_n * y) + cos_min_n * -k_n * np.cos(k_n * x) * np.exp(-k_n * y))
    return E_y_

def term(x, y, xf, yf, eps, lim):
    if (np.abs(xf) != np.inf and np.abs(yf) != np.inf):
        return np.hypot(x - xf, y - yf) > eps
    else:
        xmin, xmax, ymin, ymax = lim
        return np.abs(x - (xmin + xmax) / 2) <= (xmax - xmin) / 2 and np.abs(y - (ymin + ymax) / 2) <= (ymax - ymin) / 2
def launch(initial, final, dir, h, field, ax, lim, col):
    # field lines travel from cyan to magenta
    xi, yi = initial
    xf, yf = final
    coeffs, N = field

    x, y = xi, yi
    ax.plot(x, y, "co", markersize="2", zorder=999999)
    while term(x, y, xf, yf, h, lim):
        E_y_1, E_x_1 = E_y(x, y, coeffs, N), E_x(x, y, coeffs, N)
        E_1 = np.hypot(E_x_1, E_y_1)
        x, y = x + h * E_x_1 / E_1 * (-1) ** dir, y + h * E_y_1 / E_1 * (-1) ** dir
        ax.plot(x, y, color=col, marker="o", markersize="2")
    ax.plot(x, y, "mo", markersize="2", zorder=999999)