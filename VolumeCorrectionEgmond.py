import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

GrainSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])


dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Uncorrected/Uncorrected_Locs_MeanTransf.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Sieve/Percentage_Sieve.csv'))
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

color = cm.tab20c(np.linspace(0, 1, len(sieve_data)))


Density_Sand = 0.00165 # (g/mm**3)
Resolution = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Resolution_Locs.csv'))[:,1]
STdev = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Uncorrected/Uncorrected_Locs_StDevTransf.csv'))
Area_Fraction = []; Grain_Area = []; Grain_Volume = []; Grain_Mass = []; Mass_Fraction = np.zeros((9,14))

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
            if STdev[i, j+1] < 0.4:
                Nb_Grains.append((Area_Fraction[j]) / (np.pi*(GrainSz[j]/2)**2))
            elif STdev[i, j+1] >= 0.4 and STdev[i, j+1] < 0.5:
                Nb_Grains.append((Area_Fraction[j]) / (np.pi*0.8*(GrainSz[j]/2)**2))
            elif STdev[i, j+1] >= 0.5 and STdev[i, j+1] < 1:
                if GrainSz[j] < 1:
                    Nb_Grains.append((Area_Fraction[j]) / (np.pi*(0.75 *(GrainSz[j]/2) * (GrainSz[j]/2))))
                else:
                    Nb_Grains.append((Area_Fraction[j]) / ((1/STdev[i, j+1]* (GrainSz[j]/2))* 0.1 * np.pi*(GrainSz[j]/2)))
            else:
                Nb_Grains.append((Area_Fraction[j]) / ((STdev[i, j+1]* (GrainSz[j]/2) * 0.001) * np.pi*(GrainSz[j]/2)))



    #   Volume part
        if STdev[i, j+1] < 0.3:
            if GrainSz[j] == 0.425 or GrainSz[j] == 0.355  or GrainSz[j] == 0.300:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.0075)
            elif GrainSz[j] == 0.250:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.1)
            elif GrainSz[j] == 0.125 or GrainSz[j] == 0.063:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.01)
            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])**2 *GrainSz[j])
  
        elif STdev[i, j+1] >= 0.3 and STdev[i, j+1] < 0.5:
            if GrainSz[j] == 0.425:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.000001)
            elif GrainSz[j] == 0.355 or GrainSz[j] == 0.3:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.0001)
            elif GrainSz[j] == 0.18:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.1)
            elif GrainSz[j] == 0.125 or GrainSz[j] == 0.063:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.01)
            elif GrainSz[j] == 0.250:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.1)
            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*(1/STdev[i, j+1])*GrainSz[j]*10)

        elif STdev[i, j+1] >= 0.5 and STdev[i, j+1] < 0.8:
            if  GrainSz[j] == 0.5:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*STdev[i, j+1]*GrainSz[j]*0.001)
            elif  GrainSz[j] == 1:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*STdev[i, j+1]*GrainSz[j]*0.0001)
            elif  GrainSz[j] == 0.180:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.25)

            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*STdev[i, j+1]*GrainSz[j]*0.0075)

        else:
            if  GrainSz[j] == 0.5:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*STdev[i, j+1]*GrainSz[j]*0.0001)
            elif  GrainSz[j] == 0.71:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.00000001)

            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.000001)
   


    Grain_Mass = np.array(Grain_Volume) * Density_Sand 
    for index, value in enumerate(Grain_Mass):
        Mass_Fraction[i,index] = (Nb_Grains[index]*value)


    Mass_Fraction[i,:] = (Mass_Fraction[i,:] / np.nansum(Mass_Fraction[i,:])) * 100

df = pd.DataFrame(Mass_Fraction)
# df.to_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Corrected/Corrected_Locs.csv')


plt.subplot(2,1,1)
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
for i in range(len(sieve_data)):
    plt.scatter(sieve_open, ( sieve_data[i,2:] - Mass_Fraction[i,1:] ), color=color[i], label= sieve_data[i,0])
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xscale("log")
plt.hlines(0, 0.063, 8, color='k')
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