from Imports.Import_Modules import *
from main import GUI
from Classes.GetInput import GetInput

class Spectrogram(GUI):
    def __init__(self, master, PhotoFrame, PowerFrame, GrainFrame):
        super(GUI,self).__init__()
        self.PhotoFrame = PhotoFrame
        self.PowerFrame = PowerFrame
        self.GrainFrame = GrainFrame
        setattr(Spectrogram, 'PhotoFrame', self.PhotoFrame)
        setattr(Spectrogram, 'PowerFrame', self.PowerFrame)
        setattr(Spectrogram, 'GrainFrame', self.GrainFrame)


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

    def PlotSpectrogram(self, img_path, data, freq, line_pos, scale):

        image = cv2.imread(img_path, cv2.IMREAD_COLOR) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        nx, ny, _ = np.shape(image)
        if nx>ny:
            image= cv2.transpose(image)
        image = cv2.line(image, [0, line_pos], [len(image[1,:]), line_pos], (0, 255, 0), 10)
    
    
        fig = plt.figure(figsize=(8,8))
        fig.add_subplot(411).plot(freq[line_pos,:], data[line_pos,:])
        fig.add_subplot(412).plot(freq[line_pos,:], data[line_pos,:])
        fig.add_subplot(413).plot(freq[line_pos,:], data[line_pos,:])
        fig.add_subplot(414).plot(freq[line_pos,:], data[line_pos,:])


        fig.suptitle('test title', fontsize=20)

        f0 = ttk.Frame(Spectrogram.PowerFrame)
        canvas = FigureCanvasTkAgg(fig, f0)

        canvas._tkcanvas.pack(side=LEFT, fill=BOTH, expand=True)
        f0.place(x=0, y=0)


    def PlotImage(self, img_path, line_pos=100):
        image = cv2.imread(img_path, cv2.IMREAD_COLOR) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        nx, ny, _ = np.shape(image)
        if nx>ny:
            image= cv2.transpose(image)
        image = cv2.line(image, [0, line_pos], [len(image[1,:]), line_pos], (0, 255, 0), 10)
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

    def dgs(self):
        img_path = GetInput.Import_Image.img_path
        image = img_path
        
        try:
            im = imread(image)   # read the image straight with imread 
            im = np.squeeze(im)  # squeeze singleton dimensions
            if len(np.shape(im))>3:
                im = im[:, :, :3]            # only keep the first 3 bands

            if len(np.shape(im))==3: # if rgb, convert to grey
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

        P = []; M = []; data_cfs = []; freq = []
        for k in np.linspace(1,nx-1,100):
            [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(3, np.maximum(nx,ny)/maxscale, 1),  'morl' , .5)

            data_cfs.append(cfs)
            freq.append(frequencies)
            period = 1. / frequencies
            power =(abs(cfs)) ** 2
            power = np.mean(np.abs(power), axis=1)/(period**2)
            P.append(power)
        P = np.array(P)
        print(P)
        freq = np.array(freq)
        print(np.shape(freq))
        setattr(Spectrogram.dgs, 'power', data_cfs)

        Spectrogram.PlotSpectrogram(self, img_path, P, freq, line_pos=1, scale=GetInput.GetScale.Scale)    
        Spectrogram.PlotImage(self, img_path)
        Spectrogram.PlotIntensity(self, original)

    def update_Scale():
        Spectrogram.PlotSpectrogram(self, data_cfs, line=1, scale=GetInput.GetScale.Scale)

 
