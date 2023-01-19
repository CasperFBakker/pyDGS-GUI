import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_cor = pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/08_07_22/Percentile_corrected/Percentiles_Location_7.csv')
data_og = pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/08_07_22/Percentile_og/Percentiles_Location_7.csv')
data_og = np.array(data_og)
data_cor = np.array(data_cor)

percentiles = [5, 10, 16, 25, 30, 50,  75, 84, 90, 95] 
sieve_open = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063]
sieve_data_1 = [100, 98, 91, 73, 55, 32, 26, 19, 14, 9, 3, 0, 0]
sieve_data_2 = [97,94,89,79,74,57,49,35,22,8,1,0,0]
sieve_data_3 = [88,79,70,59,54,49,45,38,30,17,4,1,0]
sieve_data_4 = [98,91,76,53,44,33,27,19,12,5,1,0,0]
sieve_data_5 = [93,53,4,0,0,0,0,0,0,0,0,0,0]
sieve_data_6 = [99,96,92,88,85,77,72,62,50,33,11,2,0]
sieve_data_7 = [99,98,86,66,60,51,45,35,26,16,6,1,0]


plt.subplot(1,2,1)
plt.plot(sieve_open, sieve_data_7, ls='--', color='black', label='Sieved')
plt.plot(data_og[2,1:11], percentiles, ls=':', color='black', label=data_og[2,11])
for i in range(0,2):
    plt.plot(data_og[i,1:11], percentiles, marker='.', label=data_og[i,11])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.ylabel('Percent finer (%)', fontsize=20)
plt.title('Original', fontsize=20)


plt.subplot(1,2,2)
plt.plot(sieve_open, sieve_data_7, ls='--', color='black', label='Sieved')
plt.plot(data_cor[2,1:11], percentiles, ls=':', color='black', label=data_cor[2,11])
for i in range(0,2):
    plt.plot(data_cor[i,1:11], percentiles, marker='.', label=data_cor[i,11])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Corrected', fontsize=20)


# plt.subplot(2,2,3)
# plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')
# plt.plot(data_cor[14,1:11], percentiles, ls=':', color='black', label=data_cor[14,11])
# for i in range(0,5):
#     plt.plot(data_cor[i,1:11], percentiles, marker='.', label=data_cor[i,11])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)
# plt.ylabel('Percent finer (%)', fontsize=20)
# plt.title('Corrected', fontsize=20)

# plt.subplot(2,2,4)
# plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')
# plt.plot(data_cor[14,1:11], percentiles, ls=':', color='black', label=data_cor[14,11])
# for i in range(5,7):
#     plt.plot(data_cor[i,1:11], percentiles, marker='.', label=data_cor[i,11])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])

plt.suptitle('Location 7', fontsize=20)

plt.show()