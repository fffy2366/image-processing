#!bin/evn python
# encoding:utf-8

from PIL import Image
import pytesseract
import re
import sys
import cv2
import os
from bin.python.utils.string_utils import StringUtils

#print(pytesseract.image_to_string(Image.open('src/test-european.jpg'), lang='fra'))
#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='eng', boxes=False, config="-psm 6")
#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='chi_sim', boxes=False, config="-psm 6")
def delImg(file):
    if os.path.isfile(file):
        os.remove(file)
    else:
        print(file+" not a file")

def getMaxLen(s):
    su = StringUtils()
    # Todo：获取最大值
    maxDig = 0
    maxStr = ""
    for ss in s.splitlines():
        d = su.countdigits(ss)
        if(d>maxDig):
            maxStr = ss

    return maxStr
#图像处理
ori_file = 'public/uploads/ocr/'+sys.argv[1]
dis_file = 'public/uploads/ocr/o_' + sys.argv[1]
image = cv2.imread(ori_file)

#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='num+eng', boxes=False, config="-psm 6 digits")
# 灰度化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(dis_file, gray, [int(cv2.IMWRITE_JPEG_QUALITY), 100])



(h,w) = image.shape[:2]
center = (w / 2,h / 2)

# s = pytesseract.image_to_string(Image.open(ofile),lang='eng', boxes=False, config="-psm 6")
s = pytesseract.image_to_string(Image.open(dis_file),lang='eng', boxes=False, config="-psm 6")
#90 -90 10度一个图
c = 1
# for i in range(-90,100,10):
#     # print(i)
#     M = cv2.getRotationMatrix2D(center,i,0.60)#旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
#     rotated = cv2.warpAffine(image,M,(w,h))
#     file = 'public/uploads/ocr/f'+str(c)+'_'+sys.argv[1]
#     cv2.imwrite(file,rotated, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
#     s = s+"||||"+pytesseract.image_to_string(Image.open(file),lang='eng', boxes=False, config="-psm 6")
#     c = c+1
#     #删除
#     delImg(file)

# print(s)
print(s.splitlines(True))
print(getMaxLen(s))

# ret = re.findall("\d{4,12}",s)
# print len(ret)