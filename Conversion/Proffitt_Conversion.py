import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import cv2
from imageio import imread
import pywt
import scipy.stats as stats

def GetImageRes(img_path):
    filename = os.path.basename(img_path)
    dir_path = os.path.dirname(img_path)
    dir_name = os.path.basename(dir_path)

    try:
        DataFrame = pd.read_csv("Output data/data_" + dir_name +".csv")
        row = DataFrame[DataFrame["Image name"] == filename].index[0]
        resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
    except FileNotFoundError:
        tk.messagebox.showinfo(title=':(::(:(:(:(', message='This image has no data stored. Image resolution is taken as: 1. Which means that the unit is in pixels.')
        resolution = 1

    return resolution

# =========================================================
def rescale(dat,mn,mx):
    """
    rescales an input dat between mn and mx
    """
    m = min(dat.flatten())
    M = max(dat.flatten())
    return (mx-mn)*(dat-m)/(M-m)+mn

##====================================
def standardize(img):
    img = np.array(img)
    #standardization using adjusted standard deviation
    N = np.shape(img)[0] * np.shape(img)[1]
    s = np.maximum(np.std(img), 1.0/np.sqrt(N))
    m = np.mean(img)
    img = (img - m) / s
    img = rescale(img, 0, 1)
    del m, s, N

    return img

# path_of_the_directory = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Location_1/'

# for files in os.listdir(path_of_the_directory):
#     if files.endswith('.jpg'):
#         image = path_of_the_directory + files  
#         print(image)
#         resolution = GetImageRes(image)
#         print(resolution)
#         img = cv2.imread(image)
#         nxx, nyy, _ = img.shape
#         width = max(nxx, nyy)

#         x= 0

#         im = imread(image)   # read the image straight with imread
#         im = np.squeeze(im)  # squeeze singleton dimensions
#         if len(np.shape(im))>3:
#             im = im[:, :, :3]            # only keep the first 3 bands

#         if len(np.shape(im))==3: # if rgb, convert to grey
#             im = (0.299 * im[:,:,0] + 0.5870*im[:,:,1] + 0.114*im[:,:,2]).astype('uint8')

#         nx,ny = np.shape(im)
#         if nx>ny:
#             im=im.T

#         im = standardize(im)

#         region = im.copy()

#         original = rescale(region,0,255)

#         nx, ny = original.shape

#         P = []; M = []
#         for k in np.linspace(1,nx-1,100):
#             [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(np.maximum(nx,ny)/(width*resolution / 0.1), np.maximum(nx,ny)/(width*resolution / 8), 1),  'morl', .5) 
#             period = 1. / frequencies
#             power =(abs(cfs)) ** 2
#             power = np.mean(np.abs(power), axis=1)/(period**2)
#             P.append(power)

#             M.append(period[np.argmax(power)])

#         p = np.mean(np.vstack(P), axis=0)
#         p = np.array(p/np.sum(p))

#         # get real scales by multiplying by resolution (mm/pixel)
#         scales = np.array(period)

#         srt = np.sqrt(np.sum(p*((scales-np.mean(M))**2)))

#         p = p+stats.norm.pdf(scales, np.mean(M), srt/2)
#         p = np.hstack([p])
#         scales = np.hstack([scales])
#         p = p/np.sum(p)
#         x = 0
#         # area-by-number to volume-by-number
#         r_v = (p*scales**x) / np.sum(p*scales**x) #volume-by-weight proportion


#         Output = np.interp([8, 4, 2, 1, 0.71, 0.5, 0.425, 0.355, 0.3, 0.25, 0.18, 0.125, 0.063], np.hstack((0,scales)) * resolution,np.hstack((0,np.cumsum(r_v)))) 

#         for i in range(len(Output)):
#             print(Output[i]*100)
#     else:
#         continue


image= "/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Location_2/Loc_2_3.jpg"
resolution = 0.0328590785907859
img = cv2.imread(image)
nxx, nyy, _ = img.shape
width = max(nxx, nyy)

x= 0

im = imread(image)   # read the image straight with imread
im = np.squeeze(im)  # squeeze singleton dimensions
if len(np.shape(im))>3:
    im = im[:, :, :3]            # only keep the first 3 bands

if len(np.shape(im))==3: # if rgb, convert to grey
    im = (0.299 * im[:,:,0] + 0.5870*im[:,:,1] + 0.114*im[:,:,2]).astype('uint8')

nx,ny = np.shape(im)
if nx>ny:
    im=im.T

im = standardize(im)

region = im.copy()

original = rescale(region,0,255)

nx, ny = original.shape

P = []; M = []
for k in np.linspace(1,nx-1,100):
    [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(np.maximum(nx,ny)/(width*resolution / 0.1), np.maximum(nx,ny)/(width*resolution / 8), 1),  'morl', .5) 
    period = 1. / frequencies
    power =(abs(cfs)) ** 2
    power = np.mean(np.abs(power), axis=1)/(period**2)
    P.append(power)

    M.append(period[np.argmax(power)])

p = np.mean(np.vstack(P), axis=0)
p = np.array(p/np.sum(p))

# get real scales by multiplying by resolution (mm/pixel)
scales = np.array(period)

srt = np.sqrt(np.sum(p*((scales-np.mean(M))**2)))

p = p+stats.norm.pdf(scales, np.mean(M), srt/2)
p = np.hstack([p])
scales = np.hstack([scales])
p = p/np.sum(p)
x = 0
# area-by-number to volume-by-number
r_v = (p*scales**x) / np.sum(p*scales**x) #volume-by-weight proportion

plt.plot(scales*resolution, r_v)
plt.show()