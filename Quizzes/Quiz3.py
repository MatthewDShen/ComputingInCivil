import scipy
import matplotlib.pyplot as plt
import numpy as np

x = [
    0.001, 0.019, 0.039, 0.058, 0.080, 0.098, 0.119, 0.139,
    0.159, 0.180, 0.198, 0.249, 0.298, 0.349, 0.398, 0.419,
    0.439, 0.460, 0.479, 0.499, 0.519, 0.540, 0.558, 0.578,
    0.598, 0.649, 0.698, 0.749, 0.798, 0.819, 0.839, 0.859,
    0.879, 0.900, 0.920, 0.939, 0.958, 0.980, 0.998
]

y = [
    0.056, 0.077, 0.076, 0.078, 0.088, 0.078, 0.105, 0.101,
    0.107, 0.111, 0.119, 0.120, 0.155, 0.195, 0.223, 0.276,
    0.293, 0.304, 0.325, 0.349, 0.370, 0.387, 0.390, 0.386,
    0.408, 0.458, 0.449, 0.467, 0.456, 0.447, 0.436, 0.443,
    0.444, 0.423, 0.429, 0.428, 0.445, 0.416, 0.400
]

x_axis = np.arange(min(x), max(x) + 0.1, 0.1)

fig, ax = plt.subplots()
ax.scatter(x, y,)

for degree in range(2):

    poly_coefficient, residual, _, _, _ = np.polyfit(x, y, degree, full=True)

    poly_function = np.poly1d(poly_coefficient)

    ax.plot(x_axis, poly_function(x_axis), label=f'deg: {degree}, res: {residual}')

    print(residual)


ax.grid(ls='-')

plt.show()
