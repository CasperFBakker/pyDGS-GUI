from Imports.Import_Modules import *
from main import GUI
from Classes.GetInput import GetInput

class Spectrogram(GUI):
    def __init__(self, master, PhotoFrame, PowerFrame, GrainFrame, TopFrame):
        super(GUI,self).__init__()
        self.PhotoFrame = PhotoFrame
        self.PowerFrame = PowerFrame
        self.GrainFrame = GrainFrame
        self.TopFrame = TopFrame
        setattr(Spectrogram, 'PhotoFrame', self.PhotoFrame)
        setattr(Spectrogram, 'PowerFrame', self.PowerFrame)
        setattr(Spectrogram, 'GrainFrame', self.GrainFrame)
        setattr(Spectrogram, 'TopFrame', self.TopFrame)


    def GetImageRes(self, img_path):
        filename = os.path.basename(img_path)
        dir_path = os.path.dirname(img_path)
        dir_name = os.path.basename(dir_path)

        try:
            DataFrame = pd.read_csv("Output data/data_" + dir_name +".csv")
            row = DataFrame[DataFrame["Image name"] == filename].index[0]
            resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
        except FileNotFoundError:
            tk.messagebox.showinfo(title=':(::(:(:(:(', message='This image has no data stored. Image resolution is taken as: 1. Which means that the unit is in pixels.')
            resolution = 1

        return resolution
       
    def rescale(dat,mn,mx):
        """
        rescales an input dat between mn and mx
        """
        m = min(dat.flatten())
        M = max(dat.flatten())
        return (mx-mn)*(dat-m)/(M-m)+mn

    def standardize(img):
        img = np.array(img)
        #standardization using adjusted standard deviation
        N = np.shape(img)[0] * np.shape(img)[1]
        s = np.maximum(np.std(img), 1.0/np.sqrt(N))
        m = np.mean(img)
        img = (img - m) / s
        img = Spectrogram.rescale(img, 0, 1)
        del m, s, N

        return img

    def PlotSpectrogram(self, img_path, data, line_pos, pwr1, pwr2, pwr3):

        image = cv2.imread(img_path, cv2.IMREAD_COLOR) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        nx, ny, _ = np.shape(image)
        if nx>ny:
            image= cv2.transpose(image)
        image = cv2.line(image, [0, line_pos], [len(image[1,:]), line_pos], (0, 255, 0), 10)
    
        fig = plt.figure(figsize=(8,8))
        fig.add_subplot(311).plot(data[line_pos, pwr1, :])
        fig.add_subplot(312).plot(data[line_pos, pwr2, :])
        fig.add_subplot(313).plot(data[line_pos, pwr3, :])


        fig.suptitle('Spectral power, line position = 1', fontsize=20)

        f0 = ttk.Frame(Spectrogram.PowerFrame)
        canvas = FigureCanvasTkAgg(fig, f0)

        canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=True)
        f0.place(x=0, y=0)

        _, maxScale, _ = np.shape(data)
        self.PowerScale1 = tk.Scale(Spectrogram.TopFrame, variable=tk.IntVar(), from_=0,to_=(maxScale - 1), length = 400, takefocus = 1, 
                                    orient = tk.HORIZONTAL, command = lambda i : Spectrogram.update_Scale(self, data, fig, canvas))
        self.PowerScale1.set(5)
        self.PowerScale1.grid(row=0, column=2)

        self.PowerScale2 = tk.Scale(Spectrogram.TopFrame, variable=tk.IntVar(), from_=0,to_=(maxScale - 1), length = 400, takefocus = 1, 
                                    orient = tk.HORIZONTAL, command = lambda i : Spectrogram.update_Scale(self, data, fig, canvas))
        self.PowerScale2.set(6)
        self.PowerScale2.grid(row=1, column=2)

        self.PowerScale3 = tk.Scale(Spectrogram.TopFrame, variable=tk.IntVar(), from_=0,to_=(maxScale - 1), length = 400, takefocus = 1, 
                                    orient = tk.HORIZONTAL, command = lambda i : Spectrogram.update_Scale(self, data, fig, canvas))
        self.PowerScale3.set(7)
        self.PowerScale3.grid(row=2, column=2)

        self.LinePosScale = tk.Scale(Spectrogram.TopFrame, variable=tk.IntVar(), from_=0,to_=99,length = 400, takefocus = 1, 
                                     orient = tk.HORIZONTAL, command = lambda i : Spectrogram.update_Scale(self, data, fig, canvas))
        self.LinePosScale.set(1)
        self.LinePosScale.grid(row=1, column=1)


    def update_Scale(self, data, fig, canvas):

        pwr1 = self.PowerScale1.get()    
        pwr2 = self.PowerScale2.get()    
        pwr3 = self.PowerScale3.get()    
        line_pos = self.LinePosScale.get() 
    
        fig.clear()
        fig.add_subplot(311).plot(data[line_pos, pwr1, :])
        fig.add_subplot(312).plot(data[line_pos, pwr2, :])
        fig.add_subplot(313).plot(data[line_pos, pwr3, :])

        fig.suptitle(f"Spectral power, line position = {line_pos}", fontsize=20)
        fig.canvas.draw()

    def PlotImage(self, img_path, line_pos):
        image = cv2.imread(img_path, cv2.IMREAD_COLOR) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        nx, ny, _ = np.shape(image)
        if nx>ny:
            image= cv2.transpose(image)
            nx, ny, _ = np.shape(image)
        lines = np.linspace(1,nx-1,100)

        image = cv2.line(image, [0, int(lines[line_pos])], [len(image[1,:]), int(lines[line_pos])], (0, 255, 0), 10)
        px = 1/plt.rcParams['figure.dpi']
        fig = plt.figure(figsize=(440*px, 300*px))
        fig.add_subplot(111).imshow(image)
        

        f0 = ttk.Frame(Spectrogram.PhotoFrame)
        canvas = FigureCanvasTkAgg(fig, f0)
        toolbar = NavigationToolbar2Tk(canvas, f0)
        toolbar.update()
        canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=True)
        f0.place(x=10, y=100)

    def PlotIntensity(self, image):
        px = 1/plt.rcParams['figure.dpi']
        fig = plt.figure(figsize=(440*px, 300*px))
        fig.add_subplot(111).plot(np.arange(0, len(image[1,:])), image[1,:])
        
        f0 = ttk.Frame(Spectrogram.PhotoFrame)
        canvas = FigureCanvasTkAgg(fig, f0)
        toolbar = NavigationToolbar2Tk(canvas, f0)
        toolbar.update()    
        canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=True)
        f0.place(x=10, y=440)

    def PlotImshow(self, power):
        px = 1/plt.rcParams['figure.dpi']
        fig = plt.figure(figsize=(440*px, 300*px))
        fig.add_subplot(111).pcolormesh(power)
        
        f0 = ttk.Frame(Spectrogram.GrainFrame)
        canvas = FigureCanvasTkAgg(fig, f0)
        toolbar = NavigationToolbar2Tk(canvas, f0)
        toolbar.update()    
        canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=True)
        f0.place(x=10, y=440)


    def dgs(self):
        img_path = GetInput.Import_Image.img_path
        image = img_path
        
        try:
            im = imread(image)  
            im = np.squeeze(im)
            if len(np.shape(im))>3:
                im = im[:, :, :3]      

            if len(np.shape(im))==3: 
                im = (0.299 * im[:,:,0] + 0.5870*im[:,:,1] + 0.114*im[:,:,2]).astype('uint8')

            nx,ny = np.shape(im)
            if nx>ny:
                im=im.T
            im = Spectrogram.standardize(im)

        except: 
            print('cannot open '+image)
            sys.exit(2)

        region = im.copy()
        
        resolution = Spectrogram.GetImageRes(self, img_path)
        original = Spectrogram.rescale(region,0,255)
        nx, ny = original.shape
        width = max(nx, ny)
        maxscale = width / (8 / resolution)

        # ======= stage 3 ==========================
        # call cwt to get particle size distribution

        P = []
        for k in np.linspace(1,nx-1,100):
            [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(3, np.maximum(nx,ny)/maxscale, 1),  'morl' , .5)
            power =(abs(cfs)) ** 2
            P.append(power)
        P = np.array(P)

        Spectrogram.PlotSpectrogram(self, img_path, P, line_pos=1, pwr1=1, pwr2=30, pwr3=60)
        Spectrogram.PlotImage(self, img_path, line_pos=99)
        Spectrogram.PlotIntensity(self, original)


 