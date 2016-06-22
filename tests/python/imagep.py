'''
author:xue
func:image process for ocr
'''
import cv2.cv as cv
import cv2
import sys
from PIL import Image
from pylab import *
import numpy as np
##from array import*

a = array([[1, 2, 3, 4, 3, 5, 5], [3, 4, 2, 3, 2, 2, 3], [5, 4, 3, 2, 3, 6, 7]])
print a
b = a[0::1, 2::]
c = a[0::1,0:]
print b
print len(a)
print len(b)

sys.exit(0)

# Get user supplied values
##imagePath = sys.argv[1]
##cascPath = sys.argv[2]
##imagePath = ('images/371.jpg')
im = Image.open("/Users/fengxuting/Downloads/test122.jpg")
im_arr = array(im.convert('L'), 'int')

##pix = im.load()
##array1 = im_arr[30,5] - im_arr[400,333]
##print array1
print im_arr
w = im.size[0]
h = im.size[1]
print w
print h
print im_arr
im_arr1 = im_arr[0::1, 5::]
print im_arr1
x = len(im_arr)
print len(im_arr1)
im_arr2 = im_arr[0::1, 0:-5]
print im_arr2
im_arr3 = im_arr2 - im_arr1
print im_arr3

print sum(im_arr3)
im_arr4 = im_arr3
print im_arr4
##print im_arr4[30]
# for  i in range(0,h):
#     for j in range(0,w-5):
#         if abs(im_arr3[i,j]) < 32:
#             im_arr4[i,j] = 255
#         else:
#             im_arr4[i,j] = 0

for i in range(0, h - 50):
    for j in range(0, w - 10):
        for x in range(5, 25):

            if abs(im_arr3[i, j]) > 16 and im_arr1[i, j + x] == im_arr1[i, j]:
                im_arr4[i, j] = 0
                im_arr4[i, j + x] = 0
            ##                for x in range(5,25,1):
            ####                if h - j > 30:
            ##                    j+=x
            ##                    else:
            ##                        break
            ##                    if im_arr3[i,j] == 0:
            ##                        im_arr4[i,j] = 0
            ##                    else:
            ##                        im_arr4[i,j]
            ####                        x+=1

            else:
                im_arr4[i, j] = 255

imshow(im_arr4)
show()
