import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data_Prof = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Proffitt Percentile/Percentiles_Location_1.csv')) #Proffitt_test/
data_Sieve = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Proffitt Percentile/Percentiles_Sieve.csv'))


GrainSize = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.250, 0.18, 0.125, 0.063]
locations = [1, 2, 3, 4, 5, 6, 7]
# for j in range(len(data_Sieve)):
#     data_Prof =  np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Proffitt Percentile/Proffitt_test/Percentiles_Location_' + str(locations[j]) + '.csv'))
#     for i in range(len(data_Prof)):
#         plt.subplot(2,3,int(j+1))
#         plt.scatter(GrainSize, (data_Sieve[j,1:]/(data_Prof[i,1:14])), label=data_Prof[i,14])
#         plt.xscale("log")
#         plt.yscale("log")
#         plt.grid(which='major', linewidth=2, linestyle='-')
#         plt.grid(which='minor', linewidth=1, linestyle='--')
#         plt.ylim(0.0001, 100)
#         plt.legend()


test = np.mean(np.vstack(data_Prof[:,1:]), axis=0)
print(test)
popt, pcov = curve_fit(lambda fx,a,b: a*fx**b,  GrainSize[7:14],  (data_Sieve[0,8:14]/(test[7:14])))
power_y = popt[0]*GrainSize[7:14]**popt[1]

plt.plot(GrainSize[7:14], power_y, label=str(popt[0]) + 'x**' + str(-popt[1]) )

for i in range(len(data_Prof)):
    plt.scatter(GrainSize, (data_Sieve[0,1:]/(data_Prof[i,1:14])), label=data_Prof[i,0])
    
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.01, 10)
plt.legend()

plt.show()