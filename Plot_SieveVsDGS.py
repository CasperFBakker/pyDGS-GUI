import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/UncorrectedPercentage_All.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Percentage_Sieve.csv'))
error = sieve_data[:34, 2:]- dgs_data[:34, 2:]

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
error = sieve_data[:34, 2:]- dgs_data[:34, 2:]
std = np.std(error.astype(np.float64), axis=0)

plt.subplot(2,1,1)
for i in range(len(dgs_data)):
    plt.plot(sieve_open, (sieve_data[i,2:]- dgs_data[i,2:]))
plt.xscale("log")
plt.ylabel('%-Sieve - %-pyDGS', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)
plt.title('Uncorrected', fontsize=20)
plt.hlines(0, 0.063, 8, color='k')

plt.subplot(2,1,2)
# plt.plot(sieve_open, np.mean(error, axis=0))
plt.errorbar(x=sieve_open, y=np.mean(error, axis=0), yerr=std, capsize=3)
plt.ylabel('Mean Absolute Error', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)
plt.xscale('log')
plt.show()

dgs_data_cor = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Corrected/Corrected_All_PercentTransf.csv'))

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
error = sieve_data[:34, 2:]- dgs_data_cor[:34, 2:]
std = np.std(error.astype(np.float64), axis=0)

plt.subplot(2,1,1)
for i in range(len(dgs_data)):
    plt.plot(sieve_open, error[i, :])
plt.xscale("log")
plt.ylabel('%-Sieve - %-pyDGS', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)
plt.title('Corrected', fontsize=20)
plt.hlines(0, 0.063, 8, color='k')

plt.subplot(2,1,2)
plt.errorbar(x=sieve_open, y=np.mean(error, axis=0), yerr=std, capsize=3)
plt.ylabel('Mean Absolute Error', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)
plt.xscale('log')
plt.show()


Density_Sand = 0.00165 # (g/mm**3)
Resolution = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Resolution_All.csv'))[:,1]
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
std = np.std(error.astype(np.float64), axis=0)

sieve_open = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
plt.subplot(2,1,1)
for i in range(len(sieve_data)):
    plt.plot(sieve_open, ( sieve_data[i,2:] - Mass_Fraction[i,1:] ))
plt.xscale("log")
plt.ylabel('%-Sieve - %-pyDGS ', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)
plt.title('Volume correction: new method', fontsize=20)
plt.hlines(0, 0.063, 8, color='k')


plt.subplot(2,1,2)

plt.errorbar(x=sieve_open, y=np.mean(error, axis=0), yerr=std, capsize=3)
# plt.plot(sieve_open, np.mean(error, axis=0))
plt.hlines(0, 0.063, 8, color='k')
plt.ylim([-31.2, 21.1])
plt.xscale('log')
plt.ylabel('Mean Absolute Error', fontsize=20)
plt.xlabel('Grain size (mm)', fontsize=20)
plt.show()


# x = [0, 1.894556943, 4.102007219, 10.13938691, 8.543334643, 10.72416515, 8.399230289, 3.957295424, 3.620868346, 5.691698725, 13.91140123, 15.35243291, 8.945241631, 4.718380592,
#      0, 1.746068889, 2.813764553, 7.006765308, 7.414862876, 11.79479998, 11.31271694, 5.328660275, 3.788039343, 5.792404924, 13.64346485, 14.87062429, 9.577047437, 4.910780329,
#      0, 1.105796825, 1.636397456, 2.293388280, 3.385419031, 4.210759068, 11.90108039, 14.44265590, 11.29801637, 7.052458156, 15.66600577, 16.06486714, 7.337174967, 3.605980647,
#      0, 1.817207805, 2.640081452, 9.261873948, 8.827060004, 9.310767376, 10.60957278, 4.911807989, 3.785683041, 6.875032693, 16.85293535, 14.91497731, 7.217074930, 2.975925330,
#      0, 1.700072280, 1.506847064, 5.438343533, 5.258240024, 10.43173442, 13.27116221, 9.207988987, 4.545184215, 6.520852009, 15.86771287, 15.25911104, 8.014521493, 2.978229856,
#      0, 2.794027199, 5.522601036, 9.573643474, 11.53749304, 7.240197211, 7.031482498, 3.454861303, 3.520659561, 5.652671880, 14.19038853, 15.69314812, 9.237641254, 4.551184889,
#      0, 1.364833945, 1.506116768, 2.680097976, 3.426590596, 5.815359244, 11.67694222, 15.13894669, 8.751923289, 6.350525945, 16.17309177, 15.97005623, 7.615400796, 3.530114517,
#      0, 3.100925296, 5.831655559, 11.79504918, 10.69212910, 6.462759304, 6.211988358, 3.792260783, 3.312388528, 5.772475208, 13.26104662, 15.43521995, 9.062190451, 5.269911664]

# x_T = [0, 2.680172302, 4.041514766, 6.545785713, 4.544727312, 6.286521327, 7.365159882, 5.961132175, 8.402478807, 4.431122354, 6.660626651, 10.11449864, 13.56325822, 19.40300186,
#        0, 0.845826623, 1.475072374, 3.141470831, 2.888010668, 5.077341891, 7.707151436, 8.073308147, 14.49717200, 6.060650243, 7.040926882, 10.29453668, 14.59766005, 18.30087218,
#        0, 0.561007144, 0.949440415, 1.641728148, 2.535963600, 2.679353587, 6.280601947, 7.997827412, 19.14823363, 7.854351659, 8.711920417, 12.09816145, 14.54820807, 14.99320252,
#        0, 3.102640946, 3.326509216, 6.967009207, 4.668332332, 4.752104470, 7.373597700, 6.045761211, 8.629581810, 5.161093697, 8.400854688, 11.82326663, 14.37774467, 15.37150343,
#        0, 1.763768581, 1.744525969, 5.186646954, 3.389164960, 5.266799050, 7.092527611, 7.987277412, 11.74364709, 5.671348217, 8.824541333, 12.68703677, 13.79901088, 14.84370518,
#        0, 4.282146889, 5.154247518, 5.875724460, 6.200103957, 4.529872135, 6.660697767, 5.160442631, 7.507535256, 4.548417140, 7.225070593, 11.25391725, 14.73676559, 16.86505882,
#        0, 0.568758502, 0.814791531, 1.737309897, 2.101869866, 2.975177683, 5.326445798, 8.383174512, 18.88259079, 8.450803284, 9.650794282, 13.34995933, 14.69350967, 13.06481486,
#        0, 3.785981408, 4.832180538, 6.919057493, 5.873412584, 4.321359704, 6.395698601, 5.987461705, 7.281376868, 4.602936993, 7.178008995, 11.85459902, 14.91130082, 16.05662527]

# plt.scatter(x, x_T)
# plt.show()

# D = [0, 1.820312916, 3.457885886, 8.573076109, 7.979098759, 11.25948256, 9.855973615, 4.642977850, 3.704453844, 5.742051824, 13.77743304, 15.11152860, 9.261144534, 4.814580461]
# C = [0, 1.461502315, 2.138239454, 5.777631114, 6.106239517, 6.760763222, 11.25532658, 9.677231947, 7.541849704, 6.963745425, 16.25947056, 15.48992222, 7.277124948, 3.290952989]
# B = [0, 1.532453113, 1.506481916, 4.059220754, 4.342415310, 8.123546834, 12.47405221, 12.17346784, 6.648553752, 6.435688977, 16.02040232, 15.61458364, 7.814961145, 3.254172186]
# A = [0, 2.947476248, 5.677128298, 10.68434633, 11.11481107, 6.851478258, 6.621735428, 3.623561043, 3.416524044, 5.712573544, 13.72571757, 15.56418403, 9.149915853, 4.910548277]


# D_t = [0, 1.762999463, 2.758293570, 4.843628272, 3.716368990, 5.681931609, 7.536155659, 7.017220161, 11.44982541, 5.245886298, 6.850776767, 10.20451766, 14.08045913, 18.85193702]
# C_t = [0, 1.831824045, 2.137974815, 4.304368678, 3.602147966, 3.715729028, 6.827099823, 7.021794311, 13.88890772, 6.507722678, 8.556387553, 11.96071404, 14.46297637, 15.18235297]
# B_t = [0, 1.166263541, 1.279658750, 3.461978425, 2.745517413, 4.120988367, 6.209486705, 8.185225962, 15.31311894, 7.061075750, 9.237667808, 13.01849805, 14.24626027, 13.95426002]
# A_t = [0, 4.034064148, 4.993214028, 6.397390977, 6.036758271, 4.425615919, 6.528198184, 5.573952168, 7.394456062, 4.575677066, 7.201539794, 11.55425813, 14.82403321, 16.46084204]
# sieve_open = [0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
# plt.subplot(2,2,4)
# plt.plot(sieve_open, D, label='Original')
# plt.plot(sieve_open, D_t, label='Transformed 90 deg')
# plt.legend()
# plt.xscale('log')
# plt.subplot(2,2,3)
# plt.plot(sieve_open, C)
# plt.plot(sieve_open, C_t)
# plt.xscale('log')
# plt.subplot(2,2,2)
# plt.plot(sieve_open, B)
# plt.plot(sieve_open, B_t)
# plt.xscale('log')
# plt.subplot(2,2,1)
# plt.plot(sieve_open, A)
# plt.plot(sieve_open, A_t)
# plt.xscale('log')

# plt.show()