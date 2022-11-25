import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Uncorrected/UncorrectedPercentage_All.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Percentage_Sieve.csv'))

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
for i in range(len(dgs_data)):
    plt.plot(sieve_open, (dgs_data[i,2:] - sieve_data[i,2:]))
plt.xscale("log")
plt.hlines(0, 0.063, 8, color='k')
plt.show()

for i in range(len(dgs_data)):
    plt.scatter(sieve_open, (dgs_data[i,2:] - sieve_data[i,2:]), color='k')
plt.xscale("log")
plt.show()

sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/dgs_div_SieveTest.csv'))

for i in range(len(dgs_data)):
    plt.scatter(sieve_open, (sieve_data[i,2:]))
plt.xscale("log"); plt.yscale("log")
plt.show()