#!bin/evn python
# -*-coding:utf8-*-

from credential import BceCredentials
from bceocrapi import BceOCRAPI
from bin.python.images import Images
from nude import Nude
from PIL import Image as image

import base64
import sys
import os
import logging
import datetime
import cv2
import re

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
IMAGE_DIR = "/Users/fengxuting/Downloads/testphoto/"


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


def getFileList(p):
    p = str(p)
    if p == "":
        return []
    # p = p.replace( "/","\\")
    # if p[ -1] != "\\":
    #     p = p+"\\"
    a = os.listdir(p)
    b = [x for x in a if os.path.isfile(p + x)]
    return a


# print getDirList("public/images")
# print getFileList("public/images")
# 人脸识别
def face(file):
    # Get user supplied values
    imagePath = IMAGE_DIR + file
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
    return len(faces)


#黑白处理
def blackWhite(filename):
    image_file = image.open(IMAGE_DIR+filename) # open colour image
    image_file = image_file.convert('L') # convert image to black and white
    dst_path = IMAGE_DIR+"wb"+filename
    image_file.save(dst_path)
    return dst_path
#数字识别
def ocr(file):
    ocr = BceOCRAPI("02fbe03acf3042a1b40e067bba1971f7", "bb1d4aafe7924fc0829fc33fa26b3347");
    #黑白处理
    newImg = blackWhite(file)
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
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):

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
    else:
        return arg['ori_img']

#鉴别黄色图片
def isnude(file):
    #图像压缩处理
    imagePath = IMAGE_DIR + file
    disImg = IMAGE_DIR +"dis"+file
    newImg = resizeImg(ori_img=imagePath,dst_img=disImg,dst_w=300,dst_h=300,save_q=100)

    n = Nude(newImg)
    n.parse()
    print n.result
    return 1 if n.result else 0


def countdigits(s):
    digitpatt = re.compile('\d')

    return len(digitpatt.findall(s))


def one(file):
    fc = face(file)
    text = ""
    text = ocr(file)
    text = text.encode("utf-8")

    l = countdigits(text)
    is_qq = 0
    if (l > 4):
        is_qq = 1
    is_nude = isnude(file)
    i = Images()
    i.insert({'name': file, 'is_face': fc, 'ocr': text, 'is_qq': is_qq,'is_nude': is_nude,
              'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    #TODO: 删除图像


fileList = getFileList(IMAGE_DIR)
# logger.info(fileList)
# exit()

for f in fileList:
    if(f!=".DS_Store"):
        one(f)

# TODO：分组多线程


#one("1463989011986ACBE628.jpg")
# one("1463988870263AE1CF23.jpg")
one("1463989001869A87B3AA.jpg")
#one("1463989350600A622130.jpg")
#one("1463989383201A1FD90D.jpg")
