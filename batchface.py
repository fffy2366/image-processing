#!bin/evn python
# -*-coding:utf8-*-
'''
从数据库选取图片
批量检测人脸
name:batchface.py
$ python batchface.py
'''
import sys
import cv2
from bin.python.models.images import Images
import threading
import multiprocessing


# imgDir = "/Users/fengxuting/Downloads/photo/photo_del/photo_del/"
imgDir = "D:/photo/photo_pass/"
def show(name,img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
def detect(filename):
    # Get user supplied values
    imagePath = imgDir + filename
    # cascPath = "./data/haarcascades/haarcascade_frontalface_alt2.xml"
    cascPath = "./data/lbpcascades/lbpcascade_frontalface.xml"
    # cascPath = "./data/haarcascades/haarcascades_frontalface_alt_tree.xml"

    # Create the haar 级联
    facecascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray,gray)#直方图均衡化：直方图均衡化是通过拉伸像素强度分布范围来增强图像对比度的一种方法。
    # show("img1",gray)
    gray = cv2.medianBlur(gray,3)#降噪？
    # show("img2",gray)
    # print(image.shape)
    (height, width, a) = image.shape
    # Detect faces in the image
    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))
    # show("img3",gray)
    # cv2.destroyAllWindows()
    # Draw a rectangle around the faces
    # 1，如果小于0.5%的 不认为头像。2，多个头像的  与最大的对比，如果比值小于50%，不认为是头像。
    faces_area = []
    face_count = 0
    for (x, y, w, h) in faces:
        face_area = w * h
        # 脸占整个图的比例
        face_scale = (face_area) / float(height * width) * 100
        print("name %s,scale %s,x %s,y %s,w %s,h %s,area %s" % (filename,face_scale,x,y,w,h,face_area))
        # if face_scale<0.5:
        #     continue
        faces_area.append(face_area)
        # 显示
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.imshow("Faces found" ,image)
        # cv2.waitKey(0)

    # 显示
    # cv2.destroyAllWindows()


    if(len(faces_area)>1):
        face_max = max(faces_area)
        for fa in faces_area:
            # 脸占最大脸的比例
            scale = fa/float(face_max) * 100
            print("scale %s" % (scale))
            if(scale<50):
                continue
            else:
                face_count += 1
    else:
        face_count = len(faces_area)
    print "Filter Found {0} faces!".format(face_count)
    # 更新监测人脸数到数据库
    images = Images().updateFace(filename,face_count)

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

    # detect('1464319613177A1D9E90.jpg')
    # detect('1464319804427A27BB9A.jpg')
    # detect('1464319922780AEAE79B.png')
    #del
    # detect('1464320205821AB7BEE4.jpg')
    # detect('1464320345553AEE2F9E.jpg')
    # detect('1464317841826A9D45E4.jpg')
    # detect('1464317434576AC6BD82.jpg')
    # detect('1464316375514A869DAA.jpg')
    # detect('1464319394752A037CCD.jpg')
    # detect('1464317845545A3080CD.jpg')
    detect('1464318026880ADE2A0B.jpg')

    # main()