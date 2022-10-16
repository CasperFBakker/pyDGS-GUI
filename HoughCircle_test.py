import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math 

filename = '/home/casper/Desktop/IMG_2783.JPG'
img = cv.imread('/home/casper/Desktop/IMG_2783.JPG',cv.IMREAD_UNCHANGED)
src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
Blurred = cv.medianBlur(gray, 11)
edges = cv.Canny(Blurred,25,50) 

print(np.shape(edges))
print(edges[77,855])
blank = np.zeros([1750,1750])
x_coord, y_coord = np.where(edges==255)

r = 155
max_circles = 30
circle = 0
for y, x in zip(y_coord, x_coord):
  circle = circle + 1
  for theta in range(0, 360):
    a = int(x - r * math.cos(theta * math.pi / 180))
    b = int(y - r * math.sin(theta * math.pi / 180))
    if a > 0 and a < columns and b > 0 and b < rows:
      accumulator_array[b, a] = accumulator_array[b, a] + 1
      L = accumulator_array.max()
      log_accumulator_array = accumulator_array.copy()
      if np.log(L) != 0.0:
        log_accumulator_array = L * np.log(1 + accumulator_array) / np.log(L)

      # velocity of the video
      v = v + 1
      if v > velocity:
        v = 0

        if circle < max_circles:
          output_fig = plt.figure(figsize=(8, 4))
          edges_ax = output_fig.add_subplot(121)
          # draw input image with actual position and radius
          edges_ax.imshow(edges_array, cmap='gray')
          plt.title('Image edges')
          edges_ax.plot([x, a], [y, b], 'r-', linewidth=0.5)
          edges_ax.plot(a, b, 'r+', linewidth=0.5)
          edges_ax.set_xlim([0 - figure_border, columns + figure_border])
          edges_ax.set_ylim([rows + figure_border, 0 - figure_border])
          # draw ancillary lines
          edges_ax.plot([x, x], [0.0, y], color='gray', linestyle='--', linewidth=0.5)
          edges_ax.plot([0.0, x], [y, y], color='gray', linestyle='--', linewidth=0.5)

          # draw partial accumulator
          accumulator_ax = output_fig.add_subplot(122)
          accumulator_ax.imshow(log_accumulator_array, cmap='hot')
          plt.title('Accumulator')
          accumulator_ax.plot(a, b, 'r+', linewidth=0.5)
          accumulator_ax.set_xlim([0 - figure_border, columns + figure_border])
          accumulator_ax.set_ylim([rows + figure_border, 0 - figure_border])
          # save current image
          plt.tight_layout()
          output_fig.savefig(filename_in_animation+str(step).zfill(6)+".png", format='png', dpi=200)
          plt.close()
          step = step + 1
          print(step)



r = []
for i in range(1000):
    r.append(x_coord[i])
    r.append(y_coord[i])
    test = cv.circle(blank, (x_coord[i], y_coord[i]), 750, (255,0,0), 2)
    plt.imshow(test,  cmap='hot' )

print('save')
plt.savefig('test.jpg')
# plt.show()
