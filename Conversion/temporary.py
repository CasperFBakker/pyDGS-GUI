import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.pyplot import cm
import math

def power_fit(x, y, p=False):
  
  coefs = np.polyfit(np.log(x),np.log(y),1)
  a = np.exp(coefs[1])
  b = coefs[0]
  if p:
    print(a,b)

  return a*x**b 

def get_r2_numpy(x, y):
    slope, intercept = np.polyfit(np.log(x), np.log(y), 1)
    r_squared = 1 - (sum((np.log(y) - (slope * np.log(x) + intercept))**2) / ((len(y) - 1) * np.var(np.log(y), ddof=1)))
    return r_squared


def RMSE(Sieve_vals, DGS_vals):

    diffrnce = np.subtract(Sieve_vals, DGS_vals)
    sqre_err = np.square(diffrnce)
    rslt_meansqre_err = sqre_err.mean()
    root_meansqre_err = math.sqrt(rslt_meansqre_err)
    return root_meansqre_err


data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Uncorrected/Uncorrected_Locs_MeanTransf.csv'))

sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/01_12_22_Egmond/Sieve/Percentage_Sieve.csv'))
GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4])


# for i in range(len(data)):
#     plt.scatter(sieve_data[i,1:], data[i,1:])

# plt.xscale('log'); plt.yscale('log')
# plt.show()


t1 = [0.009970464, 0.926786123, 16.87658136, 8.169001323, 2.258504119, 0.820357480, 0.287229839, 0.045347506, 0.001552619, 0.000731164]
t2 = [0.011400404, 0.281745336, 6.273830042, 10.08058776, 4.598461696, 4.596895314, 1.252026824, 0.139469939, 0.003063357, 0.000885969]
t3 = [0.035479839, 0.586910570, 8.247826620, 9.847588995, 5.713696972, 3.788831660, 2.282081966, 0.939039055, 0.140476223, 0.043796245, 0.021995549, 0.004304766]
t4 = [0.005907813, 0.933618788, 7.429548999, 9.777065441, 2.382603010, 1.785436246, 0.468400417, 0.085658929, 0.005844130, 0.001047785, 0.001157231, 0.005406778]
t5 = [0.006289253, 0.536159961, 8.694465437, 8.897370897, 4.907957597, 3.071517684, 0.926637220, 0.153858744, 0.006157923, 0.002308614, 0.000790765, 0.001168569]
t6 = [0.003839265, 0.918193751, 8.220718447, 11.40846892, 2.949495953, 2.735618370, 2.032928988, 1.411428392, 0.653199632, 0.369488582, 0.303810794, 0.420344837]
t7 = [0.011878847, 1.586519519, 13.44809621, 5.511145953, 0.750116662, 0.329454889, 0.105006266, 0.029788004, 0.010565593, 0.004242837, 0.066943356]
t8 = [0.005560097, 0.354343920, 5.368828275, 7.887648498, 4.530547342, 4.074872800, 1.460170021, 0.786710112, 0.061785833, 0.011506923, 0.003774619, 0.013637385]
t9 = [0.024351945, 0.592872061, 7.024722938, 8.205608330, 3.775355901, 2.210551802, 1.116110571, 0.463142855, 0.117837935, 0.025139799, 0.015654121, 0.003372771]

power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1], t1, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1], t2, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1,2,4], t3, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1,2,4], t4, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1,2,4], t5, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1,2,4], t6, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1,4], t7, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1,2,4], t8, True)
power_fit([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1,2,4], t9, True)


GrainSz =  np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4])
GrainSz =  np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 
         0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
         0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
         0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 4, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
         0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4])

T = [0.009970464, 0.926786123, 16.87658136, 8.169001323, 2.258504119, 0.820357480, 0.287229839, 0.045347506, 0.001552619, 0.000731164, 
      0.011400404, 0.281745336, 6.273830042, 10.08058776, 4.598461696, 4.596895314, 1.252026824, 0.139469939, 0.003063357, 0.000885969, 
      0.035479839, 0.586910570, 8.247826620, 9.847588995, 5.713696972, 3.788831660, 2.282081966, 0.939039055, 0.140476223, 0.043796245, 0.021995549, 0.004304766,
      0.005907813, 0.933618788, 7.429548999, 9.777065441, 2.382603010, 1.785436246, 0.468400417, 0.085658929, 0.005844130, 0.001047785, 0.001157231, 0.005406778, 
      0.006289253, 0.536159961, 8.694465437, 8.897370897, 4.907957597, 3.071517684, 0.926637220, 0.153858744, 0.006157923, 0.002308614, 0.000790765, 0.001168569, 
      0.003839265, 0.918193751, 8.220718447, 11.40846892, 2.949495953, 2.735618370, 2.032928988, 1.411428392, 0.653199632, 0.369488582, 0.303810794, 0.420344837,
      0.011878847, 1.586519519, 13.44809621, 5.511145953, 0.750116662, 0.329454889, 0.105006266, 0.029788004, 0.010565593, 0.004242837, 0.066943356, 
      0.005560097, 0.354343920, 5.368828275, 7.887648498, 4.530547342, 4.074872800, 1.460170021, 0.786710112, 0.061785833, 0.011506923, 0.003774619, 0.013637385,
      0.024351945, 0.592872061, 7.024722938, 8.205608330, 3.775355901, 2.210551802, 1.116110571, 0.463142855, 0.117837935, 0.025139799, 0.015654121, 0.003372771]


plt.scatter(GrainSz, T)
plt.plot(GrainSz, power_fit(GrainSz, T, True))
# plt.plot(GrainSz[3:], power_fit(GrainSz[3:], True[3:], True))
print('R2 = ', get_r2_numpy(T, power_fit(GrainSz, T)))
print('RMSE =', RMSE(T, power_fit(GrainSz, T)))

# print('----------------------------------------')
# print('R2 = ', get_r2_numpy(t9[0:3], power_fit(GrainSz[0:3], t9[0:3])))
# print('RMSE =', RMSE(t9[0:3], power_fit(GrainSz[0:3], t9[0:3])))
# print('----------------------------------------')
# print('R2 = ', get_r2_numpy(t9[3:], power_fit(GrainSz[3:], t9[3:])))
# print('RMSE =', RMSE(t9[3:], power_fit(GrainSz[3:], t9[3:])))

plt.xscale('log'); plt.yscale('log')


plt.show()

GrainSz1 = np.array([0.063, 0.125, 0.180, 0.063, 0.125, 0.180,0.063, 0.125, 0.180, 0.063, 0.125, 0.180, 0.063, 0.125, 0.180, 0.063, 0.125, 0.180, 
                     0.063, 0.125, 0.180, 0.063, 0.125, 0.180, 0.063, 0.125, 0.180])
T1 = [0.009970464, 0.926786123, 16.87658136, 0.011400404, 0.281745336, 6.273830042, 0.035479839, 0.586910570, 8.247826620, 0.005907813, 0.933618788, 7.429548999,
      0.006289253, 0.536159961, 8.694465437, 0.003839265, 0.918193751, 8.220718447, 0.011878847, 1.586519519, 13.44809621, 0.005560097, 0.354343920, 5.368828275, 0.024351945, 0.592872061, 7.024722938,]

T2 = [8.169001323, 2.258504119, 0.820357480, 0.287229839, 0.045347506, 0.001552619, 0.000731164, 10.08058776, 4.598461696, 4.596895314, 1.252026824, 0.139469939, 0.003063357, 0.000885969,
      9.847588995, 5.713696972, 3.788831660, 2.282081966, 0.939039055, 0.140476223, 0.043796245, 0.021995549, 0.004304766, 9.777065441, 2.382603010, 1.785436246, 0.468400417, 0.085658929, 0.005844130, 0.001047785, 0.001157231, 0.005406778,
      8.897370897, 4.907957597, 3.071517684, 0.926637220, 0.153858744, 0.006157923, 0.002308614, 0.000790765, 0.001168569, 11.40846892, 2.949495953, 2.735618370, 2.032928988, 1.411428392, 0.653199632, 0.369488582, 0.303810794, 0.420344837,
      5.511145953, 0.750116662, 0.329454889, 0.105006266, 0.029788004, 0.010565593, 0.004242837, 0.066943356, 7.887648498, 4.530547342, 4.074872800, 1.460170021, 0.786710112, 0.061785833, 0.011506923, 0.003774619, 0.013637385, 
      8.205608330, 3.775355901, 2.210551802, 1.116110571, 0.463142855, 0.117837935, 0.025139799, 0.015654121, 0.003372771]

GrainSz2 = np.array([0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                     0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                     0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 4, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4])

plt.scatter(GrainSz1, T1)
plt.plot(GrainSz1, power_fit(GrainSz1, T1, True))
print('R2 = ', get_r2_numpy(T1, power_fit(GrainSz1, T1)))
print('RMSE =', RMSE(T1, power_fit(GrainSz1, T1)))


plt.scatter(GrainSz2, T2)
plt.plot(GrainSz2, power_fit(GrainSz2, T2, True))
print('R2 = ', get_r2_numpy(T2, power_fit(GrainSz2, T2)))
print('RMSE =', RMSE(T2, power_fit(GrainSz2, T2)))



plt.xscale('log'); plt.yscale('log')


plt.show()


T = [0.008738257, 0.567184777, 5.953565640, 1.788072693, 0.397176763, 0.155351758, 0.088671575, 0.040432270,
     0.005719223, 0.096379942, 1.563719299, 2.186881552, 1.050451392, 1.387247227, 0.643996931, 0.156515288,
     0.031262472, 0.434146119, 4.068030912, 2.860471150, 1.066977097, 0.535538773, 0.358934884, 0.431911026,
     0.003195734, 0.326783219, 1.877672970, 2.251128888, 0.634412378, 0.712712381, 0.332517659, 0.120669308,
     0.002454689, 0.150789704, 1.924115180, 1.837737851, 1.134065720, 1.000123936, 0.521242370, 0.166010246,
     0.001948444, 0.458734226, 3.273715507, 2.927147512, 0.503401220, 0.348230961, 0.260767631, 0.444764540,
     0.006149574, 0.543962394, 3.357238365, 1.259962512, 0.197801876, 0.128983951, 0.073368625, 0.038986200,
     0.002619029, 0.111502652, 1.220492127, 1.613471085, 1.051621256, 1.380029446, 0.878715855, 0.944532344,
     0.019859314, 0.313473449, 2.207711077, 1.769368897, 0.731717679, 0.521787555, 0.464770133, 0.507089961]
T1 = [0.008738257, 0.567184777, 5.953565640, 1.788072693, 0.397176763, 0.155351758, 0.088671575, 0.040432270]
T2 = [0.005719223, 0.096379942, 1.563719299, 2.186881552, 1.050451392, 1.387247227, 0.643996931, 0.156515288]
T3 = [0.031262472, 0.434146119, 4.068030912, 2.860471150, 1.066977097, 0.535538773, 0.358934884, 0.431911026]
T4 = [0.003195734, 0.326783219, 1.877672970, 2.251128888, 0.634412378, 0.712712381, 0.332517659, 0.120669308]
T5 = [0.002454689, 0.150789704, 1.924115180, 1.837737851, 1.134065720, 1.000123936, 0.521242370, 0.166010246]
T6 = [0.001948444, 0.458734226, 3.273715507, 2.927147512, 0.503401220, 0.348230961, 0.260767631, 0.444764540]
T7 = [0.006149574, 0.543962394, 3.357238365, 1.259962512, 0.197801876, 0.128983951, 0.073368625, 0.038986200]
T8 = [0.002619029, 0.111502652, 1.220492127, 1.613471085, 1.051621256, 1.380029446, 0.878715855, 0.944532344]
T9 = [0.019859314, 0.313473449, 2.207711077, 1.769368897, 0.731717679, 0.521787555, 0.464770133, 0.507089961]
GrainSzT = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500])

GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500])

plt.subplot(1,2,1)
plt.scatter(GrainSz, T)
plt.xscale('log'); plt.yscale('log')

plt.subplot(1,2,2)
plt.scatter(GrainSzT, T1)
plt.scatter(GrainSzT, T2)
plt.scatter(GrainSzT, T3)
plt.scatter(GrainSzT, T4)
plt.scatter(GrainSzT, T5)
plt.scatter(GrainSzT, T6)
plt.scatter(GrainSzT, T7)
plt.scatter(GrainSzT, T8)
plt.scatter(GrainSzT, T9)
plt.xscale('log'); plt.yscale('log')

plt.show()







T = [0.005022437, 0.062269681, 0.388433001, 1.205711946, 1.472643017, 1.751699262, 1.912040197, 2.961429071, 3.241606420, 1.354580700, 0.252808968, 0.106591552,  	0.005690591,
     0.018299314, 0.348762292, 0.980825528, 2.672470218, 2.304574701, 2.451298675, 1.675600273, 2.086332127, 2.582421092, 0.715354495, 0.064918249, 0.018012989,  	                 
     0.008630526, 0.096256971, 0.443474156, 1.231733490, 1.432935036, 1.909153473, 2.099206976, 2.115499590, 2.156162757, 1.584460779, 0.730702599, 0.226232034,  	0.001285389,
     0.008836801, 0.265828325, 0.898685451, 2.805892021, 2.097630815, 1.989602527, 1.365664624, 1.609307147, 2.344367542, 1.248187736, 0.259397024, 0.071316374,  	0.28289303,
     0.014909909, 0.215891188, 0.799153720, 1.416953957, 1.543593673, 0.913826955, 0.591593855, 0.909310877, 1.495635095, 1.789612126, 1.363885174, 0.306175795,  	0.066139908,
                 	0.162318832, 0.686267552, 1.716172506, 1.939771625, 1.279166599, 1.296941420, 1.809165927, 2.131770853, 1.338161861, 0.336197998, 0.069340704,  	                 
     0.009548930, 0.133037632, 0.565001314, 1.919320553, 1.281541595, 1.199059094, 0.897942766, 1.329570575, 2.520063502, 2.100510633, 0.623151949, 0.212714868,  	                 
     0.033319119, 0.208331754, 0.628755352, 1.523370565, 1.283756327, 0.892024179, 0.780909846, 0.892631217, 1.097020036, 1.280071640, 1.017283371, 0.841139979,  	2.370630321,
     0.009315187, 0.097639340, 0.584161434, 1.771780576, 1.204071105, 1.853284718, 1.243232415, 1.245478437, 2.029159194, 1.954423461, 0.558890252, 0.198858731,  	                 
     0.027939826, 0.177906446, 0.804710851, 3.467350139, 3.173246736, 4.328418596, 2.124747110, 1.227350063, 0.831539918, 0.691636213, 0.298933788, 0.19487941	,  0.141992377,
     0.007620856, 0.102286612, 0.241232103, 0.808621625, 0.758747562, 1.220715469, 1.360385939, 2.233285173, 2.833041499, 1.510658062, 0.409755647, 0.085466284,  	0.219986588,
     0.012408817, 0.401479257, 1.822403234, 3.269408607, 2.273498866, 1.704153238, 1.050938016, 0.935118730, 1.146001124, 1.134468776, 0.523428616, 0.24856512	,  0.513890195,
     0.023583642, 0.430145982, 1.160807158, 4.159004773, 3.607398232, 3.980266979, 2.386616824, 1.235631149, 0.990738645, 0.480153117, 0.096248126, 0.031795175,  	0.001415086,
                	0.062148692, 0.279566062, 1.348611412, 2.144175658, 2.892973544, 2.343166664, 2.259947452, 1.981580365, 1.308766760, 0.479102363, 0.21651694,                 
     0.005799739, 0.118944196, 0.492185296, 1.739460817, 1.972133776, 2.688024891, 1.836698093, 2.590546229, 2.226594649, 1.251569716, 0.530451027, 0.132311977,                   	
     0.017132163, 0.234820342, 0.632309596, 1.397843041, 1.480827604, 1.948053686, 2.042915940, 2.887359285, 2.359679003, 1.178964886, 0.375020191, 0.126085962,  	0.001501977,
     0.001252748, 0.178116494, 0.501993400, 1.368268656, 1.151190190, 1.720911204, 1.460779125, 2.118951298, 3.422983933, 2.121727681, 0.397756712, 0.047083639,  	0.001420067,
                 	0.113939823, 0.702734990, 1.942125947, 2.209902129, 3.371847442, 3.096300924, 3.220958178, 2.356317617, 0.866785632, 0.206929292, 0.046818398,  	0.001156417,
     0.002548012, 0.078608647, 0.289167171, 0.974157933, 1.211546623, 2.424488520, 2.677476330, 3.361200019, 3.176529926, 1.752282410, 0.432769895, 0.157885506,  	0.001200421,
     0.005075127, 0.266289101, 1.024416711, 2.332396491, 2.304696676, 2.148136717, 1.928710559, 2.324363232, 1.973829553, 1.253365833, 0.422863791, 0.114726854,                   	
     0.004181034, 0.188397939, 0.518840118, 1.360449954, 1.585811234, 2.451256426, 2.110104470, 2.445359693, 2.192286093, 1.525085974, 0.602065479, 0.189245558,                   	
     0.014093826, 0.239450388, 0.698632694, 1.965910500, 2.030890050, 3.192124151, 3.031083515, 3.845696913, 3.211834217, 0.889506699, 0.100899890, 0.020474358,                   	
     0.005258423, 0.194854389, 0.748334986, 1.687890154, 1.437679883, 1.805089291, 1.763777129, 2.677570037, 2.400961758, 1.642795421, 0.685992652, 0.18052167	,  0.0011296,
     0.004309154, 0.130773620, 0.317549404, 0.795739706, 0.630075652, 1.223541006, 1.203136573, 2.354499728, 3.141967170, 2.209886647, 0.900008204, 0.199108211,                   	
     0.011284073, 0.332789036, 0.877457469, 1.413195322, 1.195217312, 1.592166304, 1.837362929, 2.820463807, 2.773807498, 1.448748301, 0.548190680, 0.178337418,  	0.201568637,
     0.006220398, 0.115577669, 0.232084294, 0.746262387, 0.814899720, 1.897621106, 2.450890340, 3.724401556, 2.596317401, 1.496144717, 0.270159887, 0.109312343,                   	
     0.005339025, 0.128336461, 0.334870868, 0.705888480, 0.550555314, 1.258920054, 1.961415863, 4.206388816, 3.056608273, 1.555501844, 0.480177978, 0.152622718,  	0.001366269,
     0.012655094, 0.190914147, 0.305244672, 0.512486523, 0.340167885, 1.220393895, 2.344882502, 4.344564724, 3.015437709, 1.291432417, 0.618520550, 0.527721668,  	0.987274969,
     0.040891044, 0.238115401, 0.178844560, 0.166207306, 0.144613915, 0.447195098, 1.812630442, 4.568898122, 3.503420417, 1.323990068, 0.389315395, 0.25289488	,  0.604167757]


GrainSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,   
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                           0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                           0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                           0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8,
                    0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])

plt.scatter(GrainSz, T)
plt.plot(GrainSz, power_fit(GrainSz, T, True))
print('R2 = ', get_r2_numpy(T, power_fit(GrainSz, T)))
print('RMSE =', RMSE(T, power_fit(GrainSz, T)))


plt.xscale('log'); plt.yscale('log')

plt.show()



GrainSz1 = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,        0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,        0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,        0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500,
            0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500]
GrainSz2 = [0.710, 1, 2, 4, 8, 0.710, 1, 2, 4,   0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 0.710, 1, 2, 4,  0.710, 1, 2, 4, 8, 0.710, 1, 2, 4,
            0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4,  0.710, 1, 2, 4,  0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8,
            0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 0.710, 1, 2, 4, 0.710, 1, 2, 4, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 0.710, 1, 2, 4, 8, 0.710, 1, 2, 4, 8,
            0.710, 1, 2, 4, 8]

T1 = [0.005022437, 0.062269681, 0.388433001, 1.205711946, 1.472643017, 1.751699262, 1.912040197, 2.961429071, 0.018299314, 0.348762292, 0.980825528, 2.672470218, 2.304574701, 2.451298675, 1.675600273, 2.086332127,
      0.008630526, 0.096256971, 0.443474156, 1.231733490, 1.432935036, 1.909153473, 2.099206976, 2.115499590, 0.008836801, 0.265828325, 0.898685451, 2.805892021, 2.097630815, 1.989602527, 1.365664624, 1.609307147,
      0.014909909, 0.215891188, 0.799153720, 1.416953957, 1.543593673, 0.913826955, 0.591593855, 0.909310877,             	0.162318832, 0.686267552, 1.716172506, 1.939771625, 1.279166599, 1.296941420, 1.809165927,
      0.009548930, 0.133037632, 0.565001314, 1.919320553, 1.281541595, 1.199059094, 0.897942766, 1.329570575, 0.033319119, 0.208331754, 0.628755352, 1.523370565, 1.283756327, 0.892024179, 0.780909846, 0.892631217,
      0.009315187, 0.097639340, 0.584161434, 1.771780576, 1.204071105, 1.853284718, 1.243232415, 1.245478437, 0.027939826, 0.177906446, 0.804710851, 3.467350139, 3.173246736, 4.328418596, 2.124747110, 1.227350063,
      0.007620856, 0.102286612, 0.241232103, 0.808621625, 0.758747562, 1.220715469, 1.360385939, 2.233285173, 0.012408817, 0.401479257, 1.822403234, 3.269408607, 2.273498866, 1.704153238, 1.050938016, 0.935118730,
      0.023583642, 0.430145982, 1.160807158, 4.159004773, 3.607398232, 3.980266979, 2.386616824, 1.235631149,            	0.062148692, 0.279566062, 1.348611412, 2.144175658, 2.892973544, 2.343166664, 2.259947452, 
      0.005799739, 0.118944196, 0.492185296, 1.739460817, 1.972133776, 2.688024891, 1.836698093, 2.590546229, 0.017132163, 0.234820342, 0.632309596, 1.397843041, 1.480827604, 1.948053686, 2.042915940, 2.887359285,
      0.001252748, 0.178116494, 0.501993400, 1.368268656, 1.151190190, 1.720911204, 1.460779125, 2.118951298,             	0.113939823, 0.702734990, 1.942125947, 2.209902129, 3.371847442, 3.096300924, 3.220958178,
      0.002548012, 0.078608647, 0.289167171, 0.974157933, 1.211546623, 2.424488520, 2.677476330, 3.361200019, 0.005075127, 0.266289101, 1.024416711, 2.332396491, 2.304696676, 2.148136717, 1.928710559, 2.324363232,
      0.004181034, 0.188397939, 0.518840118, 1.360449954, 1.585811234, 2.451256426, 2.110104470, 2.445359693, 0.014093826, 0.239450388, 0.698632694, 1.965910500, 2.030890050, 3.192124151, 3.031083515, 3.845696913,
      0.005258423, 0.194854389, 0.748334986, 1.687890154, 1.437679883, 1.805089291, 1.763777129, 2.677570037, 0.004309154, 0.130773620, 0.317549404, 0.795739706, 0.630075652, 1.223541006, 1.203136573, 2.354499728,
      0.011284073, 0.332789036, 0.877457469, 1.413195322, 1.195217312, 1.592166304, 1.837362929, 2.820463807, 0.006220398, 0.115577669, 0.232084294, 0.746262387, 0.814899720, 1.897621106, 2.450890340, 3.724401556,
      0.005339025, 0.128336461, 0.334870868, 0.705888480, 0.550555314, 1.258920054, 1.961415863, 4.206388816, 0.012655094, 0.190914147, 0.305244672, 0.512486523, 0.340167885, 1.220393895, 2.344882502, 4.344564724,
      0.040891044, 0.238115401, 0.178844560, 0.166207306, 0.144613915, 0.447195098, 1.812630442, 4.568898122,]

T2 = [3.241606420, 1.354580700, 0.252808968, 0.106591552,  	0.005690591, 2.582421092, 0.715354495, 0.064918249, 0.018012989,  	            2.156162757, 1.584460779, 0.730702599, 0.226232034,  	0.001285389,
      2.344367542, 1.248187736, 0.259397024, 0.071316374,  	0.28289303, 1.495635095, 1.789612126, 1.363885174, 0.306175795,  	0.066139908,2.131770853, 1.338161861, 0.336197998, 0.069340704,  	             
      2.520063502, 2.100510633, 0.623151949, 0.212714868,  	             1.097020036, 1.280071640, 1.017283371, 0.841139979,  	2.370630321, 2.029159194, 1.954423461, 0.558890252, 0.198858731,  	            
      0.831539918, 0.691636213, 0.298933788, 0.19487941	,  0.141992377,2.833041499, 1.510658062, 0.409755647, 0.085466284,  	0.219986588, 1.146001124, 1.134468776, 0.523428616, 0.24856512	,  0.513890195,
      0.990738645, 0.480153117, 0.096248126, 0.031795175,  	0.001415086, 1.981580365, 1.308766760, 0.479102363, 0.21651694,                2.226594649, 1.251569716, 0.530451027, 0.132311977,               
      2.359679003, 1.178964886, 0.375020191, 0.126085962,  	0.001501977, 3.422983933, 2.121727681, 0.397756712, 0.047083639,  	0.001420067, 2.356317617, 0.866785632, 0.206929292, 0.046818398,  	0.001156417,
      3.176529926, 1.752282410, 0.432769895, 0.157885506,  	0.001200421, 1.973829553, 1.253365833, 0.422863791, 0.114726854,               2.192286093, 1.525085974, 0.602065479, 0.189245558,               
      3.211834217, 0.889506699, 0.100899890, 0.020474358,               2.400961758, 1.642795421, 0.685992652, 0.18052167	,  0.0011296, 3.141967170, 2.209886647, 0.900008204, 0.199108211,               
      2.773807498, 1.448748301, 0.548190680, 0.178337418,  	0.201568637, 2.596317401, 1.496144717, 0.270159887, 0.109312343,               3.056608273, 1.555501844, 0.480177978, 0.152622718,  	0.001366269,
      3.015437709, 1.291432417, 0.618520550, 0.527721668,  	0.987274969, 3.503420417, 1.323990068, 0.389315395, 0.25289488	,  0.604167757]

plt.scatter(GrainSz1, T1)
plt.plot(GrainSz1, power_fit(GrainSz1, T1, True))
print('R2 = ', get_r2_numpy(T1, power_fit(GrainSz1, T1)))
print('RMSE =', RMSE(T1, power_fit(GrainSz1, T1)))


plt.scatter(GrainSz2, T2)
plt.plot(GrainSz2, power_fit(GrainSz2, T2, True))
print('R2 = ', get_r2_numpy(T2, power_fit(GrainSz2, T2)))
print('RMSE =', RMSE(T2, power_fit(GrainSz2, T2)))



plt.xscale('log'); plt.yscale('log')


plt.show()