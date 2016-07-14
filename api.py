#!bin/evn python
# -*-coding:utf8-*-

import base64
import sys
import os
import logging
import datetime
import re
import multiprocessing

from PIL import Image as image
import cv2

from bceocrapi import BceOCRAPI
from bin.python.models.images import Images
from nude import Nude

image.LOAD_TRUNCATED_IMAGES = True


reload(sys)
sys.setdefaultencoding('utf-8')
# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('ocr.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
# logger.addHandler(ch)

# 记录一条日志
# logger.info('foorbar')
# IMAGE_DIR = "/Users/fengxuting/Downloads/testphoto/"
IMAGE_DIR = "public/uploads/api/"


def getDirList(p):
    p = str(p)
    if p == "":
        return []
        # p = p.replace( "/","\\")
        # if p[ -1] != "\\":
        # p = p+"\\"
    a = os.listdir(p)
    b = [x for x in a if os.path.isdir(p + x)]
    return b

# 人脸识别
def face(file):
    # Get user supplied values
    oriImg = IMAGE_DIR + file

    #图像压缩处理
    # disImg = IMAGE_DIR +"ocrdis"+file
    # newImg = resizeImg(ori_img=oriImg,dst_img=disImg,dst_w=2048,dst_h=2048,save_q=100)

    # cascPath = sys.argv[2]
    # cascPath = "./data/haarcascades/haarcascade_frontalface_alt.xml"
    cascPath = "./data/lbpcascades/lbpcascade_frontalface.xml"

    # Create the haar 级联
    facecascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(oriImg)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    return faces


#黑白处理
def blackWhite(filename):
    image_file = image.open(IMAGE_DIR+filename) # open colour image
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
def ocr(file):
    ocr = BceOCRAPI("02fbe03acf3042a1b40e067bba1971f7", "bb1d4aafe7924fc0829fc33fa26b3347");
    #黑白处理
    # newImg = IMAGE_DIR +file
    newImg = blackWhite(file)

    #图像压缩处理
    disImg = IMAGE_DIR +"ocrdis"+file
    newImg = resizeImg(ori_img=newImg,dst_img=disImg,dst_w=1600,dst_h=1600,save_q=100)

    with open(newImg, 'rb') as f:
        content = f.read()
        content = base64.b64encode(content)

    try:
        # ocr
        # result = ocr.get_ocr_text(content, language='CHN_ENG')
        result = ocr.get_ocr_text(content, language='ENG')
        # print("file:"+file+"----------result:"+result)
        # logger.info("file:"+file+"----------result:"+result)
        return result
    except Exception as e:
        raise

# 图片如果宽或高大于300则等比例压缩
def resizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 75}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = image.open(arg['ori_img'])
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

    im.resize((newWidth, newHeight), image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])
    return arg['dst_img']


#鉴别黄色图片
def isnude(file):
    #图像压缩处理
    imagePath = IMAGE_DIR + file
    disImg = IMAGE_DIR +"dis"+file
    newImg = resizeImg(ori_img=imagePath,dst_img=disImg,dst_w=300,dst_h=300,save_q=100)

    faces = face("dis"+file)
    n = Nude(newImg)
    n.setFaces(faces)
    # n.resize(1000,1000)
    n.parse()
    # print n.result
    return 1 if n.result else 0


def countdigits(s):
    digitpatt = re.compile('\d')

    return len(digitpatt.findall(s))


def delImg(file):
    #黑白的
    wbImg = IMAGE_DIR+"wb"+file
    ocrImg300 = IMAGE_DIR +"dis"+file
    #大于1600的
    ocrImg1600 = IMAGE_DIR +"ocrdis"+file


    if os.path.isfile(wbImg):
        os.remove(wbImg)
    if os.path.isfile(ocrImg300):
        os.remove(ocrImg300)
    if os.path.isfile(ocrImg1600):
        os.remove(ocrImg1600)

    #删除原文件
    os.remove(IMAGE_DIR+file)

def one(file):
    if(file!=".DS_Store" and os.path.isfile(IMAGE_DIR+file)):
        fc = face(file)
        text = ""
        text = ocr(file)
        text = text.encode("utf-8")

        l = countdigits(text)
        is_qq = 0
        if (l > 4):
            is_qq = 1
        is_nude = isnude(file)
        # 保存数据库
        # i = Images()
        # i.insert({'name': file, 'is_face': len(fc), 'ocr': text, 'is_qq': l,'is_nude': is_nude,
        #           'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        #删除图像
        delImg(file)
        is_pass = 1
        if(len(fc)!=1 or l>6 or is_nude==1):
            is_pass = 0
        # print {"face_count":len(fc),"digital_count":l,"is_nude":is_nude,"pass":is_pass}
        print str(len(fc))+","+str(l)+","+str(is_nude)+","+str(is_pass)

    else:
        print(file, "is not a img file")


if __name__ == '__main__':
    one(sys.argv[1])
    pass
