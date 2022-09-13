import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data_Proff = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentile/Percentiles_Location_1.csv')) #Proffitt_test/
data_Sieve = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentage/Percentages_Sieve.csv'))
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentage/MinScale_3px/Percentages_All.csv'))
data_filt = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentage/MinScale_3px/Percentages_Scraped.csv'))
data_cor = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentage/MinScale_3px/Corrected/Percentages_Location_2.csv'))
GrainSize = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

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


test = [0, 0, 0, -1.42109E-14, 5.519002422, 15.66399965, 20.23133051, 28.23999375, 44.86900116, 61.05241317, 87.69624203, 97.15556986, 100]
testx = [0.063, 0.125, 0.18, 0.25, 0.3, 0.355, 0.425, 0.5, 0.71, 1, 2, 4, 8]
sieve_open = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063]
sieve_data_2 = [97,94,89,79,74,57,49,35,22,8,1,0,0]

for i in range(len(data_cor)):
    plt.plot(GrainSize, data_cor[i,2:15], label=data_cor[i,15])

plt.plot(testx, test)
plt.plot(sieve_open, sieve_data_2, ls='--', color='black')


plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.legend()
plt.show()