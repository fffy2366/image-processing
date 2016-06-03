#!bin/evn python
# -*-coding:utf8-*-
from mysql import MySQL
import datetime
import sys
import types
reload(sys)
sys.setdefaultencoding('utf-8')

class Images:
    def insert(self,d):
        n = MySQL('127.0.0.1', 'root', '1234', 3306)

        n.selectDb('images')
        tbname = 'images'
        n.insert(tbname, d)
        n.commit()


if __name__ == '__main__':
    i = Images()
    # i.insert({'name':'test','is_face':1,'ocr':'乱码'.encode('utf-8'),'is_qq':1,'created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    #i.insert({'name':'test','is_face':1,'ocr':'乱码','is_qq':1,'created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    i.insert({'name':'test','is_face':'1','ocr':'乱码','is_qq':'1','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    #print type("bb") is types.StringType ;
    #print 'test' if True else 'not test' ;
    #print {'name':'test','is_face':1,'ocr':'乱码','is_qq':1,'created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    str = ['1','乱码','乱码2','乱码3']
    print str
    s = "('"+"','".join(str)+"')"
    print s
    #for s in str:
        #print s
        #print "("+s+")"
    #print tuple(['乱码'])
    s = ( '乱码' , '乱码2' )
    print s
    #print '乱码'

    #p = (1,'乱码','2016-06-02 18:11:09',1,'test')
    #print p