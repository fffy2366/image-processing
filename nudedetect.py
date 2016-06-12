#!bin/evn python
# encoding:utf-8

from __future__ import print_function

import os
import sys
from nude import Nude
import time
import cv2
from PIL import Image as image

ROOT = os.path.dirname(os.path.abspath(__file__))

print('start waiting', time.strftime('%H:%M:%S'), '\n<br/>')
IMAGE_DIR = "public/uploads/nude/"
file = IMAGE_DIR + sys.argv[1]
disImg = IMAGE_DIR +"nude_"+sys.argv[1]
# 图片如果宽或高大于300则等比例压缩
def resizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 75}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = image.open(arg['ori_img'])
    ori_w, ori_h = im.size
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):

        widthRatio = heightRatio = None
        ratio = 1
        if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
            if arg['dst_w'] and ori_w > arg['dst_w']:
                widthRatio = float(arg['dst_w']) / ori_w  # 正确获取小数的方式
            if arg['dst_h'] and ori_h > arg['dst_h']:
                heightRatio = float(arg['dst_h']) / ori_h

            if widthRatio and heightRatio:
                if widthRatio < heightRatio:
                    ratio = widthRatio
                else:
                    ratio = heightRatio

            if widthRatio and not heightRatio:
                ratio = widthRatio
            if heightRatio and not widthRatio:
                ratio = heightRatio

            newWidth = int(ori_w * ratio)
            newHeight = int(ori_h * ratio)
        else:
            newWidth = ori_w
            newHeight = ori_h

        im.resize((newWidth, newHeight), image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])
        return arg['dst_img']
    else:
        return arg['ori_img']
#图像压缩

# 人脸识别 排除人脸
def facedetect(file):
    # Get user supplied values
    imagePath = file
    # cascPath = sys.argv[2]
    cascPath = "./data/haarcascades/haarcascade_frontalface_alt.xml"

    # Create the haar 级联
    facecascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return faces

newImg = resizeImg(ori_img=file,dst_img=disImg,dst_w=300,dst_h=300,save_q=100)

faces = facedetect(newImg)
n = Nude(newImg)
n.setFaces(faces)
# n.resize(1000,1000)
n.parse()

print(n.result, n.inspect(), '\n<br/>')

print('stop waiting', time.strftime('%H:%M:%S'), '\n<br/>')
