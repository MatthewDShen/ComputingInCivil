import numpy as np
import matplotlib.pyplot as plt
from numpy.lib import load
import pandas as pd
from scipy.interpolate import lagrange
from scipy.optimize import ridder
from scipy.optimize import fsolve
from scipy.optimize import brentq

URL = "https://storage.googleapis.com/nm-static/deepex_fall2020/DeepEx_W3_20201217_slt_data.csv"

## Load the csv file into a dataframe
df = pd.read_csv(URL)

def capacity_calc(df, id):
    ## Pull data from 10th id set
    test = df.loc[df['lt_id'] == id]

    ## Remove unload data
    max_val = max(test['load'])
    max_index = test[test['load'] == max_val].index.values
    max_index = int(max_index[0]) - int(test[test['index'] == 1].index.values)

    test = test[:max_index]

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
    poly_coeff = np.polyfit(load, disp, 11)
    f = np.poly1d(poly_coeff)
    plt.plot(load, f(load))


    ## Determine f of delta
    line_coeff = np.polyfit((0, max_load), (delta_0, delta_max),1)
    line = np.poly1d(line_coeff)
    plt.plot(load, line(load))
    plt.plot(load,f(load))

    ## Find intersection between lines
    cap_load = fsolve(f - line, max_load)
    cap_disp = line(cap_load)
    ax.scatter(cap_load, cap_disp, edgecolors='r', facecolors='w', lw=3)

    ## Plot Formatting
    ax.invert_yaxis()
    plt.title('Displacement vs Load',fontweight = 'bold')
    plt.xlabel('Load (kips)')
    plt.ylabel('Displacement (in)')

    plt.savefig(str(id))
    plt.show()
    return cap_load, cap_disp

capacity_calc(df,10)

load_list = []
disp_list = []

print(cap_x)
ax.scatter(cap_x, line(cap_x), edgecolors='r', facecolors='w', lw=3)
# for i in set(df['lt_id']):
#     cap_load, cap_disp = capacity_calc(df,i)
#     load_list.append(cap_load)
#     disp_list.append(cap_disp)


    # test_range = []
    # for row in test.index:
    #     row
    #     test_range.append(row)

    # derv = []

    # for i in test_range[:-1]:
    #     if test['load'][i+1] - test['load'][i] == 0:
    #         continue
    #     else:
    #         derv.append((test['displacement'][i+1] - test['displacement'][i]) / (test['load'][i+1] - test['load'][i]))


    # final_derv = []
    # for i in range(0,len(derv)-1):
    #     delta_derv = derv[i+1] - derv[i]
    #     if delta_derv < 0.4:
    #         final_derv.append(delta_derv)
    #     else:
    #         break

    # test = test[:len(final_derv)+1]