import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def Proffitt_Correction(Percentage_Arr, GrainSz_Arr, Power=-1):
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append(value * (GrainSz_Arr[index]**(Power)) )

    return Corrected_Percentages 
# =========================================================
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

GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])

dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Uncorrected/Transform/Uncorrected_TransfAll.csv')) 

Density_Sand = 0.002250 # (g/mm**3)
Resolution = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Resolution_All.csv'))[:,1]
Area_Fraction = []; Grain_Area = []; Grain_Volume = []; Grain_Mass = []; Mass_Fraction = np.zeros((61,13))

Grain_Area = np.pi*(GrainSz/2)**2

Grain_Volume = np.where(GrainSz < 2, (np.pi/6)*(GrainSz)**3, np.pi*((GrainSz/2)**2)*1)
Grain_Mass = Grain_Volume * Density_Sand

for i in range(len(Resolution)):
    Nb_Grains = []
    Image_Area = (4000*Resolution[i]) * (2250 * Resolution[i])

    DGS_Fractions = dgs_data[i, 2:] /100

    Area_Fraction = (DGS_Fractions * Image_Area)

    for j in range(len(Area_Fraction)):
        if Area_Fraction[j] == 0:
            Nb_Grains.append(0)
        else:
            Nb_Grains.append((Area_Fraction[j]) / Grain_Area[j])

    for index, value in enumerate(Grain_Mass):
        Mass_Fraction[i,index] = (Nb_Grains[index]*value)


    Mass_Fraction[i,:] = (Mass_Fraction[i,:] / np.sum(Mass_Fraction[i,:])) * 100

print(Mass_Fraction[0,:])
GrainSz = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
x1 = PercentageFromSum(Proffitt_Correction(Mass_Fraction[0,:7], GrainSz, Power=-0.47))
x2 = PercentageFromSum(Proffitt_Correction(Mass_Fraction[0,7:], GrainSz, Power=-1))
x3 = x1+x2
x3 = PercentageFromSum(x3)
print(Percentage2Percentile(x3))

