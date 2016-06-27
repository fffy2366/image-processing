#!bin/evn python
# -*-coding:utf8-*-
'''
http://weipengfei.blog.51cto.com/1511707/1269034
'''
import MySQLdb
import sys
import types
reload(sys)
sys.setdefaultencoding('utf-8')

OperationalError = MySQLdb.OperationalError


class MySQL:
    def __init__(self, host='localhost', user='root', password='1234', port=3306, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset
        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password)
            self.conn.autocommit(False)
            self.conn.set_character_set(self.charset)
            #self.conn.execute("SET NAMES utf8");
            self.cur = self.conn.cursor()
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def __del__(self):
        self.close()

    def selectDb(self, db):
        try:
            self.conn.select_db(db)
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self, sql):
        try:
            n = self.cur.execute(sql)
            return n
        except MySQLdb.Error as e:
            print("Mysql Error:%s\nSQL:%s" % (e, sql))

    def fetchRow(self):
        result = self.cur.fetchone()
        return result

    def fetchAll(self):
        result = self.cur.fetchall()
        desc = self.cur.description
        d = []
        for inv in result:
            _d = {}
            for i in range(0, len(inv)):
                _d[desc[i][0]] = str(inv[i])
                d.append(_d)
        return d

    def insert(self, table_name, data):
        print(data)
        columns = data.keys()
        _prefix = "".join(['INSERT INTO `', table_name, '`'])
        _fields = ",".join(["".join(['`', column, '`']) for column in columns])
        _values = ",".join(["%s" for i in range(len(columns))])
        _sql = "".join([_prefix, "(", _fields, ") VALUES (", _values, ")"])
        _params = [ data[key] if type(data[key]) is types.StringType else data[key] for key in columns]
        #print(_sql)
        #print _params
        #print tuple(_params)
        #p = "('"+"','".join(_params)+"')"
        #print p
        #p = (1,'乱码','2016-06-02 18:11:09',1,'test')
        #return self.cur.execute(_sql, p)
        #return self.cur.execute(_sql, (1,'乱码','2016-06-02 18:11:09',1,'test'))
        return self.cur.execute(_sql, tuple(_params))

    def update(self, tbname, data, condition):
        _fields = []
        _prefix = "".join(['UPDATE `', tbname, '`', 'SET '])
        for key in data.keys():
            _fields.append("%s = %s" % (key, data[key]))
        _fieldsStr = ",".join([_field for _field in _fields])
        _sql = "".join([_prefix, _fieldsStr, " WHERE ", condition])

        return self.cur.execute(_sql)

    def delete(self, tbname, condition):
        _prefix = "".join(['DELETE FROM  `', tbname, '`', 'WHERE'])
        _sql = "".join([_prefix, condition])
        return self.cur.execute(_sql)

    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    n = MySQL('127.0.0.1', 'root', '1234', 3306)
    n.selectDb('test')
    tbname = 't1'
    a = ({'id': 3, 'title': 3}, {'id': 4, 'title': 4}, {'id': 5, 'title': 5})
    for d in a:
        n.insert(tbname, d)
    n.commit()
