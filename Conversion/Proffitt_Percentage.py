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
import tkinter as tk


def GetImageRes(img_path):
    filename = os.path.basename(img_path)
    dir_path = os.path.dirname(img_path)
    dir_name = os.path.basename(dir_path)

    try:
        DataFrame = pd.read_csv("/home/casper/Documents/Python/pyDGS GUI/pyDGS-GUI/Output data/data_" + dir_name +".csv")
        row = DataFrame[DataFrame["Image name"] == filename].index[0]
        resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
    except FileNotFoundError:
        resolution = 1
        pass
        # tk.messagebox.showinfo(title=':(::(:(:(:(', message='This image has no data stored. Image resolution is taken as: 1. Which means that the unit is in pixels.')
        # resolution = 1

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


path_of_the_directory = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Line_1/'

for files in os.listdir(path_of_the_directory):
    if files.endswith('.jpg'):
        image = path_of_the_directory + files  
        print(files)
        resolution = GetImageRes(image)
        print(resolution)
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
            [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(3, np.maximum(nx,ny)/(width*resolution / 12), 1),  'morl', .5) 
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

        a = (scales*resolution)
        minSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
        maxSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8, 12])

        for i in range(len(minSz)):
            _, length = np.shape(np.where((a>minSz[i])&(a<maxSz[i])))
            print(((np.trapz(np.interp([np.linspace(minSz[i], maxSz[i], 1000)], (scales*resolution), r_v)[0])*length/1000))*100)


    else:
        continue

