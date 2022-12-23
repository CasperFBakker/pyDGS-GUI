import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from scipy.optimize import curve_fit
import cv2
from imageio import imread
import pywt
import scipy.stats as stats
import math
# =========================================================
def Proffitt_Correction(Percentage_Arr, GrainSz_Arr, K, Power=-1):
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append(K * value * (GrainSz_Arr[index]**(Power)) )

    return Corrected_Percentages 
# =========================================================
def PercentageFromSum(Percentage_Arr):
    Sum = np.sum(Percentage_Arr)
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append((value / Sum)*100)

    return Corrected_Percentages
# =========================================================
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

Uncorrected_Percentage = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Transform Maxsc8/Uncorrected_TransfAll.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Percentile_Sieve.csv'))
GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])

GrainSz_1 = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500]


GrainSz_2= [0.500, 0.710, 1, 2, 4, 8]




# K_1 = [7.234580268, 59.95907909, 22.16990171]
# x_1 = [1.611109211, 2.677441337, 2.740046285]
# K_2 = [0.813232738, 0.643898131, 1.197507441]
# x_2 = [0.102716138, -0.801062406, -1.181495295]
# color = cm.rainbow(np.linspace(0, 1, len(x_1)))
# Locations = ['R05 A', 'R05 B', 'R05 C', ]
# for i in range(3):
#     plt.subplot(2,2,i+1)
#     Cor_1 = Proffitt_Correction(Uncorrected_Percentage[i+12, 2:9], GrainSz_1, K_1[i], x_1[i])
#     Cor_2 = Proffitt_Correction(Uncorrected_Percentage[i+12, 9:], GrainSz_2, K_2[i], x_2[i])
#     Cor_3 = PercentageFromSum(Cor_1 + Cor_2)
#     Corrected_Percentage = (PercentageFromSum(Cor_3))
#     Percentiles = Percentage2Percentile(Corrected_Percentage)
#     plt.plot(GrainSz, Percentiles, c=color[i])
#     plt.plot(GrainSz, sieve_data[i+12 ,2:], c='k', linestyle='--')
#     plt.xscale("log")

#     plt.grid(which='major', linewidth=1, linestyle='-')
#     plt.grid(which='minor', linewidth=0.5, linestyle='--')
#     plt.ylim(0,100)
#     plt.ylabel('Percent Finer (%)', fontsize=14)
#     plt.xlabel('Grain Size (mm)', fontsize=14)
#     plt.title(Locations[i], fontsize=18)

#     plt.subplot(2,2,4)
#     plt.scatter(Percentiles, sieve_data[i+12,2:], c=color[i])
#     plt.plot(np.arange(0,100), c='k', linestyle='--')
#     plt.ylim(0,100); plt.xlim(0,100)
#     plt.ylabel('Percent Finer from Sieve (%)', fontsize=14)
#     plt.xlabel('Percent Finer from pyDGS (%)', fontsize=14)


# plt.show()


def RMSE(Sieve_vals, DGS_vals):

    diffrnce = np.subtract(Sieve_vals, DGS_vals)
    sqre_err = np.square(diffrnce)
    rslt_meansqre_err = sqre_err.mean()
    root_meansqre_err = math.sqrt(rslt_meansqre_err)
    return root_meansqre_err

def MAE(Sieve_vals, DGS_vals):
    diffrnce = np.abs(np.subtract(Sieve_vals, DGS_vals))
    meanAbsErr = diffrnce.mean()
    return meanAbsErr


Uncorrected_Percentage = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Transform Maxsc8/Uncorrected_TransfAll.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Percentage_Sieve.csv'))

Cor_1 = Proffitt_Correction(Uncorrected_Percentage[33, 2:9], GrainSz_1,2.022838524, 1.378821395)
Cor_2 = Proffitt_Correction(Uncorrected_Percentage[33, 9:], GrainSz_2,1.672954784,-0.914413144)
Cor_3 = PercentageFromSum(Cor_1 + Cor_2)
DGS_Percentage = (PercentageFromSum(Cor_3))

Sieve_Percentage = sieve_data[29,2:]
Percentiles = Percentage2Percentile(DGS_Percentage)

# print(((RMSE(Sieve_Percentage, DGS_Percentage))/(max(Sieve_Percentage) - min(Sieve_Percentage))))
# print(((MAE(Sieve_Percentage, DGS_Percentage))/(max(Sieve_Percentage) - min(Sieve_Percentage))))

# print(RMSE(Sieve_Percentage, DGS_Percentage))
# print(MAE(Sieve_Percentage, DGS_Percentage))

GrainSizeBins = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8], dtype='float64')
Percentile = np.interp([5, 10, 16, 25, 30, 50, 75, 84, 90, 95], Percentiles, GrainSizeBins)
df = pd.DataFrame(Percentile)

dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/General Conversion Results/Statistics_GCCorrection.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Statistics/Statistics_photos_samples.csv'))


plt.subplot(2,3,1)
plt.scatter(sieve_data[:,2], dgs_data[:,2])
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.20,0.5); plt.ylim(0.20,0.5); 
print('D10: ', ((RMSE(sieve_data[:,2], dgs_data[:,2]))))
print('D10: ', ((RMSE(sieve_data[:,2], dgs_data[:,2]))/(max(sieve_data[:,2]) - min(sieve_data[:,2]))*100))
print('D10: ', ((MAE(sieve_data[:,2], dgs_data[:,2]))))
print('D10: ', ((MAE(sieve_data[:,2], dgs_data[:,2]))/(max(sieve_data[:,2]) - min(sieve_data[:,2]))*100))

plt.subplot(2,3,2)
plt.scatter(sieve_data[:,3], dgs_data[:,3])
print('D16: ', ((RMSE(sieve_data[:,3], dgs_data[:,3]))))
print('D16: ', ((RMSE(sieve_data[:,3], dgs_data[:,3]))/(max(sieve_data[:,3]) - min(sieve_data[:,3]))*100))
print('D16: ', ((MAE(sieve_data[:,3], dgs_data[:,3]))))
print('D16: ', ((MAE(sieve_data[:,3], dgs_data[:,3]))/(max(sieve_data[:,3]) - min(sieve_data[:,3]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.20, 0.65); plt.ylim(0.20, 0.65)

plt.subplot(2,3,3)
plt.scatter(sieve_data[:,4], dgs_data[:,4])
print('D25: ', ((RMSE(sieve_data[:,4], dgs_data[:,4]))))
print('D25: ', ((RMSE(sieve_data[:,4], dgs_data[:,4]))/(max(sieve_data[:,4]) - min(sieve_data[:,4]))*100))
print('D25: ', ((MAE(sieve_data[:,4], dgs_data[:,4]))))
print('D25: ', ((MAE(sieve_data[:,4], dgs_data[:,4]))/(max(sieve_data[:,4]) - min(sieve_data[:,4]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.25, 0.90); plt.ylim(0.25, 0.90)

plt.subplot(2,3,4)
plt.scatter(sieve_data[:,6], dgs_data[:,6])
print('D50: ', ((RMSE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]))))
print('D50: ', ((RMSE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]) - min(sieve_data[:,6]))*100))
print('D50: ', ((MAE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]))))
print('D50: ', ((MAE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]) - min(sieve_data[:,6]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.30, 1.70); plt.ylim(0.30, 1.70)

plt.subplot(2,3,5)
plt.scatter(sieve_data[:,8], dgs_data[:,8])
print('D84: ', ((RMSE(sieve_data[:,8], dgs_data[:,8]))))
print('D84: ', ((RMSE(sieve_data[:,8], dgs_data[:,8]))/(max(sieve_data[:,8]) - min(sieve_data[:,8]))*100))
print('D84: ', ((MAE(sieve_data[:,8], dgs_data[:,8]))))
print('D84: ', ((MAE(sieve_data[:,8], dgs_data[:,8]))/(max(sieve_data[:,8]) - min(sieve_data[:,8]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.60, 5); plt.ylim(0.60, 5)

plt.subplot(2,3,6)
plt.scatter(sieve_data[:,9], dgs_data[:,9])
print('D90: ', ((RMSE(sieve_data[:,9], dgs_data[:,9]))))
print('D90: ', ((RMSE(sieve_data[:,9], dgs_data[:,9]))/(max(sieve_data[:,9]) - min(sieve_data[:,9]))*100))
print('D90: ', ((MAE(sieve_data[:,9], dgs_data[:,9]))))
print('D90: ', ((MAE(sieve_data[:,9], dgs_data[:,9]))/(max(sieve_data[:,9]) - min(sieve_data[:,9]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.90, 6.6); plt.ylim(0.90, 6.6)

plt.show()