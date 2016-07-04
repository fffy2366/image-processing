#!bin/evn python
# -*-coding:utf8-*-
'''
name:face.py
$ python face.py input.jpg
'''
import sys
import cv2

# Get user supplied values
imagePath = "public/uploads/face/" + sys.argv[1]
# cascPath = sys.argv[2]
cascPath = "./data/haarcascades/haarcascade_frontalface_alt.xml"
cascPath2 = "./data/haarcascades/haarcascade_frontalface_alt2.xml"
cascPath_lbp = "./data/lbpcascades/lbpcascade_frontalface.xml"

# Create the haar 级联
facecascade = cv2.CascadeClassifier(cascPath_lbp)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(image.shape)
gray = cv2.equalizeHist(gray,gray)#直方图均衡化：直方图均衡化是通过拉伸像素强度分布范围来增强图像对比度的一种方法。
# show("img1",gray)
gray = cv2.medianBlur(gray,3)#降噪？
(height, width, a) = image.shape
# Detect faces in the image
faces = facecascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=2,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))+"\n<br/>"

# 1，如果小于0.5%的 不认为头像。2，多个头像的  与最大的对比，如果比值小于50%，不认为是头像。
faces_area = []
face_count = 0
for (x, y, w, h) in faces:
    face_area = w * h
    # 脸占整个图的比例
    face_scale = (face_area) / float(height * width) * 100
    print("scale %s,x %s,y %s" % (face_scale,x,y))
    # if face_scale<0.5:
    #     continue
    faces_area.append(face_area)

if(len(faces_area)>1):
    face_max = max(faces_area)
    for fa in faces_area:
        # 脸占最大脸的比例
        scale = fa/float(face_max) * 100
        print("scale %s" % (scale))
        print("\n<br/>")
        if(scale<50):
            continue
        else:
            face_count += 1
else:
    face_count = len(faces_area)
print "\n<br/>"+"Filter Found {0} faces!".format(face_count)+"\n<br/>"


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    face_scale = (w * h) / float(height * width) * 100
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite('public/uploads/face/f_' + sys.argv[1], image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
# 显示
# cv2.imshow("Faces found" ,image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
