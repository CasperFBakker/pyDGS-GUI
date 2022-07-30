import os, sys
import numpy as np
import pandas as pd
from screeninfo import get_monitors
import cv2
import time

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.patches import Circle

import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.filedialog import askopenfilename
from tkinter import Menu, StringVar, Label, SUNKEN, SW, X, BOTTOM, Frame, NE, NW, \
    BOTH, TOP, Button, LEFT, SE, Scrollbar, VERTICAL, Text, RIGHT, Y, END, Tk, \
    Canvas, Listbox, Entry, N, S, E, W, YES, Toplevel, ALL, Checkbutton, ttk, FLAT, GROOVE, IntVar, PhotoImage, \
    filedialog


from imageio import imread
import pywt
from tqdm import tqdm
from skimage.restoration import denoise_wavelet, estimate_sigma
from functools import partial
# rescale_sigma=True required to silence deprecation warnings
_denoise_wavelet = partial(denoise_wavelet, rescale_sigma=True)
import scipy.stats as stats
import matplotlib.pyplot as plt

from exif import Image



from Imports.Functions import *
from Imports.Import_Classes import *

from Classes.CoinPlot import *
from Classes.CoinPlot import CoinPlots as Cplt
# from Classes.CoinDector import CoinPlots as CoinDetector
from Classes.StoreData import Store_Img_data as Store

from Classes.GetInput import GetInput

