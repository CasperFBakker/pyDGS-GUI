import numpy as np
import pandas as pd
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


data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Sample_Photos/Filtered/Stats_Loc_7_MultiTrend.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Stats_Sieve.csv'))
for i in range(1, 11):
    test = [sieve_data[0,i] for j in range(len(data))]
    print(RMSE(test, data[1,i]))
    print(MAE(test, data[:,i]))
print('\n')

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Sample_Photos/Filtered/Stats_Loc_7_MultiTrend_Sub4.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Stats_Sieve.csv'))
for i in range(1, 11):
    test = [sieve_data[0,i] for j in range(len(data))]
    print(RMSE(test, data[1,i]))
    print(MAE(test, data[:,i]))
print('\n') 
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Sample_Photos/Filtered/Stats_Loc_7_AllTrend.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/08_07_22/Stats_Sieve.csv'))
for i in range(1, 11):
    test = [sieve_data[0,i] for j in range(len(data))]
    print(RMSE(test, data[1,i]))
    print(MAE(test, data[:,i]))