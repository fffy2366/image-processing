#!bin/evn python
#encoding:utf-8
__author__ = 'feng'
import os
import shutil
#文件目录
ori_dir = "/Users/fengxuting/Downloads/"
#目标目录
dst_dir = "/Users/fengxuting/Downloads/mvtest"
### 创建多层目录
def mkdirs(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        # 如果不存在则创建目录
        print path + u' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + u' 目录已存在'
        return False


if(not os.path.isdir(dst_dir)):
    mkdirs(dst_dir)

f = open("mvlist.txt", "r")
while True:
    line = f.readline()
    if line:
        print(line)
        shutil.move(ori_dir+line.replace("\n",""),dst_dir)
    else:
        break
f.close()