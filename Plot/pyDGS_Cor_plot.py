import cv2
import matplotlib.pyplot as plt
import numpy as np
def rescale(dat,mn,mx):
    """
    rescales an input dat between mn and mx
    """
    m = min(dat.flatten())
    M = max(dat.flatten())
    return (mx-mn)*(dat-m)/(M-m)+mn

# =========================================================
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


img = cv2.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Canon_Samples/Sample_1_2.JPG',cv2.IMREAD_UNCHANGED)
img_og10 = img.copy()                              # Make copy of image
img_og1 = cv2.cvtColor(img_og10, cv2.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)
img_og2 = cv2.cvtColor(img_og10, cv2.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)



nxx, nyy, _ = img.shape
width = max(nxx, nyy)

im = img   # read the image straight with imread
im = np.squeeze(im)  # squeeze singleton dimensions
if len(np.shape(im))>3:
    im = im[:, :, :3]            # only keep the first 3 bands

if len(np.shape(im))==3: # if rgb, convert to grey
    im = (0.299 * im[:,:,0] + 0.5870*im[:,:,1] + 0.114*im[:,:,2]).astype('uint8')

nxx,nyy = np.shape(im)
if nxx>nyy:
    im=im.T

im = standardize(im)
region = im.copy()
original = rescale(region,0,255)
nx, ny = original.shape


for k in np.linspace(1,nx-1,10):

    imageLine5 = cv2.line(img_og2, (0, int(k)), (int(ny),int(k)), (0,255,0), 5)

for k in np.linspace(1,nx-1,100):
    imageLine100 = cv2.line(img_og1, (0, int(k)), (int(ny),int(k)), (0,255,0), 5)
# plt.imshow(img)
plt.subplot(1,2,1)
plt.imshow(img_og1)
plt.xticks([])
plt.yticks([])
plt.subplot(1,2,2)
plt.imshow(img_og2)
plt.xticks([])
plt.yticks([])
plt.show()