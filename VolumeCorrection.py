import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

GrainSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])


dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/UncorrectedPercentage_All.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/26_10_22/Percentage_Sieve.csv'))

Density_Sand = 0.00165 # (g/mm**3)
Resolution = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/26_10_22/Resolution_All.csv'))[:,1]

Area_Fraction = []; Grain_Area = []; Grain_Volume = []; Grain_Mass = []; Mass_Fraction = np.zeros((34,14))

Image_Area = (4000*Resolution) * (2250 * Resolution)
Grain_Area = np.pi*(GrainSz/2)**2

Grain_Volume = np.where(GrainSz < 2, (np.pi/6)*(GrainSz)**3, np.pi*((GrainSz/2)**2)*1)
Grain_Mass = Grain_Volume * Density_Sand

Nb_Grains = []

for i in range(len(dgs_data)):
    Nb_Grains = []
    Image_Area = (4000*Resolution[i]) * (2250 * Resolution[i])

    DGS_Fractions = dgs_data[i, 1:] /100

    Area_Fraction = (DGS_Fractions * Image_Area)

    for j in range(len(Area_Fraction)):
        if Area_Fraction[j] == 0:
            Nb_Grains.append(0)
        else:
            Nb_Grains.append((Area_Fraction[j]) / Grain_Area[j])

    for index, value in enumerate(Grain_Mass):
        Mass_Fraction[i,index] = (Nb_Grains[index]*value)


    Mass_Fraction[i,:] = (Mass_Fraction[i,:] / np.sum(Mass_Fraction[i,:])) * 100
   
plt.subplot(2,1,1)
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
for i in range(len(sieve_data)):
    plt.plot(sieve_open, ( sieve_data[i,2:] - Mass_Fraction[i,1:] ))
plt.xscale("log")
plt.hlines(0, 0.063, 8, color='k')

plt.subplot(2,1,2)
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
for i in range(len(sieve_data)):
    plt.plot(sieve_open, (sieve_data[i,2:] / Mass_Fraction[i,1:]))
plt.xscale("log"); plt.yscale("log")
plt.hlines(0, 0.063, 8, color='k')
plt.show()



# # df = pd.DataFrame(Mass_Fraction, columns=['0 mm', '0.063 mm', '0.125 mm', '0.180 mm', '0.250 mm', '0.300 mm', '0.355 mm', '0.425 mm', '0.500 mm',' 0.710 mm', '1 mm', '2 mm', '4 mm', '8 mm'])
# # df.to_csv('Temps.csv')
# def Proffitt_Correction(Percentage_Arr, GrainSz_Arr, Power=-1):
#     Corrected_Percentages = []
#     for index, value in enumerate(Percentage_Arr):
#         Corrected_Percentages.append(value * (GrainSz_Arr[index]**(Power)) )

#     return Corrected_Percentages 

# def PercentageFromSum(Percentage_Arr):
#     Sum = np.sum(Percentage_Arr)
#     Corrected_Percentages = []
#     for index, value in enumerate(Percentage_Arr):
#         Corrected_Percentages.append((value / Sum)*100)

#     return Corrected_Percentages



# GrainSz_1 = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425]
# GrainSz_2= [0.500, 0.710, 1, 2]
# GrainSz_3= [2, 4, 8]


# Corrected_Percentage = np.zeros((34,13))
# for index, value in enumerate(Mass_Fraction):

#     Cor_1 = PercentageFromSum(Proffitt_Correction(value[1:8], GrainSz_1, Power=0.5))
#     Cor_2 = PercentageFromSum(Proffitt_Correction(value[8:12], GrainSz_2, Power=-1))
#     Cor_3 = PercentageFromSum(Proffitt_Correction(value[11:14], GrainSz_3, Power=-0.5))

#     Cor_T = Cor_1 + Cor_2 + Cor_3[1:]

#     Corrected_Percentage[index,:] = (PercentageFromSum(Cor_T))


# sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
# for i in range(len(sieve_data)):
#     plt.plot(sieve_open, ( sieve_data[i,2:] - Corrected_Percentage[i,:] ))
# plt.xscale("log")
# plt.hlines(0, 0.063, 8, color='k')
# plt.show()