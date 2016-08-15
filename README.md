# image-processing
人脸识别、图像文字识别

##重新编译安装python
./configure --prefix=/usr/local/  –enable-shared CFLAGS=-fPIC  
make  
make install



b3aa
513a
e628
7f63

confidence >0.8


## python
[python操作MySQL数据库](http://www.cnblogs.com/rollenholt/archive/2012/05/29/2524327.html)
##安装msyql

到官方下载 [MySQL for Python](https://sourceforge.net/projects/mysql-python/)

然后解压，打开README：

里面有安装过程：

  $ tar xfz MySQL-python-1.2.1.tar.gz 
  $ cd MySQL-python-1.2.1 
  $ # edit site.cfg if necessary 
  $ python setup.py build 
  $ sudo python setup.py install # or su first



python
import MySQLdb
报错：
ImportError: dlopen(/Library/Python/2.7/site-packages/MySQL_python-1.2.4b4-py2.7-macosx-10.11-intel.egg/_mysql.so, 2): Library not loaded: libmysqlclient.18.dylib
解决：
sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib
报错：
ln: /usr/lib/libmysqlclient.18.dylib: Operation not permitted

解决：
$ sudo nvram boot-args="rootless=0"
$ sudo reboot

不起作用：
cd MySQL-python-1.2.4b4s
vim site.cfg
mysql_config = /usr/local/mysql/bin/mysql_config

仍然不起作用


解决如下：
原因是 EI Capitan 增加了 System Integrity Protection 的功能，阻止了写入的操作的，默认是开启的，需要关闭。

关闭方式：

重启电脑，开机时按住 cmd + R，进入 Recovery 模式。然后打开终端工具 ，输入命令：csrutil disable，然后再次重启电脑即可。


sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib

python
import MySQLdb

成功！
centos7安装mysqldb：yum install MySQL-python

[推荐 Python 读写 Excel 2010 xlsx/xlsm](https://pypi.python.org/pypi/openpyxl)

Sample code:
from openpyxl import Workbook
wb = Workbook()
# grab the active worksheet
ws = wb.active
# Data can be directly to cells
ws['A1'] = 42
# Rows can also be appended
ws.append([1, 2, 3])
# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()
# Save the file
wb.save("sample.xlsx")


[用NODEJS处理EXCEL文件导入导出](http://www.itnose.net/news/156/6290038)

[Tesseract-OCR 字符识别---样本训练](http://blog.csdn.net/yasi_xi/article/details/8763385)

[Tesseract Training on Mac OSX:](http://khalsa.guru/posts/16)
[tesseract-ocr 第四课 如何训练新语言] (http://wangjunle23.blog.163.com/blog/static/117838171201323031458171/)
[tessdata](https://github.com/tesseract-ocr/tessdata)
[ocr 下载](https://sourceforge.net/projects/tesseract-ocr-alt/files/?source=navbar)
[ocr wiki](https://github.com/tesseract-ocr/tesseract/wiki)
[Improving the quality of the output](https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality#Segmentation_method)
https://gist.github.com/endolith/334196bac1cac45a4893
[ MAC用homebrew安装imagemagick](http://blog.csdn.net/cloudsben/article/details/8164047)
[skimage](http://scikit-image.org/download.html)
pip install -U scikit-image

error：pthread_cond_wait: Resource busy

## Test
rm /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/num.traineddata

tesseract ocr2.png result -l num
tesseract ocr2.png result -l num -psm 6 digits
tesseract ocr2.png result -l num hocr
tesseract ocr2.png result -l num digits

more result.txt

cp ~/python/image-processing/bin/num.traineddata /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/
cp ~/Downloads/num/num.traineddata /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/

cp chi_sim.traineddata /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/

## PhpStorm 2016.1 Help/Viewing Structure of a Source File
c class m method f function v variable f fields




/Users/fengxuting/python/image-processing/bin/shell/textcleaner -g -e none -f 15 -o 20 result.jpg text.jpg

sudo sh /Users/fengxuting/python/image-processing/bin/shell/textcleaner -g -e none -f 15 -o 20 result.jpg text.jpg

chmod -R 777 textcleaner
./textcleaner -g -e none -f 15 -o 20 result.jpg text.jpg
./textcleaner -g -e stretch -f 25 -o 20 -s 1 result.jpg text.jpg
./textcleaner -g -e stretch -f 25 -o 5 -s 1 result.jpg text.jpg
./textcleaner -g -e stretch -f 25 -o 10 -s 1 result.jpg text.jpg
./textcleaner -e normalize -f 15 -o 5 -S 200 -s 1 result.jpg text.jpg
./textcleaner -g -e none -f 15 -o 10 result.jpg text.jpg
./textcleaner -g -e normalize -f 15 -o 10 result.jpg text.jpg
./textcleaner -g -e normalize -f 15 -o 10 -s 1 result.jpg text.jpg


./textcleaner -e normalize -f 15 -o 5 -S 200 -s 1 test108.jpg text.jpg
./textcleaner -g -e normalize -f 15 -o 10 -s 1 test108.jpg text.jpg
./textcleaner -g -e normalize -f 15 -o 10 -s 1 1463815812385A98C108.jpg text.jpg

## OCR

[Noise Removal](http://cn.mathworks.com/help/images/noise-removal.html?requestedDomain=www.mathworks.com)

[使用ImageMagick和Tesseract做中文文本识别](http://www.ziliao1.com/Article/Show/31F48139995AD93496EA962776C6A99F.html)

一、用imagemagic对图片进行预处理，以提高识别率

convert -compress none -depth 8 -alpha off -crop 112x15+0+1 -monochrome ./1.png ./1.tif
　　1.-compress none，必选参数.必须在无压缩模式下进行，否则tesseract可能不接受图片。

　　2.-depth 8，可选参数。加上据说可以提高识别率。

　　3.-alpha off，可选参数。加上据说可以提高识别率。

　　4.-crop ... 可选参数。用来裁掉图片的空白区域和下划线。具体格式为：width x height + x + y，按照矩形区域裁剪，x和y是指矩形。

的左上角的坐标的，width和height是说矩形框的宽高，如果width或者height写0，意思是取当前图片本身的宽或者高。

　　5.-monochrome，可选参数。是把图片处理成黑白二色，即所谓的二值化，也可以尝试下-colorspace Gray来代替。

convert ./1.tif -scale 300% ./1.tif
　　放大图片，以提高识别率，少数情况下图片放大后反而识别不出来了。

二、用tesseract来识别图片

tesseract ./1.tif ./1 -l chi_sim -psm 7
　　1.-l，必选参数。用来指定语言类型，系统默认不支持中文，要到谷歌下载中文语言包，放到tesseract安装目录下的tessdata文件夹中，即chi_sim.traineddata这个文件。

　　2.-psm 7，可选参数。这个参数用来告诉tesseract目标图片当中只有一行文字，这么做可以提高识别率。


convert -compress none -depth 8 -alpha off  -monochrome ./1463904063966A83D54C.jpg ./1.tif

./1.tif ./1 -l chi_sim -psm 6


tesseract ocr.tif result
convert 1463473924704AD5ADD3.jpg -colorspace Gray ocr.tif
convert 1463473924704AD5ADD3.jpg -colorspace Gray -monochrome  ocr.tif


[matlab 车牌号码识别程序代码](http://wenku.baidu.com/link?url=jdOAtiTIx6JiFzb6VSCVN9_USnZuOkT8QJ5Px0kYEi5fBelPn0Hg2zQhctW1spk67fGstdOwSrMPSrmd82lg2ukQnUsjdErcqur-i_o03SG)

## 鉴别色情图片 nude
http://v2ex.com/t/286041#reply103

https://github.com/nixuehan/rabbit

[php](http://www.phpclasses.org/package/3269-PHP-Determine-whether-an-image-may-contain-nudity.html)

## 图像搜索：
[Google 以图搜图 - 相似图片搜索原理 - Java实现](http://m.blog.csdn.net/article/details?plg_nld=1&id=7100058&plg_auth=1&plg_uin=1&plg_usr=1&plg_vkey=1&plg_nld=1&plg_dev=1)
[利用图片指纹检测高相似度图片](http://python.jobbole.com/81277/)

https://github.com/fffy2366/image-fingerprinting


[用Python和OpenCV创建一个图片搜索引擎的完整指南](http://python.jobbole.com/80860/)
http://python.jobbole.com/80860/
[image-search-engine-python-opencv](http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/)

[图像处理之K-Means算法演示](http://blog.csdn.net/jia20003/article/details/8828648)



INSTALL:
wget http://www.cl.cam.ac.uk/Research/DTG/attarchive/pub/data/att_faces.tar.Z
tar zxvf att_faces.tar.Z
mv orl_faces/ images
sudo easy_install setuptools pycurl
sudo pip install peewee
sudo pip install -U scikit-learn

wget http://github.com/downloads/facebook/tornado/tornado-1.2.1.tar.gz


## 人脸识别
[linux下查看opencv版本](http://blog.csdn.net/shaoxiaohu1/article/details/24308335)
```
$ pkg-config --modversion opencv 
```
[使用 OpenCV 与 Face++ 实现人脸解锁](http://python.jobbole.com/84666/)
https://github.com/cyh24/Joint-Bayesian

[opencv人脸匹配](http://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html)
[百度人脸识别服务](https://segmentfault.com/a/1190000000485028?page=1)
```
scaleFactor=1.1,
minNeighbors=5,
minSize=(30, 30),
flags=cv2.cv.CV_HAAR_SCALE_IMAGE
```
scaleFactor     :    官网文档说是每次图片缩小的比例,其实可以这么理解,距离相机不同的距离,物体大小是不一样的,在物体大小不一致的情况下识别一个东西是不方便的,这就需要进行多次的缩放,这就是这个参数的作用.

minNeighbors :   可以理解为每次检测时,对检测点(Scale)周边多少有效点同时检测,因为可能选取的检测点大小不足而导致遗漏
[【原】训练自己haar-like特征分类器并识别物体（2）](http://www.cnblogs.com/wengzilin/p/3849118.html)

### 人脸识别其他方法
[Matlab人脸检测方法（Face Parts Detection）详解](http://blog.csdn.net/u013088062/article/details/50810988)
[Face Detection, Pose Estimation and Landmark Localization in the Wild](http://www.ics.uci.edu/~xzhu/face/)
[基于Matlab的简单人脸识别实例](http://blog.sina.com.cn/s/blog_725866260100ryg2.html)
[免费、高性能的人脸检测库(二进制)](http://www.opencv.org.cn/portal.php?mod=view&aid=2)
[libfacedetection](https://github.com/ShiqiYu/libfacedetection)
[人脸检测发展：从VJ到深度学习（上）](https://mp.weixin.qq.com/s?__biz=MzI5NTIxNTg0OA==&mid=2247484422&idx=2&sn=a68638b34e32b2641a003bad81b53219&scene=1&srcid=0811SMx0wAJ51tNOvhouLk9h&key=305bc10ec50ec19b13006541fdfe99de1a1480d8c683edcac33d4da35611ca2097256ade5cb4563b9efb92cd4f4a3fd5&ascene=0&uin=MTA2ODMxMjkyOA%3D%3D&devicetype=iMac+MacBookPro11%2C4+OSX+OSX+10.11.3+build(15D21)&version=11020201&pass_ticket=AhSK0mvkJf04YGh0i1uPAym7GW1PjJ1Wf%2FtIMtxdGAxSUUacmzM8JEwyzUOU1TQs)

[Python调用C语言函数](http://coolshell.cn/articles/671.html)
```pytyon
>>> from ctypes import *
>>> import os
>>> libtest = cdll.LoadLibrary(os.getcwd() + '/libtest.so')
>>> print libtest.multiply(2, 2)
4
```

## plupload
[plupload](http://www.plupload.com/download)

[demo](http://chaping.github.io/plupload/demo/index4.html)

[前端上传组件Plupload使用指南](http://www.cnblogs.com/2050/p/3913184.html)
[plupload](http://www.ophome.cn/question/60639)


##rar
<命令>
  e             解压文件到当前目录
  l[t,b]        列出压缩文档信息[technical, bare]
  p             打印文件到标准输出
  t             测试压缩我俄当
  v[t,b]        列出压缩文档的详细信息[technical,bare]
  x             解压文件到完整路径

rar x abc.rar

## MySQL
truncate table images ;
select count(*) from images ; 
select id 序号, `name` 照片名称,is_face 人脸识别结论,is_qq QQ号识别结论,is_nude 黄色图片识别结论 from images  where id>2623 group by `name` order by created_at desc, name asc;

mysqldump -uroot -p images >/backups/xx.sql
## 运行
nohup python batch.py &
[1] 15890
ps aux|grep 15890

## 导出excel
```
#!/bin/bash
# export table tablename to excel
# author:frank
# date:2014-09-08
user=root
pass=db2016
db=images
table=images
#mkdir -p /backups/
dir=/backups/
file={table}.xls
mysql --default-character-set='gb2312' -u${user} -p${pass} -e "select id 序号, name 照片名称,is_face 人脸识别结论,is_qq QQ号识别结论,is_nude 黄色图片识别结论  from ${db}.${table} where id>0 group by name order by created_at desc, name asc" > ${dir}${file}
```


## 优图
http://open.youtu.qq.com/welcome/index

http://open.youtu.qq.com/welcome/developer#/api-face-analysis-detect

http://api.youtu.qq.com/youtu/imageapi/imageporn

https://github.com/TencentYouTu/python_sdk

## 微软 认知服务
https://www.azure.cn/cognitive-services/zh-cn/face-api

## [用Python做科学计算](http://old.sebug.net/paper/books/scipydoc/index.html)

[numpy.ndarray](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html)

## 爬虫

http://scrapy.org/download/


## API
1 -检测到一个人脸
2 -检测到多个人脸
3 -数字不通过
4 -鉴黄不通过
等
2，我们告诉他一个需要的图片的尺寸  如 600*800
他会对原始图片 resize 之后传给咱们
3，他还需要一个图片的角度  值需要  0  +90  -90  180
[利用图片指纹检测高相似度图片](http://python.jobbole.com/81277/)


https://github.com/component/focus


win10:
npm config set msvs_version 2013 --global
npm install --msvs_version=2015

安装vs2015

python下如何安装.whl包？
python培训 python培训 2015-02-08 18:34:40
下载.whl包
先pip install wheel

之后pip install 包名字.whl 即可安装某模块包


到哪找.whl文件？
http://www.lfd.uci.edu/~gohlke/pythonlibs/

python -m pip install --upgrade pip
pip install numpy -U

[国内使用easy_install和pip超时问题解决](http://www.toxingwang.com/linux-unix/shell/2633.html)


"node-pluploader": "0.0.5",
q:
error
 MSB8036: The Windows SDK version 8.1 was not found. Install the required version of Windows SDK or change the SDK vers
ion in the project property pages or by right-clicking the solution and selecting "Retarget solution".
a:
https://developer.microsoft.com/en-us/windows/downloads/windows-8-1-sdk
q&a:
[Visual studio doesn't have cl.exe [closed]](http://stackoverflow.com/questions/31953769/visual-studio-doesnt-have-cl-exe}


pylab 包含numpy ,scipy,matplotlib ,从http://www.lfd.uci.edu/~gohlke/pythonlibs/下载
[有关python中的pylab的下载安装 ](http://blog.sina.com.cn/s/blog_76cb58fb0102vcx7.html)
[Installing the SciPy Stack](http://www.scipy.org/install.html)

Todo:
* 人脸数判断√
* 生成指纹 redis 存储√
* 鉴黄根据人脸比例√
* ocr matlab
* nude根据人脸皮肤排除背景 junzhi-10<cb<junzhi+10 junzhi-10<cr<junzhi+15
* 人脸识别添加皮肤判断？


## Matlab
[CentOS安装Matlab R2015b](http://www.centoscn.com/image-text/install/2016/0408/7018.html)
1. Set an X11 display, and restart the install process
2. Use the silent install feature by specifying the -mode silent option
./install -mode silent
[Matlab 2015a &2014b Mac版+教程（百度云限速破解）](http://bbs.feng.com/read-htm-tid-9711547.html)
[命令行运行matlab](http://blog.sina.com.cn/s/blog_6bebbb2f0100w6h5.html)
matlab程序也可以在命令行里直接运行，只需要使用 -r 选项。比如运行当前目录下的example.m
matlab  -nodesktop -nosplash -r example
或者
matlab  -nojvm -nosplash -r example
或者
matlab -nodisplay -r example
 可以将如下命令加到~/.bashrc文件
alias mrun='matlab -nodesktop -nosplash -r'
这样下次（或者执行source ~/.bashrc）之后就可以直接
mrun example
来在命令行运行matlab文件。
sudo pip install pillow imagehash

$ yum install tigervnc tigervnc-server -y 


放弃vnc，用下面的方法安装:
1) 修改配置文件
查看install_guide.pdf ,拷贝installer_input.txt 为my_installer_input.txt
修改配置，详见docs/my_installer_input.txt
```
destinationFolder=/mnt/MATLAB/R2015b
fileInstallationKey=09806-07443-53955-64350-21751-41297
agreeToLicense=yes
mode=silent
# licensePath=
```
2) 安装
$ ./install -inputFile ../my_installer_input.txt

安装成功！
$ /mnt/MATLAB/R2015b/bin/matlab -h
3) 破解
- Use license_standalone.lic to activate,
  or make a "licenses" folder in %installdir% and copy license_standalone.lic to it,and run matlab without activation
- after the installation finishes copy the folders to %installdir% to overwriting the originally installed files

4) 添加环境变量
$ vim ~/.bash_profile
export PATH 之前添加
PATH=$PATH:/mnt/MATLAB/R2015b/bin

$ source ~/.bash_profile
5) 测试
matlab -nodisplay -r example
6) python 调用matlab
[mlab](https://github.com/ewiger/mlab#windows)
[matlab_wrapper](https://github.com/mrkrd/matlab_wrapper)
```
$ pip install matlab_wrapper
$ yum install csh
```
[图文教程：百度云主机BCC挂载云盘CDS](http://xiaohost.com/1376.html)


## centos 安装pip
wget --no-check-certificate https://github.com/pypa/pip/archive/1.5.5.tar.gz

tar zvxf 1.5.5.tar.gz    #解压文件
cd pip-1.5.5/
python setup.py install

q:
error: no lapack/blas resources found


[Python多进程multiprocessing使用示例](http://outofmemory.cn/code-snippet/2267/Python-duojincheng-multiprocessing-usage-example)


##删除0字节图片
```
$ find -type f -size 0 -exec rm -rf {} \;
```
==============898b67a0-5e2e-11e6-b75e-87fc586a8584.png==============
Traceback (most recent call last):
  File "finger_log.py", line 93, in <module>
    main()
  File "finger_log.py", line 87, in main
    result = finger.deal()
  File "finger_log.py", line 72, in deal
    self.IMAGE_HASH = self.get_image_hash(IMAGE_DIR+self.filename)
  File "finger_log.py", line 42, in get_image_hash
    h = str(imagehash.dhash(img))
  File "/usr/lib/python2.7/site-packages/imagehash/__init__.py", line 160, in dhash
    image = image.convert("L").resize((hash_size + 1, hash_size), Image.ANTIALIAS)
  File "/usr/lib64/python2.7/site-packages/PIL/Image.py", line 699, in convert
    self.load()
  File "/usr/lib64/python2.7/site-packages/PIL/ImageFile.py", line 215, in load
    raise IOError("image file is truncated (%d bytes not processed)" % len(b))
IOError: image file is truncated (43 bytes not processed)
