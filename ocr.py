#!bin/evn python
# encoding:utf-8

from PIL import Image
import pytesseract
import re
import sys
import cv2

#print(pytesseract.image_to_string(Image.open('src/test-european.jpg'), lang='fra'))
#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='eng', boxes=False, config="-psm 6")
#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='chi_sim', boxes=False, config="-psm 6")

#图像处理
image = cv2.imread("/Users/fengxuting/Downloads/1463815812385A98C108.jpg")
#str = pytesseract.image_to_string(Image.open('public/uploads/ocr/'+sys.argv[1]),lang='num+eng', boxes=False, config="-psm 6 digits")


(h,w) = image.shape[:2]
center = (w / 2,h / 2)

s = ""
#90 -90 10度一个图
c = 1
for i in range(-90,100,10):
    # print(i)
    M = cv2.getRotationMatrix2D(center,i,0.60)#旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
    rotated = cv2.warpAffine(image,M,(w,h))
    file = 'public/uploads/ocr/f'+str(c)+'_'+sys.argv[1]
    cv2.imwrite(file,rotated, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    s = s+pytesseract.image_to_string(Image.open(file),lang='num+eng', boxes=False, config="-psm 6")
    c = c+1

print(s)
ret = re.findall("\d{4,12}",s)
print len(ret)