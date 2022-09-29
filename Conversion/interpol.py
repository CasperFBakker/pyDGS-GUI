import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_line1 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Line_1/Stats_Line_1.csv'))
data_line2 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Line_2/Stats_Line_2.csv'), dtype='float64')

# data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Sample_Photos/Location_7/Percentile_Loc_7_AllTrend.csv'), dtype='float64')
# GrainSize = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
# D_nb = np.array([5, 10, 16, 25, 30, 50, 75, 84, 90, 95]) # 10, 16, 25, 30, 50, 75, 84, 90, 95

# Loc_1 = [0, 0, 0, 1.856530419, 9.39670451, 23.38392555, 32.91814145, 41.82567712, 48.42910144, 61.99127512, 70.52566487, 87.25070218, 96.78305721, 100]
# Loc_2 = [0, 0, 0, 2.387965496, 13.10892605, 28.67345817, 40.87228444, 51.92830346, 58.79471276, 72.19727478, 80.24894027, 92.72201782, 98.08642717, 100]
# Loc_3 = [0, 0, 0, 1.75226958, 10.18711472,	24.90927538, 36.42536289,	47.89063223,	56.14447423,	69.26280194	,77.17777657,	90.48550055,	97.24673621,	100]
# Loc_4 = [0, 0,	0,	3.611757741,	15.97791105,	30.61574005,	41.31316744,	50.17198699	,56.81260046,	69.55637623,	76.98588424,	90.18940987	,97.24355626,	100]
# Loc_6 = [0,0,	0.196020497,	4.032892483,	16.44109248,	31.89684871,	44.46874861,	54.09664424,	61.89067586,	74.61477438,	81.81144527	,92.67216839	,97.49341654,	100]
# Loc_7 = [0,0,	0	,0,	14.41249007,	29.02615505	,43.17339908,	52.85734096,	60.54484546,	74.3564125,	82.37946288,	93.91097274,	98.32668027,	100]

# for i in range(len(D_nb)):
#     print(np.interp(D_nb[i], Loc_7[:], GrainSize))

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