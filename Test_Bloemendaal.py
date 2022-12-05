from Imports.Import_Modules import * 
from datetime import datetime
from random import uniform
from time import sleep
from tqdm import tqdm

start_time = datetime.now()

Date = '01_12_22_Egmond'

def Setup_Dir(Date, SubFolder=False):
    if SubFolder:        
        Photo_Dir = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/' + Date + '/' + SubFolder + '/'
        ImageData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/' + Date + '/' + SubFolder + '/'
        OutputData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/' + SubFolder + '/'
        OutputCorrected_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/' +  SubFolder + '/Corrected/'
        OutputOriginal_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/' + SubFolder + '/Uncorrected/'
    else:
        Photo_Dir = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/' + Date + '/'
        ImageData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/' + Date + '/'
        OutputData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/'
        OutputCorrected_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/Corrected/'
        OutputOriginal_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/Uncorrected/'
    return Photo_Dir, ImageData_Dir, OutputData_Dir, OutputCorrected_Dir, OutputOriginal_Dir

def GetImageRes(img_path):
    filename = os.path.basename(img_path)
    dir_path = os.path.dirname(img_path)
    dir_name = os.path.basename(dir_path)

    try:
        DataFrame = pd.read_csv(ImageData_Dir + "data_" + dir_name +".csv")
        row = DataFrame[DataFrame["Image name"] == filename].index[0]
        resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
    except FileNotFoundError:
        DataFrame = pd.read_csv("'/home/casper/Documents/Python/pyDGS-GUI/Output data/Image_data/'data_" + dir_name +".csv")
        row = DataFrame[DataFrame["Image name"] == filename].index[0]
        resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
    return resolution

def PercentageFromPDF(r_v, scales, resolution):
    # Calculating Percentages
    a = (scales*resolution)
    minSz = np.array([0, 0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
    maxSz = np.array([0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8, 20])
    percentage = []
    # if a[0] > 0.063:

    #     percentage.append(69)
    #     minSz = np.array([0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8])
    #     maxSz = np.array([0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8, 12])

    #     _, length =  np.shape(np.where(a<0.125))
    #     percentage.append(((np.trapz(np.interp([np.linspace(a[0], 0.125, 1000)], (scales*resolution), r_v)[0])*length/1000))*100)
    #     for i in range(len(minSz)):
    #         _, length = np.shape(np.where((a>minSz[i])&(a<maxSz[i])))   
    #         percentage.append(((np.trapz(np.interp([np.linspace(minSz[i], maxSz[i], 1000)], (scales*resolution), r_v)[0])*length/1000))*100)
    # else: 
    for i in range(len(minSz)):
        _, length = np.shape(np.where((a>minSz[i])&(a<maxSz[i])))   
        percentage.append(((np.trapz(np.interp([np.linspace(minSz[i], maxSz[i], 1000)], (scales*resolution), r_v)[0])*length/1000))*100)
    return percentage

def Proffitt_Correction(Percentage_Arr, GrainSz_Arr, Power=-1):
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append(value * (GrainSz_Arr[index]**(Power)) )

    return Corrected_Percentages 

def PercentageFromSum(Percentage_Arr):
    Sum = np.sum(Percentage_Arr)
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append((value / Sum)*100)

    return Corrected_Percentages

def Percentage2Percentile(Percentage):
    Percentage = Percentage[::-1]
    Percentile = 100 - np.nancumsum(Percentage)

    Percentile_cor = []
    for index, value in enumerate(Percentile):
        if value < 0:
            Percentile_cor.append(0)
        else:
            Percentile_cor.append(value)

    Percentile_cor = Percentile_cor[::-1]
    
    return Percentile_cor

def rescale(dat,mn,mx):
    """
    rescales an input dat between mn and mx
    """
    m = min(dat.flatten())
    M = max(dat.flatten())
    return (mx-mn)*(dat-m)/(M-m)+mn

# =========================================================
def standardize(img):
    img = np.array(img)
    #standardization using adjusted standard deviation
    N = np.shape(img)[0] * np.shape(img)[1]
    s = np.maximum(np.std(img), 1.0/np.sqrt(N))
    m = np.mean(img)
    img = (img - m) / s
    img = rescale(img, 0, 1)
    del m, s, N

    return img

# =========================================================
def Store_Percentile(path_of_the_directory, Image_Name, Percentile, Description):          

        data = Image_Name, 0, Percentile[0], Percentile[1], Percentile[2], Percentile[3], Percentile[4], Percentile[5], Percentile[6], Percentile[7], Percentile[8], Percentile[9], Percentile[10], Percentile[11], Percentile[12] 
        columns = ['Image name', '0 mm', '0.063 mm', '0.125 mm', '0.180 mm', '0.250 mm', '0.300 mm', '0.355 mm', '0.425 mm', '0.500 mm', '0.710 mm', '1 mm', '2 mm', '4 mm', '8 mm']
                
        dir_path = os.path.dirname(path_of_the_directory)
        dir_name = os.path.basename(dir_path)

        temp = pd.DataFrame([data], columns=columns)
        temp.to_csv('Output data/Percentiles/temp_percentile.csv', index=False)

        try: 
            if len(Description) != 0:
                DF = pd.read_csv(OutputCorrected_Dir + "Percentile_" + dir_name + "_" + Description + ".csv")
            else:
                DF = pd.read_csv(OutputCorrected_Dir + "Percentile_" + dir_name + ".csv")

            if Image_Name in DF.values:
                pass
            else:
                temp = pd.DataFrame([data], columns=columns)
                merged = pd.concat([temp, DF])
                if len(Description) != 0:
                    merged.to_csv(OutputCorrected_Dir + "Percentile_" + dir_name + "_" + Description + ".csv", index=False)
                else:
                    merged.to_csv(OutputCorrected_Dir + "Percentile_" + dir_name + ".csv", index=False)


        except FileNotFoundError:
            temp = pd.DataFrame([data], columns=[columns])
            if len(Description) != 0:
                temp.to_csv(OutputCorrected_Dir + "Percentile_" + dir_name + "_" + Description + ".csv", index=False)
            else:
                temp.to_csv(OutputCorrected_Dir + "Percentile_" + dir_name + ".csv", index=False)
# =========================================================
def Store_Percentage(path_of_the_directory, Image_Name, Percentage, Description):          

        data = Image_Name, Percentage[0], Percentage[1], Percentage[2], Percentage[3], Percentage[4], Percentage[5], Percentage[6], Percentage[7], Percentage[8], Percentage[9], Percentage[10], Percentage[11], Percentage[12], Percentage[13] 
        columns = ['Image name', '0 mm', '0.063 mm', '0.125 mm', '0.180 mm', '0.250 mm', '0.300 mm', '0.355 mm', '0.425 mm', '0.500 mm', '0.710 mm', '1 mm', '2 mm', '4 mm', '8 mm']
                
        dir_path = os.path.dirname(path_of_the_directory)
        dir_name = os.path.basename(dir_path)

        temp = pd.DataFrame([data], columns=columns)
        temp.to_csv('Output data/Percentage/temp_percentage.csv', index=False)

        try: 
            if len(Description) != 0:
                DF = pd.read_csv(OutputOriginal_Dir + "UncorrectedPercentage_" + dir_name + "_" + Description + ".csv")
            else:
                DF = pd.read_csv(OutputOriginal_Dir + "UncorrectedPercentage_" + dir_name + ".csv")

            if Image_Name in DF.values:
                pass
            else:
                temp = pd.DataFrame([data], columns=columns)
                merged = pd.concat([temp, DF])
                if len(Description) != 0:              
                    merged.to_csv(OutputOriginal_Dir + "UncorrectedPercentage_" + dir_name + "_" + Description + ".csv", index=False)
                else:
                    merged.to_csv(OutputOriginal_Dir + "UncorrectedPercentage_" + dir_name + ".csv", index=False)

        except FileNotFoundError:
            temp = pd.DataFrame([data], columns=[columns])
            if len(Description) != 0:            
                temp.to_csv(OutputOriginal_Dir + "UncorrectedPercentage_" + dir_name + "_" + Description + ".csv", index=False)
            else:
                temp.to_csv(OutputOriginal_Dir + "UncorrectedPercentage_" + dir_name + ".csv", index=False)
# =========================================================

input_dir = False

while input_dir == False:
    input_directory = input('Type the name of the directory: ')

    if input_directory.endswith("/"):
        Photo_Dir, ImageData_Dir, OutputData_Dir, OutputCorrected_Dir, OutputOriginal_Dir = Setup_Dir(Date)
        input_dir = True
    else:
        print('Please end the directory name with: "/" ')
        input_dir = False

path_of_the_directory = os.path.join(Photo_Dir, input_directory)
dir_path = os.path.dirname(path_of_the_directory)
dir_name = os.path.basename(dir_path)
print('The working directory will be: ', path_of_the_directory)
print('____________________________________________________________________________________________________________________')
answer = False 

while answer == False:
    save_Percentages = input('Do you want to save the uncorrected percentages? (y/n) ')

    if save_Percentages == "y" or "yes":
        print("Uncorrected percentages will be stored")
        answer = True     
    elif save_Percentages == "n" or "no":
        print("Uncorrected percentages will not be stored")
        answer = True
    else: 
        print("please answer with y or n")
print('____________________________________________________________________________________________________________________')
Correction = False 

while Correction == False:
    save_Correction = input('Do you want to apply and store the correction? (y/n) ')

    if save_Correction == "y" or "yes":
        print("Correction will be preformed")
        Correction = True     
    elif save_Correction == "n" or "no":
        print("No correction is done")
        Correction = True
    else: 
        print("please answer with y or n")

print('____________________________________________________________________________________________________________________')
Description_Data = input('Give a description for stored data: ')
if len(Description_Data) == 0:
    print("The data will be stored as: /..._" + dir_name + ".csv")
else:
    print("The data will be stored as: /..._" + dir_name + "_" + Description_Data + ".csv")
print('____________________________________________________________________________________________________________________')

ext = ('.jpg', '.JPG', '.jpeg', '.heif', '.png')

for files in os.listdir(path_of_the_directory):
    if files.endswith(ext):
        image = path_of_the_directory + files  
        resolution = GetImageRes(image)
        print(files, resolution)

        # ========================================================================
        # **************************** Pre-Processing ****************************
        # ======================================================================== 

        img = cv2.imread(image)
        nxx, nyy, _ = img.shape
        width = max(nxx, nyy)

        im = imread(image)   # read the image straight with imread
        im = np.squeeze(im)  # squeeze singleton dimensions
        if len(np.shape(im))>3:
            im = im[:, :, :3]            # only keep the first 3 bands

        if len(np.shape(im))==3: # if rgb, convert to grey
            im = (0.299 * im[:,:,0] + 0.5870*im[:,:,1] + 0.114*im[:,:,2]).astype('uint8')

        nx,ny = np.shape(im)
        if nx>ny:
            im=im.T

        im = standardize(im)
        region = im.copy()
        original = rescale(region,0,255)
        nx, ny = original.shape

        # ========================================================================
        # ***************************** Small Scales *****************************
        # ======================================================================== 

        P = []; M = []
        for k in tqdm(np.linspace(1,nx-1,100)):
            [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(5, np.maximum(nx,ny)/(width*resolution / 8), 1),  'morl', .5) 
            period = 1. / frequencies
            power =(abs(cfs)) ** 2
            power = np.mean(np.abs(power), axis=1)/(period**2)
            P.append(power)

            M.append(period[np.argmax(power)])
            sleep(uniform(0.005, 0.01))
        p = np.mean(np.vstack(P), axis=0)
        p = np.array(p/np.sum(p))

        # get real scales by multiplying by resolution (mm/pixel)
        scales = np.array(period)

        srt = np.sqrt(np.sum(p*((scales-np.mean(M))**2)))

        p = p+stats.norm.pdf(scales, np.mean(M), srt/2)
        p = np.hstack([p])
        scales = np.hstack([scales])
        p = p/np.sum(p)
        # x = -0.5
        # r_v = (p*scales**x) / np.sum(p*scales**x) #volume-by-weight proportion
        # scales = np.array(period)*resolution

        # pddd = np.interp([.05,.1,.16,.25,.3,.5,.75,.84,.9,.95],np.hstack((0,np.cumsum(r_v))), np.hstack((0,scales)) )
        # print(pddd)
        percentage_1 = PercentageFromPDF(p, scales, resolution)
        Uncorrected_Percentage = PercentageFromSum(percentage_1)
        # ========================================================================
        # ****************************** Correction ******************************
        # ======================================================================== 
        GrainSz_1 = [0.063, 0.125, 0.180, 0.250, 0.300, 0.355, 0.425, 0.500, 0.710, 1, 2, 4, 8]

        Cor_1_1 = PercentageFromSum(percentage_1[1:])
        Cor_1_2 = PercentageFromSum(Proffitt_Correction(Cor_1_1, GrainSz_1, Power=-1))
        Corrected_Percentage = Cor_1_2
        Percentiles = Percentage2Percentile(Cor_1_2)

        Store_Percentile(path_of_the_directory, files, Percentiles, Description_Data)
        
        if save_Percentages == "y":
            Store_Percentage(path_of_the_directory, files, Uncorrected_Percentage, Description_Data)

        if save_Correction == "y":
            Percentiles = Percentage2Percentile(Corrected_Percentage)
            
            Store_Percentile(path_of_the_directory, files, Percentiles, Description_Data)


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
