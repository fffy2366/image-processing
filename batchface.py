#!bin/evn python
# -*-coding:utf8-*-
'''
从数据库选取图片
批量检测人脸
name:face.py
$ python face.py input.jpg
'''
import sys
import cv2
from bin.python.models.images import Images
imgDir = "/Users/fengxuting/Downloads/photo/photo_pass/photo_pass/"

def detect(filename):
    # Get user supplied values
    imagePath = imgDir + filename
    cascPath = "./data/haarcascades/haarcascade_frontalface_alt.xml"

    # Create the haar 级联
    facecascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(image.shape)
    (height, width, a) = image.shape
    # Detect faces in the image
    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        face_scale = (w * h) / float(height * width) * 100
        print("name %s,scale %s" % (filename,face_scale))


if __name__ == '__main__':
    images = Images().findByFace(2)
    for i in images:
        # print(i['name'])
        detect(i['name'])