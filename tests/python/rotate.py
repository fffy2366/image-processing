#!bin/evn python
# -*-coding:utf8-*-


import cv
import math
'''
http://www.cnblogs.com/xianglan/archive/2010/12/26/1917247.html
'''

def LRotate(image,angle):
    h = image.height
    w = image.width
    anglePi = angle*math.pi/180.0
    cosA = math.cos(anglePi)
    sinA = math.sin(anglePi)
    X1 = math.ceil(abs(0.5*h*cosA + 0.5*w*sinA))
    X2 = math.ceil(abs(0.5*h*cosA - 0.5*w*sinA))
    Y1 = math.ceil(abs(-0.5*h*sinA + 0.5*w*cosA))
    Y2 = math.ceil(abs(-0.5*h*sinA - 0.5*w*cosA))
    H = int(2*max(Y1,Y2))
    W = int(2*max(X1,X2))
    size = (W+1,H+1)
    iLRotate = cv.CreateImage(size,image.depth,image.nChannels)

    for i in range(h):
        for j in range(w):
            x = int(cosA*i-sinA*j-0.5*w*cosA+0.5*h*sinA+0.5*W)
            y = int(sinA*i+cosA*j-0.5*w*sinA-0.5*h*cosA+0.5*H)
            if x>-1 and x<image.height and y>-1 and y<image.width:
                iLRotate[x,y] = image[i,j]
    return iLRotate

image = cv.LoadImage('/Users/fengxuting/Downloads/1463815812385A98C108.jpg',1)

iLRotate30 = LRotate(image,30)
iLRotate90 = LRotate(image,90)
cv.SaveImage('/Users/fengxuting/Downloads/result.jpg',iLRotate30)

# cv.ShowImage('image',image)
# cv.ShowImage('iLRotate30',iLRotate30)
# cv.ShowImage('iLRotate90',iLRotate90)
# cv.WaitKey(0)