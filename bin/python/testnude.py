#!bin/evn python
# encoding:utf-8
from __future__ import print_function

import os
from nude import Nude
import time
import cv2
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 人脸识别 排除人脸
def facedetect(file):
    # Get user supplied values
    imagePath = file
    # cascPath = sys.argv[2]
    cascPath = "../../data/haarcascades/haarcascade_frontalface_alt.xml"

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

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return faces
print('start waiting', time.strftime('%H:%M:%S'))
# n = Nude("/Users/fengxuting/Downloads/testphoto/1464317011202A33605A.jpg")
file = ROOT+"/public/uploads/nude/1464319781149AC72DF3.jpg"
faces = facedetect(file)

#计算人脸面积占整个图片的比例
im = Image.open(file)
ori_w, ori_h = im.size
area = 0
for (x, y, w, h) in faces :
    area = area+w*h


print(file)
print((float(area)/(ori_w*ori_h))*100)
n = Nude(file)
n.setFaces(faces)
# n.resize(1000,1000)
n.parse()

# print "",time.strftime()('%H:%M:%S')

print(n.result, n.inspect())

print('stop waiting', time.strftime('%H:%M:%S'))

