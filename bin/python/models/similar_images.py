#!bin/evn python
# -*-coding:utf8-*-
from mysql import MySQL
import datetime
import sys
import types
import cPickle

reload(sys)
sys.setdefaultencoding('utf-8')

class SimilarImages:
    def insert(self,d):
        n = MySQL()

        n.selectDb('images')
        tbname = 'similar_images'
        n.insert(tbname, d)
        n.commit()

    def findByName(self,name):
        n = MySQL()

        n.selectDb('images')
        tbname = 'similar_images'
        n.query("select name,features from similar_images where name='"+name+"'")
        return  n.fetchRow()
    def findAll(self):
        n = MySQL()

        n.selectDb('images')
        tbname = 'similar_images'
        n.query("select name,features from similar_images")
        return  n.fetchAll()
if __name__ == '__main__':
    s = SimilarImages()

    # s.insert({'name':'test3','features':cPickle.dumps([11,22]),'created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    result = s.findByName("1464319479517AE6DB61.jpg")

    print(result)
    print(result!=None)