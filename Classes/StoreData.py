from Imports.Import_Modules import *


class Store_Img_data():
    def __init__(self):
        self.Meta_data()

    def Meta_data(self, img_path, r_coin, coin_type):
        with open(img_path, 'rb') as img_file:
            img = Image(img_file)

        filename = os.path.basename(img_path)

        height, width, size_pixel = Scale_Img(self, img_path, r_coin, coin_type)
        heightabovebed = Calc_HeightAboveBed(self, img.get("model"), img.get("focal_length"), img.get("image_height"), img.get("image_width"), size_pixel)
        img_height = img.get("image_height") * size_pixel
        img_width = img.get("image_width") * size_pixel

        test = pd.DataFrame([filename, size_pixel, img.get("datetime_original"), img.get("model"), 
                      img.get("gps_latitude"), img.get("gps_longitude"), img_height, img_width, heightabovebed
                     ], 
                     ['Image name', 'Pixel size (mm/pixel)', 'Date/time', 'Device', 
                      'Latitude', 'Longitude', 'Image height (mm)', 'Image width (mm)', 'Heigth above bed (mm)'])
        test.to_csv('test.csv')

        df = pd.read_csv('test.csv')
        print(df)

def Scale_Img(self, img_path, r_final, coin_type):
    coin_bank = {"Select Coin Type": 0,"2_Euro": 25.75, "1_Euro": 23.25, "50_Cent": 24.25,
                "20_Cent": 22.25, "10_Cent": 19.75, "5_Cent": 21.25}

    dia_coin_pix = r_final * 2 
    coin_dia_mm = coin_bank[coin_type]
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