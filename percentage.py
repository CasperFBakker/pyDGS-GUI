import numpy as np
import sys, os
from imageio.v2 import imread
import pywt
from tqdm import tqdm
from skimage.restoration import denoise_wavelet, estimate_sigma
from functools import partial
# rescale_sigma=True required to silence deprecation warnings
_denoise_wavelet = partial(denoise_wavelet, rescale_sigma=True)
import scipy.stats as stats
from scipy.stats import gmean
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import scipy
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

image= "/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Dried/Location_1_4.jpg"
resolution = 0.0340214067278287
img = cv2.imread(image)
nxx, nyy, _ = img.shape
width = max(nxx, nyy)
maxscale= width*resolution / 8

x= 0
verbose = 1

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

filter=False

if filter:
    sigma_est = estimate_sigma(im, multichannel=False, average_sigmas=True)
    region = denoise_wavelet(im, multichannel=False, rescale_sigma=True,
                                method='VisuShrink', mode='soft', sigma=sigma_est*2)
else:
    region = im.copy()

original = rescale(region,0,255)

nx, ny = original.shape


P = []; M = []
for k in np.linspace(1,nx-1,100):
    [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(np.maximum(nx,ny)/(width*resolution / 0.1), np.maximum(nx,ny)/(width*resolution / 20), 1),  'morl', .5) #cmor10-1.9
    period = 1. / frequencies
    power =(abs(cfs)) ** 2
    power = np.mean(np.abs(power), axis=1)/(period**2)
    P.append(power)

    M.append(period[np.argmax(power)])

p = np.mean(np.vstack(P), axis=0)
p = np.array(p/np.sum(p))

# get real scales by multiplying by resolution (mm/pixel)
scales_3 = np.array(period)

srt = np.sqrt(np.sum(p*((scales_3-np.mean(M))**2)))

# plt.plot(scales, p,'m', lw=2)

p = p+stats.norm.pdf(scales_3, np.mean(M), srt/2)
p = np.hstack([p])
scales_3 = np.hstack([scales_3])
p = p/np.sum(p)
x = 0
# area-by-number to volume-by-number
r_v_3 = (p*scales_3**x) / np.sum(p*scales_3**x) #volume-by-weight proportion

a = scales_3*resolution
print(a)

try:
    S_0 = scipy.integrate.simps(r_v_3[np.where((a<0.063))]) * 100
except IndexError:
    S_0 = 0 

try:
    S_63 = scipy.integrate.simps(r_v_3[np.where((a>0.063)&(a<0.125))]) * 100
except IndexError:
    S_63 = 0 

try:
    S_125 = scipy.integrate.simps(r_v_3[np.where((a>0.125)&(a<0.180))]) * 100
except IndexError:
    S_125 = 0 

try:
    S_180 = scipy.integrate.simps(r_v_3[np.where((a>0.180)&(a<0.250))]) * 100
except IndexError:
    S_180 = 0 

try:
    S_250 = scipy.integrate.simps(r_v_3[np.where((a>0.250)&(a<0.300))]) * 100
except IndexError:
    S_250 = 0 

try:
    S_300 = scipy.integrate.simps(r_v_3[np.where((a>0.300)&(a<0.355))]) * 100
except IndexError:
    S_300 = 0 

try:
    S_355 = scipy.integrate.simps(r_v_3[np.where((a>0.355)&(a<0.425))]) * 100
except IndexError:
    S_355 = 0 

try:
    S_425 = scipy.integrate.simps(r_v_3[np.where((a>0.425)&(a<0.500))]) * 100
except IndexError:
    S_425 = 0 

try:
    S_500 = scipy.integrate.simps(r_v_3[np.where((a>0.500)&(a<0.710))]) * 100
except IndexError:
    S_500 = 0 

try:
    S_710 = scipy.integrate.simps(r_v_3[np.where((a>0.710)&(a<1))]) * 100
except IndexError:
    S_710 = 0 

try:
    S_1000 = scipy.integrate.simps(r_v_3[np.where((a>1)&(a<2))]) * 100
except IndexError:
    S_1000 = 0 

try:
    S_2000 = scipy.integrate.simps(r_v_3[np.where((a>2)&(a<4))]) * 100
except IndexError:
    S_2000 = 0 

try:
    S_4000 = scipy.integrate.simps(r_v_3[np.where((a>4)&(a<8))]) * 100
except IndexError:
    S_4000 = 0 

try:
    S_8000 = scipy.integrate.simps(r_v_3[np.where((a>8))]) * 100
except IndexError:
    S_8000 = 0 


print(S_0)
print(S_63)
print(S_125)
print(S_180)
print(S_250)
print(S_300)
print(S_355)
print(S_425)
print(S_500)
print(S_710)
print(S_1000)
print(S_2000)
print(S_4000)
print(S_8000)