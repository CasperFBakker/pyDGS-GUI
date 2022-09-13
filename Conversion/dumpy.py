import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data_Prof = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22//Proffitt Percentile/Percentiles_Location_1.csv')) #Proffitt_test/
data_Sieve = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentile/Percentiles_Sieve.csv'))


GrainSize = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.250, 0.18, 0.125, 0.063]
locations = [1, 2, 3, 4,6, 7]
for j in range(len(locations)):
    data_Prof =  np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Proffitt Percentile/Proffitt_test/Percentiles_Location_' + str(locations[j]) + '.csv'))
    for i in range(len(data_Prof)):
        plt.subplot(2,3,int(j+1))
        plt.scatter(GrainSize, (data_Sieve[j,1:]/(data_Prof[i,1:14])), label=data_Prof[i,14])
        plt.xscale("log")
        plt.yscale("log")
        plt.grid(which='major', linewidth=2, linestyle='-')
        plt.grid(which='minor', linewidth=1, linestyle='--')
        plt.ylim(0.0001, 100)
        plt.legend()


# test = np.mean(np.vstack(data_Prof[:,1:]), axis=0)
# print(test)
# popt, pcov = curve_fit(lambda fx,a,b: a*fx**b,  GrainSize[7:14],  (data_Sieve[0,8:14]/(test[7:14])))
# power_y = popt[0]*GrainSize[7:14]**popt[1]

# plt.plot(GrainSize[7:14], power_y, label=str(popt[0]) + 'x**' + str(-popt[1]) )

# for i in range(len(data_Prof)):
#     plt.scatter(GrainSize, (data_Sieve[0,1:]/(data_Prof[i,1:14])), label=data_Prof[i,0])
    
# plt.xscale("log")
# plt.yscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.ylim(0.01, 10)
# plt.legend()

plt.show()








##############################################################################################################################################################################




plt.subplot(3,3,(1,3))
for i in range(1, 14):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend()

plt.subplot(3,3,4)
for i in range(14, 22):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend()

plt.subplot(3,3,5)
for i in range(22, 26):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend()

plt.subplot(3,3,6)
for i in range(26, 34):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend()

plt.subplot(3,3,7)
for i in range(34, 38):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend()

plt.subplot(3,3,8)
for i in range(38, 46):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend()

plt.subplot(3,3,9)
for i in range(46, 48):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend()

plt.show()

##############################################################################################################################################################################

xfit = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
yfit = np.array([0.208307862, 1.031856376, 2.142537041, 3.388183378, 2.571073162, 2.308543947, 1.495428404, 1.42181968, 0.811075903, 0.533655452, 0.561671272,0.541487501, 0])


z = np.polyfit(xfit, yfit, 8)
p = np.poly1d(z)
print(p)
plt.plot(xfit, p(xfit))

for i in range(len(data)):
    plt.scatter(GrainSize, data[i,1:15], label=data[i,15])

plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)
plt.legend(loc='lower right')


plt.show()

##############################################################################################################################################################################


plt.subplot(2,3,1)
yfit = np.array([0.176626657, 1.149030204, 1.746586149, 2.215164335, 1.781314253, 2.286232085, 1.607402283, 2.44237334, 1.538243408, 0.590077708, 0.359543279, 0.218923259, 0])
z = np.polyfit(xfit, yfit, 1)
p = np.poly1d(z)
plt.plot(xfit, p(xfit))
for i in range(1, 14):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)


plt.subplot(2,3,2)
yfit = np.array([0.00889454, 0.230734461, 1.648808468, 4.599172591, 4.049283888, 3.195208036, 1.788540941, 1.368561054, 0.462574893, 0.353190373, 0.439846551, 0.451551121, 0])
z = np.polyfit(xfit, yfit, 1)
p = np.poly1d(z)
plt.plot(xfit, p(xfit))
for i in range(14, 22):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)


plt.subplot(2,3,3)
yfit = np.array([0.16589751, 1.157312251, 1.880347959, 4.077461111, 2.068472567, 2.250635769, 0.81612999, 0.62415191, 0.369584838, 0.41590902, 0.570582606, 1.193496832, 0])
z = np.polyfit(xfit, yfit, 2)
p = np.poly1d(z)
plt.plot(xfit, p(xfit))
for i in range(22, 26):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)


plt.subplot(2,3,4)
yfit = np.array([0.019167218, 0.25233682, 0.997561335, 2.460717724, 2.179598949, 2.210662032, 1.416211902, 1.181008823, 0.7737245, 0.871518857, 0.956430865, 0.919591828, 0])
z = np.polyfit(xfit, yfit, 2)
p = np.poly1d(z)
plt.plot(xfit, p(xfit))
for i in range(26, 34):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)


plt.subplot(2,3,5)
yfit = np.array([0.451262702, 1.908525304, 4.148775983, 4.377803853, 2.894428257,	2.116281809, 1.247392395, 0.705122146, 0.259743226, 0.168323336, 0.356195223, 0.497164551, 0])
z = np.polyfit(xfit, yfit, 2)
p = np.poly1d(z)
plt.plot(xfit, p(xfit))
for i in range(38, 46):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)

plt.subplot(2,3,6)
yfit = np.array([0.303844799, 1.136298578, 1.904667157, 4.00033541, 2.177002854, 1.93570507, 1.160930013, 0.745733681, 0.442602337, 0.792728525, 1.008779219, 0.277695006, 0])
z = np.polyfit(xfit, yfit, 2)
p = np.poly1d(z)
plt.plot(xfit, p(xfit))
for i in range(46, 48):
    plt.scatter(GrainSize, data[i, 1:15], label=data[i,15])
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.ylim(0.0001, 100)

plt.show()