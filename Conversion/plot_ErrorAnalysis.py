import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_Multi = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Error_Analysis/Error_PercentileFilt_MultiTrend.csv'))
data_Sub = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Error_Analysis/Error_PercentileFilt_MultiTrend_Sub4.csv'))
data_All = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Error_Analysis/Error_PercentileFilt_AllTrend.csv'))

plt.subplot(2,3,1)
plt.plot(np.arange(0, 10, 1),data_Multi[0,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_Sub[0,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_All[0,1:], marker='o')
plt.xticks(np.arange(0, 10, 1), ['D5', 'D10', 'D16', 'D25', 'D30', 'D50', 'D75', 'D84', 'D90', 'D95'])
plt.ylim([0,1.5])
plt.title('Location 1', fontsize=15)

plt.subplot(2,3,2)
plt.plot(np.arange(0, 10, 1),data_Multi[2,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_Sub[2,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_All[2,1:], marker='o')
plt.xticks(np.arange(0, 10, 1), ['D5', 'D10', 'D16', 'D25', 'D30', 'D50', 'D75', 'D84', 'D90', 'D95'])
plt.ylim([0,1.5])
plt.title('Location 2', fontsize=15)

plt.subplot(2,3,3)
plt.plot(np.arange(0, 10, 1),data_Multi[4,1:], marker='o', label='MultiFrac')
plt.plot(np.arange(0, 10, 1),data_Sub[4,1:], marker='o', label='MultiFrac, w/o loc 4')
plt.plot(np.arange(0, 10, 1),data_All[4,1:], marker='o', label='AllTrend')
plt.xticks(np.arange(0, 10, 1), ['D5', 'D10', 'D16', 'D25', 'D30', 'D50', 'D75', 'D84', 'D90', 'D95'])
plt.ylim([0,1.5])
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.title('Location 3', fontsize=15)

plt.subplot(2,3,4)
plt.plot(np.arange(0, 10, 1),data_Multi[6,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_Sub[6,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_All[6,1:], marker='o')
plt.xticks(np.arange(0, 10, 1), ['D5', 'D10', 'D16', 'D25', 'D30', 'D50', 'D75', 'D84', 'D90', 'D95'])
plt.ylim([0,1.5])
plt.title('Location 4', fontsize=15)
plt.xlabel('Percentiles', fontsize=15)
plt.ylabel('Root Mean Square Error (mm)', fontsize=15)

plt.subplot(2,3,5)
plt.plot(np.arange(0, 10, 1),data_Multi[8,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_Sub[8,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_All[8,1:], marker='o')
plt.xticks(np.arange(0, 10, 1), ['D5', 'D10', 'D16', 'D25', 'D30', 'D50', 'D75', 'D84', 'D90', 'D95'])
plt.ylim([0,1.5])
plt.title('Location 6', fontsize=15)

plt.subplot(2,3,6)
plt.plot(np.arange(0, 10, 1),data_Multi[10,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_Sub[10,1:], marker='o')
plt.plot(np.arange(0, 10, 1),data_All[10,1:], marker='o')
plt.xticks(np.arange(0, 10, 1), ['D5', 'D10', 'D16', 'D25', 'D30', 'D50', 'D75', 'D84', 'D90', 'D95'])
plt.ylim([0,1.5])
plt.title('Location 7', fontsize=15)

plt.suptitle('Root Mean Square Error', fontsize=20)



plt.show()

