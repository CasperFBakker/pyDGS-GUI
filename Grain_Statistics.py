import numpy as np
import pandas as pd
import os

def Store_Stats(path_of_the_directory, Image_Name, Percentile):          

        data = Image_Name, Percentile[0], Percentile[1], Percentile[2], Percentile[3], Percentile[4], Percentile[5], Percentile[6], Percentile[7], Percentile[8], Percentile[9] 
        columns = ['Image name', 'D5', 'D10', 'D16', 'D25', 'D30', 'D50', 'D75', 'D84', 'D90', 'D95']
                
        temp = pd.DataFrame([data], columns=columns)
        temp.to_csv('Output data/temp_stats.csv', index=False)

        try: 
            DF = pd.read_csv(Output_Dir + "Statistics_" + dir_name + ".csv")
            if Image_Name in DF.values:
                pass
            else:
                temp = pd.DataFrame([data], columns=columns)
                merged = pd.concat([temp, DF])
                merged.to_csv(Output_Dir + "Statistics_" + dir_name + ".csv", index=False)

        except FileNotFoundError:
            temp = pd.DataFrame([data], columns=[columns])
            temp.to_csv(Output_Dir + "Statistics_" + dir_name + ".csv", index=False)


dir_name = 'Stats_Test.csv'
Output_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/'

ImageName = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Test.csv'))
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Test.csv', index_col=0), dtype='float64')
GrainSizeBins = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8], dtype='float64')

for i in range(len(data)):
    Percentile = np.interp([5, 10, 16, 25, 30, 50, 75, 84, 90, 95], data[i,:], GrainSizeBins)

    Store_Stats(Output_Dir, ImageName[i,0], Percentile)
