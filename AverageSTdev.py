import numpy as np 
import pandas as pd
import math
import os

import os
import glob
import pandas as pd


df = pd.read_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Uncorrected/UncorrectedPercentage_21_04_23_Transf.csv')

Average = df.groupby(np.arange(len(df))//16).mean()
Average.to_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Uncorrected/UncorrectedPercentage_21_04_23_MeanTransf.csv')

StDev = df.groupby(np.arange(len(df))//16).std()
StDev.to_csv('/home/casper/Documents/Python/pyDGS-GUI/Output data/21_04_23/Uncorrected/UncorrectedPercentage_21_04_23_StDevTransf.csv')