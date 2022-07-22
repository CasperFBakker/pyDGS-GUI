# from Imports.Import_Modules import *

# #=========================================
# def moving_r_window(image, RadiusWindow, minRadius=0, maxRadius=5):
#     coin = 1
#     timeout = time.time() + 15
#     while np.size(coin) != 3:
#         coin = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 120, param1=50, param2=30, 
#                                         minRadius=minRadius, maxRadius=maxRadius)
#         [minRadius, maxRadius] = [minRadius + RadiusWindow, maxRadius + RadiusWindow]
#         if time.time() > timeout: # Set timer of 15s, to prevent endless loop
#             raise Exception("Cannot distinguish the coin from image."  
#                              "Recommended: change kernel size of median blur.") from None
#             break

#     return coin

# #=========================================
# # def Scale_Image(image, r_coin, coin_type):
# #     coin_bank = {"Select Coin Type": 0,"2_Euro": 25.75, "1_Euro": 23.25, "50_Cent": 24.25,
# #                  "20_Cent": 22.25, "10_Cent": 19.75, "5_Cent": 21.25}

# #     dia_coin_pix = r_coin * 2 
# #     coin_dia_mm = coin_bank[coin_type]
# #     size_pixel = coin_dia_mm / dia_coin_pix # pixel size in mm
# #     [height, width, _] = np.shape(image)
# #     height *= size_pixel
# #     width *= size_pixel

# #     return height, width, size_pixel


# #=========================================
# def draw_coin(self, image, y_coin, x_coin, r_coin):
                 
#     cv2.circle(image, (y_coin, x_coin), r_coin, (0, 255, 0), 2) # draw edge of coin
#     cv2.circle(image, (y_coin, x_coin), 2, (255, 255, 255), 3) # draw center of coin

#     # [height, width, size_pixel] = Scale_Image(image, r_coin, coin_type) # find scale of image (in mm)

#     # cv2.putText(image, f'Heigth {height} mm', (50, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 0, 0), 2)
#     # cv2.putText(image, f'Width {width} mm', (550, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 0, 0), 2)
#     # print( f'Heigth: {height} mm, Width: {width} mm, 1 pixel is {size_pixel} mm')
#     return image
    