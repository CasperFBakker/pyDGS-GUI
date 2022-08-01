import os
from natsort import natsorted 
img_path = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/08_07_22/Line_1/Line_1_1.jpg'
path_of_the_directory = os.path.split(img_path)[0]
ext = ('.jpeg', 'jpg')
list_pdf = []
for files in natsorted(os.listdir(path_of_the_directory)):
    if files.endswith(ext):
        list_pdf.append(files)  
    else:
        continue

print(list_pdf[0])
'Line_1_38.jpg'
print(list_pdf.index('Line_1_38.jpg'))


index = 1
last = 0
Last = True
if Last:  
    index = index + 1 + last
    Last = False

print(index)