import os
import sys
from functools import partial

import numpy as np
import pywt
from imageio.v2 import imread
from skimage.restoration import denoise_wavelet, estimate_sigma
from tqdm import tqdm

# rescale_sigma=True required to silence deprecation warnings
_denoise_wavelet = partial(denoise_wavelet, rescale_sigma=True)
import tkinter as tk

import cv2
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
from exif import Image
from scipy.stats import gmean

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Canon_Test/Canon_Volume_Area.csv'))

GrainSize = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4]
Sieve = [0.169343023, 2.055677041, 8.424447242, 21.91593223, 17.82740265, 11.56833727, 10.01627166, 5.260677814, 7.844999595, 3.029767558, 4.034781584, 3.975879663, 2.897238236, 0.979244436]

for i in range(5):
    plt.scatter(GrainSize, data[i, 2:14], color='b', label='Loc_1')
    plt.scatter(GrainSize, data[i+5, 2:14], color='g', label='Loc_2')
    plt.scatter(GrainSize, data[i+10, 2:14], color='r', label='Loc_3')
    plt.scatter(GrainSize, data[i+15, 2:14], color='pink', label='Loc_4')
    plt.scatter(GrainSize, data[i+20, 2:14], color='grey', label='Loc_6')
    plt.scatter(GrainSize, data[i+25, 2:14], color='cyan', label='Loc_7')

plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.show()
# 0.148597278, 
# 0.008683264, 
# 0.216738201, 
# 0.023980671, 
# 0.676852795, 
# 0.290200805, 
####### [0.125000000, 0.180000000,  0.250000000, 0.300000000, 0.355000000, 0.425000000, 0.500000000, 0.710000000, 1.000000000, 2.000000000, 4.000000000]
loc_1 = [1.266866149, 1.877556331,	2.255660207, 1.721245708, 2.511556993, 1.530079302,	2.3428572 ,  1.557115116, 0.605814065, 0.364562933,	0.205546663]            
loc_2 = [0.269080143, 1.998641239,	5.961839209, 4.794802701, 3.82363378,  2.397772427,	1.749179278, 0.527692927, 0.343169056, 0.283023691,	0.240964159]    
loc_3 = [1.582391363, 3.805976676,	5.796237937, 3.726991452, 2.242338404, 1.029703252,	0.690447184, 0.412431208, 0.39649632,  0.427441727, 0.823549688]
loc_4 = [0.409973985, 1.27799601 ,  3.148445937, 2.326959229, 2.526866959, 1.520752195,	1.202311239, 0.78596808	, 0.822518604, 0.765318451, 0.770353047]
loc_6 = [2.902412854, 5.522443546,	6.275851844, 3.882378345, 2.661947471, 1.393047684,	0.812313388, 0.269463841, 0.154345667, 0.222271072, 0.314897465]
loc_7 = [1.976828152, 3.139432124,	4.043443854, 3.66083334	, 3.070290191, 1.608089313,	0.981915085, 0.535561869, 0.721162659, 0.569188263,	0.149589102]

 ##0.010629978,  [0.349370857, 2.037759073, 5.976322015, 4.887660951, 3.81002105, 2.49647698, 1.718080908, 0.507354278, 0.333553176, 0.271758512, 0.26058242]
loc_6_2 = [2.864090048, 5.795584208, 6.479530322, 4.006444432, 2.568239338, 1.35292634, 0.787777519,  0.259375872, 0.150699402, 0.229397698, 0.324942646]
#0.111860866, 0.737824252,

plt.plot(GrainSize[1:],loc_1, label='Loc_1')
plt.plot(GrainSize[1:],loc_2, label='Loc_2')

plt.plot(GrainSize[1:],loc_3, label='Loc_3')
plt.plot(GrainSize[1:],loc_4, label='Loc_4')
plt.plot(GrainSize[1:],loc_6, label='Loc_6')
plt.plot(GrainSize[1:],loc_6_2, label='Loc_6_2')
plt.plot(GrainSize[1:],loc_7, label='Loc_7')

plt.legend()
plt.xscale("log")

plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.show()

data = np.array(pd.read_csv('/home/casper/Documents/Python/pyDGS GUI/Output data/08_07_22/Sample_Photos/Canon_Test/Original_Canon_Samples_Test.csv'))

for i in range(5):
    plt.scatter(GrainSize, data[i, 2:14], color='b', label='Loc_1')
    plt.scatter(GrainSize, data[i+5, 2:14], color='g', label='Loc_2')
    plt.scatter(GrainSize, data[i+10, 2:14], color='r', label='Loc_3')
    plt.scatter(GrainSize, data[i+15, 2:14], color='pink', label='Loc_4')
    plt.scatter(GrainSize, data[i+20, 2:14], color='grey', label='Loc_6')
    plt.scatter(GrainSize, data[i+25, 2:14], color='cyan', label='Loc_7')

plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.grid(which='major', linewidth=2, linestyle='-')
plt.grid(which='minor', linewidth=1, linestyle='--')
plt.show()
