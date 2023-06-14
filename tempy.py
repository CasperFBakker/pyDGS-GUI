import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import math
from matplotlib.ticker import AutoMinorLocator
from scipy.interpolate import Rbf
from loess.loess_2d import loess_2d
x = 117418
y = 560058

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


def Create_Rotated_Grid(y_value, ax, Horizontal, Vertical):

    if Horizontal == True:
        for i, value in enumerate(y_value):
            x, y = create_horizontal_line(value, 114000, 118000)
            ax.plot(np.array(rot(x, y)[0]), np.array(rot(x, y)[1]), color='lightgrey', linestyle='--')

    elif Vertical == True: 
        for i, value in enumerate(y_value):
            x, y = create_vertical_line(value, 557000, 570250)
            ax.plot(np.array(rot(x, y)[0]), np.array(rot(x, y)[1]), color='lightgrey', linestyle='--')
    return 

def Plot_Rotated_Maps(label, D_Stats=0, lvl_colors=8, DEM=False):
    fig, ax = plt.subplots(1,1)
    Create_Rotated_Grid([558000, 558250, 558500, 558750, 559000, 559250, 559500, 559750, 560000, 560250], ax, Horizontal=True, Vertical=False)
    Create_Rotated_Grid([115250, 115500, 115750, 116000, 116250, 116500, 116750, 117000, 117250, 117500], ax, Horizontal=False, Vertical=True)

    data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/EURECCA 20230421 (RD2018).csv'))
    x = data[:,2]
    y = data[:,3]
    if DEM == True:
        cmap = plt.get_cmap('terrain', 24)
        z = data[:,4]
    else: 
        cmap = plt.get_cmap('coolwarm', lvl_colors)        
        Stat = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Statistics/Statistics_21_04_23.csv'))
        z = Stat[:,D_Stats]
        z[z == -999] = np.nan
    
    x0 = 115187; y0 = 558045
    ang_rot = 315 * np.pi/180
    NSx_0 = x - x0; NSy_0 = y - y0

    x = NSx_0*np.cos(ang_rot) - NSy_0*np.sin(ang_rot)
    y = NSx_0*np.sin(ang_rot) + NSy_0*np.cos(ang_rot)
    
    nan_indices = [index for index, value in enumerate(z) if math.isnan(value)]
    z = [value for index, value in enumerate(z) if index not in nan_indices]
    x = [value for index, value in enumerate(x) if index not in nan_indices]
    y = [value for index, value in enumerate(y) if index not in nan_indices]

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    
    grid_x, grid_y = np.mgrid[min(x):max(x):1000j, min(y):max(y):1000j]
    # grid_z = griddata((x, y), z, (grid_x, grid_y), method='linear')

    df2 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Grid_210423.csv'))
    xi = df2[:,0]
    yi = df2[:,1]

    xi = NSx_0*np.cos(ang_rot) - NSy_0*np.sin(ang_rot)
    yi = NSx_0*np.sin(ang_rot) + NSy_0*np.cos(ang_rot)
    
    nan_indices = [index for index, value in enumerate(z) if math.isnan(value)]
    xi = [value for index, value in enumerate(x) if index not in nan_indices]
    yi = [value for index, value in enumerate(y) if index not in nan_indices]

    xi = np.array(x)
    yi = np.array(y)


    grid_z, _ = loess_2d(x, y, z, xnew=xi, ynew=yi, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)

    MAP = ax.tricontourf(xi,yi,grid_z, cmap=cmap) #imshow(grid_z, extent=(min(x), max(x), min(y), max(y)), origin='lower', cmap=cmap)
    plt.scatter(x,y, color='k', s=0.75)
    colorbar = plt.colorbar(MAP, orientation='horizontal', label=label)

    # Create Rotated axis-ticks/labels:
    secax = ax.secondary_xaxis('top')
    secay = ax.secondary_yaxis('right')
    xticks_lst_bot = []; xticks_lst_top = []
    for i in range(9):
        xticks_lst_bot.append(242.688 + (i*(math.sqrt(250**2 + 250**2))))
        xticks_lst_top.append(89.913 + (i*(math.sqrt(250**2 + 250**2))))

    ax.set_xticks(xticks_lst_bot)
    ax.set_xticklabels(['115500', '115750', '116000', '116250', '116500', '116750', '117000', '117250', '117500'], rotation=45)
    secax.set_xticks(xticks_lst_top)
    secax.set_xticklabels(['558250', '558500', '558750', '559000', '559250', '559500', '559750', '551000', '551250'])

    ax.set_yticks([-13.6395, -139.087])
    ax.set_yticklabels(['558000', '115250'])

    secay.set_yticks([132.477, 68.34093])
    secay.set_yticklabels(['117250', '551250'])

    plt.ylim([-200, 200])
    plt.xlim([-50, 3050])

    plt.show()



# fig, axes = plt.subplots(3,1)
Plot_Rotated_Maps(label='Elevation [m]', DEM=True)
Plot_Rotated_Maps(D_Stats=9, lvl_colors=7, label='D90 [mm]', DEM=False)
Plot_Rotated_Maps(D_Stats=6, lvl_colors=20, label='D50 [mm]',DEM=False)

