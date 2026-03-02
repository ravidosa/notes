import scipy.optimize
from utils import feven, fodd, V_qho

b = 8
for n in range(6):
    eneg = scipy.optimize.bisect(feven if n % 2 == 0 else fodd, 2 * n, 2 * n + 2, xtol=1e-4, args=(V_qho, b))
    print("n =", str(n) + ", E =", eneg)