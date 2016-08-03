#!bin/evn python
# -*-coding:utf8-*-
'''
从数据库选取图片
批量鉴黄
name:batchnude.py
$ python batchnude.py
$ nohup python batchnude.py &
'''
import os
import sys
import cv2
import threading
import multiprocessing
from PIL import Image
from nude import Nude
from bin.python.models.images import Images
from bin.python.config.config import configs

# imgDir = "/Users/fengxuting/Downloads/photo/photo_del/photo_del/"
IMAGE_DIR = configs['image_dir']
class BatchNude:
    # 人脸识别
    def face(self,file):
        # Get user supplied values
        oriImg = IMAGE_DIR + file

        #图像压缩处理
        # disImg = IMAGE_DIR +"ocrdis"+file
        # newImg = resizeImg(ori_img=oriImg,dst_img=disImg,dst_w=2048,dst_h=2048,save_q=100)

        # cascPath = "./data/haarcascades/haarcascade_frontalface_alt.xml"
        cascPath = "./data/lbpcascades/lbpcascade_frontalface.xml"

        # Create the haar 级联
        facecascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(oriImg)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray, gray)  # 直方图均衡化：直方图均衡化是通过拉伸像素强度分布范围来增强图像对比度的一种方法。
        gray = cv2.medianBlur(gray, 3)  # 降噪？
        (height, width, a) = image.shape
        # Detect faces in the image
        faces = facecascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=2,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        # 1，如果小于0.5%的 不认为头像。2，多个头像的  与最大的对比，如果比值小于50%，不认为是头像。
        faces_area = []
        face_count = 0
        for (x, y, w, h) in faces:
            face_area = w * h
            # 脸占整个图的比例
            face_scale = (face_area) / float(height * width) * 100
            # print("name %s,scale %s,x %s,y %s,w %s,h %s,area %s" % (file,face_scale,x,y,w,h,face_area))
            # if face_scale<0.5:
            #     continue
            faces_area.append(face_area)

            # 显示
            # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.imshow("Faces found" ,image)
            # cv2.waitKey(0)
        # 显示
        # cv2.destroyAllWindows()

        faces_new = []
        if(len(faces_area)>1):
            face_max = max(faces_area)
            for index,face in enumerate(faces) :
                (x, y, w, h) = face
                # 脸占最大脸的比例
                scale = (w*h)/float(face_max) * 100
                # print("scale %s" % (scale))
                if(scale<50):
                    # delete(faces,index,axis=0)
                    pass
                else:
                    faces_new.append(face)
        else:
            faces_new = faces

        return faces_new

    # 裁剪人脸以下的图片
    def cropImg(self,file,faces):
        oriImg =  IMAGE_DIR + file
        # 裁剪人脸以下最多五倍高度的图片
        # ipl_image = cv.LoadImage(oriImg)
        ipl_image = Image.open(oriImg)

        # print(ipl_image.height)
        if (len(faces) < 1):
            print("no face")
            return faces
        (x, y, w, h) = faces[0]
        yy = int(y + 1.5*h)

        hh = h * 6
        (width,height) = ipl_image.size
        if (hh > height - y):
            hh = height - y
        if(yy>=height):
            return False
        dst = ipl_image.crop((x, yy, x + w, y + hh))
        dst.save(IMAGE_DIR + file)
        return True
    # 文件是否存在
    def is_file(self,file):
        if (not os.path.isfile(file)):
            print(file," not exist")
            # sys.exit(0)
        return 1
    # 图片如果宽或高大于300则等比例压缩
    def resizeImg(self,**args):
        args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 75}
        arg = {}
        for key in args_key:
            if key in args:
                arg[key] = args[key]
        im = Image.open(arg['ori_img'])
        ori_w, ori_h = im.size

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

        im.resize((newWidth, newHeight), Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])
        return arg['dst_img']

    # 检测并保存数据库
    def detect(self,file):
        print file
        result = self.isnude(file)
        # 更新数据库
        images = Images().updateNude(file, result)
        self.delImg(file)
    #鉴别黄色图片
    def isnude(self,file):
        #图像压缩处理
        imagePath = IMAGE_DIR + file
        nudeImg = IMAGE_DIR +"nude_"+file
        print  nudeImg
        # disImg = IMAGE_DIR +file
        self.resizeImg(ori_img=imagePath,dst_img=nudeImg,dst_w=300,dst_h=300,save_q=100)

        # faces = self.face("dis"+file)
        faces = self.face("nude_"+file)
        if(len(faces)!=1):
            print("no face or lt 2")
            self.delImg(file)
            return -1
        else:
            if(not self.cropImg("nude_"+file, faces)):
                return 0
        n = Nude(nudeImg)
        # n = Nude(newImg)
        # n.setFaces(faces)
        # n.resize(1000,1000)
        n.parse()
        # print n.result
        return 1 if n.result else 0

    # 删除截图
    def delImg(self,file):
        nudeImg = IMAGE_DIR +"nude_"+file
        if os.path.isfile(nudeImg):
            os.remove(nudeImg)

    # 多进程
    def main(self):
        count = multiprocessing.cpu_count()-1
        pool = multiprocessing.Pool(processes=count)
        # images = Images().findByNude(1)
        images = Images().findAll()
        print("file count:"+str(len(images)))
        # sys.exit(0)
        for f in images:
            # print f['name']
            if(not os.path.isfile(IMAGE_DIR + f['name'])):
                print(IMAGE_DIR + f['name'], " not exist")
            else:
                # self.detect(f['name'])
                # pool.map(self.detect,f['name'] )
                pool.apply_async(detect, (f['name'],))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

                # bn = BatchNude()
                # pool.apply_async(bn.detect(f['name']))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

        print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
        pool.close()
        pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
        print "Sub-process(es) done."


# 检测并保存数据库
def detect(file):
    print file
    batch_nude = BatchNude()
    result = batch_nude.isnude(file)
    # 更新数据库
    images = Images().updateNude(file, result)
    batch_nude.delImg(file)


if __name__ == '__main__':
    batch_nude = BatchNude()
    batch_nude.main()
    # batch_nude.detect('1464317845545A3080CD.jpg')

