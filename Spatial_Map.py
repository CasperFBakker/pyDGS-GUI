import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (RD2018).csv'))
# print(data[:,2])

plt.scatter(data[8:12,2], data[8:12,3], label = data[8,0])
plt.scatter(data[14:18,2], data[14:18,3], label = data[14,0])
plt.scatter(data[20:23,2], data[20:23,3], label = data[20,0])
plt.scatter(data[26:29,2], data[26:29,3], label = data[26,0])
plt.scatter(data[32:36,2], data[32:36,3], label = data[32,0])
plt.scatter(data[38:42,2], data[38:42,3], label = data[38,0])
plt.scatter(data[44:48,2], data[44:48,3], label = data[44,0])
plt.scatter(data[51:57,2], data[51:57,3], label = data[51,0])

plt.legend()

plt.show()


