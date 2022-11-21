import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from loess.loess_2d import loess_2d
import cv2 as cv
df = pd.read_csv("/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/TexelDEM.csv", usecols = ['Easting','Northing','Elevation'])
x = df['Easting'].values;   x = list(x)
y = df['Northing'].values;  y = list(y)
z = df['Elevation'].values; z = list(z)


plt.tricontourf(x,y,z, cmap='coolwarm')
plt.colorbar()
plt.scatter(x,y, color='k')
data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (RD2018) (copy 1).csv'))
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

# # plt.show()

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

df = pd.read_csv("/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/TexelDEM.csv", usecols = ['Easting','Northing','Elevation'])
x1 = df['Easting'].values;   x1 = list(x1)
y1 = df['Northing'].values;  y1 = list(y1)
z1 = df['Elevation'].values; z1 = list(z1)

df2 = pd.read_csv("/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (RD2018).csv", usecols = ['Easting','Northing','Elevation'])
x2 = df2['Easting'].values;   x2 = list(x2)
y2 = df2['Northing'].values;  y2 = list(y2)
z2 = df2['Elevation'].values; z2 = list(z2)

x = x1+x2; y=y1+y2; z=z1+z2
x = np.array(x); y = np.array(y); z= np.array(z); x_cross = x_cross.flatten(); y_cross=y_cross.flatten()

zout_DEM, _ = loess_2d(x, y, z, xnew=x_cross, ynew=y_cross, degree=1, frac=0.5, npoints=None, rescale=False, sigz=None)

print(np.shape(zout_DEM))
plt.tricontourf(x_cross,y_cross,zout_DEM, cmap='coolwarm')
plt.colorbar().set_label(label='Elevation (m)', fontsize=15)
# plt.title(r"D${90}$", fontsize=20)

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Texel 20221026 (RD2018) (copy 1).csv'))
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

img_1 = cv.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R7/R7_A3.jpg',cv.IMREAD_UNCHANGED)
img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

img_2 = cv.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R7/R7_B3.jpg',cv.IMREAD_UNCHANGED)
img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

img_3 = cv.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R7/R7_C1.jpg',cv.IMREAD_UNCHANGED)
img_3 = cv.cvtColor(img_3, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

img_4 = cv.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R7/R7_D1.jpg',cv.IMREAD_UNCHANGED)
img_4 = cv.cvtColor(img_4, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

img_5 = cv.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R7/R7_E3.jpg',cv.IMREAD_UNCHANGED)
img_5 = cv.cvtColor(img_5, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)


GrainDisData =  np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/AVG/Percentile_R7.csv'))
sieve_open = [0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

PercentileData = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/AVG/Statistics_R7.csv'))
Cross_X = [83.91617101, 89.10198328, 94.83225398, 98.23149339, 100.9333933]

df = pd.read_csv("/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/DEM_Profile4.csv", usecols = ['Elevation', 'Distance'])
Elevation = df['Elevation'].values; 
CrossShore = df['Distance'].values; 

plt.subplot(5,5,(1,5))
plt.plot(CrossShore, Elevation)
plt.xlim([0,160])
plt.xlabel('Crossshore distance (m)')
plt.ylabel('Elevation (m)')
plt.subplot(5,5,(6,10))
plt.plot(CrossShore[58:73], Elevation[58:73])

plt.scatter(83.91617101, 1, label='A')
plt.scatter(89.10198328, 0.75, label='B')
plt.scatter(94.83225398, 0.5, label='C')
plt.scatter(98.23149339, 0.25, label='D')
plt.scatter(100.9333933, 0, label='E')
plt.xlim([81.4,101.5])
plt.legend()
plt.xlabel('Crossshore distance (m)')
plt.ylabel('Elevation (m)')

plt.subplot(5,5,(11,15))
for i in range(len(PercentileData)):
    plt.scatter(Cross_X[i], PercentileData[i,1], color='blue')
    plt.scatter(Cross_X[i], PercentileData[i,5], color='green')
    plt.scatter(Cross_X[i], PercentileData[i,9], color='red')
plt.xlim([81.4,101.5])
plt.ylabel('Grain size (mm)')
plt.xlabel('Crossshore distance (m)')
plt.legend(['D16', 'D50', 'D90'])

plt.subplot(5,5,16)
plt.imshow(img_1)
plt.title('A')
plt.xticks([]); plt.yticks([])
plt.subplot(5,5,17)
plt.title('B')
plt.imshow(img_2)
plt.xticks([]); plt.yticks([])
plt.subplot(5,5,18)
plt.title('C')
plt.imshow(img_3)
plt.xticks([]); plt.yticks([])
plt.subplot(5,5,19)
plt.title('D')
plt.imshow(img_4)
plt.xticks([]); plt.yticks([])
plt.subplot(5,5,20)
plt.title('D')
plt.imshow(img_5)
plt.xticks([]); plt.yticks([])

plt.subplot(5,5,21)
plt.plot(sieve_open, GrainDisData[0,1:])
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])
plt.xlabel('Grain size (mm)')
plt.ylabel('Percent finer')

plt.subplot(5,5,22)
plt.plot(sieve_open, GrainDisData[1,1:])
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])

plt.subplot(5,5,23)
plt.plot(sieve_open, GrainDisData[2,1:])
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])

plt.subplot(5,5,24)
plt.plot(sieve_open, GrainDisData[3,1:])
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])

plt.subplot(5,5,25)
plt.plot(sieve_open, GrainDisData[4,1:])
plt.xscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.yticks(np.arange(0,110, 10), ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'] )
plt.xticks([0.1, 1, 10], [0.1,1,10])


plt.show()