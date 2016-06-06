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


rm /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/num.traineddata

tesseract ocr2.png result -l num
more result.txt

cp ~/python/image-processing/bin/num.traineddata /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/
cp ~/Downloads/num/num.traineddata /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/

cp chi_sim.traineddata /usr/local/Cellar/tesseract/3.04.01_1/share/tessdata/