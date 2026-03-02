import numpy as np

def central_2nd(y, h):
    y__ = (np.roll(y, 1) - 2 * y + np.roll(y, -1)) / h ** 2
    y__[0], y__[-1] = 0, 0
    return y__

def norm(x, y):
    x_ = x - np.roll(x, 1)
    x_[0] = 0
    return y / np.sqrt(np.sum((np.dot(x_, y ** 2))))

def energy(x, y, V, par):
    h = x[1] - x[0]
    return h * np.sum(y * (-central_2nd(y, h) + V(x, par) * y))

def V_fp(x, par):
    OFFSET = par
    return OFFSET * np.ones(np.shape(x))

def V_inf_pot(x, par):
    B = par
    return np.piecewise(x, [x < -1, (-1 <= x) & (x < 1), 1 <= x], [B, 0, B])

def V_inf_pot_pet(x, par):
    B = par
    return np.piecewise(x, [x < -1, (-1 <= x) & (x < 1), 1 <= x], [B, lambda y: -np.cos(np.pi / 2 * y), B])

def V_qho(x, par):
    return x ** 2