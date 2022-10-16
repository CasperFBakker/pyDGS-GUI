  
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
img = cv.imread('/home/casper/Desktop/IMG_2783.JPG',cv.IMREAD_UNCHANGED)
src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
Blurred = cv.medianBlur(gray, 11)
edges = cv.Canny(Blurred,25,50)

# plt.subplot(231),plt.imshow(plt.imread(filename))
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(232),plt.imshow(gray,cmap = 'gray')
# plt.title('Gray-Scaled'), plt.xticks([]), plt.yticks([])

# plt.subplot(233),plt.imshow(Blurred,cmap = 'gray')
# plt.title('Blurred'), plt.xticks([]), plt.yticks([])

# plt.subplot(234),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()


img = cv.imread('/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Canon_Samples/Sample_1_2.JPG',0)
img = cv.medianBlur(img,15)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,120,
                            param1=50,param2=30,minRadius=500,maxRadius=750)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

plt.imshow(cimg)
plt.show()

