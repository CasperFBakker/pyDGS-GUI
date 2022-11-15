from loess.loess_2d import loess_2d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x = [53.02639198, 53.02633808, 53.02630940, 53.02629376, 53.02628040, 53.02476170, 53.02469221, 
     53.02463652, 53.02461669, 53.02294045, 53.02286287, 53.02280042, 53.01956095, 53.01951312, 
     53.01945812, 53.01617533, 53.01613385, 53.01609877, 53.01606940, 53.01605320, 53.01445194, 
     53.01440521, 53.01438717, 53.01436512, 53.01434758, 53.01183165, 53.01182039, 53.01181063, 
     53.01180128, 53.01179270, 53.00930056, 53.00929038, 53.00928151, 53.00927090, 53.00926183]

y = [4.82693436, 4.82708005, 4.82715863, 4.82720289, 4.82724014, 4.82475596, 4.82485407, 
     4.82492970, 4.82495663, 4.82135553, 4.82144284, 4.82151391, 4.81433260, 4.81438624, 
     4.81444434, 4.80713695, 4.80719761, 4.80724631, 4.80728130, 4.80730830, 4.80346521, 
     4.80354183, 4.80356506, 4.80359459, 4.80361456, 4.79906021, 4.79909594, 4.79912253, 
     4.79914948, 4.79917559, 4.79582995, 4.79586122, 4.79588509, 4.79591200, 4.79594034]

z_D90 = [2.772125110, 2.708446273, 2.596546982, 2.505028902, 2.895541900, 2.957331303, 2.662954673, 
         2.555310847, 2.928162461, 3.291021936, 2.654708546, 2.844908127, 3.485950514, 2.780278765, 
         2.750291211, 2.730179683, 2.498821655, 2.482770387, 2.616623218, 2.408652557, 2.526332138, 
         2.814525254, 2.819735228, 2.504342763, 2.661228610, 2.797869254, 2.850688325, 2.805805813, 
         2.872274515, 2.862906123, 2.352284465, 2.685123104, 2.426909297, 2.675505335, 2.345321535]

z_D50 = [0.658181624, 0.647798963, 0.637089442, 0.643158142, 0.678416179, 0.650245765, 0.679468701, 
         0.665604388, 0.649152746, 0.688656274, 0.643027666, 0.663620233, 0.693409927, 0.673876266, 
         0.662631758, 0.648923592, 0.643772414, 0.640133418, 0.650726350, 0.635867743, 0.650554638, 
         0.645537556, 0.647415646, 0.645368045, 0.656129738, 0.645254396, 0.652636444, 0.658884274, 
         0.641755971, 0.650124497, 0.643424179, 0.656357864, 0.650890618, 0.651343243, 0.649618356]

z_D16 = [0.325316976, 0.374401938, 0.332644585, 0.357094180, 0.446073410, 0.345379214, 0.446790519, 
         0.425849777, 0.383289460, 0.462177209, 0.368926458, 0.404802085, 0.471878604, 0.408379472, 
         0.405796000, 0.314723645, 0.323158400, 0.313056617, 0.315099269, 0.321497587, 0.311528302, 
         0.312434852, 0.301369047, 0.312052359, 0.313303223, 0.307859641, 0.311651001, 0.315817767,
         0.318445893, 0.316527133, 0.308297186, 0.309128851, 0.318474345, 0.306266544, 0.314185035]

x = np.array(x); y = np.array(y); z_D90 = np.array(z_D90); z_D50 = np.array(z_D50); z_D16 = np.array(z_D16); 

zout_D90, _ = loess_2d(x, y, z_D90, xnew=None, ynew=None, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)
zout_D50, _ = loess_2d(x, y, z_D50, xnew=None, ynew=None, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)
zout_D16, _ = loess_2d(x, y, z_D16, xnew=None, ynew=None, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)

xnew = []

plt.subplot(3,1,1)
plt.tricontourf(x,y,zout_D16, cmap='coolwarm')
plt.colorbar().set_label(label=r'D$_{16}$ (mm)', fontsize=15)
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (WGS84).csv'))
plt.scatter(data[8:12,2], data[8:12,3], label = data[7,0])
plt.scatter(data[14:18,2], data[14:18,3], label = data[13,0])
plt.scatter(data[20:23,2], data[20:23,3], label = data[19,0])
plt.scatter(data[26:29,2], data[26:29,3], label = data[25,0])
plt.scatter(data[32:36,2], data[32:36,3], label = data[31,0])
plt.scatter(data[38:42,2], data[38:42,3], label = data[37,0])
plt.scatter(data[44:48,2], data[44:48,3], label = data[43,0])
plt.scatter(data[51:57,2], data[51:57,3], label = data[50,0])
plt.title(r"D${16}$", fontsize=20)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")

plt.subplot(3,1,2)
plt.tricontourf(x,y,zout_D50, cmap='coolwarm')
plt.colorbar().set_label(label=r'D$_{50}$ (mm)', fontsize=15)
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (WGS84).csv'))
plt.scatter(data[8:12,2], data[8:12,3], label = data[7,0])
plt.scatter(data[14:18,2], data[14:18,3], label = data[13,0])
plt.scatter(data[20:23,2], data[20:23,3], label = data[19,0])
plt.scatter(data[26:29,2], data[26:29,3], label = data[25,0])
plt.scatter(data[32:36,2], data[32:36,3], label = data[31,0])
plt.scatter(data[38:42,2], data[38:42,3], label = data[37,0])
plt.scatter(data[44:48,2], data[44:48,3], label = data[43,0])
plt.scatter(data[51:57,2], data[51:57,3], label = data[50,0])
plt.title(r"D${50}$", fontsize=20)
# plt.legend()

plt.subplot(3,1,3)
plt.tricontourf(x,y,zout_D90, cmap='coolwarm')
plt.colorbar().set_label(label=r'D$_{90}$ (mm)', fontsize=15)
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (WGS84).csv'))
plt.scatter(data[8:12,2], data[8:12,3], label = data[7,0])
plt.scatter(data[14:18,2], data[14:18,3], label = data[13,0])
plt.scatter(data[20:23,2], data[20:23,3], label = data[19,0])
plt.scatter(data[26:29,2], data[26:29,3], label = data[25,0])
plt.scatter(data[32:36,2], data[32:36,3], label = data[31,0])
plt.scatter(data[38:42,2], data[38:42,3], label = data[37,0])
plt.scatter(data[44:48,2], data[44:48,3], label = data[43,0])
plt.scatter(data[51:57,2], data[51:57,3], label = data[50,0])
# plt.legend()
plt.title(r"D${90}$", fontsize=20)
plt.show()




