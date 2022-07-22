from Imports.Import_Modules import *

def get_screen_resolution():
    monitors = get_monitors()
    primary = monitors[0]
    w, h = primary.width, primary.height
    return w, h