from Imports.Import_Modules import * 
from Imports.Functions import *
from Imports.Import_Classes import *


class GUI(object):
    def __init__(self, master):
        super().__init__()
        self.initComplete = 0

        self.frame = ttk.Frame(master)
        self.frame.pack(fill=BOTH, expand=tk.YES)
        self.master = master

        # set the window location
        self.master.title("pyDGS GUI")
        self.master.geometry(f"{get_screen_resolution()[0]}x{get_screen_resolution()[1]}")

        self.image_imported = False

        # ======================  Make a Widget Frame =============
        self.notebook = ttk.Notebook(self.frame)
        tab_1 = ttk.Frame(self.notebook)

        tab_1.grid_columnconfigure(0, weight=1)
        tab_1.grid_rowconfigure(0, weight=1)
        tab_1.grid_columnconfigure(1, weight=50)
        tab_1.grid_columnconfigure(2, weight=50)
        tab_1.grid_rowconfigure(1, weight=1)
        tab_1.grid_rowconfigure(2, weight=1)

        tab_1.grid(row=0, column=0,sticky='NSEW')
        tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(tab_1, text="Image Resolution")
        self.notebook.add(tab_2, text="pyDGS: Spectrogram")
        self.notebook.pack(fill=BOTH, expand=tk.YES)

        # ------------ tab_1 -----------------
        # ------------ Import Image -------------
        tab_1_left_frame = ttk.LabelFrame(tab_1, text="Import Image")
        tab_1_left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.import_file = ttk.Button(tab_1_left_frame, text="From Files", width="14")
        self.import_file.grid(row=0, column=1, sticky="nsew")
        self.import_file.bind("<ButtonRelease-1>", self.Import_Image)

        # ------------ Coin Detection -------------
        tab_1_left_frame_2 = ttk.LabelFrame(tab_1, text="Detection Settings")
        tab_1_left_frame_2.grid(row=1, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")
        self.winframe = tab_1_left_frame_2
        self.CoinVar = StringVar()
        self.coin_bank = {"Select Coin Type": 0,"2 Euro": '2_Euro', "1 Euro": '1_Euro', "50 Cent": '50_Cent',
                     "20 Cent": '20_Cent', "10 Cent": '10_Cent', "5 Cent": '5_Cent'}
        self.CoinType = ttk.OptionMenu(tab_1_left_frame_2, self.CoinVar,  *self.coin_bank, command=self.GetCoinType)
        self.CoinType.grid(row=0, column=0, sticky="nsew")

        
        self.BlurSlide = tk.Scale(tab_1_left_frame_2, from_=1,to_=31, resolution = 2,
                                  length = 400, takefocus = 1, tickinterval=2,orient = tk.HORIZONTAL, command=self.GetBlur)
        self.BlurSlide.set(5)
        self.BlurSlide.grid(row=2, column=0)
    


        self.minR = tk.Scale(tab_1_left_frame_2, from_= 0, to= 150, orient='horizontal', command=self.SelectMinR)
        self.maxR = tk.Scale(tab_1_left_frame_2, from_= 0, to= 150, orient='horizontal', command=self.SelectMaxR)
        self.minR.set(0); self.maxR.set(5) 
        self.minR.configure(state=DISABLED); self.maxR.configure(state=DISABLED)
        self.minR.grid(row=4, column=0, sticky="nsew"); self.maxR.grid(row=5, column=0, sticky="nsew")
        global minRadius, maxRadius
        minRadius = 0; maxRadius = 5
        

        Window_Sizes = ['Select difference min/max radius', 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        self.WindowVar = IntVar()
        self.WindowSize = ttk.OptionMenu(tab_1_left_frame_2, self.WindowVar, *Window_Sizes, command=self.GetWindowSz)
        self.WindowSize.grid(row=3, column=0, sticky="nsew")

        Radius_Steps = ['Select steps radius window', 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        self.RadiusVar = IntVar()

        self.RadiusStep = ttk.OptionMenu(tab_1_left_frame_2, self.RadiusVar, *Radius_Steps, command=self.GetRadiusSp)
        self.RadiusStep.grid(row=6, column=0, sticky="nsew")
        global RadiusWindow
        RadiusWindow = 10
        self.Coin_Detect = ttk.Button(tab_1_left_frame_2, text="Run") 
        self.Coin_Detect.grid(row=7, column=0)
        self.Coin_Detect.bind("<ButtonRelease-1>", self.Search_Coin)

        self.tab_1_mid_frame = ttk.LabelFrame(tab_1, text="Show Image")
        self.tab_1_mid_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

        # ------------ Show Image -------------
        self.tab_1_right_frame = ttk.LabelFrame(tab_1, text="Show Image")
        self.tab_1_right_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky=tk.NSEW)
        
        # ---------- Output Text Box  ----------------
        tab_1_right_frame_3 = ttk.LabelFrame(tab_1, text="Output")
        tab_1_right_frame_3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        self.Save_Data = ttk.Button(tab_1_right_frame_3, text="Save") 
        self.Save_Data.grid(row=1, column=0)
        self.Save_Data.bind("<ButtonRelease-1>", self.Storing_data)


    # Functions
    def Import_Image(self, another_P):
        filetypes = [('Images', '*.png *.jpg *.jpeg *.heif'),
                     ('Any File', '*.*')]
        global img_path
        img_path = askopenfilename(parent=self.master, title='Open Image file',
                                                filetypes=filetypes)
        if img_path:
            print("Importing:", img_path)
        return img_path


    def Search_Coin(self, *args):
        global img_og, y_coin, x_coin, r_coin
        y_coin, x_coin, r_coin, img_og = Coin_Dector(self, img_path, ks_blur, RadiusWindow, minRadius, maxRadius)
        plt.close('all')

        image_coin = Cplt.CoinPlot(self, img_og, y_coin, x_coin, r_coin)
        Cplt.CropCoinPlot(self, image_coin, y_coin, x_coin, r_coin)
            
    def Storing_data(self, *args):
        if hasattr(up, 'r_final'):
            Store.Meta_data(self, img_path, up.r_final, coin_type)
        else:
            Store.Meta_data(self, img_path, r_coin, coin_type)

    def GetCoinType(self, *args):
        global coin_type
        coin_type = self.coin_bank[self.CoinVar.get()]

    def GetBlur(self, val):
        global ks_blur
        ks_blur = int(val)



    def refreshWindowScale(self):
        self.minR = tk.Scale(self.winframe, from_= 0, to= 150, length=330, width=10, orient='horizontal', command=self.SelectMinR)
        self.maxR = tk.Scale(self.winframe, from_= 0, to= 150, length=330, width=10, orient='horizontal', command=self.SelectMaxR)
        self.minR.grid(row=4, column=0, sticky="nsew");     self.maxR.grid(row=5, column=0, sticky="nsew")

    def GetWindowSz(self, frame):
        self.refreshWindowScale()
        self.maxR.configure(state=NORMAL); self.minR.configure(state=NORMAL)
        
        self.WindowSz = self.WindowVar.get()
        
        self.minR.configure(to=(150 - int(self.WindowSz)))
        self.maxR.configure(from_=(0 + int(self.WindowSz)))

    def SelectMinR(self, *argv):
        global minRadius
        self.minR = int(argv[0])
        minRadius = self.minR
        self.maxR.configure(state=NORMAL)

        self.maxR.set(self.minR + self.WindowSz)
        self.maxR.configure(state=DISABLED)

    def SelectMaxR(self, *argv):
        global maxRadius
        maxRadius = int(argv[0])
        self.maxR.configure(state=DISABLED)

    def GetRadiusSp(self, *args):
        global RadiusWindow
        RadiusWindow = self.RadiusVar.get()

def main(): 
    root = ThemedTk(theme="breeze")
    app = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()