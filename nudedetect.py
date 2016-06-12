#!bin/evn python
# encoding:utf-8

from __future__ import print_function

import os
import sys
from nude import Nude
import time
import cv2

ROOT = os.path.dirname(os.path.abspath(__file__))

print('start waiting', time.strftime('%H:%M:%S'), '\n<br/>')
file = "public/uploads/nude/" + sys.argv[1]


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

faces = facedetect(file)
n = Nude(file)
n.setFaces(faces) ;
# n.resize(1000,1000)
n.parse()

print(n.result, n.inspect(), '\n<br/>')

print('stop waiting', time.strftime('%H:%M:%S'), '\n<br/>')
