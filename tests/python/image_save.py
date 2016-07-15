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
import os

f = "../../public/images/damita.jpg"
if(not os.path.isfile(f)):
    print f+"not exsit"
im = Image.open(f)
im_arr = array(im.convert('L'), 'int')


im2 = Image.fromarray(im_arr).convert('RGB')
im2.save("../../public/uploads/test.jpg")

Image.open(f).convert('RGB').save("../../public/uploads/test2.jpg")