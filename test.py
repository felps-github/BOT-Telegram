import os
from PIL import Image
import pytesseract

path = os.path.abspath('./')
dirs = os.listdir(path)
list_photos = []

for file in dirs:
    if ".jpg" in file or ".png" in file:
        list_photos.append(file)

print(list_photos)

for photo in list_photos:
    print(pytesseract.image_to_string(Image.open(photo), config='--psm 6'))