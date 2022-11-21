
from exif import Image


img_path = '/home/casper/Documents/Aardwetenschappen/MSc Thesis/Photo/Bloemendaal/photos_samples/sample01.jpg'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)


print(img.list_all())

print(img.get('model'))
print(img.get('pixel_x_dimension'))
