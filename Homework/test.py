from scipy.optimize import fsolve

import numpy as np

def f(xy):
   x, y = xy
   z = np.array([y - x**2, y - x - 1.0])
   print(z)
   return z

fsolve(f, [1.0, 2.0])
