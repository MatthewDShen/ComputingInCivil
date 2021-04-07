import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import lagrange
from scipy.optimize import ridder
from scipy.optimize import fsolve
from scipy.optimize import brentq

URL = "https://storage.googleapis.com/nm-static/deepex_fall2020/DeepEx_W3_20201217_slt_data.csv"

## Load the csv file into a dataframe
df = pd.read_csv(URL)

## Pull data from 10th id set
test = df.loc[df['lt_id'] == 45]

## save relevant data into variables
load = np.array(test['load'])
disp = np.array(test['displacement'])
aeol = test['aeol'].values[0]
diam = test['diameter'].values[0]

## criterion for P = 0
delta_0 = 1/aeol * 0 + 0.15 + diam/120

## criterion for max P plus 10% (to extend the line a bit)
max_load = np.max(load)
delta_max = 1/aeol * max_load*1.1 + 0.15 + diam/120

## Start plotting
fig, ax = plt.subplots()

ax.plot(load, disp)
ax.plot((0, max_load), (delta_0, delta_max))

## Determine poly of disp vs load
poly_coeff = np.polyfit(load, disp, 11) #len(load))
f = np.poly1d(poly_coeff)
# plt.plot(load, f(load))

## Determine f of delta
line_coeff = np.polyfit((0, max_load), (delta_0, delta_max),1)
line = np.poly1d(line_coeff)
plt.plot(load, line(load))


# plt.xlim(0, 800)
# plt.ylim(2, 0)
# Solving for intersection

x = 0
cap_x = -1

# print("f= ", f, "\n\n")
# print("line= ", line, "\n\n")
# print("f - line= ", f - line, "\n\n")

# while cap_x < 0:
#     cap_x = ridder(f - line, 0, max_load)
#     x += 100
#     print(cap_x)


# print(f)
# print(line)

plt.plot(load,f(load))
# print(len(f))
# print(len(f-line))
# print(np.roots(f-line))
# print(ridder(f - line, 0, max_load))
# print(brentq(f - line, 0, max_load))
cap_x = fsolve(f - line, max_load)

ax.scatter(cap_x, line(cap_x), edgecolors='r', facecolors='w', lw=3)

ax.invert_yaxis()
plt.show()