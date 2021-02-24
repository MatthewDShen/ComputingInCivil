#imports

import numpy as np

k1 = 4
k2 = 5
k3 = 2
k4 = 1
k5 = 3

W = [
10,
2,
10,
]

k_array = np.zeros((len(W),len(W)))

k_array[0] = [k1+k2+k3+k5, -k3, -k5]
k_array[1] = [-k3, k3+k4, -k4]
k_array[2] = [-k5, -k4, k4+k5]

k_inv = np.linalg.inv(k_array)

x = k_inv.dot(W)
x = np.reshape(x, (len(x),1)).astype(float)

print(x)