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
sys.path.append("../..")
from bin.python.models.youyuan_log import YouyuanLog
from nude import Nude
import imagehash
from bin.python.utils import logger
from bin.python.models.redis_results import RedisResults


Image.LOAD_TRUNCATED_IMAGES = True

reload(sys)
sys.setdefaultencoding('utf-8')
IMAGE_DIR = ""
'''
生成指纹，从缓存取检测结果保存到mysql
'''
class Figerlog(object):
    def __init__(self, path):
        self.filename = path
    	self.IMAGE_HASH = ""
 	# 获取图片哈希值
    def get_image_hash(self,file):
        img = Image.open(file)
        h = str(imagehash.dhash(img))
        return h
    # 获取图片列表
    def getFileList(self,p):
        p = str(p)
        if p == "":
            return []
        a = os.listdir(p)
        b = [x for x in a if os.path.isfile(p + x)]
        return a
	# redis数据是否存在，并返回检测结果
    def get_result_from_redis(self,hash):
        rr = RedisResults()
        return rr.get(hash)

    def save_log(self,result):
    	pass
    	# youyuan = Youyuanlog()
    	#{'name':'test','finger':'xxx','is_face':'1','ocr':'乱码','is_qq':'1','is_pass':'1','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    	# youyuan.insert(result)

    def get_result(self):
    	redis_result = self.get_result_from_redis(self.IMAGE_HASH)
        if(redis_result):
        	args = redis_result.split(",")
        	return {'name':self.filename,'finger':self.IMAGE_HASH,'is_face':args[0],'ocr':args[1],'is_qq':args[1],'is_nude':args[2],'is_pass':args[3],'created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        else:
        	return False

    def deal(self):
    	self.IMAGE_HASH = self.get_image_hash(IMAGE_DIR+self.filename)
    	result = self.get_result()
    	if(result):
    		# self.save_log(result)
    		return result
    	else:
    		return False


def main():
	figerlog = Figerlog("")
	fileList = figerlog.getFileList(IMAGE_DIR)
	for file in fileList:
		print("=============="+file+"==============")
		finger = Figerlog(file)
		result = finger.deal()
		youyuan = Youyuanlog()
    	#{'name':'test','finger':'xxx','is_face':'1','ocr':'乱码','is_qq':'1','is_pass':'1','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    	youyuan.insert(result)

if __name__ == "__main__":
    main()
