import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/EURECCA 20230421 (RD2018).csv'))
x = data[:,2]
y = data[:,3]
z = data[:,4]

grid_x, grid_y = np.mgrid[min(x):max(x):1000j, min(y):max(y):1000j]
grid_z = griddata((x, y), z, (grid_x, grid_y), method='linear')
plt.imshow(grid_z.T, extent=(min(x), max(x), min(y), max(y)), origin='lower', cmap='coolwarm')
grid_x, grid_y = np.mgrid[min(x):max(x):10j, min(y):max(y):10j]
plt.plot(grid_x, grid_y, linestyle='--', color='lightgrey')
plt.colorbar(label='Z')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolated 2D Map')
plt.show()


###############################################################################################################################
# plt.subplot(1,2,2)

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/EURECCA 20230421 (RD2018).csv'))
x = data[:,2]
y = data[:,3]
z = data[:,4]

x0 = 115187
y0 = 558045
ang_rot = 315 * np.pi/180
NSx_0 = x - x0; NSy_0 = y - y0

x = NSx_0*np.cos(ang_rot) - NSy_0*np.sin(ang_rot)
y = NSx_0*np.sin(ang_rot) + NSy_0*np.cos(ang_rot)

grid_x, grid_y = np.mgrid[min(x):max(x):1000j, min(y):max(y):1000j]

grid_z = griddata((x, y), z, (grid_x, grid_y), method='linear')

plt.imshow(grid_z.T, extent=(min(x), max(x), min(y), max(y)), origin='lower', cmap='coolwarm')
# plt.scatter(x, y, c=z, cmap='viridis', edgecolors='white')
# plt.colorbar(label='Z')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Interpolated 2D Map')
plt.show()

