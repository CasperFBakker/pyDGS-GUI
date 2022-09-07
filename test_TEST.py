from Imports.Import_Modules import * 

data = pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Corrected_Loc1/Data_Location_1.csv')
data = np.array(data)

percentiles = [5, 10, 16, 25, 30, 50,  75, 84, 90, 95] 
sieve_open = [8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063]
sieve_data_1 = [100, 98, 91, 73, 55, 32, 26, 19, 14, 9, 3, 0, 0]


test4 = [100,	98.03742039,	86.50478147,	54.62367944, 39.3832256,	27.29937681,	22.87518019,	13.77354752, 11.0635036, 5.912429852, 1.870618875, 0.492045907, 0.027050264]
test5 = [100,	97.91915857,	87.87140515	,57.6366499,	42.32830503	,29.62617099,24.80889593,	14.88713785, 11.89542279, 6.313682975, 1.962224645, 0.499545384,	0.020401643]
test6 = [100, 97.749458,	85.720625,	64.42260906, 48.08843951, 29.29367, 24.586666, 21.63884949, 12.33749639, 6.635463912, 2.110120993, 0.568223161, 0.042683111]
test7 = [100,	99.33303457,	94.88778758,	68.12689832,	51.1802888,	36.37036607,	30.61019488	,18.40931733,14.68263386, 7.736628744, 2.360307627, 0.602593609, 0.036187792]
test9 = [100,	98.21427663,	89.41588979	,60.91013688,	45.58005154,	32.6890377,	27.72012729,	16.86195956	,13.63983225, 7.336113877, 2.331340378, 0.612870904, 0.031412156]
#test15 = [100, 96.33211434, 79.66298505, 49.47298694, 35.7032497, 24.70939609, 20.66571499, 23.96702411, 13.71528599, 7.426824419, 2.383277287, 0.62931437, 0.031850385]
testdry = [100, 97.87438321,85.85206557	,52.41154005	,36.66916928,	24.34635003,	19.92316888	,11.68049418	,9.161883091, 4.782885766, 1.461140507, 0.378269059, 0.021486793]
plt.subplot(1,1,1)
plt.plot(sieve_open, sieve_data_1, ls='--', color='black', label='Sieved')

plt.plot(sieve_open, test4, marker='.', label='Top (10.3 cm)')
plt.plot(sieve_open, test5, marker='.', label='Top (6.35 cm)')
plt.plot(sieve_open, test7, marker='.', label='Scraped top (11.3 cm)')
plt.plot(sieve_open, test9, marker='.', label='Top auto-hdr (9.44 cm)')
#plt.plot(sieve_open, test15, marker='.')
plt.plot(sieve_open, testdry, marker='.', label='Dried')

plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size d (mm)', fontsize=20)
plt.ylabel('Percent finer (%)', fontsize=20)
plt.title('Location 1: Corrected Proffitt', fontsize=20)



# plt.suptitle('Location 1', fontsize=20)

plt.show()