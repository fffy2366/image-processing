#!bin/evn python
# -*-coding:utf8-*-

import base64
import sys
import os
import logging
import datetime
import re
import multiprocessing
# from pylab import *

from PIL import Image
import cv2

from bceocrapi import BceOCRAPI
from bin.python.models.images import Images
from nude import Nude
import imagehash
from bin.python.utils import logger
from bin.python.models.redis_results import RedisResults


Image.LOAD_TRUNCATED_IMAGES = True

reload(sys)
sys.setdefaultencoding('utf-8')
#日志
# 默认log存放目录,需要在程序入口调用才能生效,可省略
logger.log_dir = "./logs"
# log文件名前缀,需要在程序入口调用才能生效,可省略
logger.log_name = "api"

conf = logger.Logger()
# conf.debug('debug')
# conf.warn('tr-warn')
# conf.info('ds-info')
# conf.error('ss-error')

# IMAGE_DIR = "/Users/fengxuting/Downloads/testphoto/"
IMAGE_DIR = "public/uploads/api/"
class Api:
    def __init__(self):
        self.IMAGE_HASH = ""
    # 获取图片哈希值
    def get_image_hash(self,file):
        img = Image.open(file)
        h = str(imagehash.dhash(img))
        return h
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


    #黑白处理
    def blackWhite(self,filename):
        image_file = Image.open(IMAGE_DIR+filename) # open colour image
        #exception : Premature end of JPEG file . IOError: image file is truncated (1 bytes not processed)
        try:
            image_file = image_file.convert('L') # convert image to black and white
        except Exception as e:
            raise
            return IMAGE_DIR+filename


        dst_path = IMAGE_DIR+"wb"+filename
        image_file.save(dst_path)
        return dst_path

    #数字识别
    def ocr(self,file):
        ocr = BceOCRAPI("02fbe03acf3042a1b40e067bba1971f7", "bb1d4aafe7924fc0829fc33fa26b3347");
        #黑白处理
        # newImg = IMAGE_DIR +file
        newImg = self.blackWhite(file)

        #图像压缩处理
        disImg = IMAGE_DIR +"ocrdis"+file
        newImg = self.resizeImg(ori_img=newImg,dst_img=disImg,dst_w=1600,dst_h=1600,save_q=100)

        with open(newImg, 'rb') as f:
            content = f.read()
            content = base64.b64encode(content)

        try:
            # ocr
            # result = ocr.get_ocr_text(content, language='CHN_ENG')
            result = ocr.get_ocr_text(content, language='ENG')
            # print("file:"+file+"----------result:"+result)
            # conf.info("file:"+file+"----------result:"+result)
            return result
        except Exception as e:
            raise

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

    # 裁剪人脸以下的图片
    def cropImg(self, file, faces):
        oriImg = IMAGE_DIR + file
        # 裁剪人脸以下最多五倍高度的图片
        # ipl_image = cv.LoadImage(oriImg)
        ipl_image = Image.open(oriImg)

        # print(ipl_image.height)
        if (len(faces) < 1):
            # print("no face")
            return faces
        (x, y, w, h) = faces[0]
        yy = int(y + 1.5*h)
        hh = h * 6
        (width, height) = ipl_image.size
        if (hh > height - y):
            hh = height - y
        if(yy>=height):
            return False
        dst = ipl_image.crop((x, yy, x + w, y + hh))
        dst.save(IMAGE_DIR + file)


    #鉴别黄色图片
    def isnude(self,file):
        #图像压缩处理
        imagePath = IMAGE_DIR + file
        nudeImg = IMAGE_DIR +"nude_"+file
        self.resizeImg(ori_img=imagePath,dst_img=nudeImg,dst_w=300,dst_h=300,save_q=100)

        faces = self.face("nude_"+file)
        self.cropImg("nude_"+file,faces)
        n = Nude(nudeImg)
        # n.setFaces(faces)
        # n.resize(1000,1000)
        n.parse()
        # print n.result
        return 1 if n.result else 0

    # 统计数字个数
    def countdigits(self,s):
        digitpatt = re.compile('\d')

        return len(digitpatt.findall(s))

    # 删除图片
    def delImg(self,file):
        #黑白的
        wbImg = IMAGE_DIR+"wb"+file
        ocrImg300 = IMAGE_DIR +"dis"+file
        #大于1600的
        ocrImg1600 = IMAGE_DIR +"ocrdis"+file
        nudeImg = IMAGE_DIR +"nude_"+file

        if os.path.isfile(wbImg):
            os.remove(wbImg)
        if os.path.isfile(ocrImg300):
            os.remove(ocrImg300)
        if os.path.isfile(ocrImg1600):
            os.remove(ocrImg1600)
        # 鉴黄裁剪图
        if os.path.isfile(nudeImg):
            os.remove(nudeImg)

        #删除原文件
        # os.remove(IMAGE_DIR+file)

    def one(self,file):
        filepath = IMAGE_DIR+file
        if(os.path.isfile(filepath)):
            self.IMAGE_HASH = self.get_image_hash(filepath)
            redis_result = self.get_result_from_redis(self.IMAGE_HASH)
            if(redis_result):
                #删除图像
                self.delImg(file)
                print redis_result
                sys.exit(0)
            is_pass = 1
            #人脸检测
            fc = self.face(file)
            # 如果人脸不是1则 ocr和鉴黄不用检测
            if(len(fc)!=1):
                l = -1
                is_nude = -1
                is_pass = 0
            else:
                #ocr
                text = ""
                text = self.ocr(file)
                text = text.encode("utf-8")

                l = self.countdigits(text)
                if (l > 6):
                    is_nude = -1
                    is_pass = 0
                else:
                    #鉴黄
                    is_nude = self.isnude(file)
                if(is_nude==1):
                    is_pass = 0

            #删除图像
            self.delImg(file)

            # print {"face_count":len(fc),"digital_count":l,"is_nude":is_nude,"pass":is_pass}
            result = str(len(fc))+","+str(l)+","+str(is_nude)+","+str(is_pass)
            # 结果保存redis数据库
            self.save_redis(self.IMAGE_HASH,result)
            print result

        else:
            print("error:",file, "is not a img file")

    # 保存redis
    def save_redis(self,hash,result):
        rr = RedisResults()
        rr.save(hash,result)

    # redis数据是否存在，并返回检测结果
    def get_result_from_redis(self,hash):
        rr = RedisResults()
        return rr.get(hash)

if __name__ == '__main__':
    api = Api()
    api.one(sys.argv[1])
    # api.one("9d27d550-4beb-11e6-aefd-4f827560e966.png")
    # api.one("91787150-4bf1-11e6-aefd-4f827560e966.png")
    pass
