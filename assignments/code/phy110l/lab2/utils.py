import numpy as np
import matplotlib as plt
import functools

class Charge:
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q
        return
    def potential_grid(self, xgrid, ygrid):
        r = np.hypot(xgrid - self.x, ygrid - self.y)
        return self.q/r
    def field_grid(self, xgrid, ygrid):
        r = np.hypot(xgrid - self.x, ygrid - self.y)
        return self.q * (ygrid - self.y) / r ** 3, self.q * (xgrid - self.x) / r ** 3
    def potential(self, x, y):
        r = np.hypot(x - self.x, y - self.y)
        return self.q/r
    def field(self, x, y):
        r = np.hypot(x - self.x, y - self.y)
        return self.q * (y - self.y) / r ** 3, self.q * (x - self.x) / r ** 3

def central_2nd(f, h):
    dim = len(np.shape(f))
    df = [None] * dim
    for d in range(dim):
        mi, ma = ((slice(None),) * (d - 1) + (0,)) + (slice(None),) * max((dim - max(d, 1)), 0), ((slice(None),) * (d - 1) + (-1,)) + (slice(None),) * max((dim - max(d, 1)), 0)
        f_ = (np.roll(f, -1, axis=d) - np.roll(f, 1, axis=d)) / (2 * h)
        f_[mi], f_[ma] = ((np.roll(f, -1, axis=d) - f) / (h))[mi], ((f - np.roll(f, 1, axis=d)) / (h))[ma]
        df[d] = f_
    return df

def launch(initial, final, dir, h, charge_list, ax):
    # field lines travel from cyan to magenta
    xi, yi = initial
    xf, yf = final

    x, y = xi, yi
    ax.plot(x, y, "co", markersize="2", zorder=999999)
    while np.hypot(x - xf, y - yf) > h:
        E_y, E_x = functools.reduce(lambda e, c : np.add(e, c.field(x, y)), charge_list, (0, 0))
        E = np.hypot(E_x, E_y)
        x, y = x + h * E_x / E * (-1) ** dir, y + h * E_y / E * (-1) ** dir
        ax.plot(x, y, "ko", markersize="2")
    ax.plot(x, y, "mo", markersize="2", zorder=999999)
