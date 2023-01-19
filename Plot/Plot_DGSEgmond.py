import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Sieve/Percentage_Sieve.csv'))
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Uncorrected/Uncorrected_Locs_MeanTransf.csv'))

GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4])


color = cm.rainbow(np.linspace(0, 1, len(sieve_data)))
plt.rc('legend',fontsize=15) # using a size in points

for i in range(len(sieve_data)):
    plt.scatter(GrainSz, (sieve_data[i,2:14]/data[i,2:14]), color=color[i], label= sieve_data[i,0])
plt.xscale('log'); plt.yscale('log')
plt.legend(bbox_to_anchor=(1,1), loc="upper left")

plt.ylabel('%-Sieve / %-pyDGS', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)
plt.xticks(fontsize = 15); plt.yticks(fontsize = 15)

plt.show()