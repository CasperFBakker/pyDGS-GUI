import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

GrainSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])


dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Transform/Uncorrected_TransfAll_2.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Percentage_Sieve.csv'))
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]


Density_Sand = 0.00165 # (g/mm**3)
Resolution = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Resolution_All.csv'))[:,1]
STdev = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Transform/Uncorrected_TransfAll_Stdev_2.csv'))
Area_Fraction = []; Grain_Area = []; Grain_Volume = []; Grain_Mass = []; Mass_Fraction = np.zeros((34,14))

Grain_Area = np.pi*(GrainSz/2)**2

Nb_Grains = []

for i in range(len(Resolution)):
    Nb_Grains = []
    Image_Area = (4000*Resolution[i]) * (2250 * Resolution[i])

    DGS_Fractions = dgs_data[i, 1:] /100

    Area_Fraction = (DGS_Fractions * Image_Area)
    Grain_Volume = []
    for j in range(len(Area_Fraction)):
        
        if Area_Fraction[j] == 0:
            Nb_Grains.append(0)
        else:
            Nb_Grains.append((Area_Fraction[j]) / Grain_Area[j])

        if STdev[i, j+1] < 0.5:
            if GrainSz[j] == 4 or GrainSz[j] == 2:
                Grain_Volume.append(np.pi*((GrainSz[j]/2)**2)*0.001)
            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])**3)
        else:
            if GrainSz[j]<=1:
                Grain_Volume.append(np.pi*((GrainSz[j]/2)**2)*0.75*GrainSz[j])
            elif GrainSz[j] == 8:
                Grain_Volume.append(np.pi*((GrainSz[j]/2)**2)*0.001)
            else:
                Grain_Volume.append(np.pi*((GrainSz[j]/2)**2)*0.001)

    Grain_Mass = np.array(Grain_Volume) * Density_Sand

    for index, value in enumerate(Grain_Mass):
        Mass_Fraction[i,index] = (Nb_Grains[index]*value)


    Mass_Fraction[i,:] = (Mass_Fraction[i,:] / np.sum(Mass_Fraction[i,:])) * 100

print(Mass_Fraction[0,:])
plt.subplot(2,1,1)
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
for i in range(len(sieve_data)):
    plt.plot(sieve_open, ( sieve_data[i,2:] - Mass_Fraction[i,1:] ))
plt.xscale("log")
plt.hlines(0, 0.063, 8, color='k')
plt.title('Different Grain Shapes', fontsize=20)
plt.ylabel('%-Sieve - %-pyDGS ', fontsize=20)

error = sieve_data[:34, 2:]- Mass_Fraction[:34, 1:]
std = np.std(error.astype(np.float64), axis=0)

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
plt.subplot(2,1,2)

plt.errorbar(x=sieve_open, y=np.mean(error, axis=0), yerr=std, capsize=3)
plt.hlines(0, 0.063, 8, color='k')
plt.xscale('log')
plt.ylabel('Mean Absolute Error', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)

plt.show()



# sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
# for i in range(len(sieve_data)):
#     plt.plot(sieve_open, ( sieve_data[i,2:] / Mass_Fraction[i,1:] ))
# plt.xscale("log")
# plt.yscale("log")


D50_DGS = [0.796498314, 0.688669056, 0.725538634, 0.705858211, 0.725722849, 0.651177092, 0.687364834, 0.678357009, 0.747364352, 
           0.703754498, 0.665784621, 0.667078012, 0.697949106, 0.710923478, 0.688925427, 0.677240196, 0.694635217, 0.779892510, 
           0.725280786, 0.672104752, 0.686870005, 0.701706523, 0.636929161, 0.740872554, 0.716753902, 0.615066028, 0.712954126, 
           0.686337869, 0.634639045, 0.692385228, 0.707811151, 0.743064054, 0.655862722, 0.775350472]

D50_SIE = [0.752629387, 0.787396040, 0.714336374, 1.633363137, 0.653926004, 0.657958213, 1.053660270, 0.691918682, 0.498216612,
           0.670115814, 0.510694292, 0.679176535, 0.471877608, 0.821651788, 0.590637416, 0.589795421, 0.594801158, 0.368168797,
           0.399921977, 0.707293095, 0.451919315, 1.582074936, 0.726551059, 1.411990139, 0.472872340, 0.817800759, 0.650493511, 
           0.591879264, 1.258297872, 0.483782269, 0.512578390, 0.748987844, 0.462944623, 0.677670244]

plt.scatter(D50_DGS, D50_SIE)
plt.plot(np.arange(0,10), linestyle='--', color='k')
plt.xlim(0,2); plt.ylim(0,2)
plt.xlabel('D50 DGS (mm)', fontsize=20)
plt.ylabel('D50 Sieve (mm)', fontsize=20)
plt.show()


dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Transform/Uncorrected_R1_Transformed.csv'))\

for i in range(16):
    plt.plot(sieve_open, dgs_data[i+1, 2:], label=dgs_data[i+1, 0])
plt.xlabel('Grain size (mm)', fontsize=20)
plt.ylabel('Percentage', fontsize=20)
plt.xscale('log')
plt.legend()
plt.show()