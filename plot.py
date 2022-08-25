from Imports.Import_Modules import * 

data = pd.read_csv('Output data/Percentiles/Percentiles_Location_1.csv')
data = np.array(data)
percentiles = [5, 10, 16, 25, 30, 50,  75, 84, 90, 95] 
sieve_open = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063]
sieve_data_1 = [100, 98, 91, 73, 55, 32, 26, 19, 14, 9, 3, 0, 0]
sieve_data_2 = [97,94,89,79,74,57,49,35,22,8,1,0,0]
sieve_data_3 = [88,79,70,59,54,49,45,38,30,17,4,1,0]
sieve_data_4 = [98,91,76,53,44,33,27,19,12,5,1,0,0]
sieve_data_5 = [93,53,4,0,0,0,0,0,0,0,0,0,0]
sieve_data_6 = [99,96,92,88,85,77,72,62,50,33,11,2,0]
sieve_data_7 = [99,98,86,66,60,51,45,35,26,16,6,1,0]

for i in range(len(data)):
    plt.plot(data[i,1:11], percentiles, marker='.', label=data[i,11])

plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.ylabel('Percent finer (%)', fontsize=20)
plt.title('Location 1',  fontsize=20)
plt.show()