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
plt.plot(sieve_open, [0, 3.55271E-15, 3.55271E-15, 0.054731947, 0.360860121, 2.085958215, 5.063654116, 10.08644802, 25.62427631, 52.79891459, 63.25639834, 84.21874153, 96.24964875, 99.36775911])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 1', fontsize=20)

plt.subplot(2,3,2)
plt.plot(sieve_open, data_sieve[1,1:], ls=':', color='black')
plt.plot(sieve_open, data[1,1:])
plt.plot(sieve_open, [0, 0, 0, 0.01855452, 0.197010421, 1.198012875, 2.457469454, 6.328211308, 18.0092531, 52.54023329, 62.60496181, 82.94633254, 95.63562558, 99.33957599])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 2', fontsize=20)

plt.subplot(2,3,3)
plt.plot(sieve_open, data_sieve[2,1:], ls=':', color='black', label='Sieve')
plt.plot(sieve_open, data[2,1:])
plt.plot(sieve_open, [0, 1.42109E-14, 1.42109E-14, 1.42109E-14, 0.218929179, 1.276696609, 2.838439989, 6.315535577, 19.77207099, 52.07153641, 59.58465833, 77.87621604, 92.61381382, 98.82454659])

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
plt.plot(sieve_open, [0, 0, 0, 0, 0.13676705, 1.191171336, 2.395959484, 6.425883676, 20.30785072, 52.60734692, 61.22379254, 82.24719298, 95.70659494, 99.44227418])

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
plt.plot(sieve_open, [0, 0, 0, 0.011615362, 0.20273059, 1.014339313, 2.843866293, 9.575560384, 24.81732326, 52.94559746, 63.32503827, 83.59982733, 95.62704, 99.2583964])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 6', fontsize=20)

plt.subplot(2,3,6)
plt.plot(sieve_open, data_sieve[6,1:], ls=':', color='black')
plt.plot(sieve_open, data[5,1:])
plt.plot(sieve_open, [0, 0, 0, 0.008233724, 0.230633405, 1.064627454, 2.753321864, 7.190043743, 21.05086706, 52.84687376, 62.74981153, 83.56743534, 96.06987983, 99.41652508])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])

plt.title('Location 7', fontsize=20)

plt.show()



##########################################################################################################################
plt.subplot(1,3,1)
plt.plot(sieve_open, [0, 3.55271E-15, 3.55271E-15, 1.33193302, 4.491451553, 12.77812322, 20.27638362, 28.27324904, 40.24333584, 52.88225419,  62.77615248, 82.6005543, 94.77672699, 99.12195191], color='black')
plt.plot(sieve_open, [0, 5.32907E-15, 5.32907E-15, 0.134075896, 0.897935046, 4.200041939, 8.832041966, 17.02361623, 32.44987514, 52.74714509, 62.4924965, 82.07373702, 94.49661909, 99.05473575])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 2', fontsize=20)

plt.subplot(1,3,2)
plt.plot(sieve_open, [0, 4.73695E-15, 4.73695E-15, 0.97697771, 3.455030806 , 11.46329102, 18.3704567 , 27.20035389, 39.6025681,  53.53903378, 64.88009605, 84.80866994, 95.83647404, 99.27411223], color='black')
plt.plot(sieve_open, [0, 7.10543E-15, 7.10543E-15, 0.102605567, 0.521561222, 2.950368673, 7.254553838, 16.17742173, 34.21355767, 53.04437943, 63.26875995, 83.42273498, 95.5458214, 99.36651478])

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.title('Location 3', fontsize=20)

plt.subplot(1,3,3)
plt.plot(sieve_open, [0, 4.06024E-15, 4.06024E-15, 1.277692546, 4.868197565, 13.3876165, 20.44370012, 29.34184478, 40.96045268, 53.55230631, 65.16397333, 85.07699612, 96.03559074, 99.30433408], color='black', label='Sample')
plt.plot(sieve_open, [0, 3.55271E-15, 0.000773119, 0.04816035, 0.236769064, 1.207881186, 3.153112376, 8.598378855, 24.16615982, 52.79834914, 63.30089942, 84.22974724, 96.21917916, 99.46793404], label='Top')
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.legend()
plt.title('Location 4', fontsize=20)
plt.show()


# plt.subplot(1,2,1)
# plt.plot(sieve_open, [0, 5.32907E-15, 0.000560444, 0.163645626, 0.817059867, 3.783402357, 8.877262323, 18.98208402, 35.66979966, 52.63822077, 62.3191097, 82.16987894, 94.90916937, 99.17436638], color='blue', label='Photo')
# plt.plot(sieve_open, [0, 0.114299503, 0.349248481, 2.178040526, 9.433518964, 18.1837809, 25.24876017, 31.13137458, 34.14126149, 40.82143243, 46.10460944, 69.25343375, 90.81158997, 99.00940431], color='black', label='Sieve')
# plt.xscale("log")
# plt.grid(which='major', linewidth=2, linestyle='-')
# plt.grid(which='minor', linewidth=1, linestyle='--')
# plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
# plt.xticks([0.1, 1, 10], [0.1,1,10])
# plt.legend()
# plt.title('Location 1', fontsize=20)

# plt.subplot(1,2,2)
plt.plot(sieve_open, [0, 8.88178E-15, 8.88178E-15, 0.427355008, 1.816394826, 7.021030454, 13.41638936, 23.36168233, 38.07889003, 52.69872721, 62.62058857, 82.24666105, 94.72116902, 99.08980437], color='blue', label='Current correction')
plt.plot(sieve_open, [0, 0.181095765, 0.711949618, 4.183582453, 13.76381869, 28.2012055, 37.41925021, 45.87128686, 50.68248777, 60.37246263, 66.61080628, 80.74438468, 92.83455415, 97.18625835], linestyle='--', color='black', label='Sieve')
plt.plot(sieve_open, [0, 5.32907E-15, 5.32907E-15, 0.134075896, 0.897935046, 4.200041939, 8.832041966, 17.02361623, 32.44987514, 52.74714509, 62.4924965, 82.07373702, 94.49661909, 99.05473575], label='Field photo')
plt.plot(sieve_open, [0, 5.32907E-15, 10.67963684, 17.85835689, 25.30473638, 29.63834868, 34.11194871, 39.41506373, 44.59672325, 56.46996356, 68.585504, 89.87926651, 98.52149316, 100], label='Standard correction')
plt.plot(sieve_open, [0, 2.66454E-15, 2.66454E-15, 0.739601896, 2.721684553, 8.999084051,16.06011338, 26.20157261, 40.01433855, 52.69872721, 62.62058857, 82.24666105, 94.72116902, 99.08980437], label='All pow -1')
plt.plot(sieve_open, [0, 1.77636E-15, 12.28623841, 20.39721924, 30.41437149, 36.65078887, 42.50369946, 47.75971243, 50.83386697, 52.69872721, 62.62058857, 82.24666105, 94.72116902, 99.08980437], label='No volume correction')

plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.legend()
plt.title('Location 2', fontsize=20)

plt.show()