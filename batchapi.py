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
from bin.python.models.youyuan_log import YouyuanLog
from nude import Nude
import imagehash
from bin.python.utils import logger
from bin.python.models.redis_results import RedisResults
import matlab_wrapper


Image.LOAD_TRUNCATED_IMAGES = True

reload(sys)
sys.setdefaultencoding('utf-8')


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
        matlab = matlab_wrapper.MatlabSession()

        matlab.put('filename', file)
        matlab.put('IMAGE_DIR', IMAGE_DIR)
        matlab.eval('face')

        count = matlab.get('count')

        has_crop = matlab.get('has_crop')

        return int(count),int(has_crop)==1


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


    #鉴别黄色图片
    def isnude(self,file):
        #图像压缩处理
        imagePath = IMAGE_DIR + file
        nudeImg = IMAGE_DIR +"nude_"+file
        # self.resizeImg(ori_img=imagePath,dst_img=nudeImg,dst_w=300,dst_h=300,save_q=100)

        # faces = self.face("nude_"+file)
        # self.cropImg("nude_"+file,faces)
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
        self.resizeImg(ori_img=filepath,dst_img=filepath,dst_w=480,dst_h=640,save_q=100)
        if(os.path.isfile(filepath)):
            # self.IMAGE_HASH = self.get_image_hash(filepath)
            # redis_result = self.get_result_from_redis(self.IMAGE_HASH)
            # if(redis_result):
            #     #删除图像
            #     self.delImg(file)
            #     print redis_result
            #     sys.exit(0)
            is_pass = 1
            #人脸检测
            count,has_crop = self.face(file)
            print("count:")
            print(count)
            print("has_crop:")
            print(has_crop)
            # 如果人脸不是1则 ocr和鉴黄不用检测
            if(count!=1):
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
                    #鉴黄 没有截图通过
                    if not has_crop:
                        is_nude = 0
                        is_pass = 1

                    else:
                        is_nude = self.isnude(file)
                        if(is_nude==1):
                            is_pass = 0
                        else:
                            is_pass = 1

            #删除图像
            self.delImg(file)

            # print {"face_count":len(fc),"digital_count":l,"is_nude":is_nude,"pass":is_pass}
            result = str(count)+","+str(l)+","+str(is_nude)+","+str(is_pass)
            # 结果保存redis数据库
            self.save_redis(self.IMAGE_HASH,result)
            print result
            return {"is_face":count,"is_qq":l,"is_nude":is_nude,"is_pass":is_pass}

        else:
            print("error:",file, "is not a img file")
            return {"is_face":-1,"is_qq":-1,"is_nude":-1,"is_pass":-1}

    # 保存redis
    def save_redis(self,hash,result):
        rr = RedisResults()
        rr.save(hash,result)

    # redis数据是否存在，并返回检测结果
    def get_result_from_redis(self,hash):
        rr = RedisResults()
        return rr.get(hash)
    # 多进程
    def main(self):
        count = multiprocessing.cpu_count()-1
        pool = multiprocessing.Pool(processes=1)
        # images = Images().findByNude(1)
        youyuan = YouyuanLog().findByFace(0)
        print("file count:"+str(len(youyuan)))
        # sys.exit(0)
        for f in youyuan:
            # print f['name']
            if(not os.path.isfile(IMAGE_DIR + f['name'])):
                print(IMAGE_DIR + f['name'], " not exist")
            else:
                # self.detect(f['name'])
                # pool.map(self.detect,f['name'] )
                pool.apply_async(detect, (f['name'],))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
                # detect(f['name'])

        print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
        pool.close()
        pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
        print "Sub-process(es) done."

# 检测并保存数据库
def detect(file):
    print file
    api = Api()
    result = api.one(file)
    # 更新数据库
    YouyuanLog().update(file, result)

if __name__ == '__main__':
    api = Api()
    api.main()
    # api.one(sys.argv[1])
    # api.one("9d27d550-4beb-11e6-aefd-4f827560e966.png")
    # api.one("91787150-4bf1-11e6-aefd-4f827560e966.png")
    pass
