import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Corrected/Percentile_Locations_AVG.csv'))

data_sieve = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Percentile_Sieve.csv'))



sieve_open = [0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

# plt.plot(sieve_open, data_sieve[0,1:15], ls='--', color='black', label=data_sieve[0,0])


# plt.plot(sieve_open,corrected_data_1, ls=':', color='blue', label='corrected')
# for i in range(0, len(data_loc_1)):
#     plt.plot(sieve_open, data_loc_1[i,1:15], marker='.', label=data_loc_1[i,0])
# plt.legend()
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.xlabel('Grain size d (mm)', fontsize=20)
# plt.ylabel('Percent finer (%)', fontsize=20)
# plt.title('Original', fontsize=20)

# plt.show()

plt.subplot(2,3,1)
plt.plot(sieve_open, data_sieve[0,1:], ls=':', color='black')
plt.plot(sieve_open, data[0,1:])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 1', fontsize=20)

plt.subplot(2,3,2)
plt.plot(sieve_open, data_sieve[1,1:], ls=':', color='black')
plt.plot(sieve_open, data[1,1:])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 2', fontsize=20)

plt.subplot(2,3,3)
plt.plot(sieve_open, data_sieve[2,1:], ls=':', color='black', label='Sieve')
plt.plot(sieve_open, data[2,1:])
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 3', fontsize=20)

plt.subplot(2,3,4)
plt.plot(sieve_open, data_sieve[3,1:], ls=':', color='black')
plt.plot(sieve_open, data[3,1:])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.ylabel('Percent finer (%)', fontsize=20)
plt.title('Location 4', fontsize=20)

plt.subplot(2,3,5)
plt.plot(sieve_open, data_sieve[5,1:], ls=':', color='black')
plt.plot(sieve_open, data[4,1:])
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 6', fontsize=20)

plt.subplot(2,3,6)
plt.plot(sieve_open, data_sieve[6,1:], ls=':', color='black')
plt.plot(sieve_open, data[5,1:])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])

plt.title('Location 7', fontsize=20)

plt.show()


