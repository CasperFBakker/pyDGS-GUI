import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.pyplot import cm
import math

def Percentage2Percentile(Percentage):
    Percentage = Percentage[::-1]
    Percentile = 100 - np.nancumsum(Percentage)

    Percentile_cor = []
    for index, value in enumerate(Percentile):
        if value < 0:
            Percentile_cor.append(0)
        else:
            Percentile_cor.append(value)

    Percentile_cor = Percentile_cor[::-1]
    
    return Percentile_cor

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Corrected/Corrected_All_GrainShape.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Percentile_Sieve.csv'))
GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])

est1 = Percentage2Percentile(data[1,2:])sieve1 = sieve_data[1,2:]plt.plot(GrainSz, sieve1, ls='--', color='black')
plt.plot(GrainSz, test1)
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.ylabel('Percent finer (%)', fontsize=20)
plt.show()









sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

plt.subplot(2,1,1)
for i in range(len(sieve_data)):
    plt.scatter(sieve_open, ( sieve_data[i,2:] - dgs_data[i,2:] ), color=color[i], label= sieve_data[i,0])
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xscale("log")
plt.hlines(0, 0.063, 8, color='k')
plt.title('Different Grain Shapes', fontsize=20)


























label('%-Sieve - %-pyDGS ', fontsize=20)


error = sieve_data[:34, 2:]- dgs_data[:34, 2:]
std = np.std(error.astype(np.float64), axis=0)

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
plt.subplot(2,1,2)

plt.errorbar(x=sieve_open, y=np.mean(error, axis=0), yerr=std, capsize=3)
plt.hlines(0, 0.063, 8, color='k')
plt.xscale('log')
plt.ylabel('Mean Absolute Error', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)

plt.show()
