import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


def f(lam):
    return (1/lam) * (math.cosh(80 * lam) - 1) - 15

lam_range = np.linspace(0.0001, 0.01)

plt.plot(lam_range, [f(i) for i in lam_range])

plt.grid()

plt.show()

root, details = scipy.optimize.ridder(f, 0.0001, 1, full_output=True)

def s(lam):
    return 2/lam * math.sinh(80 * lam)

print('length:', s(root))