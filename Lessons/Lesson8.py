# Advance Visualization

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 3

plt.plot(x, y, color = '#de2d26')

plt.plot(x,y)
plt.show()


#Subplots w/ defining a figure

plt.subplot(2, 2, 1) #<-- nrow, ncol, number of plot

plt.plot(x, y, 'r--')
plt.plot(y, x, 'g*-')
plt. subplot(2, 2, 3)
plt.plot(y, x, 'y-')

fig, ax = plt.subplots(figsize=(7,5))

ax.set_title('Main Title', fontweight = 'bold')
ax.set_ylabel('Y Label')
ax.set_xlabel('X Label')
ax.grid()

ax.plot(x, y, color = '#de2d26')


fig, ax - plt.subplots(nrows = 1, ncols = 2, figsize= (7,5 ))

ax[0].plot(x, y, 'r--')

ax[1].plot(y, x, 'g*-')

plt.show()