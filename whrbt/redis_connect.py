import redis
class Connect:
    def __init__(self,host="localhost",port=6379,password=None):
        self.r=redis.Redis(host=host,port=port,password=password)
    def addUser(self,city,wechat_id):
        self.r.sadd(city,wechat_id)
    def deleteUser(self,city,wechat_id):
        self.r.srem(city,wechat_id)
