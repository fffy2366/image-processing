#!bin/evn python
# -*-coding:utf8-*-
import datetime
import sys
sys.path.append("../../..")
from bin.python.models.mysql import MySQL

reload(sys)
sys.setdefaultencoding('utf-8')

class YouyuanLog:
    def insert(self,d):
        n = MySQL()

        n.selectDb('images')
        tbname = 'youyuan_log'
        n.insert(tbname, d)
        n.commit()
    def findByFace(self,v):
        n = MySQL()

        n.selectDb('images')
        tbname = 'youyuan_log'
        n.query("select name from %s where is_face = %s" %(tbname,v))
        return n.fetchAll()
    def findByNude(self,v):
        n = MySQL()

        n.selectDb('images')
        tbname = 'youyuan_log'
        n.query("select name from %s where is_nude = %s" %(tbname,v))
        return n.fetchAll()
    def findAll(self):
        n = MySQL()

        n.selectDb('images')
        tbname = 'youyuan_log'
        # n.query("select name from %s where updated_at <'2016-06-27 00:00:00'" %(tbname) )
        # n.query("select name from %s where is_face!=1 " %(tbname) )
        n.query("select name from %s " %(tbname) )
        return n.fetchAll()
    def updateFace(self,filename,count):
        n = MySQL()
        n.selectDb('images')
        tbname = 'youyuan_log'
        n.update(tbname, { 'is_face': count}, "name='"+filename+"'")
        n.commit()
    def updateNude(self,filename,result):
        n = MySQL()
        n.selectDb('images')
        tbname = 'youyuan_log'
        n.update(tbname, { 'is_nude': result}, "name='"+filename+"'")
        n.commit()
    def update(self,filename,result):
        n = MySQL()
        n.selectDb('images')
        tbname = 'youyuan_log'
        n.update(tbname, result, "name='"+filename+"'")
        n.commit()

if __name__ == '__main__':
    i = YouyuanLog()
    i.insert({'name':'test','finger':'xxx','is_face':'1','ocr':'乱码','is_qq':'1','is_pass':'1','created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

   