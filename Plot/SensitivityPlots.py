import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Sensitivity_Analysis/Uncorrected/UncorrectedPercentage_HeightAboveBed.csv'))
GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])

for i in [0,1,2,3,5]:
    plt.plot(GrainSz, data[i, 2:])

plt.legend(['h=9.22cm', 'h=17.3cm', 'h=26.9cm', 'h=37.4cm',  'h=56.6cm',])
plt.xscale('log')
plt.show()
