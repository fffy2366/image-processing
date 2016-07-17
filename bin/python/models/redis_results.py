import redis
class RedisResults:
    def __init__(self):
        self.conn = redis.Redis(host='localhost', port=6379, db=0,password='db2016')
    def save(self,hash,result):
        self.conn.set(hash,result,3600*24*3)

    def get(self,hash):
        return self.conn.get(hash)


if __name__ == '__main__':
    rr = RedisResults()
    rr.save("hash","value")

    print rr.get("hash")

    if(rr.get("test")):
        print "exist"
    else:
        print "not exist"