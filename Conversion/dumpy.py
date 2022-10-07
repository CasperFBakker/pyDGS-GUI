# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# data_Prof = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22//Proffitt Percentile/Percentiles_Location_1.csv')) #Proffitt_test/
# data_Sieve = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentile/Percentiles_Sieve.csv'))


# GrainSize = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.250, 0.18, 0.125, 0.063]
# locations = [1, 2, 3, 4,6, 7]
# for j in range(len(locations)):
#     data_Prof =  np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentile/Proffitt_test/Percentiles_Location_' + str(locations[j]) + '.csv'))
#     for i in range(len(data_Prof)):
#         plt.subplot(2,3,int(j+1))
#         plt.scatter(GrainSize, (data_Sieve[j,1:]/(data_Prof[i,1:14])), label=data_Prof[i,14])
#         plt.xscale("log")
#         plt.yscale("log")
#         plt.grid(which='major', linewidth=2, linestyle='-')
#         plt.grid(which='minor', linewidth=1, linestyle='--')
#         plt.ylim(0.0001, 100)
#         plt.legend()


# # test = np.mean(np.vstack(data_Prof[:,1:]), axis=0)
# # print(test)
# # popt, pcov = curve_fit(lambda fx,a,b: a*fx**b,  GrainSize[7:14],  (data_Sieve[0,8:14]/(test[7:14])))
# # power_y = popt[0]*GrainSize[7:14]**popt[1]

# # plt.plot(GrainSize[7:14], power_y, label=str(popt[0]) + 'x**' + str(-popt[1]) )

# # for i in range(len(data_Prof)):
# #     plt.scatter(GrainSize, (data_Sieve[0,1:]/(data_Prof[i,1:14])), label=data_Prof[i,0])
    
# # plt.xscale("log")
# # plt.yscale("log")
# # plt.grid(which='major', linewidth=2, linestyle='-')
# # plt.grid(which='minor', linewidth=1, linestyle='--')
# # plt.ylim(0.01, 10)
# # plt.legend()

# plt.show()








# ##############################################################################################################################################################################




# plt.subplot(3,3,(1,3))
# for i in range(1, 14):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend()

# plt.subplot(3,3,4)
# for i in range(14, 22):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend()

# plt.subplot(3,3,5)
# for i in range(22, 26):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend()

# plt.subplot(3,3,6)
# for i in range(26, 34):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend()

# plt.subplot(3,3,7)
# for i in range(34, 38):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend()

# plt.subplot(3,3,8)
# for i in range(38, 46):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend()

# plt.subplot(3,3,9)
# for i in range(46, 48):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend()

# plt.show()

# ##############################################################################################################################################################################

# xfit = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
# yfit = np.array([0.208307862, 1.031856376, 2.142537041, 3.388183378, 2.571073162, 2.308543947, 1.495428404, 1.42181968, 0.811075903, 0.533655452, 0.561671272,0.541487501, 0])


# z = np.polyfit(xfit, yfit, 8)
# p = np.poly1d(z)
# print(p)
# plt.plot(xfit, p(xfit))

# for i in range(len(data)):
#     plt.scatter(GrainSize, data[i,1:15], label=data[i,15])

# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)
# plt.legend(loc='lower right')


# plt.show()

# ##############################################################################################################################################################################


# plt.subplot(2,3,1)
# yfit = np.array([0.176626657, 1.149030204, 1.746586149, 2.215164335, 1.781314253, 2.286232085, 1.607402283, 2.44237334, 1.538243408, 0.590077708, 0.359543279, 0.218923259, 0])
# z = np.polyfit(xfit, yfit, 1)
# p = np.poly1d(z)
# plt.plot(xfit, p(xfit))
# for i in range(1, 14):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)


# plt.subplot(2,3,2)
# yfit = np.array([0.00889454, 0.230734461, 1.648808468, 4.599172591, 4.049283888, 3.195208036, 1.788540941, 1.368561054, 0.462574893, 0.353190373, 0.439846551, 0.451551121, 0])
# z = np.polyfit(xfit, yfit, 1)
# p = np.poly1d(z)
# plt.plot(xfit, p(xfit))
# for i in range(14, 22):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)


# plt.subplot(2,3,3)
# yfit = np.array([0.16589751, 1.157312251, 1.880347959, 4.077461111, 2.068472567, 2.250635769, 0.81612999, 0.62415191, 0.369584838, 0.41590902, 0.570582606, 1.193496832, 0])
# z = np.polyfit(xfit, yfit, 2)
# p = np.poly1d(z)
# plt.plot(xfit, p(xfit))
# for i in range(22, 26):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)


# plt.subplot(2,3,4)
# yfit = np.array([0.019167218, 0.25233682, 0.997561335, 2.460717724, 2.179598949, 2.210662032, 1.416211902, 1.181008823, 0.7737245, 0.871518857, 0.956430865, 0.919591828, 0])
# z = np.polyfit(xfit, yfit, 2)
# p = np.poly1d(z)
# plt.plot(xfit, p(xfit))
# for i in range(26, 34):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)


# plt.subplot(2,3,5)
# yfit = np.array([0.451262702, 1.908525304, 4.148775983, 4.377803853, 2.894428257,	2.116281809, 1.247392395, 0.705122146, 0.259743226, 0.168323336, 0.356195223, 0.497164551, 0])
# z = np.polyfit(xfit, yfit, 2)
# p = np.poly1d(z)
# plt.plot(xfit, p(xfit))
# for i in range(38, 46):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)

# plt.subplot(2,3,6)
# yfit = np.array([0.303844799, 1.136298578, 1.904667157, 4.00033541, 2.177002854, 1.93570507, 1.160930013, 0.745733681, 0.442602337, 0.792728525, 1.008779219, 0.277695006, 0])
# z = np.polyfit(xfit, yfit, 2)
# p = np.poly1d(z)
# plt.plot(xfit, p(xfit))
# for i in range(46, 48):
#     plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.0001, 100)

# plt.show()

import numpy as np
import matplotlib.pyplot as plt
r_v = np.array([0.00795932, 0.00834145, 0.00916391, 0.01012103, 0.01094719, 0.01156347,
                0.01201073, 0.01233946, 0.01259231, 0.01272005, 0.01277457, 0.0128138,
                0.01282152, 0.01276866, 0.01275641, 0.01271445, 0.01259701, 0.01257101, 
                0.01253504, 0.01244079, 0.01234598, 0.01225595, 0.01218528, 0.01208824,
                0.012006  , 0.01193989, 0.01187094, 0.01178279, 0.01164048, 0.01157002,
                0.01147927, 0.01137656, 0.01123797, 0.01115344, 0.01104343, 0.01091602,
                0.01082083, 0.01071659, 0.01059261, 0.01050636, 0.01035282, 0.01022662,
                0.01009368, 0.00996071, 0.00981971, 0.00966568, 0.00951928, 0.00937268,
                0.00922755, 0.00905923, 0.00889348, 0.00875662, 0.0085947 , 0.00844988,
                0.00828836, 0.00815106, 0.00799504, 0.00783897, 0.00769066, 0.00751245,
                0.00740258, 0.00723742, 0.00709034, 0.00694983, 0.00679389, 0.00665118,
                0.00650588, 0.00636644, 0.00623163, 0.00609366, 0.00596038, 0.00582618,
                0.00569361, 0.00556713, 0.00543496, 0.00531518, 0.00519611, 0.00507776,
                0.0049599 , 0.00484083, 0.00473045, 0.0046224 , 0.00451866, 0.00440542,
                0.00430106, 0.00419772, 0.00409659, 0.0039978 , 0.00390232, 0.00380928,
                0.00371389, 0.0036223 , 0.00352274, 0.00344611, 0.00336163, 0.00327541,
                0.00319424, 0.00311594, 0.0030348 , 0.0029635 , 0.00288393, 0.00280951,
                0.00273925, 0.00266299, 0.00260593, 0.00253742, 0.00247099, 0.00240895,
                0.00234859, 0.00228826, 0.00222931, 0.00217472, 0.0021197 , 0.00206732,
                0.00201422, 0.00196544, 0.00191807, 0.00186815, 0.00182319, 0.00177869,
                0.00173592, 0.00169371, 0.0016535 , 0.00162094, 0.00158171, 0.00153165,
                0.00150191, 0.00146796, 0.00143581, 0.00140351, 0.0013719 , 0.00134195,
                0.00131325, 0.00128538, 0.00125781, 0.00123191, 0.00120588, 0.00118187,
                0.0011601 , 0.00113603, 0.00111312, 0.00109304, 0.00107178, 0.00105247,
                0.00103279, 0.00101484, 0.00099618, 0.0009799 , 0.00096395, 0.00094745,
                0.00093222, 0.00091737, 0.00090263, 0.00088915, 0.00087544, 0.00086253,
                0.00084642, 0.00083849, 0.0008266 , 0.00081457, 0.000804  , 0.00079296,
                0.00078251, 0.000772  , 0.00076232, 0.00075333, 0.00074347, 0.00073604,
                0.00072344, 0.00071617, 0.00070824, 0.00069977, 0.00069117, 0.00068301,
                0.00067572, 0.00066725, 0.00066075, 0.00065241, 0.00064554, 0.0006381,
                0.0006309 , 0.00062432, 0.00061668, 0.00061016, 0.00060325, 0.00059695
                , 0.0005904 , 0.0005804 , 0.00057983, 0.00057163, 0.00056577, 0.00055945,
                0.00055314, 0.00054731, 0.00054111, 0.0005357 , 0.00052992, 0.00052506,
                0.0005188 , 0.00051353, 0.00050874, 0.00050322, 0.00049779, 0.00049299,
                0.00048821, 0.00048271, 0.00047842, 0.0004735 , 0.00046907, 0.00046448,
                0.00046055, 0.00045572, 0.00045126, 0.00044749, 0.00044271, 0.00043875,
                0.00043531, 0.00043084, 0.00042692, 0.00042354, 0.00041816, 0.00041601,
                0.00041259, 0.00040905, 0.00040562, 0.00040227, 0.000399  , 0.0003961,
                0.00039269, 0.00038989, 0.00038662, 0.00038328, 0.00038159, 0.00037802
                , 0.00037518, 0.00037247, 0.00036994, 0.00036696, 0.00036457, 0.00036209,
                0.00035959, 0.00035725, 0.00035466, 0.0003524 , 0.00035012, 0.00034795,
                0.00034572, 0.00034346, 0.0003414 , 0.00033926, 0.00033715, 0.00033686,
                0.00033404, 0.00032997, 0.00032846, 0.00032721, 0.00032545, 0.00032353,
                0.00032172, 0.0003198 , 0.00031826, 0.00031644, 0.00031459, 0.00031295,
                0.00031129, 0.00030961, 0.00030799, 0.00030631, 0.00030489, 0.00030332,
                0.0003017 , 0.00030032, 0.00029867, 0.00029717, 0.00029566, 0.00029418,
                0.00029279, 0.00029137, 0.00029027, 0.00028851, 0.00028712, 0.00028597,
                0.00028444, 0.00028314, 0.00028116, 0.00028067, 0.00027917, 0.00027789,
                0.00027672, 0.00027545, 0.00027411, 0.00027285, 0.00027173, 0.00027049,
                0.0002693 , 0.0002682 , 0.00026677, 0.00026584, 0.0002647 , 0.00026352,
                0.00026244, 0.00026138, 0.00026021, 0.00025919, 0.00025801, 0.0002571,
                0.000256  , 0.00025499, 0.000254  , 0.00025299, 0.00025193, 0.00025087
                , 0.00024991, 0.00024899, 0.00024807, 0.00024593, 0.00024645, 0.0002453,
                0.00024486, 0.00024346, 0.00024257, 0.00024168])

scales = np.array([0.06824578, 0.09099437, 0.11374296, 0.13649156, 0.15924015,0.18198874,
                    0.20473733, 0.22748593, 0.25023452, 0.27298311, 0.2957317 , 0.3184803
                    , 0.34122889, 0.36397748, 0.38672607, 0.40947467, 0.43222326, 0.45497185,
                    0.47772044, 0.50046904, 0.52321763, 0.54596622, 0.56871482, 0.59146341,
                    0.614212  , 0.63696059, 0.65970919, 0.68245778, 0.70520637, 0.72795496,
                    0.75070356, 0.77345215, 0.79620074, 0.81894933, 0.84169793, 0.86444652,
                    0.88719511, 0.9099437 , 0.9326923 , 0.95544089, 0.97818948, 1.00093808,
                    1.02368667, 1.04643526, 1.06918385, 1.09193245, 1.11468104, 1.13742963,
                    1.16017822, 1.18292682, 1.20567541, 1.228424  , 1.25117259, 1.27392119,
                    1.29666978, 1.31941837, 1.34216696, 1.36491556, 1.38766415, 1.41041274,
                    1.43316133, 1.45590993, 1.47865852, 1.50140711, 1.52415571, 1.5469043
                    , 1.56965289, 1.59240148, 1.61515008, 1.63789867, 1.66064726, 1.68339585,
                    1.70614445, 1.72889304, 1.75164163, 1.77439022, 1.79713882, 1.81988741,
                    1.842636  , 1.86538459, 1.88813319, 1.91088178, 1.93363037, 1.95637896,
                    1.97912756, 2.00187615, 2.02462474, 2.04737334, 2.07012193, 2.09287052,
                    2.11561911, 2.13836771, 2.1611163 , 2.18386489, 2.20661348, 2.22936208,
                    2.25211067, 2.27485926, 2.29760785, 2.32035645, 2.34310504, 2.36585363,
                    2.38860222, 2.41135082, 2.43409941, 2.456848  , 2.4795966 , 2.50234519,
                    2.52509378, 2.54784237, 2.57059097, 2.59333956, 2.61608815, 2.63883674,
                    2.66158534, 2.68433393, 2.70708252, 2.72983111, 2.75257971, 2.7753283
                    , 2.79807689, 2.82082548, 2.84357408, 2.86632267, 2.88907126, 2.91181985,
                    2.93456845, 2.95731704, 2.98006563, 3.00281423, 3.02556282, 3.04831141,
                    3.07106   , 3.0938086 , 3.11655719, 3.13930578, 3.16205437, 3.18480297,
                    3.20755156, 3.23030015, 3.25304874, 3.27579734, 3.29854593, 3.32129452,
                    3.34404311, 3.36679171, 3.3895403 , 3.41228889, 3.43503748, 3.45778608,
                    3.48053467, 3.50328326, 3.52603186, 3.54878045, 3.57152904, 3.59427763,
                    3.61702623, 3.63977482, 3.66252341, 3.685272  , 3.7080206 , 3.73076919,
                    3.75351778, 3.77626637, 3.79901497, 3.82176356, 3.84451215, 3.86726074,
                    3.89000934, 3.91275793, 3.93550652, 3.95825512, 3.98100371, 4.0037523
                    , 4.02650089, 4.04924949, 4.07199808, 4.09474667, 4.11749526, 4.14024386,
                    4.16299245, 4.18574104, 4.20848963, 4.23123823, 4.25398682, 4.27673541,
                    4.299484  , 4.3222326 , 4.34498119, 4.36772978, 4.39047837, 4.41322697,
                    4.43597556, 4.45872415, 4.48147275, 4.50422134, 4.52696993, 4.54971852,
                    4.57246712, 4.59521571, 4.6179643 , 4.64071289, 4.66346149, 4.68621008,
                    4.70895867, 4.73170726, 4.75445586, 4.77720445, 4.79995304, 4.82270163,
                    4.84545023, 4.86819882, 4.89094741, 4.913696  , 4.9364446 , 4.95919319,
                    4.98194178, 5.00469038, 5.02743897, 5.05018756, 5.07293615, 5.09568475,
                    5.11843334, 5.14118193, 5.16393052, 5.18667912, 5.20942771, 5.2321763
                    , 5.25492489, 5.27767349, 5.30042208, 5.32317067, 5.34591926, 5.36866786,
                    5.39141645, 5.41416504, 5.43691364, 5.45966223, 5.48241082, 5.50515941,
                    5.52790801, 5.5506566 , 5.57340519, 5.59615378, 5.61890238, 5.64165097,
                    5.66439956, 5.68714815, 5.70989675, 5.73264534, 5.75539393, 5.77814252,
                    5.80089112, 5.82363971, 5.8463883 , 5.86913689, 5.89188549, 5.91463408,
                    5.93738267, 5.96013127, 5.98287986, 6.00562845, 6.02837704, 6.05112564,
                    6.07387423, 6.09662282, 6.11937141, 6.14212001, 6.1648686 , 6.18761719,
                    6.21036578, 6.23311438, 6.25586297, 6.27861156, 6.30136015, 6.32410875,
                    6.34685734, 6.36960593, 6.39235452, 6.41510312, 6.43785171, 6.4606003
                    , 6.4833489 , 6.50609749, 6.52884608, 6.55159467, 6.57434327, 6.59709186,
                    6.61984045, 6.64258904, 6.66533764, 6.68808623, 6.71083482, 6.73358341,
                    6.75633201, 6.7790806 , 6.80182919, 6.82457778, 6.84732638, 6.87007497,
                    6.89282356, 6.91557216, 6.93832075, 6.96106934, 6.98381793, 7.00656653,
                    7.02931512, 7.05206371, 7.0748123 , 7.0975609 , 7.12030949, 7.14305808,
                    7.16580667, 7.18855527, 7.21130386, 7.23405245, 7.25680104, 7.27954964,
                    7.30229823, 7.32504682, 7.34779541, 7.37054401])

plt.subplot(2,1,1)
plt.plot(scales, r_v)
plt.xlabel('Grain size (mm)')
plt.ylabel('pdf(Grain Size)')
plt.xlim(0,8)
plt.ylim(0, 0.01350)

plt.vlines(0.063, 0, 0.008, colors ="k")
plt.vlines(0.125, 0, 0.009642, colors ="k")
plt.vlines(0.180, 0, 0.011513, colors ="k")
plt.vlines(0.250, 0, 0.012598, colors ="k")
plt.vlines(0.300, 0, 0.012786, colors ="k")
plt.vlines(0.355, 0, 0.012793, colors ="k")
plt.vlines(0.425, 0, 0.012644, colors ="k")
plt.vlines(0.500, 0, 0.012441, colors ="k")
plt.vlines(0.710, 0, 0.011634, colors ="k")
plt.vlines(1, 0, 0.010233, colors ="k")
plt.vlines(2, 0, 0.004212, colors ="k")
plt.vlines(4, 0, 0.000687, colors ="k")
plt.vlines(8, 0, 0.00025, colors ="k")

a = (scales)
minSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
maxSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8, 12])

_, length = np.shape(np.where((a>0.180)&(a<0.250)))

a = (np.interp([np.linspace(0.180, 0.250, 101)], (scales), r_v)[0])

plt.subplot(2,3,4)
a = (np.interp([np.linspace(0.180, 0.250, 1001)], (scales), r_v)[0])
plt.plot(a)
plt.plot(np.arange(0,1001), a, color='red')
plt.xticks([0,1000], ["0.180", "0.250"])
for i in range(1001):
    plt.vlines(i, 0, (a[i]), alpha=0.25,color='red')
plt.fill_between(np.arange(0,1001), a, alpha=0.1, color='red')
plt.ylim([0, 0.0128])
plt.xlim([0, 1000])
percentage = round(((np.trapz(np.interp([np.linspace(0.180, 0.250, 1000)], (scales), r_v)[0])*length/1000))*100, 2)
plt.text(675, 0.00175, f'Area: {percentage}%', fontsize = 15, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel('Grain size (mm)', fontsize=15)
plt.ylabel('pdf(Grain size)', fontsize=15)


a = (scales)
_, length = np.shape(np.where((a>0.710)&(a<1)))
a = (np.interp([np.linspace(0.710, 1, 101)], (scales), r_v)[0])


plt.subplot(2,3,5)
a = (np.interp([np.linspace(0.710, 1, 1001)], (scales), r_v)[0])
plt.plot(a)
plt.plot(np.arange(0,1001), a, color='red')
plt.xticks([0,1000], ["0.710", "1"])
for i in range(1001):
    plt.vlines(i, 0, (a[i]), alpha=0.25,color='red')
plt.fill_between(np.arange(0,1001), a, alpha=0.1, color='red')
plt.ylim([0, 0.0128])
plt.xlim([0, 1000])
percentage = round(((np.trapz(np.interp([np.linspace(0.710, 1, 1000)], (scales), r_v)[0])*length/1000))*100, 2)
plt.text(650, 0.00175, f'Area: {percentage}%', fontsize = 15, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel('Grain size (mm)', fontsize=15)
plt.ylabel('pdf(Grain size)', fontsize=15)

a = (scales)
_, length = np.shape(np.where((a>2)&(a<4)))
a = (np.interp([np.linspace(2, 4, 101)], (scales), r_v)[0])

plt.subplot(2,3,6)
a = (np.interp([np.linspace(2, 4, 1001)], (scales), r_v)[0])
plt.plot(a)
plt.plot(np.arange(0,1001), a, color='red')
plt.xticks([0,1000], ["2", "4"])
for i in range(1001):
    plt.vlines(i, 0, (a[i]), alpha=0.25,color='red')
plt.fill_between(np.arange(0,1001), a, alpha=0.1, color='red')
plt.ylim([0, 0.0128])
plt.xlim([0, 1000])
percentage = round(((np.trapz(np.interp([np.linspace(2, 4, 1000)], (scales), r_v)[0])*length/1000))*100, 2)
plt.text(650, 0.00175, f'Area: {percentage}%', fontsize = 15, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel('Grain size (mm)', fontsize=15)
plt.ylabel('pdf(Grain size)', fontsize=15)
plt.show()