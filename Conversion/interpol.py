import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_line1 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Line_1/Stats_Line_1.csv'))
data_line2 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Line_2/Stats_Line_2.csv'), dtype='float64')
GrainSize = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
# D_nb = np.array([95]) # 10, 16, 25, 30, 50, 75, 84, 90, 95
# for i in range(len(data)):
#     print(np.interp(D_nb, data[i,:], GrainSize)[0])

steps_line1 = np.arange(0, 190, 5)

steps_line2 = np.arange(0, 130, 5)

plt.subplot(3,2,1)
plt.scatter(steps_line1, data_line1[0:38, 2])
plt.title('Line 1 \n D10')

plt.ylim(0, 0.5)

plt.subplot(3,2,2)
plt.scatter(steps_line2, data_line2[0:26, 2])
plt.title('Line 2 \n D10')
plt.ylim(0, 0.5)

plt.subplot(3,2,3)
plt.scatter(steps_line1, data_line1[0:38, 5])
plt.title('D50')
plt.ylabel('Grain size (mm)', fontsize=20)
plt.ylim(0.25, 0.75)

plt.subplot(3,2,4)
plt.scatter(steps_line2, data_line2[0:26, 5])
plt.title('D50')
plt.ylim(0.25, 0.75)
plt.subplot(3,2,5)
plt.scatter(steps_line1, data_line1[0:38, 8])
plt.title('D90')
plt.xlabel('Cross-shore distance (m)', fontsize=20)
plt.ylim(1,4)

plt.subplot(3,2,6)
plt.scatter(steps_line2, data_line2[0:26, 8])
plt.title('D90')
plt.xlabel('Cross-shore distance (m)', fontsize=20)
plt.ylim(1,4)

plt.show()