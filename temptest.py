import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/UncorrectedPercentage_All.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/26_10_22/Sieve/Percentage_Sieve.csv'))
error = sieve_data[:34, 2:]- dgs_data[:34, 2:]

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
plt.subplot(2,1,1)
for i in range(len(dgs_data)):
    plt.plot(sieve_open, (sieve_data[i,2:]- dgs_data[i,2:]))
plt.xscale("log")
plt.ylabel('%-Sieve - %-pyDGS', fontsize=20)
plt.xlabel('Grain size', fontsize=20)
plt.title('Uncorrected', fontsize=20)
plt.hlines(0, 0.063, 8, color='k')

plt.subplot(2,1,2)
plt.plot(sieve_open, np.mean(error, axis=0))
plt.xscale('log')
plt.show()

dgs_data_cor = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/26_10_22/Mobile/Corrected/Corrected_All_Percent.csv'))

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
error = sieve_data[:34, 2:]- dgs_data_cor[:34, 2:]

plt.subplot(2,1,1)
for i in range(len(dgs_data)):
    plt.plot(sieve_open, error[i, :])
plt.xscale("log")
plt.ylabel('%-Sieve - %-pyDGS', fontsize=20)
plt.xlabel('Grain size', fontsize=20)
plt.title('Corrected', fontsize=20)
plt.hlines(0, 0.063, 8, color='k')

plt.subplot(2,1,2)
plt.plot(sieve_open, np.mean(error, axis=0))
plt.xscale('log')
plt.show()


Density_Sand = 0.00165 # (g/mm**3)
Resolution = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/26_10_22/Resolution_All.csv'))[:,1]
GrainSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])


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
   
error = sieve_data[:34, 2:]- Mass_Fraction[:34, 1:]

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
plt.subplot(2,1,1)
for i in range(len(sieve_data)):
    plt.plot(sieve_open, ( sieve_data[i,2:] - Mass_Fraction[i,1:] ))
plt.xscale("log")
plt.ylabel('%-Sieve - %-pyDGS ', fontsize=20)
plt.xlabel('Grain size', fontsize=20)
plt.title('Volume correction: new method', fontsize=20)
plt.hlines(0, 0.063, 8, color='k')


plt.subplot(2,1,2)
plt.plot(sieve_open, np.mean(error, axis=0))
plt.xscale('log')
plt.show()
