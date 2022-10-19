from Imports.Import_Modules import * 

def Percentage2Percentile(Percentage):
    Percentage = Percentage[::-1]
    Percentile = 100 - np.nancumsum(Percentage)

    Percentile_cor = []
    for index, value in enumerate(Percentile):
        if value < 0:
            Percentile_cor.append(0)
        else:
            Percentile_cor.append(value)

    Percentile_cor = Percentile_cor[::-1]
    
    return Percentile_cor

resolution =0.018297697368421
percentage = [0.425931219, 4.100124297, 3.642748199, 4.895685552, 3.466024906, 3.879507572, 4.906735323, 5.266609742, 14.11528309, 17.26461274, 31.12557044, 6.306970104, 0.467816199, 0]
percentage = [0, 0.767875176, 3.97300173, 4.959831971, 3.721121061, 4.273234917, 5.156282013, 5.662466322, 15.49416788 ,18.69547084 ,31.78456414,	5.013404206	,0.359111923	,0]
C_s = 41.3281038949403 
P_s = 2.099379347511153
C_m = 1.0917327321057564
P_m = -0.24251553614253563
C_l = 0.4884623531908277
P_l = 1.3267257131505128

C_s = 191.13808985413237
P_s = 2.804953092790458
C_m = 0.1854802814657743
P_m = -2.1493016950684303
C_l = 0.3530984202702832
P_l = 1.887249670551427

 
minSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
maxSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8, 12])

for index, value in enumerate(minSz):
    if (value/resolution) <5:
        percentage[index] = np.nan
    else:
        pass

first_step = []

for index, value in enumerate(percentage):
    if value != 0:
        if minSz[index] <=0.250:
            first_step.append(value*(C_s * pow(minSz[index], P_s)))
        elif minSz[index] > 0.250 and  minSz[index] < 1:
            first_step.append(value*(C_m * pow(minSz[index], P_m)))
        elif minSz[index] >= 1:
            first_step.append(value*(C_l * pow(minSz[index], P_l)))
    else: 
        first_step.append(np.nan)

total_sum = np.nansum(first_step)
Corrected_Percentage = []
for index, value in enumerate(first_step):
    Corrected_Percentage.append(((value/total_sum)*100))

print(Percentage2Percentile(Corrected_Percentage))
