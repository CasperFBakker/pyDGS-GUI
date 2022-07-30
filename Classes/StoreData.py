from Imports.Import_Modules import *
from Classes.GetInput import GetInput

class Store_Img_data():
    def __init__(self):
        self.Meta_data()
        
    def Scale_Img(self, img_path, r_final, coin_type):
        coin_vault = {"2_Euro": 25.75, "1_Euro": 23.25, "50_Cent": 24.25,
                    "20_Cent": 22.25, "10_Cent": 19.75, "5_Cent": 21.25}

        dia_coin_pix = r_final * 2 
        coin_dia_mm = coin_vault[coin_type]
        size_pixel = coin_dia_mm / dia_coin_pix # pixel size in mm

        image = cv2.imread(img_path, cv2.IMREAD_COLOR) # Read the image 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        [height, width, _] = np.shape(image)
        height *= size_pixel
        width *= size_pixel

        return height, width, size_pixel

    def Calc_HeightAboveBed(self, model, focal_length, height, width, size_pixel):
        if model == 'SM-A515F':
            img_heigth = min(height, width)
            heightabovebed = (focal_length * img_heigth / 3.4) * size_pixel
        else: 
            heightabovebed = np.nan
        return heightabovebed

    def Convert_GPS(self, gps_latitude, gps_latitude_ref, gps_longitude, gps_longitude_ref):
        lat = gps_latitude
        lon = gps_longitude

        Latitude = (str(int(lat[0]))+"°"+str(int(lat[1]))+"'"+str(lat[2])+'" '+gps_latitude_ref) 
        Longitude = (str(int(lon[0]))+"°"+str(int(lon[1]))+"'"+str(lon[2])+'" '+gps_longitude_ref) 
        return Latitude, Longitude
    
    
    def Storing_data(self, *args):
        path = GetInput.Import_Image.img_path
        coin_type = GetInput.GetCoinType.coin_type

        if hasattr(Cplt.update, 'r_final'):
            Store_Img_data.Meta_data(self, path, Cplt.update.r_final, coin_type)
        else:
            Store_Img_data.Meta_data(self, path, Cplt.update.r_coin, coin_type)

    def Meta_data(self, img_path, r_coin, coin_type):
        with open(img_path, 'rb') as img_file:
            img = Image(img_file)

        filename = os.path.basename(img_path)

        height, width, size_pixel = Store_Img_data.Scale_Img(self, img_path, r_coin, coin_type)
        heightabovebed = Store_Img_data.Calc_HeightAboveBed(self, img.get("model"), img.get("focal_length"), img.get("image_height"), img.get("image_width"), size_pixel)
        img_height = img.get("image_height") * size_pixel
        img_width = img.get("image_width") * size_pixel
        Latitude, Longitude = Store_Img_data.Convert_GPS(self, img.get("gps_latitude"), img.get("gps_latitude_ref"), img.get("gps_longitude"), img.get("gps_longitude_ref"))
        
        data = {'Image name': filename, 'Pixel size (mm/pixel)': size_pixel, 'Date/time': img.get("datetime_original"), 'Device': img.get("model"), 
                'Latitude': str(Latitude), 'Longitude': str(Longitude), 'Image height (mm)': img_height, 
                'Image width (mm)': img_width, 'Heigth above bed (mm)': heightabovebed}

        Data = pd.read_csv('data.csv')

        if filename in Data.values:
            tk.messagebox.askquestion(title=':(::(:(:(:(', message='Already exists ')
        else:
            temp = pd.DataFrame(data, index=[0])
            temp.to_csv('temp.csv', index=False)
            
            merged = pd.concat([temp, Data], axis="rows")
            merged.to_csv("data.csv", index=False)