from Imports.Import_Modules import * 
from Imports.Functions import *
from Imports.Import_Classes import *

def GetImageRes(img_path, directory_path):
    filename = os.path.basename(img_path)
    dir_path = os.path.dirname(directory_path)
    dir_name = os.path.basename(dir_path)

    try:
        DataFrame = pd.read_csv("Output data/data_" + dir_name +".csv")
        row = DataFrame[DataFrame["Image name"] == filename].index[0]
        resolution = DataFrame.at[row, 'Pixel size (mm/pixel)']
    except IndexError:
        resolution = 1
    return resolution
    
# =========================================================
def rescale(dat,mn,mx):
    """
    rescales an input dat between mn and mx
    """
    m = min(dat.flatten())
    M = max(dat.flatten())
    return (mx-mn)*(dat-m)/(M-m)+mn

##====================================
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

def run_dgs(image, resolution):
    img = cv2.imread(image)
    nxx, nyy, _ = img.shape
    width = max(nxx, nyy)
    maxscale= width*resolution / 8

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
    filter=False

    if filter:
        sigma_est = estimate_sigma(im, multichannel=False, average_sigmas=True)
        region = denoise_wavelet(im, multichannel=False, rescale_sigma=True,
                                    method='VisuShrink', mode='soft', sigma=sigma_est*2)
    else:
        region = im.copy()

    original = rescale(region,0,255)

    nx, ny = original.shape

    P = []; M = []
    for k in np.linspace(1,nx-1,100):
        [cfs, frequencies] = pywt.cwt(original[int(k),:], np.arange(np.maximum(nx,ny)/(width*resolution / .1), np.maximum(nx,ny)/(width*resolution / 8), 1),  'morl' , .5)
        period = 1. / frequencies
        power =(abs(cfs)) ** 2
        power = np.mean(np.abs(power), axis=1)/(period**2)
        P.append(power)

        M.append(period[np.argmax(power)])

    p = np.mean(np.vstack(P), axis=0)
    p = np.array(p/np.sum(p))

    # get real scales by multiplying by resolution (mm/pixel)
    scales = np.array(period)

    srt = np.sqrt(np.sum(p*((scales-np.mean(M))**2)))

    # plt.plot(scales, p,'m', lw=2)

    p = p+stats.norm.pdf(scales, np.mean(M), srt/2)
    p = np.hstack([0,p])
    scales = np.hstack([0,scales])
    p = p/np.sum(p)
    x = 0
    # area-by-number to volume-by-number
    r_v = (p*scales**x) / np.sum(p*scales**x) #volume-by-weight proportion

    pd = np.interp([.05,.1,.16,.25,.3,.5,.75,.84,.9,.95],np.hstack((0,np.cumsum(r_v))), np.hstack((0,scales)) )

    return pd


path_of_the_directory = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Location_1/'
ext = ('.jpg','.jpeg', '.heif', '.png')

for files in os.listdir(path_of_the_directory):
    if files.endswith(ext):
        dir_name = os.path.basename(os.path.dirname(path_of_the_directory))
        filename = files

        print(files, ': ', GetImageRes(files, path_of_the_directory))  

        [Per_5, Per_10, Per_16, Per_25, Per_30, Per_50, Per_75, Per_84, Per_90, Per_95] = run_dgs((path_of_the_directory + files), GetImageRes(files, path_of_the_directory))
           
        data = files, Per_5, Per_10, Per_16, Per_25, Per_30, Per_50, Per_75, Per_84, Per_90, Per_95

        columns = ['Image name', '5 Percentile', '10 Percentile', '16 Percentile', '25 Percentile', '30 Percentile',
                   '50 Percentile', '75 Percentile', '84 Percentile', '90 Percentile', '95 Percentile']

        temp = pd.DataFrame([data], columns=columns)
        temp.to_csv('Output data/Percentiles/temp_percentile.csv', index=False)


        try: 
            DF = pd.read_csv("Output data/Percentiles/Percentiles_" + dir_name +".csv")

            if filename in DF.values:
                result = tk.messagebox.askquestion(title='Data exist', message='The data from this image is already stored. Do you want to replace the data?')
                if result == 'yes':
                    temp = pd.DataFrame([data], columns=columns)
                    merged = pd.concat([temp, DF])

                    merged = merged.drop_duplicates(subset=['Image name'])
                    merged.to_csv("Output data/Percentiles/Percentiles_" + dir_name +".csv", index=False)

                else:
                    pass
            else:
                temp = pd.DataFrame([data], columns=columns)
                merged = pd.concat([temp, DF])
                merged.to_csv("Output data/Percentiles/Percentiles_" + dir_name +".csv", index=False)

        except FileNotFoundError:
            temp = pd.DataFrame([data], columns=[columns])
            temp.to_csv("Output data/Percentiles/Percentiles_" + dir_name +".csv", index=False)



    else:
        continue
