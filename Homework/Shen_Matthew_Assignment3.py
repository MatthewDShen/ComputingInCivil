# Matthew Shen # Assignment3 # Square of Roots #

# Imports
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from scipy.optimize import fsolve
import pint

# Units
units = pint.UnitRegistry()


# Variables

A = 25800 * units.mm**2
e = 85 * units.mm
c = 170 * units.mm
r = 142 * units.mm
L = 7100 * units.mm
E = 71e9 * units.Pa
sigma_max = 120e6 * units.Pa

# Sigma_max function
def f(u):
    return u * (1 + 0.7166 / math.cos(25 * math.sqrt(u))) - (sigma_max/E)

P = -1
i = 0

while P < 0:
    u   = fsolve(f,i)
    P =  (u * E * A).to('kN')
    i = i + 1e-10

print(P)