import tkinter as tk
from tkinter import ttk
from tkinter import *
class Gui(tk.Tk):
    def __init__(self, parent=None):

        tk.Tk.__init__(self, parent)
       
        self.panel = ttk.Frame()


        self.minR = tk.Scale(self.panel, from_= 0, to= 100, orient='horizontal', command=self.SelectMinR)
        self.maxR = tk.Scale(self.panel, from_= 0, to= 100, orient='horizontal', command=self.SelectMaxR)
        self.minR.grid(row=1, column=0, sticky="nsew")
        self.maxR.grid(row=2, column=0, sticky="nsew")
        self.minR.configure(state=DISABLED)
        self.maxR.configure(state=DISABLED)
        Window_Sizes = ['Select', 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        
        self.WindowVar = IntVar()
        self.WindowSize = ttk.OptionMenu(self.panel, self.WindowVar, *Window_Sizes, command=self.GetWindowSz)
        self.WindowSize.grid(row=0, column=0, sticky="nsew")

        self.panel.grid(row=0, column=0, sticky="w")


    def GetWindowSz(self, size):
        global WindowSz
        self.minR = tk.Scale(self.panel, from_= 0, to= 100, length=330, width=10, orient='horizontal', command=self.SelectMinR)
        self.maxR = tk.Scale(self.panel, from_= 0, to= 100, length=330, width=10, orient='horizontal', command=self.SelectMaxR)
        self.minR.grid(row=1, column=0, sticky="nsew")
        self.maxR.grid(row=2, column=0, sticky="nsew")

        self.WindowSz = self.WindowVar.get()
        self.minR.configure(to=(100 - int(self.WindowSz)))
        self.maxR.configure(from_=(0 + int(self.WindowSz)))



    def SelectMinR(self, *argv):
           
        self.minR = int(argv[0])
        self.maxR.configure(state=NORMAL)

        self.maxR.set(self.minR + self.WindowSz)
        self.maxR.configure(state=DISABLED)

    def SelectMaxR(self, *argv):
        self.maxR.configure(state=DISABLED)

if __name__ == "__main__":
    app = Gui(None)
    app.title('Example')
    app.mainloop() 