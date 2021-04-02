from re import I
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import lagrange
from scipy.optimize import fsolve

URL = "https://storage.googleapis.com/nm-static/deepex_fall2020/DeepEx_W3_20201217_slt_data.csv"

# Load the csv file into a dataframe
df = pd.read_csv(URL)

test = df.loc[df['lt_id'] == 10]
# save relevant data into variables
load = np.array(test['load'])
disp = np.array(test['displacement'])
aeol = test['aeol'].values[0]
diam = test['diameter'].values[0]

# criterion for P = 0
delta_0 = 1/aeol * 0 + 0.15 + diam/120

# criterion for max P plus 10% (to extend the line a bit)
max_load = np.max(load)
delta_max = 1/aeol * max_load*1.1 + 0.15 + diam/120

# Start plotting
fig, ax = plt.subplots()

ax.plot(load, disp)
criterion = ax.plot((0, max_load), (delta_0, delta_max))
# ax.invert_yaxis()

poly_coeff = np.polyfit(load, disp, 11)
f = np.poly1d(poly_coeff)

plt.plot(load, f(load))
# plt.xlim(0, 800)
# plt.ylim(2, 0)
line = lagrange([0 , delta_0],[max_load , delta_max])

# criterion = int.lagrange([0,delta_0],[max_load,delta_max])


# Solving for intersection

# opt.fsolve(test_load_curve, 0)

# ax.scatter((747), (0.63), edgecolors='r', facecolors='w', lw=3)

plt.show()