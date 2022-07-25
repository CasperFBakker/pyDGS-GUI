import tkinter as tk
from tkinter import ttk
from tkinter import *
from Imports.Import_Modules import *

img_path = '20220708_084819.jpg'


with open(img_path, 'rb') as img_file:
    img = Image(img_file)

lat = img.get("gps_latitude")
lon = img.get("gps_longitude")

Latitude = (str(int(lat[0]))+"°"+str(int(lat[1]))+"'"+str(lat[2])+'" '+img.get("gps_latitude_ref")) 
Longitude = (str(int(lon[0]))+"°"+str(int(lon[1]))+"'"+str(lon[2])+'" '+img.get("gps_longitude_ref")) 


