#!bin/evn python
# -*-coding:utf8-*-
import MySQLdb




try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='1234',db='test',port=3306,charset="utf8")
    cur=conn.cursor()
    #cur.execute('select * from t1')
    # result=cur.fetchone()
    # print result
    # print 'ID: %s info %s' % result

    # results=cur.fetchmany(5)
    # for r in results:
    #     print r
    sql = "INSERT INTO news(title) VALUES('中文')" ;
    text = u'中文'
    print text
    cur.execute("insert into t1 (title) values( '%s' )" % (text))
    # cur.execute(sql)
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])