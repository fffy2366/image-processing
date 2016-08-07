#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import os
import copy
import math
import sys
import time
from collections import namedtuple
from PIL import Image
sys.path.append("../..")
from bin.python.config.config import configs
from bin.python.utils import logger
# IMAGE_DIR = configs['image_dir']
IMAGE_DIR = "D:/photo/skins/"

class Ycbcr(object):
    def __init__(self, path):
        self.filename = path
        if(os.path.isfile(IMAGE_DIR+path)):
            self.image = Image.open(IMAGE_DIR+path)
            self.width, self.height = self.image.size
    # 读取图片
    # 转cbcr
    # 写日志
    def open(self):
        pixels = self.image.load()
        for y in range(self.height):
            for x in range(self.width):
                r = pixels[x, y][0]   # red
                g = pixels[x, y][1]   # green
                b = pixels[x, y][2]   # blue
                _id = x + y * self.width + 1
                _ycbcr = self._to_ycbcr(r,g,b)
                self.log((self.filename,)+_ycbcr)
        self.log(self.filename) ;
    def _to_ycbcr(self, r, g, b):
        # Copied from here.
        # http://stackoverflow.com/questions/19459831/rgb-to-ycbcr-conversion-problems
        y = .299*r + .587*g + .114*b
        cb = 128 - 0.168736*r - 0.331364*g + 0.5*b
        cr = 128 + 0.5*r - 0.418688*g - 0.081312*b
        return y, cb, cr
    def log(self,ycbcr):
        from bin.python.utils import logger
        # 默认log存放目录,需要在程序入口调用才能生效,可省略
        logger.log_dir = "../../logs"
        # log文件名前缀,需要在程序入口调用才能生效,可省略
        logger.log_name = "ycbcr_"+self.filename
        conf = logger.Logger()
        conf.info(ycbcr)
    def getFileList(self,p):
        p = str(p)
        if p == "":
            return []
        # p = p.replace( "/","\\")
        # if p[ -1] != "\\":
        #     p = p+"\\"
        a = os.listdir(p)
        b = [x for x in a if os.path.isfile(p + x)]
        return a
def main():
    ycbcr = Ycbcr("nude_test.jpg")
    fileList = ycbcr.getFileList(IMAGE_DIR)
    for file in fileList:
        print("=============="+file+"==============")
        ycbcr = Ycbcr(file)
        ycbcr.open()

if __name__ == "__main__":
    main()
