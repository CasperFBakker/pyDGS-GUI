from Imports.Import_Modules import * 
from datetime import datetime
from random import uniform
from time import sleep
from tqdm import tqdm
import imutils

from scipy.ndimage import rotate as rotate_image

ext = ('.jpg', '.JPG', '.jpeg', '.heif', '.png')
path_of_the_directory = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R5/'

image = path_of_the_directory + 'R5_A1.jpg'  
img = cv2.imread(image)
im = rotate_image(img,40)

plt.imshow(im)
plt.show()
