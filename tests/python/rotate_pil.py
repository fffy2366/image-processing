#!bin/evn python
# -*-coding:utf8-*-

from PIL import Image
'''
Python 之 使用 PIL 库做图像处理
http://www.cnblogs.com/way_testlife/archive/2011/04/17/2019013.html
'''
im = Image.open("/Users/fengxuting/Downloads/1463815812385A98C108.jpg")
print im.format, im.size, im.mode

out = im.rotate(45) ##逆时针旋转 45 度角。
#out = out.resize((1000,1000),Image.BILINEAR)
#out = out.rotate(-45) ##逆时针旋转 45 度角。
# out = im.transpose(Image.FLIP_LEFT_RIGHT)       #左右对换。
# out = im.transpose(Image.FLIP_TOP_BOTTOM)       #上下对换。
# out = im.transpose(Image.ROTATE_90)             #旋转 90 度角。
# out = im.transpose(Image.ROTATE_180)            #旋转 180 度角。
# out = im.transpose(Image.ROTATE_270)

#out.show()
out.save('/Users/fengxuting/Downloads/result.jpg')