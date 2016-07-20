#!bin/evn python
# -*-coding:utf8-*-
import datetime
import sys

from bin.python.models.mysql import MySQL

reload(sys)
sys.setdefaultencoding('utf-8')

class Images:
    def insert(self,d):
        n = MySQL()

        n.selectDb('images')
        tbname = 'images'
        n.insert(tbname, d)
        n.commit()
    def findByFace(self,v):
        n = MySQL()

        n.selectDb('images')
        tbname = 'images'
        n.query("select name from %s where is_face = %s" %(tbname,v))
        return n.fetchAll()
    def findAll(self):
        n = MySQL()

        n.selectDb('images')
        tbname = 'images'
        # n.query("select name from %s where updated_at <'2016-06-27 00:00:00'" %(tbname) )
        # n.query("select name from %s where is_face!=1 " %(tbname) )
        n.query("select name from %s " %(tbname) )
        return n.fetchAll()
    def updateFace(self,filename,count):
        n = MySQL()
        n.selectDb('images')
        tbname = 'images'
        n.update(tbname, { 'is_face': count}, "name='"+filename+"'")
        n.commit()
    def updateNude(self,filename,result):
        n = MySQL()
        n.selectDb('images')
        tbname = 'images'
        n.update(tbname, { 'is_nude': result}, "name='"+filename+"'")
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