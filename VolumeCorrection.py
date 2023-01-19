import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

GrainSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])


dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Uncorrected_R10Inb_MeanTransf.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Percentage_Sieve_Sort.csv'))
sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

color = cm.tab20c(np.linspace(0, 1, len(sieve_data)))


Density_Sand = 0.00165 # (g/mm**3)
Resolution = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/Image_data/26_10_22/Mobile/data_R10.csv'))[:,1]
STdev = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Uncorrected_R10Inb_StDevTransf.csv'))
Area_Fraction = []; Grain_Area = []; Grain_Volume = []; Grain_Mass = []; Mass_Fraction = np.zeros((21,14))

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
            if STdev[i, j+1] < 0.5:
                Nb_Grains.append((Area_Fraction[j]) / (np.pi*(GrainSz[j]/2)**2))
            elif STdev[i, j+1] >= 0.5 and STdev[i, j+1] < 1:
                if GrainSz[j] < 1:
                    Nb_Grains.append((Area_Fraction[j]) / (np.pi*(0.75 *(GrainSz[j]/2) * (GrainSz[j]/2))))
                else:
                    Nb_Grains.append((Area_Fraction[j]) / ((1/STdev[i, j+1]* (GrainSz[j]/2))* 0.1 * np.pi*(GrainSz[j]/2)))
            else:
                Nb_Grains.append((Area_Fraction[j]) / ((STdev[i, j+1]* (GrainSz[j]/2) * 0.001) * np.pi*(GrainSz[j]/2)))



    #   Volume part
        if STdev[i, j+1] < 0.5:
            if GrainSz[j] == 0.71:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])**2 * 0.001*GrainSz[j])
            elif GrainSz[j] == 0.5:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])**2 * 0.05*GrainSz[j])
            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])**2 * 0.1*GrainSz[j])

        elif STdev[i, j+1] >= 0.5 and STdev[i, j+1] < 1:
            if GrainSz[j] == 0.71:
                Grain_Volume.append((np.pi/6)*(GrainSz[j]*GrainSz[j]*0.75*GrainSz[j])*0.1)
            elif GrainSz[j] == 0.5:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*STdev[i, j+1]*GrainSz[j]*0.1)
            elif GrainSz[j] == 2:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*GrainSz[j]*0.0005)
            elif GrainSz[j] == 8:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*GrainSz[j]*0.00075)
            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*STdev[i, j+1]*GrainSz[j]*0.01)

        else:
            if GrainSz[j] == 0.5:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.000001)
            elif GrainSz[j]<1:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j])
            elif GrainSz[j] == 2:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*GrainSz[j]*0.000001)
            elif GrainSz[j] == 1:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.00025)
            elif GrainSz[j] == 0.710:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j])
            elif GrainSz[j] == 4:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.000001)
            elif GrainSz[j] == 8:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j]*0.000001)
            else:
                Grain_Volume.append((np.pi/6)*(GrainSz[j])*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j])

    Grain_Mass = np.array(Grain_Volume) * Density_Sand 
    for index, value in enumerate(Grain_Mass):
        Mass_Fraction[i,index] = (Nb_Grains[index]*value)


    Mass_Fraction[i,:] = (Mass_Fraction[i,:] / np.nansum(Mass_Fraction[i,:])) * 100

df = pd.DataFrame(Mass_Fraction)
# df.to_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Corrected/Corrected_R10Inb.csv')

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

#__________________________________________________________________________________________________________________________________________________________________________
#==========================================================================================================================================================================
#__________________________________________________________________________________________________________________________________________________________________________


# dgs_data_sort = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Transform Maxsc8/Uncorrected_TransfAll_Sort.csv'))
# sieve_data_sort = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Percentage_Sieve_Sort.csv'))

# plt.subplot(2,1,1)
# sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
# for i in range(len(sieve_data_sort)):
#     plt.scatter(sieve_open, ( sieve_data_sort[i,2:] - Mass_Fraction[i,1:] ), color=color[i], label= sieve_data_sort[i,0])
# plt.legend(bbox_to_anchor=(1,1), loc="upper left")
# plt.xscale("log")
# plt.hlines(0, 0.063, 8, color='k')
# # plt.title('Different Grain Shapes', fontsize=20)
# plt.ylabel('%-Sieve - %-pyDGS ', fontsize=20)


# error = sieve_data[:34, 2:]- Mass_Fraction[:34, 1:]
# std = np.std(error.astype(np.float64), axis=0)

# sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
# plt.subplot(2,1,2)

# plt.errorbar(x=sieve_open, y=np.mean(error, axis=0), yerr=std, capsize=3)
# plt.hlines(0, 0.063, 8, color='k')
# plt.xscale('log')
# plt.ylabel('Mean Absolute Error', fontsize=20)
# plt.xlabel('Grain size (mm)', fontsize=20)

# plt.show()


        # if STdev[i, j+1] < 0.5:
        #     if GrainSz[j] == 0.71:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])**2 * 0.001*GrainSz[j])
        #     elif GrainSz[j] == 0.5:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])**2 * 0.05*GrainSz[j])
        #     else:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])**2 * 0.1*GrainSz[j])

        # elif STdev[i, j+1] >= 0.5 and STdev[i, j+1] < 1:
        #     if GrainSz[j] == 0.71:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j]*0.001*GrainSz[j]*0.75*GrainSz[j]))
        #     elif GrainSz[j] == 0.5:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.001*GrainSz[j]*1/STdev[i, j+1]*GrainSz[j])
        #     elif GrainSz[j] == 2:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.0001*GrainSz[j]*0.001*GrainSz[j])
        #     else:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.0001*GrainSz[j]*0.001*1/STdev[i, j+1]*GrainSz[j])

        # else:
        #     if GrainSz[j] == 0.5:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.0001*GrainSz[j]*0.001*STdev[i, j+1]*GrainSz[j])
        #     elif GrainSz[j]<1:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.001*GrainSz[j]*STdev[i, j+1]*GrainSz[j])
        #     elif GrainSz[j] == 2:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.0001*GrainSz[j]*0.0001*GrainSz[j])
        #     elif GrainSz[j] == 1:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.0001*GrainSz[j]*0.0005*STdev[i, j+1]*GrainSz[j])
        #     elif GrainSz[j] == 0.710:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.00001*GrainSz[j]*0.0001*STdev[i, j+1]*GrainSz[j])
        #     elif GrainSz[j] == 4:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.00001*GrainSz[j]*0.0001*STdev[i, j+1]*GrainSz[j])
        #     elif GrainSz[j] == 8:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.0001*GrainSz[j]*0.00001*STdev[i, j+1]*GrainSz[j])
        #     else:
        #         Grain_Volume.append((np.pi/6)*(GrainSz[j])*0.001*GrainSz[j]*0.001*STdev[i, j+1]*GrainSz[j])


# sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
# for i in range(len(sieve_data)):
#     plt.plot(sieve_open, ( sieve_data[i,2:] / Mass_Fraction[i,1:] ))
# plt.xscale("log")
# plt.yscale("log")


# D50_DGS = [0.796498314, 0.688669056, 0.725538634, 0.705858211, 0.725722849, 0.651177092, 0.687364834, 0.678357009, 0.747364352, 
#            0.703754498, 0.665784621, 0.667078012, 0.697949106, 0.710923478, 0.688925427, 0.677240196, 0.694635217, 0.779892510, 
#            0.725280786, 0.672104752, 0.686870005, 0.701706523, 0.636929161, 0.740872554, 0.716753902, 0.615066028, 0.712954126, 
#            0.686337869, 0.634639045, 0.692385228, 0.707811151, 0.743064054, 0.655862722, 0.775350472]

# D50_SIE = [0.752629387, 0.787396040, 0.714336374, 1.633363137, 0.653926004, 0.657958213, 1.053660270, 0.691918682, 0.498216612,
#            0.670115814, 0.510694292, 0.679176535, 0.471877608, 0.821651788, 0.590637416, 0.589795421, 0.594801158, 0.368168797,
#            0.399921977, 0.707293095, 0.451919315, 1.582074936, 0.726551059, 1.411990139, 0.472872340, 0.817800759, 0.650493511, 
#            0.591879264, 1.258297872, 0.483782269, 0.512578390, 0.748987844, 0.462944623, 0.677670244]

# plt.scatter(D50_DGS, D50_SIE)
# plt.plot(np.arange(0,10), linestyle='--', color='k')
# plt.xlim(0,2); plt.ylim(0,2)
# plt.xlabel('D50 DGS (mm)', fontsize=20)
# plt.ylabel('D50 Sieve (mm)', fontsize=20)
# # plt.show()


# dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Uncorrected/Transform/Uncorrected_R1_Transformed.csv'))

# for i in range(16):
#     plt.plot(dgs_data[i+1, 1:], label=dgs_data[i+1, 0])
# plt.xlabel('Grain size (mm)', fontsize=20)
# plt.ylabel('Percentage', fontsize=20)
# plt.legend()
# plt.show()






# plt.subplot(2,1,1)
# for i in range(len(dgs_data)):
#     plt.scatter(sieve_open, ( sieve_data[i,2:] - dgs_data[i,2:] ), color=color[i], label= sieve_data[i,0])
# plt.legend(bbox_to_anchor=(1,1), loc="upper left")
# plt.xscale("log")
# plt.hlines(0, 0.063, 8, color='k')
# plt.title('Different Grain Shapes', fontsize=20)
# plt.ylabel('%-Sieve - %-pyDGS ', fontsize=20)


# error = sieve_data[:34, 2:]- dgs_data[:34, 2:]
# std = np.std(error.astype(np.float64), axis=0)

# sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
# plt.subplot(2,1,2)

# plt.errorbar(x=sieve_open, y=np.mean(error, axis=0), yerr=std, capsize=3)
# plt.hlines(0, 0.063, 8, color='k')
# plt.xscale('log')
# plt.ylabel('Mean Absolute Error', fontsize=20)
# plt.xlabel('Grain size (mm)', fontsize=20)

# plt.show()
