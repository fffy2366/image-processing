#!bin/evn python
# -*-coding:utf8-*-
'''

检测眼睛
name:eyedetect.py
$ python eyedetect.py
'''
import sys
import cv2
from bin.python.models.images import Images
import threading
import multiprocessing


imgDir = "/Users/fengxuting/Downloads/photo/photo_pass/photo_pass/"
def detecteyes(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
def detect(filename):
    # Get user supplied values
    imagePath = imgDir + filename
    # cascPath = "./data/haarcascades/haarcascade_eye.xml"
    # cascPath = "./data/haarcascades/haarcascade_mcs_nose.xml"
    cascPath = "./data/haarcascades/haarcascade_mcs_mouth.xml"
    # cascPath = "./data/haarcascades/haarcascades_frontalface_alt_tree.xml"

    # Create the haar 级联
    eyecascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(image.shape)
    (height, width, a) = image.shape
    # Detect faces in the image
    # eyes = eyecascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.1,
    #     minNeighbors=2,
    #     minSize=(30, 30),
    #     flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    # )
    eyes = detecteyes(gray.copy(), eyecascade)
    vis = image.copy()
    draw_rects(vis, eyes, (255, 0, 0))
    cv2.imshow('facedetect', vis)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print "Found {0} eyes!".format(len(eyes))

    # Draw a rectangle around the faces
    # 1，如果小于0.5%的 不认为头像。2，多个头像的  与最大的对比，如果比值小于50%，不认为是头像。
    faces_area = []


    print "Filter Found {0} eyes!".format(len(eyes))
    # 更新监测人脸数到数据库
    # images = Images().updateFace(filename,len(faces))

# 多进程
def main():
    count = multiprocessing.cpu_count()-1
    pool = multiprocessing.Pool(processes=count)
    images = Images().findAll()
    print(len(images))
    # sys.exit(0)
    for f in images:
        pool.apply_async(detect, (f['name'],))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print "Sub-process(es) done."

if __name__ == '__main__':
    # images = Images().findByFace(0)
    # images = Images().findAll()
    # c = 0
    # for i in images:
    #     # print(i['name'])
    #     detect(i['name'])
        # c += 1
        # if c >5 :
        #     break

    detect('1464319613177A1D9E90.jpg')
    # detect('1464319804427A27BB9A.jpg')
    # detect('1464319922780AEAE79B.png')
    # main()