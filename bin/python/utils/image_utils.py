# -*- coding: utf-8 -*-
'''
http://blog.csdn.net/zhangtaolmq/article/details/38438037
'''

__author__ = 'feng'
from PIL import Image




import os
from PIL import *

curdir="/Users/fengxuting/Downloads/"

os.chdir(curdir)

class ImageUtils:
    # 灰度化
    def faceBlankWhite(filename):
        image_file = Image.open(curdir+filename) # open colour image
        image_file = image_file.convert('L') # convert image to black and white
        image_file.save('/Users/fengxuting/Downloads/result.jpg')
    # 二值化
    def RGB2BlackWhite(filename):
        im=Image.open(filename)
        print "image info,",im.format,im.mode,im.size
        (w,h)=im.size
        R=0
        G=0
        B=0

        for x in xrange(w):
            for y in xrange(h):
                pos=(x,y)
                rgb=im.getpixel( pos )
                (r,g,b)=rgb
                R=R+r
                G=G+g
                B=B+b

        rate1=R*1000/(R+G+B)
        rate2=G*1000/(R+G+B)
        rate3=B*1000/(R+G+B)

        print "rate:",rate1,rate2,rate3


        for x in xrange(w):
            for y in xrange(h):
                pos=(x,y)
                rgb=im.getpixel( pos )
                (r,g,b)=rgb
                n= r*rate1/1000 + g*rate2/1000 + b*rate3/1000
                #print "n:",n

                if n>=200 and n <=250:
                    #white
                    im.putpixel( pos,(255,255,255))
                    pass
                else:
                    #black
                    im.putpixel( pos,(0,0,0))

        im.save("/Users/fengxuting/Downloads/result.png")

    def saveAsBmp(fname):
        pos1=fname.rfind('.')
        fname1=fname[0:pos1]
        fname1=fname1+'_2.bmp'
        im = Image.open(fname)
        new_im = Image.new("RGB", im.size)
        new_im.paste(im)
        new_im.save(fname1)
        return fname1



if __name__=="__main__":
    #filename=saveAsBmp("1463988841228ABFC41A.jpg")
    #filename=saveAsBmp("test110.jpg")
    iu = ImageUtils()
    filename=iu.saveAsBmp("1463815812385A98C108.jpg")
    iu.RGB2BlackWhite(filename)

    #faceBlankWhite("p3.png")
