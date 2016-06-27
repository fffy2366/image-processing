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

## 鉴别色情图片
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

http://api.youtu.qq.com/youtu/imageapi/imageporn

## 微软 认知服务
https://www.azure.cn/cognitive-services/zh-cn/face-api