from Imports.Import_Modules import * 

data = pd.read_csv('Output data/Percentiles/Percentiles_Line_2.csv')
data = np.array(data)
percentiles = [5, 10, 16, 25, 30, 50,  75, 84, 90, 95] 

for i in range(1, len(data)):
    plt.plot(data[i,1:], percentiles, marker='.', label=data[i,0])

plt.legend()
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])

plt.show()