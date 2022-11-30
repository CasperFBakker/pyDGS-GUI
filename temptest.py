from Imports.Import_Modules import * 
from datetime import datetime
from random import uniform
from time import sleep
from tqdm import tqdm
import imutils
import multiprocessing as mp

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

def PercentageFromSum(Percentage_Arr):
    Sum = np.sum(Percentage_Arr)
    Corrected_Percentages = []
    for index, value in enumerate(Percentage_Arr):
        Corrected_Percentages.append((value / Sum)*100)

    return Corrected_Percentages

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

def Store_Percentage(path_of_the_directory, OutputOriginal_Dir, Image_Name, Percentage, Description):          

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

def Angle_loop(Angles):
    
    image = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/26_10_22/Mobile/R10/R10_A1.jpg'
    resolution = 0.0303884711779449
    Photo_Dir, ImageData_Dir, OutputData_Dir, OutputCorrected_Dir, OutputOriginal_Dir = Setup_Dir('26_10_22', 'Mobile')
    # ========================================================================
    # **************************** Pre-Processing ****************************
    # ======================================================================== 

    img = cv2.imread(image)
    nxx, nyy, _ = img.shape
    width = min(nxx, nyy)

    im = imread(image)   # read the image straight with imread
    im = np.squeeze(im)  # squeeze singleton dimensions
    if len(np.shape(im))>3:
        im = im[:, :, :3]            # only keep the first 3 bands

    if len(np.shape(im))==3: # if rgb, convert to grey
        im = (0.299 * im[:,:,0] + 0.5870*im[:,:,1] + 0.114*im[:,:,2]).astype('uint8')

    nx,ny = np.shape(im)
    
    im = rotate_image(img,Angles)  

    im = standardize(im)
    region = im.copy()
    original = rescale(region,0,255)
    nx, ny = original.shape
    # ========================================================================
    # ***************************** Small Scales *****************************
    # ======================================================================== 

    P = []; M = []
    for k in tqdm(np.linspace(1,nx-1,100)):
        [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(5, np.maximum(nx,ny)/(width*resolution / 1), 1),  'morl', .5) 
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

    percentage_1 = PercentageFromPDF(p, scales, resolution)

    # ========================================================================
    # ***************************** Large Scales *****************************
    # ======================================================================== 

    P = []; M = []
    for k in tqdm(np.linspace(1,nx-1,10)):
        [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(np.maximum(nx,ny)/(width*resolution / 1), 
                                                                    np.maximum(nx,ny)/(width*resolution / 20), 1),  'morl', .5) 
        period = 1. / frequencies
        power =(abs(cfs)) ** 2
        power = np.mean(np.abs(power), axis=1)/(period**2)
        P.append(power)

        M.append(period[np.argmax(power)])
        sleep(uniform(0.005, 0.01))
    p = np.mean(np.vstack(P), axis=0)
    p = np.array(p/np.sum(p))

    scales = np.array(period)

    srt = np.sqrt(np.sum(p*((scales-np.mean(M))**2)))

    p = p+stats.norm.pdf(scales, np.mean(M), srt/2)
    p = np.hstack([p])
    scales = np.hstack([scales])
    p = p/np.sum(p)

    percentage_2 = PercentageFromPDF(p, scales, resolution)


    Uncorrected_Percentage = PercentageFromSum((percentage_1[0:10] + percentage_2[10:]))

    Store_Percentage('/home/casper/Documents/Python/pyDGS GUI/Output data/26_10_22/Mobile/Transformed_360/', OutputOriginal_Dir, 'Angle_' + str(Angles), Uncorrected_Percentage, Description='Transformed')


if __name__ == '__main__':

    Angle_List = np.arange(1, 361)

    pool_obj = mp.Pool()
    pool_obj.map(Angle_loop,range(1,360))
