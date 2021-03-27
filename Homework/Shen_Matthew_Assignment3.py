# Matthew Shen # Assignment3 # Square of Roots #

# Imports
import numpy as np
import matplotlib.pyplot as plt
import pint

# Pint/Unit Setup
units = pint.UnitRegistry()

# Variables

A = 25800
e = 85
c = 170
r = 142
L = 7100
E = 71*10**9
sigma_max = 120 * 10 ** 6

# Sigma_max function
def sigma(P):
    sigma_line = P/A
    sigma = sigma_line * (1 +  (e*c/r**2) * 1/np.cos((L/2*r) * np.sqrt(sigma_line/E)))
    return sigma


x_vals = np.linspace(0,1,sigma_max)

plt.plot(x_vals , sigma(x_vals))
plt.plot(x_vals , [sigma_max] * len(x_vals))
plt.show()
