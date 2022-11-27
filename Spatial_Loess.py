from loess.loess_2d import loess_2d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x_t = np.array([117409.381, 117261.811, 117032.068, 116557.854, 116071.970, 115824.012, 115526.010, 115306.900])
y_t = np.array([560087.034, 559906.751, 559705.862, 559333.503, 558960.603, 558770.808, 558481.620, 558201.731])

x_b = np.array([117429.800, 117276.787, 117043.922, 116566.903, 116083.360, 115833.942, 115533.718, 115314.275])	
y_b = np.array([560074.458, 559888.839, 559685.688, 559317.602, 558946.919, 558759.114, 558477.223, 558197.360])

def PointsCreator(x,y, AlongShoreRes):
    x = np.sort(x)
    y = np.sort(y)
    m = np.zeros(len(x)-1)

    for i in range(len(x)-1):
        m[i] = ((y[i+1]-y[i])/(x[i+1]-x[i])) 

    Dis_Points = np.zeros(len(x)-1)
    for i in range(len(x)-1):
        Dis_Points[i] = np.sqrt((y[i+1]-y[i])**2 + (x[i+1]-x[i])**2) 
    Dis_Points = np.cumsum(Dis_Points)
    
    Distance = np.arange(0, Dis_Points[-1], AlongShoreRes)


    boundaries = np.repeat(Dis_Points, 2)
    boundaries = np.insert(boundaries, 0, 0); boundaries = np.delete(boundaries, -1)
    boundaries.reshape((2, len(Dis_Points)))
    boundaries = np.reshape(boundaries, (len(Dis_Points), 2))


    m_idx = []
    for j in range(len(Distance)):
        m_idx.append([j for j, val in enumerate((np.min(boundaries,1) <= Distance[j]) & (Distance[j] < np.max(boundaries, 1))) if val])
    m_idx = np.array(m_idx).flatten()

    new_m = m[m_idx]

    x_new = []; y_new = []
    x_new.append(x[0])
    y_new.append(y[0])
    for k in range(len(Distance)):
        if k == 0:
            x_new.append( x[0] + (AlongShoreRes * (np.sqrt(1 / (1 + (new_m[k]*new_m[k]))))) )
            y_new.append( y[0] + (new_m[k] * AlongShoreRes * (np.sqrt(1 / (1 + (new_m[k]*new_m[k]))))) )
        else:
            x_new.append( x_new[-1] + (AlongShoreRes * (np.sqrt(1 / (1 + (new_m[k]*new_m[k]))))) )
            y_new.append( y_new[-1] + (new_m[k] * AlongShoreRes * (np.sqrt(1 / (1 + (new_m[k]*new_m[k]))))) )


    return x_new, y_new

def GridCreator(x_top, y_top, x_bot, y_bot, CrossShoreRes, BeachWidth=15):
    CrossSteps = int(BeachWidth / CrossShoreRes)
    y_cross = np.zeros((len(y_top), CrossSteps))
    x_cross = np.zeros((len(x_top), CrossSteps))
    for i in range(len(x_top)):
        y_cross[i] = np.linspace(y_top[i], y_bot[i], CrossSteps)
        x_cross[i] = np.linspace(x_top[i], x_bot[i], CrossSteps)


    return x_cross, y_cross

x_tnew, y_tnew = PointsCreator(x_t,y_t, 50)
x_bnew, y_bnew = PointsCreator(x_b,y_b, 50)

x_cross, y_cross = GridCreator(x_tnew, y_tnew, x_bnew, y_bnew, 0.5)


# plt.show()

x = [117409.381, 117419.109, 117424.357, 117427.312, 117429.800, 117261.811, 117268.333, 
     117273.359, 117275.149, 117032.068, 117037.858, 117042.572, 116557.854, 116561.411,
     116565.261, 116071.970, 116076.004, 116079.241, 116081.563, 116083.360, 115824.012, 
     115829.112, 115830.656, 115832.617, 115833.942, 115526.010, 115528.398, 115530.174, 
     115531.973, 115533.718, 115306.900, 115308.990, 115310.584, 115312.381, 115314.275]

y = [560087.034, 560080.960, 560077.728, 560075.964, 560074.458, 559906.751, 559898.967, 
     559892.730, 559890.509, 559705.862, 559697.183, 559690.196, 559333.503, 559328.152, 
     559322.001, 558960.603, 558955.954, 558952.024, 558948.737, 558946.919, 558770.808, 
     558765.567, 558763.547, 558761.077, 558759.114, 558481.620, 558480.347, 558479.247, 
     558478.192, 558477.223, 558201.731, 558200.581, 558199.581, 558198.385, 558197.360]

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

z_D90 = [2.772125110, 2.708446273, 2.596546982, 2.505028902, 2.895541900, 2.957331303, 2.662954673, 
         2.555310847, 2.928162461, 3.291021936, 2.654708546, 2.844908127, 3.485950514, 2.780278765, 
         2.750291211, 2.730179683, 2.498821655, 2.482770387, 2.616623218, 2.408652557, 2.526332138, 
         2.814525254, 2.819735228, 2.504342763, 2.661228610, 2.797869254, 2.850688325, 2.805805813, 
         2.872274515, 2.862906123, 2.352284465, 2.685123104, 2.426909297, 2.675505335, 2.345321535]


z_D50 = [0.6776702439024390, 0.4629446231617650, 0.7489878444084290, 0.5125783898305080, 0.4837822690217390, 
         1.2582978723404300, 0.5918792636708170, 0.6504935108713970, 0.8178007590132830, 0.4728723404255330, 
         1.4119901389511500, 0.7265510590015130, 1.5820749361339800, 0.4519193154034230, 0.7072930946291560, 
         0.3999219765929780, 0.3681687973997830, 0.5948011583011580, 0.5897954209748890, 0.5906374162096290, 
         0.8216517879161530, 0.4718776077885950, 0.6791765346103610, 0.5106942924159510, 0.6701158140742670, 
         0.4982166123778500, 0.6919186819027370, 1.0536602700781800, 0.6579582132564840, 0.6579582132564840, 
         0.6539260042283300, 1.6333631370545400, 0.7143363736871180, 0.7873960396039610, 0.7526293868921770]


z_D90 = [ 1.8506228373702400, 1.1922189720016700, 3.0548139983466600, 1.8466917960088700, 1.8237737763124500, 
          3.6192292813569500, 2.5402676181980400, 1.8948531951640800, 2.9073216063723900, 3.0627871362940400, 
          6.6221368948247200, 2.7550176263219700, 3.8123119266055000, 1.9248255062473100, 2.0634764826176000, 
          3.0184792792792800, 0.9921879558948250, 2.5245337895637300, 2.4668045977011500, 1.9631809523809500, 
          1.9603628486325500, 1.5418316648127600, 2.1950075490689500, 2.0221532846715500, 2.7848005409060200, 
          1.3438197266346500, 2.9046979865771800, 3.2023456199138300, 2.7640784313725500, 2.7640784313725500, 
          1.8702259136212600, 3.8096856039713200, 2.3782558139534700, 4.2338058368076200, 2.6214279048063400]

z_D16 = [0.3542593582887700, 0.2879885948238050, 0.3599045737051790, 0.2883899873790490, 0.2515277145026580, 
         0.3243780363830930, 0.3181775206922500, 0.3599578385171220, 0.3401308929820470, 0.2618818596621040, 
         0.3409287596677170, 0.3545834762045520, 0.4762575539568340, 0.3030270157068070, 0.4260432535885170, 
         0.2482133142105890, 0.2624525957105630, 0.3401779694519320, 0.3192200209643610, 0.3250272663056280, 
         0.3555920277296360, 0.2992026229508200, 0.3761508363397840, 0.2797635339378950, 0.3396023048716600, 
         0.2935575953923690, 0.3095591426303260, 0.4404704225352110, 0.3050286182251340, 0.3050286182251340, 
         0.3996249716231560, 0.6095850769907620, 0.4380195740365110, 0.4509124604012670, 0.5178486587591240]
x = np.array(x); y = np.array(y); z_D90 = np.array(z_D90); z_D50 = np.array(z_D50); z_D16 = np.array(z_D16); 
x_cross = x_cross.flatten(); y_cross=y_cross.flatten()


zout_D90, _ = loess_2d(x, y, z_D90, xnew=x_cross, ynew=y_cross, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)
zout_D50, _ = loess_2d(x, y, z_D50, xnew=x_cross, ynew=y_cross, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)
zout_D16, _ = loess_2d(x, y, z_D16, xnew=x_cross, ynew=y_cross, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)


plt.subplot(3,1,1)
plt.tricontourf(x_cross,y_cross,zout_D16, cmap='coolwarm')
plt.colorbar().set_label(label=r'D$_{16}$ (mm)', fontsize=15) 
plt.title(r"D${16}$", fontsize=20)

plt.subplot(3,1,2)
plt.tricontourf(x_cross,y_cross,zout_D50, cmap='coolwarm')
plt.colorbar().set_label(label=r'D$_{50}$ (mm)', fontsize=15)
plt.title(r"D${50}$", fontsize=20)

plt.subplot(3,1,3)
plt.tricontourf(x_cross,y_cross,zout_D90, cmap='coolwarm')
plt.colorbar().set_label(label=r'D$_{90}$ (mm)', fontsize=15)
plt.title(r"D${90}$", fontsize=20)

# x_cross, y_cross = GridCreator(x_tnew, y_tnew, x_bnew, y_bnew, 0.5)
# for i in range(len(x_cross)):
#     plt.scatter(x_cross[i], y_cross[i], color='green')
# plt.scatter(x_tnew, y_tnew, color='blue')
# plt.scatter(x_bnew, y_bnew, color='red')
# plt.scatter(x_t, y_t, color='k')
plt.show()

plt.subplot(2,3,(1,3))
plt.tricontourf(x_cross,y_cross,zout_D16, cmap='coolwarm')
plt.colorbar(orientation="horizontal").set_label(label=r'D$_{16}$ (mm)', fontsize=15) 

plt.title(r"D${16}$", fontsize=20)

plt.subplot(2,3,4)
plt.tricontourf(x_cross,y_cross,zout_D16, cmap='coolwarm')
plt.xlim([115250, 116125])
plt.ylim([558200, 559100])
 
plt.subplot(2,3,5)
plt.tricontourf(x_cross,y_cross,zout_D16, cmap='coolwarm')
plt.xlim([116125, 116875])
plt.ylim([558750, 559750])

plt.subplot(2,3,6)
plt.tricontourf(x_cross,y_cross,zout_D16, cmap='coolwarm')
plt.xlim([116875, 117550])
plt.ylim([559500, 560200])

plt.show()
