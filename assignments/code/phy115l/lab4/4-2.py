import numpy as np
from utils import norm

# normalization check
x = np.linspace(-10, 10, 100)
y = np.random.uniform(size=np.size(x))
y = norm(x, y)
print(np.sum(y ** 2) * (x[1] - x[0]))