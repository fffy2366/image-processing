#!bin/evn python
#-*-coding:utf8-*-
'''
name:face.py
$ python face.py input.jpg
'''
import sys
import cv2

# Get user supplied values
imagePath = "public/uploads/face/"+sys.argv[1]
#cascPath = sys.argv[2]
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
   flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
   cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('public/uploads/face/f_'+sys.argv[1],image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
#显示
#cv2.imshow("Faces found" ,image)
#cv2.waitKey(0)   
#cv2.destroyAllWindows()