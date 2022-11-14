import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns

data_R1 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R1.csv'))
data_R2 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R2.csv'))
data_R3 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R3.csv'))
data_R5 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R5.csv'))
data_R7 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R7.csv'))
data_R8 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R8.csv'))
data_R9 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R9.csv'))
data_R10 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R10.csv'))

Elevation = np.array([1,0.75,0.5, 0.25, 0])
Colors = ['r', 'darkorange', 'gold', 'yellow', 'lawngreen', 'green', 'cyan', 'blue']
index_lst = [1, 2, 3, 5, 6, 7, 8, 9]

plt.subplot(2,4,1)
for i in range(len(data_R1)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R1[i,index_lst[j]], color=Colors[j])
plt.title('R1')
plt.xlim(-0.05, 1.05)

plt.subplot(2,4,2)
for i in range(len(data_R2)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R2[i,index_lst[j]], color=Colors[j])
plt.title('R2')
plt.xlim(-0.05, 1.05)

plt.subplot(2,4,3)
for i in range(len(data_R3)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R3[i,index_lst[j]], color=Colors[j])
plt.title('R3')
plt.xlim(-0.05, 1.05)
plt.subplot(2,4,4)
for i in range(len(data_R5)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R5[i,index_lst[j]], color=Colors[j])
plt.title('R5')
plt.xlim(-0.05, 1.05)
plt.subplot(2,4,5)
for i in range(len(data_R7)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R7[i,index_lst[j]], color=Colors[j])
plt.title('R7')
plt.xlim(-0.05, 1.05)
plt.xlabel('Elevation (m)', fontsize=18)
plt.ylabel('Grain size (mm)', fontsize=18)
plt.subplot(2,4,6)
for i in range(len(data_R8)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R8[i,index_lst[j]], color=Colors[j])
plt.title('R8')
plt.xlim(-0.05, 1.05)
plt.subplot(2,4,7)
for i in range(len(data_R9)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R9[i,index_lst[j]], color=Colors[j])
plt.title('R9')
plt.xlim(-0.05, 1.05)
plt.subplot(2,4,8)
for i in range(len(data_R10)):
    for j in range(8):
        plt.scatter(Elevation[i], data_R10[i,index_lst[j]], color=Colors[j])
plt.title('R10')
plt.xlim(-0.05, 1.05)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.show()


D16_HeatMap = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/All_D16.csv', index_col=0))
D16_HeatMap[D16_HeatMap==0] = np.nan

plt.imshow(D16_HeatMap , cmap = 'coolwarm', interpolation=None)
plt.colorbar().set_label(label=r'D$_{16}$ (mm)', fontsize=15)
plt.xticks(np.arange(0,8,1), ['R1','R2','R3','R5','R7','R8','R9','R10'])
plt.yticks(np.arange(0,5,1), ['1', '0.75', '0.50', '0.25', '0'], rotation=0)
plt.title(r"D${16}$", fontsize=20)
plt.ylabel("Elevation (m)", fontsize=15)
plt.show()



D50_HeatMap = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/All_D50.csv', index_col=0))
D50_HeatMap[D50_HeatMap==0] = np.nan

plt.imshow(D50_HeatMap , cmap = 'coolwarm', interpolation=None)
plt.colorbar().set_label(label=r'D$_{50}$ (mm)', fontsize=15)
plt.xticks(np.arange(0,8,1), ['R1','R2','R3','R5','R7','R8','R9','R10'])
plt.yticks(np.arange(0,5,1), ['1', '0.75', '0.50', '0.25', '0'], rotation=0)
plt.title("Median Grain Size", fontsize=20)
plt.ylabel("Elevation (m)", fontsize=15)
plt.show()

D90_HeatMap = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/All_D90.csv', index_col=0))
D90_HeatMap[D90_HeatMap==0] = np.nan

plt.imshow(D90_HeatMap , cmap = 'coolwarm', interpolation=None)
plt.colorbar().set_label(label=r'D$_{90}$ (mm)', fontsize=15)
plt.xticks(np.arange(0,8,1), ['R1','R2','R3','R5','R7','R8','R9','R10'])
plt.yticks(np.arange(0,5,1), ['1', '0.75', '0.50', '0.25', '0'], rotation=0)
plt.title(r"D${90}$", fontsize=20)
plt.ylabel("Elevation (m)", fontsize=15)
plt.show()

data_Test2 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_Test_2.csv'))
x = np.arange(0,16,0.5)

for i in range(len(data_Test2)):
    plt.scatter(x[i], data_Test2[i,1], color='r')
    plt.scatter(x[i], data_Test2[i,2], color='darkorange')
    plt.scatter(x[i], data_Test2[i,3], color='gold')
    plt.scatter(x[i], data_Test2[i,5], color='yellow')
    plt.scatter(x[i], data_Test2[i,6], color='lawngreen')
    plt.scatter(x[i], data_Test2[i,7], color='green')
    plt.scatter(x[i], data_Test2[i,8], color='cyan')
    plt.scatter(x[i], data_Test2[i,9], color='blue')

plt.xlabel('Cross-shore distance (m)', fontsize=15)
plt.ylabel('Grain size (mm)', fontsize=15)
plt.title(r'High resolution ($\approx$ 0.5 m) Cross-shore line, Test 2', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.show()  



CrossShore = np.arange(0, 13, 1)
CrossShore_R10 = np.array([0,3,6,9,12])
CrossShore_R10_in = np.array([1,2,4,5,7,8,10,11])
data_R10_Inbetween = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R10_Inbetween.csv'))

plt.subplot(2,1,1)
for i in range(len(data_R10)):
    plt.scatter(CrossShore_R10[i], data_R10[i,1], color='r')
    plt.scatter(CrossShore_R10[i], data_R10[i,2], color='darkorange')
    plt.scatter(CrossShore_R10[i], data_R10[i,3], color='gold')
    plt.scatter(CrossShore_R10[i], data_R10[i,5], color='yellow')
    plt.scatter(CrossShore_R10[i], data_R10[i,6], color='lawngreen')
    plt.scatter(CrossShore_R10[i], data_R10[i,7], color='green')
    plt.scatter(CrossShore_R10[i], data_R10[i,8], color='cyan')
    plt.scatter(CrossShore_R10[i], data_R10[i,9], color='blue')

for i in range(len(data_R10_Inbetween)):
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,1], color='r')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,2], color='darkorange')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,3], color='gold')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,5], color='yellow')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,6], color='lawngreen')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,7], color='green')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,8], color='cyan')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,9], color='blue')

plt.xticks(np.arange(0,13,1), ['A','A_1','A_2','B','B_1','B_2','C','C_1','C_2','D','D_1','D_2','E'])
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.title('R10, inbetween', fontsize=20)
plt.subplot(2,1,2)
for i in range(len(data_R10)):
    plt.scatter(CrossShore_R10[i], data_R10[i,1], color='r')
    plt.scatter(CrossShore_R10[i], data_R10[i,2], color='darkorange')
    plt.scatter(CrossShore_R10[i], data_R10[i,3], color='gold')
    plt.scatter(CrossShore_R10[i], data_R10[i,5], color='yellow')
    plt.scatter(CrossShore_R10[i], data_R10[i,6], color='lawngreen')
    plt.scatter(CrossShore_R10[i], data_R10[i,7], color='green')
    plt.scatter(CrossShore_R10[i], data_R10[i,8], color='cyan')
    plt.scatter(CrossShore_R10[i], data_R10[i,9], color='blue')
plt.plot(CrossShore_R10, data_R10[:,1], color='r')
plt.plot(CrossShore_R10, data_R10[:,2], color='darkorange')
plt.plot(CrossShore_R10, data_R10[:,3], color='gold')
plt.plot(CrossShore_R10, data_R10[:,5], color='yellow')
plt.plot(CrossShore_R10, data_R10[:,6], color='lawngreen')
plt.plot(CrossShore_R10, data_R10[:,7], color='green')
plt.plot(CrossShore_R10, data_R10[:,8], color='cyan')
plt.plot(CrossShore_R10, data_R10[:,9], color='blue')
for i in range(len(data_R10_Inbetween)):
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,1], color='r')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,2], color='darkorange')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,3], color='gold')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,5], color='yellow')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,6], color='lawngreen')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,7], color='green')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,8], color='cyan')
    plt.scatter(CrossShore_R10_in[i], data_R10_Inbetween[i,9], color='blue')

plt.xticks(np.arange(0,13,1), ['A','A_1','A_2','B','B_1','B_2','C','C_1','C_2','D','D_1','D_2','E'])
plt.ylabel('Grain size (mm)', fontsize=20)
plt.show()  

# import seaborn as sns

# dataCanon =  np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Canon/Statistics_AVG/Statistics_All.csv'))
# dataMobile = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_All.csv'))
# x = []; y = []
# for i in range(len(dataCanon)):
#     x.append(dataMobile[i,1:])
#     y.append(dataCanon[i,1:])

# x = np.squeeze(np.reshape(np.array(x), [1,330]))
# y = np.squeeze(np.reshape(np.array(y), [1,330]))
# x = np.array(x, dtype='float64')
# y = np.array(y, dtype='float64')
# # ax = sns.lineplot(x, y, ci=50)
# ax = sns.regplot(x, y, ci=80)
# plt.plot(np.arange(0,6,1), linestyle='--', color='k')
# plt.xlabel('Grain size from mobile phone camera (mm)', fontsize=18)
# plt.ylabel('Grain size from photo camera (mm)', fontsize=18)
# plt.xlim(0,5); plt.ylim(0,5)
# plt.show()


data_R5_Inbetween = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R5_Inbetween.csv'))
data_R5 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R5.csv'))
R5_Cross = np.array([0,4,7])
R5InbetweenCross = np.array([1,2,3,5,6]) 
plt.subplot(2,1,1)

for i in range(len(data_R5)):
    for j in range(8):
        plt.scatter(R5_Cross[i], data_R5[i,index_lst[j]], color=Colors[j])
for i in range(len(data_R5_Inbetween)):
    for j in range(8):
        plt.scatter(R5InbetweenCross[i], data_R5_Inbetween[i,index_lst[j]], color=Colors[j])

plt.xticks([0,1,2,3,4,5,6,7], ['A', 'A_1', 'A_2', 'A_3', 'B', 'B_1', 'B_2', 'C'])
plt.title('R5, inbetween', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")

plt.subplot(2,1,2)

for i in range(len(data_R5)):
    for j in range(8):
        plt.scatter(R5_Cross[i], data_R5[i,index_lst[j]], color=Colors[j])

for i in range(len(data_R5)):
    for j in range(len(index_lst)):
        plt.plot(R5_Cross, data_R5[:,index_lst[j]], color=Colors[j])

for i in range(len(data_R5_Inbetween)):
    for j in range(8):
        plt.scatter(R5InbetweenCross[i], data_R5_Inbetween[i,index_lst[j]], color=Colors[j])

plt.xticks([0,1,2,3,4,5,6,7], ['A', 'A_1', 'A_2', 'A_3', 'B', 'B_1', 'B_2', 'C'])
plt.ylabel('Grain size (mm)', fontsize=20)
plt.show()  



data_R3_Inbetween = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R3_Inbetween.csv'))
data_R3 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_R3.csv'))
R3_Cross = np.array([0,5,9])
R3InbetweenCross = np.array([1,2,3,4,6,7,8]) 
plt.subplot(2,1,1)

for i in range(len(data_R3)):
    for j in range(8):
        plt.scatter(R3_Cross[i], data_R3[i,index_lst[j]], color=Colors[j])
for i in range(len(data_R3_Inbetween)):
    for j in range(8):
        plt.scatter(R3InbetweenCross[i], data_R3_Inbetween[i,index_lst[j]], color=Colors[j])

plt.xticks([0,1,2,3,4,5,6,7,8,9], ['A', 'A_1', 'A_2', 'A_3', 'A_4', 'B', 'B_1', 'B_2', 'B_3', 'C'])
plt.title('R3, inbetween', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")

plt.subplot(2,1,2)

for i in range(len(data_R3)):
    for j in range(8):
        plt.scatter(R3_Cross[i], data_R3[i,index_lst[j]], color=Colors[j])

for i in range(len(data_R3)):
    for j in range(len(index_lst)):
        plt.plot(R3_Cross, data_R3[:,index_lst[j]], color=Colors[j])

for i in range(len(data_R3_Inbetween)):
    for j in range(8):
        plt.scatter(R3InbetweenCross[i], data_R3_Inbetween[i,index_lst[j]], color=Colors[j])

plt.xticks([0,1,2,3,4,5,6,7,8,9], ['A', 'A_1', 'A_2', 'A_3', 'A_4', 'B', 'B_1', 'B_2', 'B_3', 'C'])
plt.ylabel('Grain size (mm)', fontsize=20)
plt.show()  


data_Test3 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_Test_3.csv'))
x = np.arange(0,14)
Colors = ['r', 'darkorange', 'gold', 'yellow', 'lawngreen', 'green', 'cyan', 'blue']
index_lst = [1, 2, 3, 5, 6, 7, 8, 9]

for i in range(len(data_Test3)):
    for j in range(len(index_lst)):
        plt.scatter(x[i], data_Test3[i,index_lst[j]], color=Colors[j])

plt.xlabel('Cross-shore distance (m)', fontsize=15)
plt.ylabel('Grain size (mm)', fontsize=15)
plt.title(r'High resolution ($\approx$1 m) Cross-shore line, Test 3', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.show()  


data_Test4 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_Test_4.csv'))
x = np.arange(0,18)
Colors = ['r', 'darkorange', 'gold', 'yellow', 'lawngreen', 'green', 'cyan', 'blue']
index_lst = [1, 2, 3, 5, 6, 7, 8, 9]

for i in range(len(data_Test4)):
    for j in range(len(index_lst)):
        plt.scatter(x[i], data_Test4[i,index_lst[j]], color=Colors[j])

plt.xlabel('Cross-shore distance (m)', fontsize=15)
plt.ylabel('Grain size (mm)', fontsize=15)
plt.title(r'High resolution ($\approx$1 m) Cross-shore line, Test 4', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.show()  

data_Test5 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_Test_5.csv'))
x = np.arange(0,13)
Colors = ['r', 'darkorange', 'gold', 'yellow', 'lawngreen', 'green', 'cyan', 'blue']
index_lst = [1, 2, 3, 5, 6, 7, 8, 9]

for i in range(len(data_Test5)):
    for j in range(len(index_lst)):
        plt.scatter(x[i], data_Test5[i,index_lst[j]], color=Colors[j])

plt.xlabel('Cross-shore distance (m)', fontsize=15)
plt.ylabel('Grain size (mm)', fontsize=15)
plt.title(r'High resolution ($\approx$1 m) Cross-shore line, Test 5', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.show()  

data_Test6 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_Test_6.csv'))
x = np.arange(0,11)
Colors = ['r', 'darkorange', 'gold', 'yellow', 'lawngreen', 'green', 'cyan', 'blue']
index_lst = [1, 2, 3, 5, 6, 7, 8, 9]

for i in range(len(data_Test6)):
    for j in range(len(index_lst)):
        plt.scatter(x[i], data_Test6[i,index_lst[j]], color=Colors[j])

plt.xlabel('Cross-shore distance (m)', fontsize=15)
plt.ylabel('Grain size (mm)', fontsize=15)
plt.title(r'High resolution ($\approx$1 m) Cross-shore line, Test 6', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.show()  

data_Test1 = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/Statistics_Test_1.csv'))
x = np.arange(0,16)
Colors = ['r', 'darkorange', 'gold', 'yellow', 'lawngreen', 'green', 'cyan', 'blue']
index_lst = [1, 2, 3, 5, 6, 7, 8, 9]

for i in range(len(data_Test1)):
    for j in range(len(index_lst)):
        plt.scatter(x[i], data_Test1[i,index_lst[j]], color=Colors[j])

plt.xlabel('Cross-shore distance (m)', fontsize=15)
plt.ylabel('Grain size (mm)', fontsize=15)
plt.title(r'High resolution ($\approx$1 m) Cross-shore line, Test 1', fontsize=20)
plt.legend(['D5', 'D10', 'D16', 'D30', 'D50', 'D75', 'D84', 'D90'], bbox_to_anchor=(1,1), loc="upper left")
plt.show()  


HighLowRes = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Statistics_AVG/HeatmapHighVLowRes.csv', index_col=0))
HighLowRes[HighLowRes==0] = np.nan

plt.subplot(3,1,1)
plt.imshow(HighLowRes[[0,1,2],:], cmap = 'coolwarm', interpolation=None)
plt.colorbar().set_label(label=r'D$_{16}$ (mm)', fontsize=15)
plt.yticks(np.arange(0,3,1), ['Test_2', 'Test_1', 'R7'])
plt.xticks(np.arange(0,32,1), np.arange(0,16, 0.5))
plt.title(r"D${16}$", fontsize=20)
plt.xlabel('Cross-shore distance (m)', fontsize=15)

plt.subplot(3,1,2)
plt.imshow(HighLowRes[[3,4,5],:], cmap = 'coolwarm', interpolation=None)
plt.colorbar().set_label(label=r'D$_{50}$ (mm)', fontsize=15)
plt.yticks(np.arange(0,3,1), ['Test_2', 'Test_1', 'R7'])
plt.xticks(np.arange(0,32,1), np.arange(0,16, 0.5))
plt.title(r"D${50}$", fontsize=20)
plt.xlabel('Cross-shore distance (m)', fontsize=15)

plt.subplot(3,1,3)
plt.imshow(HighLowRes[[6,7,8],:], cmap = 'coolwarm', interpolation=None)
plt.colorbar().set_label(label=r'D$_{90}$ (mm)', fontsize=15)
plt.yticks(np.arange(0,3,1), ['Test_2', 'Test_1', 'R7'])
plt.xticks(np.arange(0,32,1), np.arange(0,16, 0.5))
plt.title(r"D${90}$", fontsize=20)
plt.xlabel('Cross-shore distance (m)', fontsize=15)
plt.show()
