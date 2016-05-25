#!bin/evn python
#-*-coding:utf8-*-

from credential import BceCredentials
from bceocrapi import BceOCRAPI
import base64
import sys
import os
import logging

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
#logger.addHandler(ch)

# 记录一条日志
#logger.info('foorbar')
IMAGE_DIR = "/Users/fengxuting/Downloads/testphoto/"
def getDirList( p ):
        p = str( p )
        if p=="":
              return [ ]
        #p = p.replace( "/","\\")
        #if p[ -1] != "\\":
             #p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isdir( p + x ) ]
        return b
def getFileList( p ):
        p = str( p )
        if p=="":
              return [ ]
        #p = p.replace( "/","\\")
        #if p[ -1] != "\\":
        #     p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isfile( p + x ) ]
        return a
#print getDirList("public/images")
#print getFileList("public/images")

def ocrone(file):
    ocr = BceOCRAPI("02fbe03acf3042a1b40e067bba1971f7", "bb1d4aafe7924fc0829fc33fa26b3347") ;


    with open(IMAGE_DIR+file, 'rb') as f:
        content = f.read()
        content = base64.b64encode(content)

    try:
        #result = ocr.get_ocr_text(content, language='CHN_ENG')
        result = ocr.get_ocr_text(content, language='CHN_ENG')

        #result = ocr.get_ocr_line(content, language='CHN_ENG')

        # result = ocr.get_ocr_char(content, language='CHN_ENG')

        #print("file:"+file+"----------result:"+result)
        logger.info("file:"+file+"----------result:"+result)
    except Exception as e:
        raise

fileList = getFileList(IMAGE_DIR)
#logger.info(fileList)
#exit()
for f in fileList:
   ocrone(f)

#ocrone("1463988870263AE1CF23.jpg")