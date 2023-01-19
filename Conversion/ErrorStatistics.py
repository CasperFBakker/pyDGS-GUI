import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def RMSE(Sieve_vals, DGS_vals):

    diffrnce = np.subtract(Sieve_vals, DGS_vals)
    sqre_err = np.square(diffrnce)
    rslt_meansqre_err = sqre_err.mean()
    root_meansqre_err = math.sqrt(rslt_meansqre_err)
    return root_meansqre_err

def MAE(Sieve_vals, DGS_vals):
    diffrnce = np.abs(np.subtract(Sieve_vals, DGS_vals))
    meanAbsErr = diffrnce.mean()
    return meanAbsErr


dgs_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Statistics/Statistics_Stats_GrainShape_Sort.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Sieve/Statistics/Statistics_Sieve_Sort.csv'))


plt.subplot(2,3,1)
plt.scatter(sieve_data[:,2], dgs_data[:,2])
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.15,0.50); plt.ylim(0.15,0.50); 
print('D10: ', ((RMSE(sieve_data[:,2], dgs_data[:,2]))))
print('D10: ', ((RMSE(sieve_data[:,2], dgs_data[:,2]))/(max(sieve_data[:,2]) - min(sieve_data[:,2]))*100))
print('D10: ', ((MAE(sieve_data[:,2], dgs_data[:,2]))))
print('D10: ', ((MAE(sieve_data[:,2], dgs_data[:,2]))/(max(sieve_data[:,2]) - min(sieve_data[:,2]))*100))
plt.title('10th', fontsize=16)

plt.subplot(2,3,2)
plt.scatter(sieve_data[:,3], dgs_data[:,3])
print('D16: ', ((RMSE(sieve_data[:,3], dgs_data[:,3]))))
print('D16: ', ((RMSE(sieve_data[:,3], dgs_data[:,3]))/(max(sieve_data[:,3]) - min(sieve_data[:,3]))*100))
print('D16: ', ((MAE(sieve_data[:,3], dgs_data[:,3]))))
print('D16: ', ((MAE(sieve_data[:,3], dgs_data[:,3]))/(max(sieve_data[:,3]) - min(sieve_data[:,3]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.20,0.55); plt.ylim(0.20,0.55); 
plt.title('16th', fontsize=16)

plt.subplot(2,3,3)
plt.scatter(sieve_data[:,4], dgs_data[:,4])
print('D25: ', ((RMSE(sieve_data[:,4], dgs_data[:,4]))))
print('D25: ', ((RMSE(sieve_data[:,4], dgs_data[:,4]))/(max(sieve_data[:,4]) - min(sieve_data[:,4]))*100))
print('D25: ', ((MAE(sieve_data[:,4], dgs_data[:,4]))))
print('D25: ', ((MAE(sieve_data[:,4], dgs_data[:,4]))/(max(sieve_data[:,4]) - min(sieve_data[:,4]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.25, 0.60); plt.ylim(0.25, 0.60)
plt.title('25th', fontsize=16)

plt.subplot(2,3,4)
plt.scatter(sieve_data[:,6], dgs_data[:,6])
print('D50: ', ((RMSE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]))))
print('D50: ', ((RMSE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]) - min(sieve_data[:,6]))*100))
print('D50: ', ((MAE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]))))
print('D50: ', ((MAE(sieve_data[:,6], dgs_data[:,6]))/(max(sieve_data[:,6]) - min(sieve_data[:,6]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.35, 1.5); plt.ylim(0.35, 1.5)
plt.title('50th', fontsize=16)
plt.xlabel('Measured (mm)', fontsize=18); plt.ylabel('Estimated (mm)', fontsize=18)

plt.subplot(2,3,5)
plt.scatter(sieve_data[:,8], dgs_data[:,8])
print('D84: ', ((RMSE(sieve_data[:,8], dgs_data[:,8]))))
print('D84: ', ((RMSE(sieve_data[:,8], dgs_data[:,8]))/(max(sieve_data[:,8]) - min(sieve_data[:,8]))*100))
print('D84: ', ((MAE(sieve_data[:,8], dgs_data[:,8]))))
print('D84: ', ((MAE(sieve_data[:,8], dgs_data[:,8]))/(max(sieve_data[:,8]) - min(sieve_data[:,8]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.6, 4.5); plt.ylim(0.6, 4.5)
plt.title('84th', fontsize=16)

plt.subplot(2,3,6)
plt.scatter(sieve_data[:,9], dgs_data[:,9])
print('D90: ', ((RMSE(sieve_data[:,9], dgs_data[:,9]))))
print('D90: ', ((RMSE(sieve_data[:,9], dgs_data[:,9]))/(max(sieve_data[:,9]) - min(sieve_data[:,9]))*100))
print('D90: ', ((MAE(sieve_data[:,9], dgs_data[:,9]))))
print('D90: ', ((MAE(sieve_data[:,9], dgs_data[:,9]))/(max(sieve_data[:,9]) - min(sieve_data[:,9]))*100))
plt.plot(np.arange(0,100), color='k', linestyle='--')
plt.xlim(0.95, 7); plt.ylim(0.95, 7)
plt.title('90th', fontsize=16)

plt.show()