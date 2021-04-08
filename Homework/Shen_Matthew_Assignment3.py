# Matthew Shen # Assignment3 # Square of Roots #

# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.interpolate import lagrange
from scipy.optimize import fsolve
import pint

# Units
u = pint.UnitRegistry()


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


x_vals = np.linspace(0 , sigma_max*1.25, 100)

# Generate polynomial for maxiumum function
sigma_poly = lagrange(x_vals , sigma(x_vals)) - sigma_max

# Determine intersection between polynomial and line
P   = fsolve(sigma_poly,0)
print(P)
print (sigma(P))
