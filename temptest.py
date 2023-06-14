import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

grid = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Grid_210423.csv'))
x_grid = grid[:,0]
y_grid = grid[:,1]

x_g, y_g = np.meshgrid(x_grid, y_grid)

plt.scatter(x_g.flatten(), y_g.flatten())
plt.show()