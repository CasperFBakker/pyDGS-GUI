from Imports.Import_Modules import * 

dataMob = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Avg_OgPercent.csv'))
dataCan = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Canon/Avg_OgPercent.csv'))


# for i in range(len(dataCan)):
#     plt.scatter(dataCan[i,1:], dataMob[i,1:])

# plt.plot(np.arange(0,50,1), linestyle='--', color='k')
# plt.xlim(0,40); plt.ylim(0,40)
# plt.show()



value = []

for i in range(len(dataCan)):
    for j in range(1, len(dataMob[1,1:])+1):
        try:
            ans = dataMob[i,j]/dataCan[i,j]
            value.append(ans)
        except ZeroDivisionError:
            value.append(np.nan)

value = np.reshape(value, (33,14))

GrainSz = [0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]
for i in range(len(value)):
    plt.scatter(GrainSz, value[i,:])

plt.ylim(0,10)
plt.xscale("log")
plt.show()


# dataMob = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Avg_OgPercent.csv'))
# dataCan = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Canon/Avg_OgPercent.csv'))
# print(np.shape(dataMob))
# print(np.shape(dataCan))
# for i in range(len(dataCan)):
#     plt.scatter(dataCan[i,1:], dataMob[i,1:])

# plt.plot(np.arange(0,50,1), linestyle='--', color='k')
# plt.xlim(0,40); plt.ylim(0,40)
# plt.show()


