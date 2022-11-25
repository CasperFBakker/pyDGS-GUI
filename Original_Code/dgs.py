"""
pyDGS - a Python framework for wavelet-based digital grain size analysis
pyDGS is an open-source project dedicated to provide a Python framework to
compute estimates of grain size distribution  using the continuous wavelet transform method
of Buscombe (2013) from an image of sediment where grains are clearly resolved.
This program implements the algorithm of:
Buscombe, D. (2013)
Transferable Wavelet Method for Grain-Size Distribution from Images of Sediment Surfaces and Thin Sections,
and Other Natural Granular Patterns. Sedimentology 60, 1709-1732
http://dbuscombe-usgs.github.io/docs/Buscombe2013_Sedimentology_sed12049.pdf
 Author:  Daniel Buscombe
           Marda Science, LLC
           Flagstaff, AZ
           daniel@mardascience.com
 First Revision January 18 2013
For more information visit https://github.com/dbuscombe-usgs/pyDGS
"""

import numpy as np
import sys, os
from imageio import imread
import pywt
from tqdm import tqdm
from skimage.restoration import denoise_wavelet, estimate_sigma
from functools import partial
# rescale_sigma=True required to silence deprecation warnings
_denoise_wavelet = partial(denoise_wavelet, rescale_sigma=True)
import scipy.stats as stats
import pandas as pd
import cv2
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

# =========================================================
# =========================================================
def dgs(image, resolution=1, maxscale=4, verbose=1, x=-0.5, f=0):

   # exit program if no input folder given

   # print given arguments to screen and convert data type where necessary
   if image:
      print('Input image is '+image)

   # ======= stage 1 ==========================
   # read image
   if verbose==1:
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print('Processing image '+image)
   try:
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

   except: # IOError:
       print('cannot open '+image)
       sys.exit(2)


   # # ======= stage 2 ==========================
   # Denoised image using default parameters of `denoise_wavelet`
   # filter=False

   if f==1:
      sigma_est = estimate_sigma(im, multichannel=False, average_sigmas=True)
      region = denoise_wavelet(im, multichannel=False, rescale_sigma=True,
                                 method='VisuShrink', mode='soft', sigma=sigma_est*2)
   else:
      region = im.copy()

   original = rescale(region,0,255)

   nx, ny = original.shape

   # ======= stage 3 ==========================
   # call cwt to get particle size distribution

   P = []; M = []
   for k in np.linspace(1,nx-1,100):
      [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(3, np.maximum(nx,ny)/maxscale, 1),  'morl' , .5)
      period = 1. / frequencies
      power =(abs(cfs)) ** 2
      power = np.mean(np.abs(power), axis=1)/(period**2)
      P.append(power)

      M.append(period[np.argmax(power)])

   p = np.mean(np.vstack(P), axis=0)
   p = np.array(p/np.sum(p))

   scales = np.array(period)#*resolution

   srt = np.sqrt(np.sum(p*((scales-np.mean(M))**2)))

   # plt.plot(scales, p,'m', lw=2)

   p = p+stats.norm.pdf(scales, np.mean(M), srt/2)
   p = np.hstack([0,p])
   scales = np.hstack([0,scales])
   p = p/np.sum(p)

   ind = np.where(p>0)
   p = p[ind]
   scales = scales[ind]

   # area-by-number to volume-by-number
   r_v = (p*scales**x) / np.sum(p*scales**x) #volume-by-weight proportion
   print(r_v)
   # get real scales by multiplying by resolution (mm/pixel)
   scales = np.array(period)
   # ======= stage 5 ==========================
   # calc particle size stats

   pd = np.interp([0, 0.063, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8], (scales*resolution), r_v)

   return {'percentile_values': pd}
   # plt.plot(scales, r_v,'k', lw=2); plt.show()

   # ======= stage 6 ==========================
   # return a dict object of stats


def GetImageRes(img_path):
    filename = os.path.basename(img_path)
    dir_path = os.path.dirname(img_path)
    dir_name = os.path.basename(dir_path)

    try:
        DataFrame = pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/26_10_22/Mobile/' + "data_" + dir_name +".csv")
        row = DataFrame[DataFrame["Image name"] == filename].index[0]
        resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
    except FileNotFoundError:
        DataFrame = pd.read_csv("'/home/casper/Documents/Python/pyDGS-GUI/Output data/Image_data/'data_" + dir_name +".csv")
        row = DataFrame[DataFrame["Image name"] == filename].index[0]
        resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
    return resolution


# =========================================================
# =========================================================
if __name__ == '__main__':

    path_of_the_directory = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R1/'
    ext = ('.jpg', '.JPG', '.jpeg', '.heif', '.png')

    for files in os.listdir(path_of_the_directory):
        if files.endswith(ext):

            image = path_of_the_directory + files  
            resolution = GetImageRes(image)

            img = cv2.imread(image)
            nxx, nyy, _ = img.shape
            width = max(nxx, nyy)
            maxscale = (width*resolution / 8)

            print(dgs(image, resolution=resolution, maxscale=maxscale, verbose=0, x=0, f=0))

            break