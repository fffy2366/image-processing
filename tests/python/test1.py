import cv2.cv as cv
import cv2
import sys
from PIL import Image
from pylab import *
import numpy as np
##from array import*


im = Image.open('8.jpg')



##x = np.array([[1,2,3,4],[3,2,4,3]])
##print x
##y = x.tolist()
##x.shape = 1,-1
##print x
##print x[0].tolist().count(3)




pix = im.load()
width = im.size[0]
height = im.size[1]
print width, height
print int(width * height * 0.01), int(width * height * 0.03)

im_Gray = np.array(im.convert('L'), 'int')
print im_Gray[80, 120]

im_Gray1 = im_Gray.reshape((1, -1))

l = im_Gray1[0].tolist()
for i in range(0, 256):
    y = l.count(i)
    ##    print i,y


    if y > 2500 and y < 5000:
        # print i, y

        for a in range(0, width):
            for b in range(0, height):
                if im_Gray[a, b] <> i:
                    im_Gray[a, b] = 255
                else:
                    im_Gray[a, b] = 0
    break

gray()
imshow(im_Gray)
show()
