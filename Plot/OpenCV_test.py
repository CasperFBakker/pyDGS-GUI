  
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt

# img = cv.imread('/home/casper/Desktop/IMG_2783.JPG',0)
# edges = cv.Canny(img,25,50)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()


###############################################################    

import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

filename = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Canon_Samples/Sample_1_2.JPG'
img = cv.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Canon_Samples/Sample_1_2.JPG',cv.IMREAD_UNCHANGED)
src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
Blurred = cv.medianBlur(gray, 15)
edges = cv.Canny(Blurred,25,50)

# plt.subplot(411),plt.imshow(plt.imread(filename))
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(412),plt.imshow(gray,cmap = 'gray')
# plt.title('Gray-Scaled'), plt.xticks([]), plt.yticks([])

# plt.subplot(413),plt.imshow(Blurred,cmap = 'gray')
# plt.title('Blurred'), plt.xticks([]), plt.yticks([])

# plt.subplot(414),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

img_og1 = img.copy()                              # Make copy of image
img_og1 = cv.cvtColor(img_og1, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

circles1 = cv.HoughCircles(Blurred, cv.HOUGH_GRADIENT, 1, 120, param1=50, param2=30, minRadius=0, maxRadius=50)
circles2 = cv.HoughCircles(Blurred, cv.HOUGH_GRADIENT, 1, 120, param1=50, param2=30, minRadius=300, maxRadius=350)
circles3 = cv.HoughCircles(Blurred, cv.HOUGH_GRADIENT, 1, 120, param1=50, param2=30, minRadius=600, maxRadius=650)

if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in circles1[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(img_og1, center, 2, (255, 255, 255), 3) 
        # circle outline
        radius = i[2]
        cv.circle(img_og1, center, radius,  (0, 255, 0), 20)

img_og2 = img.copy()                              # Make copy of image
img_og2 = cv.cvtColor(img_og2, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

if circles2 is not None:
    circles2 = np.uint16(np.around(circles2))
    for i in circles2[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(img_og2, center, 2, (255, 255, 255), 3) 
        # circle outline
        radius = i[2]
        cv.circle(img_og2, center, radius,  (0, 255, 0), 20)


img_og3= img.copy()                              # Make copy of image
img_og3 = cv.cvtColor(img_og3, cv.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

if circles3 is not None:
    circles3 = np.uint16(np.around(circles3))
    for i in circles3[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(img_og3, center, 2, (255, 255, 255), 3) 
        # circle outline
        radius = i[2]
        cv.circle(img_og3, center, radius,  (0, 255, 0), 20)



plt.imshow(img_og1), plt.xticks([]), plt.yticks([]),plt.title('Min r: 0, Max r:50', fontsize=20);plt.show()
plt.imshow(img_og2), plt.xticks([]), plt.yticks([]),plt.title('Min r: 300, Max r:350', fontsize=20);plt.show()
plt.imshow(img_og3), plt.xticks([]), plt.yticks([]),plt.title('Min r: 600, Max r:650', fontsize=20);plt.show()
plt.imshow(plt.imread(filename)), plt.title('Original Image', fontsize=20), plt.xticks([]), plt.yticks([]);plt.show()
plt.imshow(gray,cmap = 'gray'), plt.title('Gray-Scaled', fontsize=20), plt.xticks([]), plt.yticks([]);plt.show()
plt.imshow(Blurred,cmap = 'gray'), plt.title('Blurred', fontsize=20), plt.xticks([]), plt.yticks([]);plt.show()

plt.imshow(edges,cmap = 'gray'), plt.title('Edge Image', fontsize=20), plt.xticks([]), plt.yticks([]); plt.show()
