import numpy as np 
import pandas as pd
import math

df = pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Uncorrected_R10_Transf.csv')

Average = df.groupby(np.arange(len(df))//16).mean()
Average.to_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Uncorrected_R10Inb_MeanTransf.csv')

StDev = df.groupby(np.arange(len(df))//16).std()
StDev.to_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/26_10_22/Mobile/Uncorrected/Uncorrected_R10Inb_StDevTransf.csv')