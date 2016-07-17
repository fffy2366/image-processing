__author__ = 'feng'
# import the necessary packages
from PIL import Image
import imagehash
imagePath = "../../public/images/damita_c.jpg"
image = Image.open(imagePath)
h = str(imagehash.dhash(image))

print h