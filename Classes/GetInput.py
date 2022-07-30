from Imports.Import_Modules import *
from main import GUI

class GetInput(GUI):
    def __init__(self, master, WindFrame):
        super(GUI,self).__init__()
        self.WindowFrame = WindFrame
        
    def Import_Image(self, *args):
        filetypes = [('Images', '*.png *.jpg *.jpeg *.heif'),
                     ('Any File', '*.*')]
        self.img_path = askopenfilename(title='Open Image file', filetypes=filetypes)
        if self.img_path:
            print("Importing:", self.img_path)
        setattr(GetInput.Import_Image, 'img_path', self.img_path)


    def GetCoinType(self, coin_bank, CoinVar):
        self.coin_type = coin_bank[CoinVar.get()]
        setattr(GetInput.GetCoinType, 'coin_type', self.coin_type)

    def GetBlur(self, val):
        self.ks_blur = int(val)
        setattr(GetInput.GetBlur, 'ks_blur', self.ks_blur)
        return self.ks_blur

    def refreshWindowScale(self):
        self.minR = tk.Scale(self.WindowFrame, from_= 0, to= 150, length=330, width=10, orient='horizontal', command = lambda val: self.SelectMinR(val))
        self.maxR = tk.Scale(self.WindowFrame, from_= 0, to= 150, length=330, width=10, orient='horizontal', command = lambda val: self.SelectMaxR(val))
        self.minR.grid(row=4, column=0, sticky="nsew");     self.maxR.grid(row=5, column=0, sticky="nsew")


    def GetWindowSz(self, WindowVar):
        self.refreshWindowScale()
        self.maxR.configure(state=NORMAL); self.minR.configure(state=NORMAL)
        
        self.WindowSz = WindowVar.get()
        
        self.minR.configure(to=(150 - int(self.WindowSz)))
        self.maxR.configure(from_=(0 + int(self.WindowSz)))

    def SelectMinR(self, val):
        self.minRad = int(val)
        self.maxR.configure(state=NORMAL)
        self.maxR.set(self.minRad + self.WindowSz)
        self.maxR.configure(state=DISABLED)
        setattr(GetInput.SelectMinR, 'MinR', self.minRad)

    def SelectMaxR(self, val):
        self.maxRad = int(val)
        setattr(GetInput.SelectMaxR, 'MaxR', self.maxRad)

    def GetRadiusSp(self, RadiusVar):
        self.RadiusWindow = RadiusVar.get()
        setattr(GetInput.GetRadiusSp, 'RadiusWindow', self.RadiusWindow)