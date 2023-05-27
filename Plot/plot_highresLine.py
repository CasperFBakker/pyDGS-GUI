import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Statistics/Statistics_R10Inb.csv'))
sieve_data =  np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Statistics/Statistics_photos_samples.csv'))
# print(sieve_data[0:5, 9])
plt.subplot(3,1,1)
plt.scatter([0,2,4,6,8], sieve_data[0:5, 9], color='k', label='Sieve')
plt.scatter( np.arange(0, len(data)), data[:, 9], label='pyDGS')#, yerr=0.672, fmt="o", capsize=3
plt.xticks( [0,1,2,3,4,5,6,7,8], [])
plt.xlim([-0.5,8.5])
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.ylabel('Grain size (mm)', fontsize=18)
plt.title('D90', fontsize=20)

plt.subplot(3,1,2)
plt.scatter([0,2,4,6,8], sieve_data[0:5, 6], color='k')
plt.scatter( np.arange(0, len(data)), data[:, 6])#, yerr=0.154, fmt="o", capsize=3)
plt.xticks( [0,1,2,3,4,5,6,7,8], [])
plt.ylabel('Grain size (mm)', fontsize=18)
plt.title('D50', fontsize=20)
plt.xlim([-0.5,8.5])

plt.subplot(3,1,3)
plt.scatter([0,2,4,6,8], sieve_data[0:5, 3], color='k')
plt.scatter( np.arange(0, len(data)), data[:, 3])#, yerr=0.0750, fmt="o", capsize=3)
plt.xticks([0,2,4,6,8], ['1', '0.75', '0.50', '0.25', '0'])
plt.xlabel('Cross-shore elevation (m)', fontsize=18)
plt.ylabel('Grain size (mm)', fontsize=18)
plt.title('D16', fontsize=20)
plt.xlim([-0.5,8.5])
plt.show()


# data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Statistics/Statistics_Test_2.csv'))
# # data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Statistics/Statistics_Line_2.csv'))
# plt.subplot(3,2,1)
# cross_shore = np.arange(0, len(data))
# plt.errorbar( cross_shore, data[:, 9], yerr=1.051081833, fmt="o", capsize=3)#, label='pyDGS')
# # plt.legend(bbox_to_anchor=(1,1), loc="upper left")
# plt.ylabel('Grain size (mm)', fontsize=18)
# plt.xticks(cross_shore[::2], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'])
# plt.title('D90', fontsize=20)
# plt.ylim([0.10, 5.70])

# plt.subplot(3,2,3)
# plt.errorbar( cross_shore, data[:, 6],  yerr=0.237032128, fmt="o", capsize=3)
# plt.ylabel('Grain size (mm)', fontsize=18)
# plt.xticks(cross_shore[::2], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'])
# plt.title('D50', fontsize=20)
# plt.ylim([0.2, 1.1])

# plt.subplot(3,2,5)
# plt.errorbar(cross_shore, data[:, 3], yerr=0.076684919, fmt="o", capsize=3)
# plt.xticks(cross_shore[::2], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'])
# plt.xlabel('Cross-shore distance (m)', fontsize=18)
# plt.ylabel('Grain size (mm)', fontsize=18)
# plt.title('D16', fontsize=20)
# plt.ylim([0.15, 0.55])
# # plt.show()


data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Statistics/Statistics_Test_4.csv'))

plt.subplot(3,1,1)
plt.errorbar(np.arange(0, len(data)), data[:, 9], yerr=1.051081833, fmt="o", capsize=3, label='pyDGS')
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xticks(np.arange(0, len(data)), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'])
plt.ylabel('Grain size (mm)', fontsize=18)
plt.title('D90', fontsize=20)
plt.ylim([0.10, 5.70])

plt.subplot(3,1,2)
plt.errorbar( np.arange(0, len(data)), data[:, 6], yerr=0.237032128, fmt="o", capsize=3)
plt.ylabel('Grain size (mm)', fontsize=18)
plt.xticks(np.arange(0, len(data)), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'])
plt.title('D50', fontsize=20)
plt.ylim([0.2, 1.1])

plt.subplot(3,1,3)
plt.errorbar( np.arange(0, len(data)), data[:, 3], yerr=0.076684919, fmt="o", capsize=3)
plt.xticks(np.arange(0, len(data)), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'])
plt.xlabel('Cross-shore distance (m)', fontsize=18)
# plt.ylabel('Grain size (mm)', fontsize=18)
plt.title('D16', fontsize=20)
plt.ylim([0.15, 0.55])
plt.show()