#!bin/evn python
# -*-coding:utf8-*-
'''
name:face.py
$ python face.py input.jpg
'''
import sys
import cv2

imggray = cv2.imread('../../public/images/skew-linedetection.png');
# cv2.subplot(221);
cv2.imshow('1',imggray)

imgbw = cv2.im2bw(imggray, 0.5)
cv2.subplot(222)
cv2.imshow(imgbw)
imgbw = cv2.im2bw(imggray, 0.25)
cv2.subplot(223)
cv2.imshow(imgbw)
level = cv2.graythresh(imggray)
imgbw = cv2.im2bw(imggray, level)
cv2.subplot(224)
cv2.imshow(imgbw)
