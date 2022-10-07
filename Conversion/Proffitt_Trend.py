import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/All_Data/Percentile_Proffitt_trends.csv'))

Sieves = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])

for i in range(0, 20):
    plt.scatter(Sieves[3:13], data[i, 3:13], color='blue')
    plt.scatter(Sieves[3:13], data[i+20, 3:13], color='red')
    plt.scatter(Sieves[3:13], data[i+40, 3:13], color='green')
    plt.scatter(Sieves[3:13], data[i+60, 3:13], color='orange')
    plt.scatter(Sieves[3:13], data[i+80, 3:13], color='cyan')
    plt.scatter(Sieves[3:13], data[i+100, 3:13], color='black')
plt.xscale("log")
plt.yscale("log")
plt.show()