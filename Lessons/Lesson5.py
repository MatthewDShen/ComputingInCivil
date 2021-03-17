# Interpolation & Curve Fitting

import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

x_vals = [0, 2, 3]
y_vals = [7, 11, 28]

f = lagrange(x_vals, y_vals)


x_vals = [
    0.1, 0.2, 0.5, 0.6, 0.8, 1.2, 1.5
]

y_vals = [
    -1.5342, -1.0811, -0.4445, -0.3085, -0.0868, 0.2281, 0.3824
]

f = lagrange(x_vals, y_vals)

f(1)

plt.scatter(x_vals, y_vals, c = 'red', marker = '*')
plt.show()