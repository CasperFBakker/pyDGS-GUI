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


data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Location_1/Stats_Loc_1.csv'))
sieve_data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Stats_Sieve.csv'))

for i in range(len(data)):
    print(data[i, 0])
    print(RMSE(sieve_data[0,1:11], data[i, 1:11]))
    print(MAE(sieve_data[0,1:11], data[i, 1:11]))
    print('\n')