import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Proffitt_Correction(Percentage_Arr, GrainSz_Arr, Power=-1):
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append(value * (GrainSz_Arr[index]**(Power)) )

    return Corrected_Percentages 

def PercentageFromSum(Percentage_Arr):
    Sum = np.sum(Percentage_Arr)
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append((value / Sum)*100)
    return Corrected_Percentages

def Percentage2Percentile(Percentage):
    Percentage = Percentage[::-1]
    Percentile = 100 - np.nancumsum(Percentage)

    Percentile_cor = []
    for index, value in enumerate(Percentile):
        if value < 0:
            Percentile_cor.append(0)
        else:
            Percentile_cor.append(value)

    Percentile_cor = Percentile_cor[::-1]
    
    return Percentile_cor
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/01_12_22_Egmond/Statistics/Statistics_Stats_Line_2.csv'))

plt.subplot(3,1,1)
for i in range(len(data)):
    plt.scatter(i, data[i, 3], color='k')
plt.title('D16', fontsize=20)
plt.ylabel('Grain size (mm)', fontsize=20)

plt.subplot(3,1,2)
for i in range(len(data)):
    plt.scatter(i, data[i, 6], color='k')
plt.title('D50', fontsize=20)
plt.ylabel('Grain size (mm)', fontsize=20)

plt.subplot(3,1,3)
for i in range(len(data)):
    plt.scatter(i, data[i, 9], color='k')
plt.title('D90', fontsize=20)
plt.xlabel('Cross Shore distance (m)', fontsize=20)
plt.ylabel('Grain size (mm)', fontsize=20)

plt.show()

plt.subplot(4,1,1)
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/01_12_22_Egmond/Uncorrected/UncorrectedPercentage_Line_2.csv'))
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
for i in range(len(data)):
    plt.plot(sieve_open, data[i,2:])

plt.xscale("log")

plt.xlabel('Grain size (mm)', fontsize=20)
plt.ylabel('Percentage', fontsize=20)
plt.subplot(4,1,2)
for i in range(len(data)):
    plt.plot(sieve_open, Percentage2Percentile(data[i,2:]))

plt.xscale("log")

plt.subplot(4,1,3)
for i in range(len(data)):
     plt.plot(sieve_open, PercentageFromSum(Proffitt_Correction(data[i,2:], sieve_open, Power=-1)))
plt.xscale("log")

plt.subplot(4,1,4)
for i in range(len(data)):
     plt.plot(sieve_open, Percentage2Percentile(PercentageFromSum(Proffitt_Correction(data[i,2:], sieve_open, Power=-1))))
plt.xscale("log")
plt.show()