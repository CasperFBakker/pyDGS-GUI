from Imports.Import_Modules import * 

data_loc_1 = np.array(pd.read_csv('Output data/Percentile_Location_1_Corrected.csv'))

data_sieve = np.array(pd.read_csv('Output data/08_07_22/Percentile_Sieve.csv'))



corrected_data_1 = [1.4210854715202004e-14, 1.4210854715202004e-14, 1.4210854715202004e-14, 2.043367002885333, 7.528125767636112, 15.729329053250169, 21.847053728062335, 28.93369117157414, 36.38365270110589, 55.98110645550718, 77.69989058576434, 92.90389428230068, 98.91921327419799, 100.0]
#corrected_data_1 = [0, 0, 0, 1.9530565916577274, 7.596733410222711, 15.56004135496947, 21.34989808147236, 28.379880486714, 35.60321271041876, 54.214612457186846, 75.12268490949143, 90.64359128988413, 98.5322790708675, 100.0]
sieve_open = [0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

plt.plot(sieve_open, data_sieve[0,1:15], ls='--', color='black', label=data_sieve[0,0])


plt.plot(sieve_open,corrected_data_1, ls=':', color='blue', label='corrected')
for i in range(0, len(data_loc_1)):
    plt.plot(sieve_open, data_loc_1[i,1:15], marker='.', label=data_loc_1[i,0])
plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.ylabel('Percent finer (%)', fontsize=20)
plt.title('Original', fontsize=20)

plt.show()