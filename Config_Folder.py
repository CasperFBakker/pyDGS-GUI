
Date = '26_10_22'

def Setup_Dir(Date, SubFolder=False):
    if SubFolder:        
        Photo_Dir = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/' + Date + '/' + SubFolder + '/'
        ImageData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/' + Date + '/' + SubFolder + '/'
        OutputData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/' + SubFolder + '/'
        OutputCorrected_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/' +  SubFolder + '/Corrected/'
        OutputOriginal_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/' + SubFolder + '/UnCorrected/'
    else:
        Photo_Dir = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/' + Date + '/'
        ImageData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/Image_data/' + Date + '/'
        OutputData_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/'
        OutputCorrected_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/Corrected/'
        OutputOriginal_Dir = '/home/casper/Documents/Python/pyDGS GUI/Output data/' + Date + '/UnCorrected/'
    return Photo_Dir, ImageData_Dir, OutputData_Dir, OutputCorrected_Dir, OutputOriginal_Dir

print(Setup_Dir(Date, 'Mobile'))