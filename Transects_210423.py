import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/EURECCA 20230421 (RD2018).csv'))
name = data[:,0]
d = data[:,6]
z = data[:,4]
Stat = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Statistics/Statistics_21_04_23.csv'))
Stat[Stat == -999] = np.nan
index = []

for i in range(len(d)):
    if name[i][0:3] == 'T25':
        index.append(i)
d = d[index]
# print(index)
plt.subplots(3,1, sharex=True)
plt.subplot(3,1,1)
plt.scatter(d, Stat[index,8])
minErr = np.array(Stat[index,8]) - 0.672; maxErr = np.array(Stat[index,8]) + 0.672

if any(math.isnan(x) for x in minErr):
    nan_indices = [index for index, value in enumerate(minErr) if math.isnan(value)]
    new_list = [value for index, value in enumerate(d) if index not in nan_indices]

    minErr = [x for x in minErr if not math.isnan(x)]; maxErr = [x for x in maxErr if not math.isnan(x)]
    plt.fill_between(np.array(new_list, dtype=float), np.array(minErr, dtype=float), np.array(maxErr, dtype=float), color='gray', alpha=0.2)
else: 
    plt.fill_between(np.array(d, dtype=float), np.array(minErr, dtype=float), np.array(maxErr, dtype=float), color='gray', alpha=0.2)
plt.grid(which='major', linewidth=0.75, linestyle='--')
plt.ylabel('D$_{90}$ [mm]', fontsize=14)
plt.title(f'Transect: {name[index[0]][1:3]}', fontsize=16)

plt.subplot(3,1,2)
plt.scatter(d, Stat[index,5])
minErr = np.array(Stat[index,5]) - 0.154; maxErr = np.array(Stat[index,5]) + 0.154

if any(math.isnan(x) for x in minErr):
    nan_indices = [index for index, value in enumerate(minErr) if math.isnan(value)]
    new_list = [value for index, value in enumerate(d) if index not in nan_indices]

    minErr = [x for x in minErr if not math.isnan(x)]; maxErr = [x for x in maxErr if not math.isnan(x)]
    plt.fill_between(np.array(new_list, dtype=float), np.array(minErr, dtype=float), np.array(maxErr, dtype=float), color='gray', alpha=0.2)
else: 
    plt.fill_between(np.array(d, dtype=float), np.array(minErr, dtype=float), np.array(maxErr, dtype=float), color='gray', alpha=0.2)

plt.grid(which='major', linewidth=0.75, linestyle='--')
plt.ylabel('D$_{50}$ [mm]', fontsize=14)

plt.subplot(3,1,3)
plt.plot(d, z[index], color='k')
plt.grid(which='major', linewidth=0.75, linestyle='--')
plt.ylabel('Elevation [m]', fontsize=14)
plt.xlabel('Cross-shore Distance [m]', fontsize=14)
plt.show()