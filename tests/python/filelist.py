#!bin/evn python
#encoding:utf-8
__author__ = 'feng'
import os
import sys
import logging
import cv2
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')
# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('y.log')
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
def _to_ycbcr(r, g, b):
    # Copied from here.华中科技大学 刘宏硕士研究
    # 百度文库
    y = .301*r + .586*g + .113*b
    cb = 128 - (44/256)*r - (87/256)*g + (131/256)*b
    cr = 128 + (131/256)*r - (110/256)*g - (21/256)*b
    return y, cb, cr

def average(seq):
    return float(sum(seq)) / len(seq)


IMAGE_DIR = "/Users/fengxuting/Downloads/photo/photo_pass/photo_pass/"
# IMAGE_DIR = "/Users/fengxuting/Downloads/"
fileList = getFileList(IMAGE_DIR)


def one(f):
    print(IMAGE_DIR+f)
    BGRImg = cv2.imread(IMAGE_DIR+f)
    B, G, R = cv2.split(BGRImg)
    (y,cb,cr) = _to_ycbcr(R,G,B)
    # print R[0]*.301
    y = np.average(np.array(.301*R + .586*G + .113*B))
    print y
    logger.info(f)
    logger.info(y)
def main():
    count = 1
    for f in fileList:
        print(f)
        one(f)
        count += 1
        if(count>5):
            break


if __name__=='__main__':
    main()
    # one("1464316313260AEA76C5.jpg")