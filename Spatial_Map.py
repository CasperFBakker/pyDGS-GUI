import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/TexelContour.csv'))
x = data[:,0]
y = data[:,1]
z = data[:,2]

print(list(x))
print(list(y))
print(list(z))
# for i in range(len(x)):
#     Data.append(data[i,1])
#     Data.append(data[i,2])


plt.tricontourf(list(x), list(y), list(z))
plt.colorbar()

# data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (RD2018).csv'))
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (WGS84).csv'))
plt.scatter(data[8:12,2], data[8:12,3], label = data[8,0])
plt.scatter(data[14:18,2], data[14:18,3], label = data[14,0])
plt.scatter(data[20:23,2], data[20:23,3], label = data[20,0])
plt.scatter(data[26:29,2], data[26:29,3], label = data[26,0])
plt.scatter(data[32:36,2], data[32:36,3], label = data[32,0])
plt.scatter(data[38:42,2], data[38:42,3], label = data[38,0])
plt.scatter(data[44:48,2], data[44:48,3], label = data[44,0])
plt.scatter(data[51:57,2], data[51:57,3], label = data[51,0])
plt.legend()

plt.show()

###################????????????????????
# contour_data = pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/TexelContour.csv')

# Z = contour_data.pivot_table(index='x', columns='y', values='z').T.values
# Z = contour_data.pivot_table(index='x', columns='y', values='z')
# X_unique = np.sort(contour_data.x.unique())
# Y_unique = np.sort(contour_data.y.unique())
# X, Y = np.meshgrid(contour_data.x, contour_data.y)

# plt.contour(X,Y,Z)
# plt.show()


from scipy.interpolate import griddata
import numpy as np
from numpy import inf
import loess
import math
# construct a dummy df like you have
contour_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/TexelContour.csv'))

x = contour_data[:,0]
y = contour_data[:,1]
z = contour_data[:,2]

values = np.stack((x,y), axis=1)
length_values = len(x) * len(y)

# create grid
x_grid, y_grid = np.meshgrid(x, y)
points = np.empty((length_values, 2))
points[:, 0] = x_grid.flatten()
points[:, 1] = y_grid.flatten()
# np.arange()
print(np.shape(x_grid))

Z = griddata(values, z, points, method='linear', fill_value=0)

Z[Z==math.inf] = 0



