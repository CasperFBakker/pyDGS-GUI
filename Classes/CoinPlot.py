from Imports.Import_Modules import *

class CoinPlots():

    def CoinPlot(self, img_og, y_coin, x_coin, r_coin):
        image_coin = draw_coin(self, img_og, y_coin, x_coin, r_coin)

        fig = plt.figure(figsize=(5,5))
        fig.add_subplot(111).imshow(image_coin)

        f0 = ttk.Frame(self.tab_1_right_frame)
        canvas = FigureCanvasTkAgg(fig, f0)
        toolbar = NavigationToolbar2Tk(canvas, f0)
        toolbar.update()

        canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=True)
        f0.place(x=90, y=40)
        return image_coin

    def CropCoinPlot(self, image, y_coin, x_coin, r_coin):
        crop_image = image[(x_coin - 25 - r_coin): (x_coin + 25 + r_coin),
                           (y_coin - 25 - r_coin):(y_coin + 25 + r_coin)]
        nx, ny, _ = np.shape(crop_image)
        XCenter = int(nx/2); YCenter = int(ny/2)
        
        fig = Figure(figsize=(7,7))
        fig.subplots_adjust(0,0,1,1,0,0)

        ax = fig.add_subplot(111)
        ax.imshow(crop_image)

        f0 = ttk.Frame(self.tab_1_mid_frame)
        canvas = FigureCanvasTkAgg(fig, f0)
        canvas._tkcanvas.grid(row=0, column=0)


        fig.canvas.draw()

        self.r_slider = tk.Scale(f0,variable=tk.IntVar(), from_=-25, 
                    to=25, label='Fine-tune Radius', 
                    orient=tk.HORIZONTAL,length=int(fig.bbox.width), 
                    width=int(fig.bbox.height * 0.05), command = 
                    lambda i : update(self, crop_image, XCenter, YCenter, r_coin, ax, fig, canvas))
        self.r_slider.set(0)
        self.r_slider.grid(row=1, column=0)

        self.x_slider = tk.Scale(f0,variable=tk.IntVar(), from_=-25, 
                    to=25, label='Fine-tune x-position', 
                    orient=tk.HORIZONTAL,length=int(fig.bbox.width), 
                    width=int(fig.bbox.height * 0.05), command = 
                    lambda i : update(self, crop_image, XCenter, YCenter, r_coin, ax, fig, canvas))
        self.x_slider.set(0)
        self.x_slider.grid(row=2, column=0)

        self.y_slider = tk.Scale(f0,variable=tk.IntVar(), from_=-25, 
                    to=25, label='Fine-tune y-position', 
                    orient=tk.HORIZONTAL,length=int(fig.bbox.width), 
                    width=int(fig.bbox.height * 0.05), command = 
                    lambda i : update(self, crop_image, XCenter, YCenter, r_coin, ax, fig, canvas))
        self.y_slider.set(0)
        self.y_slider.grid(row=3, column=0)

        f0.place(x=8, y=10)



def update(self, image, XCenter, YCenter, r_coin, ax, fig, canvas):

    r = self.r_slider.get()
    x = self.x_slider.get()
    y = self.y_slider.get()

    ax.clear()
    ax.imshow(image)

    ax.add_patch(Circle(((x + XCenter),(y + YCenter)), (r + r_coin), fill=False, color="red"))
    ax.add_patch(Circle(((x + XCenter),(y + YCenter)), 2, fill=True, color="black"))
    ax.plot([(XCenter+x-r_coin-r), (x+XCenter+r_coin+r)], [(y+YCenter), (y+YCenter)], color="red", linestyle="--")
    ax.plot([(XCenter+x), (x+XCenter)], [(y+YCenter-r_coin-r), (y+YCenter+r_coin+r)], color="red", linestyle="--")
    fig.canvas.draw()

    setattr(update, 'r_final', (r+r_coin))

def Coin_Dector(self, img_path, ks_blur):

    image = img_path
    img = cv2.imread(image, cv2.IMREAD_COLOR) # Read the image 
    img_og = img.copy() # Make copy of image
    img_og = cv2.cvtColor(img_og, cv2.COLOR_BGR2RGB) # Converting the image to RGB pattern (default = BGR)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Grayscale image
    img = cv2.medianBlur(img, ks_blur) # Blur image 

    find_coin = moving_r_window(img, RadiusWindow=10)   # find the coin in image
    find_coin = np.reshape(find_coin, (1,3))            # remove unused dimension
    pos_coin_rounded = np.uint16(np.around(find_coin))  # rounded position
    [y_coin, x_coin, r_coin]= pos_coin_rounded[0,:] # position of coin and radius of coin (in pixels)

    return y_coin, x_coin, r_coin, img_og

def moving_r_window(image, RadiusWindow, minRadius=0, maxRadius=5):
    coin = 1
    timeout = time.time() + 15
    while np.size(coin) != 3:
        coin = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 120, param1=50, param2=30, 
                                        minRadius=minRadius, maxRadius=maxRadius)
        [minRadius, maxRadius] = [minRadius + RadiusWindow, maxRadius + RadiusWindow]
        if time.time() > timeout: # Set timer of 15s, to prevent endless loop
            raise Exception("Cannot distinguish the coin from image."  
                             "Recommended: change kernel size of median blur.") from None
            break

    return coin

def draw_coin(self, image, y_coin, x_coin, r_coin):
                 
    cv2.circle(image, (y_coin, x_coin), r_coin, (0, 255, 0), 2) # draw edge of coin
    cv2.circle(image, (y_coin, x_coin), 2, (255, 255, 255), 3) # draw center of coin

    return image
    