import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def DMS_2_DD(DMS):

    D = DMS[0:DMS.find('°')]
    M = DMS[DMS.find('°')+1:DMS.find("'")]
    S = DMS[DMS.find("'")+1:DMS.find('"')]
    DD = float(D) + float(M)/60 + float(S)/3600

    return DD


R1 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R1.csv'))
R2 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R2.csv'))
R3 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R3.csv'))
R5 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R5.csv'))
R7 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R7.csv'))
R8 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R8.csv'))
R9 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R9.csv'))
R10 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_R10.csv'))

T1 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_Test_1.csv'))
T2 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_Test_2.csv'))
T3 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_Test_3.csv'))
T4 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_Test_4.csv'))
T5 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_Test_5.csv'))
T6 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/data_Test_6.csv'))

size = [0, len(R1), len(R2), len(R3), len(R5), len(R7), len(R8), len(R9), len(R10), len(T1), len(T2), len(T3), len(T4), len(T5), len(T6)]
size = np.cumsum(size)

dic = {"R1": R1, "R2": R2, "R3": R3, "R5": R5, "R7": R7, "R8": R8, "R9": R9, "R10": R10, "T1": T1, "T2": T2, "T3": T3, "T4": T4, "T5": T5, "T6": T6}

Lat = []; Lon = []
for Line in ['R1', 'R2', 'R3', 'R5', 'R7', 'R8', 'R9', 'R10', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6']:
    data = dic[Line]
    for row, value in enumerate(data):
        Lat.append(DMS_2_DD(data[row,4]))
        Lon.append(DMS_2_DD(data[row,5]))
        

plt.scatter(Lat[size[0]:size[1]], Lon[size[0]:size[1]], label='R1',  color='darkorange')
plt.scatter(Lat[size[1]:size[2]], Lon[size[1]:size[2]], label='R2',  color='tan')
plt.scatter(Lat[size[2]:size[3]], Lon[size[2]:size[3]], label='R3',  color='burlywood')
plt.scatter(Lat[size[3]:size[4]], Lon[size[3]:size[4]], label='R5',  color='navajowhite')
plt.scatter(Lat[size[4]:size[5]], Lon[size[4]:size[5]], label='R7',  color='moccasin')
plt.scatter(Lat[size[5]:size[6]], Lon[size[5]:size[6]], label='R8',  color='wheat')
plt.scatter(Lat[size[6]:size[7]], Lon[size[6]:size[7]], label='R9',  color='papayawhip')
plt.scatter(Lat[size[7]:size[8]], Lon[size[7]:size[8]], label='R10', color='oldlace')

plt.scatter(Lat[size[8]:size[9]],   Lon[size[8]:size[9]],   label='T1', color='dimgray')
plt.scatter(Lat[size[9]:size[10]],  Lon[size[9]:size[10]],  label='T2', color='gray')
plt.scatter(Lat[size[10]:size[11]], Lon[size[10]:size[11]], label='T3', color='darkgray')
plt.scatter(Lat[size[11]:size[12]], Lon[size[11]:size[12]], label='T4', color='silver')
plt.scatter(Lat[size[12]:size[13]], Lon[size[12]:size[13]], label='T5', color='lightgray')
plt.scatter(Lat[size[13]:size[14]], Lon[size[13]:size[14]], label='T6', color='gainsboro')

plt.legend()
plt.xlabel('Latitude (DD)', fontsize=18)
plt.ylabel('Longitude (DD)', fontsize=18)
plt.title('Field-day 26/10/22', fontsize=22)
plt.show()

