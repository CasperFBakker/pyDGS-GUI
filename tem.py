import numpy as np
from scipy.spatial.distance import cdist
import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf
from scipy.interpolate import griddata

def rot(x,y):
    x0 = 115187
    y0 = 558045
    ang_rot = 315 * np.pi/180
    NSx_0 = x - x0; NSy_0 = y - y0

    x = NSx_0*np.cos(ang_rot) - NSy_0*np.sin(ang_rot)
    y = NSx_0*np.sin(ang_rot) + NSy_0*np.cos(ang_rot)
    return x,y

def create_horizontal_line(y_value, x_start, x_end):
    x_coords = np.arange(x_start, x_end + 1)
    y_coords = np.full_like(x_coords, y_value)
    x_coords = x_coords[0], x_coords[-1]
    y_coords = y_coords[0], y_coords[-1]
    return np.array(x_coords), np.array(y_coords)

def create_vertical_line(x_value, y_start, y_end):
    y_coords = np.arange(y_start, y_end + 1)
    x_coords = np.full_like(y_coords, x_value)
    x_coords = x_coords[0], x_coords[-1]
    y_coords = y_coords[0], y_coords[-1]
    return np.array(x_coords), np.array(y_coords)


def Create_Rotated_Grid(y_value, Horizontal, Vertical):

    if Horizontal == True:
        for i, value in enumerate(y_value):
            x, y = create_horizontal_line(value, 114000, 118000)
            ax.plot(np.array(rot(x, y)[0]), np.array(rot(x, y)[1]), color='lightgrey', linestyle='--')

    elif Vertical == True: 
        for i, value in enumerate(y_value):
            x, y = create_vertical_line(value, 557000, 570250)
            ax.plot(np.array(rot(x, y)[0]), np.array(rot(x, y)[1]), color='lightgrey', linestyle='--')
    return 


data = pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/EURECCA 20230421 (RD2018).csv')
x = np.array(data['Easting'], dtype='float64')
y = np.array(data['Northing'], dtype='float64')
z = np.array(data['Elevation'], dtype='float64')
fig, ax = plt.subplots()

Create_Rotated_Grid([558000, 558250, 558500, 558750, 559000, 559250, 559500, 559750, 560000, 560250], Horizontal=True, Vertical=False)
Create_Rotated_Grid([115250, 115500, 115750, 116000, 116250, 116500, 116750, 117000, 117250, 117500], Horizontal=False, Vertical=True)

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


grid = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Grid_210423.csv'))
x_grid = grid[:,0]
y_grid = grid[:,1]

NSx_0 = x_grid - x0; NSy_0 = y_grid - y0
grid_x = NSx_0*np.cos(ang_rot) - NSy_0*np.sin(ang_rot)
grid_y = NSx_0*np.sin(ang_rot) + NSy_0*np.cos(ang_rot)
grid_x, grid_y = np.meshgrid(grid_x, grid_y)

grid_z = griddata((x, y), z, (grid_x.flatten(), grid_y.flatten()), method='linear')
grid_z = grid_z.reshape(grid_x.shape)
DEM = ax.imshow(grid_z, extent=(min(x), max(x), min(y), max(y)), origin='lower', cmap='terrain')
ax.scatter(x, y, c=z, cmap='viridis', edgecolors='white')

# colorbar = plt.colorbar(DEM)
# secax = ax.secondary_xaxis('top')
# secay = ax.secondary_yaxis('right')
# xticks_lst_bot = []; xticks_lst_top = []
# for i in range(9):
#     xticks_lst_bot.append(242.688 + (i*(math.sqrt(250**2 + 250**2))))
#     xticks_lst_top.append(89.913 + (i*(math.sqrt(250**2 + 250**2))))
# ax.set_xticks(xticks_lst_bot)
# ax.set_xticklabels(['115500', '115750', '116000', '116250', '116500', '116750', '117000', '117250', '117500'], rotation=45)
# secax.set_xticks(xticks_lst_top)
# secax.set_xticklabels(['558250', '558500', '558750', '559000', '559250', '559500', '559750', '551000', '551250'])

# ax.set_yticks([-13.6395, -139.087])
# ax.set_yticklabels(['558000', '115250'])

# secay.set_yticks([132.477, 68.34093])
# secay.set_yticklabels(['117250', '551250'])

# plt.ylim([-200, 200])
# plt.xlim([-50, 3050])
plt.show()

