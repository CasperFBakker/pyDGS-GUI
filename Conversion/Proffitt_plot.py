import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data_Proff = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Proffitt Percentile/Percentiles_Location_1.csv')) #Proffitt_test/
data_Sieve = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Proffitt Percentage/Percentages_Sieve.csv'))
#data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/DiplasSutherland/Percentiles_All_NewTrends.csv'))
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Percentile_Sample_subLoc4.csv'))
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Percentile_Sample_TrendAll.csv'))

#data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/DiplasSutherland/Percentiles_All_NewTrends.csv'))
data_filt = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/DiplasSutherland/Percentiles_All_retryCor_Filt.csv'))
data_cor = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Proffitt Percentage/MinScale_3px/Corrected/Percentages_Location_2.csv'))
GrainSize = [0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

yfit = np.array([0.020935676, 0.542458378, 1.533985016, 2.96107423, 2.331361229, 2.225390513, 1.432469352, 1.400264352, 0.791868859, 0.51059136, 0.523111247, 0.521509998, 0])
xfit = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])

# z = np.polyfit(xfit, yfit, 8)
# p = np.poly1d(z)
# print(p)
# plt.plot(xfit, p(xfit))

# for i in range(len(data)):
#     plt.scatter(GrainSize, data[i,1:15], label=data[i,15])

# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend(loc='lower right')


# plt.show()


# for i in range(len(data_cor)):
#     plt.scatter(GrainSize, data_cor[i,1:15], label=data_cor[i,15])

# plt.plot(GrainSize, data_Sieve[2,1:15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend(loc='lower right')


# plt.show()


# test = [0, 0, 0, -1.42109E-14, 5.519002422, 15.66399965, 20.23133051, 28.23999375, 44.86900116, 61.05241317, 87.69624203, 97.15556986, 100]
# testx = [0.063, 0.125, 0.18, 0.25, 0.3, 0.355, 0.425, 0.5, 0.71, 1, 2, 4, 8]
# sieve_open = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063]
# sieve_data_2 = [97,94,89,79,74,57,49,35,22,8,1,0,0]

# for i in range(len(data_cor)):
#     plt.plot(GrainSize, data_cor[i,2:15], label=data_cor[i,15])

# plt.plot(testx, test)
# plt.plot(sieve_open, sieve_data_2, ls='--', color='black')


# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.legend()
# plt.show()



######################################################################################################################################################################
percentiles = [5, 10, 16, 25, 30, 50,  75, 84, 90, 95] 
sieve_open = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063]
sieve_data_1 = [100, 98, 91, 73, 55, 32, 26, 19, 14, 9, 3, 0, 0]
sieve_data_2 = [97,94,89,79,74,57,49,35,22,8,1,0,0]
sieve_data_3 = [88,79,70,59,54,49,45,38,30,17,4,1,0]
sieve_data_4 = [98,91,76,53,44,33,27,19,12,5,1,0,0]
sieve_data_5 = [93,53,4,0,0,0,0,0,0,0,0,0,0]
sieve_data_6 = [99,96,92,88,85,77,72,62,50,33,11,2,0]
sieve_data_7 = [99,98,86,66,60,51,45,35,26,16,6,1,0]


plt.subplot(2,3,1)
plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')
for i in range(1, 14):
    plt.plot(GrainSize, data[i, 1:15], label=data[i,15])
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
for i in range(14, 22):
    plt.plot(GrainSize, data[i, 1:15], label=data[i,15])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 2')

plt.subplot(2,3,3)
plt.plot(sieve_open, sieve_data_3, ls='--', color='black', label='Sieved')
for i in range(22, 26):
    plt.plot(GrainSize, data[i, 1:15], label=data[i,15])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 3')

plt.subplot(2,3,4)
plt.plot(sieve_open, sieve_data_4, ls='--', color='black', label='Sieved')
for i in range(26, 34):
    plt.plot(GrainSize, data[i, 1:15], label=data[i,15])
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
for i in range(34, 42):
    plt.plot(GrainSize, data[i, 1:15], label=data[i,15])
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
for i in range(42, 44):
    plt.plot(GrainSize, data[i, 1:15], label=data[i,15])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.title('Location 7')

#plt.suptitle('Fit without data of location 4', fontsize=20)
plt.show()
# plt.subplot(2,3,1)
# plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')
# for i in range(1, 9):
#     plt.plot(GrainSize, data_filt1[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.ylabel('Percent finer (%)', fontsize=20)

# plt.subplot(2,3,2)
# plt.plot(sieve_open, sieve_data_2, ls='--', color='black', label='Sieved')
# for i in range(9, 14):
#     plt.plot(GrainSize, data_filt1[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])

# plt.subplot(2,3,3)
# plt.plot(sieve_open, sieve_data_3, ls='--', color='black', label='Sieved')
# for i in range(14, 16):
#     plt.plot(GrainSize, data_filt1[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])


# plt.subplot(2,3,4)
# plt.plot(sieve_open, sieve_data_4, ls='--', color='black', label='Sieved')
# for i in range(16, 24):
#     plt.plot(GrainSize, data_filt1[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)
# plt.ylabel('Percent finer (%)', fontsize=20)


# plt.subplot(2,3,5)
# plt.plot(sieve_open, sieve_data_6, ls='--', color='black', label='Sieved')
# for i in range(24, 30):
#     plt.plot(GrainSize, data_filt1[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)

# plt.subplot(2,3,6)
# plt.plot(sieve_open, sieve_data_7, ls='--', color='black', label='Sieved')
# for i in range(30, 31):
#     plt.plot(GrainSize, data_filt1[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)


# plt.show()

# ######################################################################################################################################################################
# plt.subplot(2,3,1)
# plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')
# for i in range(1, 9):
#     plt.plot(GrainSize, data_filt[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.ylabel('Percent finer (%)', fontsize=20)

# plt.subplot(2,3,2)
# plt.plot(sieve_open, sieve_data_2, ls='--', color='black', label='Sieved')
# for i in range(9, 14):
#     plt.plot(GrainSize, data_filt[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])

# plt.subplot(2,3,3)
# plt.plot(sieve_open, sieve_data_3, ls='--', color='black', label='Sieved')
# for i in range(14, 16):
#     plt.plot(GrainSize, data_filt[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])


# plt.subplot(2,3,4)
# plt.plot(sieve_open, sieve_data_4, ls='--', color='black', label='Sieved')
# for i in range(16, 24):
#     plt.plot(GrainSize, data_filt[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)
# plt.ylabel('Percent finer (%)', fontsize=20)


# plt.subplot(2,3,5)
# plt.plot(sieve_open, sieve_data_6, ls='--', color='black', label='Sieved')
# for i in range(24, 30):
#     plt.plot(GrainSize, data_filt[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)

# plt.subplot(2,3,6)
# plt.plot(sieve_open, sieve_data_7, ls='--', color='black', label='Sieved')
# for i in range(30, 31):
#     plt.plot(GrainSize, data_filt[i, 1:15], label=data_filt[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)

# plt.show()



########################################################################################
# TOP JORN
# data_JORN = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Percentile_JornTop.csv'))
# sieve_data_T1 = [100,100,100,99,97,90,85,76,64,44,18,2,0]
# sieve_data_T2 = [95,87,76,62,56,47,43,34,25,13,5,1,0]
# sieve_data_T3 = [98,93,76,55,40,22,16,9,5,2,0,0,0]
# sieve_data_T4 = [99, 95,81,58,47,32,24,15,8,3,0,0,0]

# plt.subplot(2,2,1)
# plt.plot(sieve_open, sieve_data_T1, ls='--', color='black', label='Sieved')
# for i in range(1, 5):
#     plt.plot(GrainSize, data_JORN[i, 1:15], label=data_JORN[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.ylabel('Percent finer (%)', fontsize=20)

# plt.subplot(2,2,2)
# plt.plot(sieve_open, sieve_data_T2, ls='--', color='black', label='Sieved')
# for i in range(5, 7):
#     plt.plot(GrainSize, data_JORN[i, 1:15], label=data_JORN[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])

# plt.subplot(2,2,3)
# plt.plot(sieve_open, sieve_data_T3, ls='--', color='black', label='Sieved')
# for i in range(7, 11):
#     plt.plot(GrainSize, data_JORN[i, 1:15], label=data_JORN[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])


# plt.subplot(2,2,4)
# plt.plot(sieve_open, sieve_data_T4, ls='--', color='black', label='Sieved')
# for i in range(11, 14):
#     plt.plot(GrainSize, data_JORN[i, 1:15], label=data_JORN[i,15])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)
# plt.ylabel('Percent finer (%)', fontsize=20)


# plt.show()
