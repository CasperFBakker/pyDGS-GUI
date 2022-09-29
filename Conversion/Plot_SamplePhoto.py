import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/All_Data/Percentile_SamplePhotos_CorrectedAVG.csv'))

percentiles = [5, 10, 16, 25, 30, 50,  75, 84, 90, 95] 
sieve_open = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063]
sieve_data_1 = [100, 98, 91, 73, 55, 32, 26, 19, 14, 9, 3, 0, 0]
sieve_data_2 = [97,94,89,79,74,57,49,35,22,8,1,0,0]
sieve_data_3 = [88,79,70,59,54,49,45,38,30,17,4,1,0]
sieve_data_4 = [98,91,76,53,44,33,27,19,12,5,1,0,0]
sieve_data_5 = [93,53,4,0,0,0,0,0,0,0,0,0,0]
sieve_data_6 = [99,96,92,88,85,77,72,62,50,33,11,2,0]
sieve_data_7 = [99,98,86,66,60,51,45,35,26,16,6,1,0]
GrainSize = [0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]


plt.subplot(2,3,1)
plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')
plt.plot(GrainSize, data[0,1:])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.ylabel('Percent finer (%)', fontsize=20)
plt.title('Location 1')

plt.subplot(2,3,2)
plt.plot(sieve_open, sieve_data_2, ls='--', color='black', label='Sieved')
plt.plot(GrainSize, data[1,1:])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 2')

plt.subplot(2,3,3)
plt.plot(sieve_open, sieve_data_3, ls='--', color='black', label='Sieved')
plt.plot(GrainSize, data[2,1:])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 3')

plt.subplot(2,3,4)
plt.plot(sieve_open, sieve_data_4, ls='--', color='black', label='Sieved')
plt.plot(GrainSize, data[3,1:])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.ylabel('Percent finer (%)', fontsize=20)
plt.title('Location 4')

plt.subplot(2,3,5)
plt.plot(sieve_open, sieve_data_6, ls='--', color='black', label='Sieved')
plt.plot(GrainSize, data[4,1:])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.title('Location 6')

plt.subplot(2,3,6)
plt.plot(sieve_open, sieve_data_7, ls='--', color='black', label='Sieved')
plt.plot(GrainSize, data[5,1:])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.title('Location 7')

plt.show()