import numpy as np

class Charge:
    def __init__(self, x, y, q):
        self.x = x
        self.y = y
        self.q = q
        return
    def potential(self, xgrid, ygrid):
        r = np.hypot(xgrid - self.x, ygrid - self.y)
        return self.q/r