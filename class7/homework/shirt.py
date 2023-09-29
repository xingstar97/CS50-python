import sys
from PIL import Image, ImageOps
from os import path 

if len(sys.argv)!=3:
    sys.exit("Wrong command line arguments!")
before = sys.argv[1]
after = sys.argv[2]
ext_before = path.splitext(before)[1].lower()
ext_after = path.splitext(after)[1].lower()
if not ext_before or not ext_after in [".jpg",".jpeg",".png"]:
    sys.exit("Wrong file format!")
if ext_before != ext_after:
    sys.exit("File formats do not match!")

shirt = Image.open("shirt.png")
size = shirt.size
try:
    image = Image.open(before)
    image = ImageOps.fit(image, size = size)
    image.paste(shirt, shirt)
    image.save(after)
except FileNotFoundError:
    sys.exit("File not found!")
