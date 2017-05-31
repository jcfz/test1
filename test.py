# -*- coding:utf-8 -*-

__author__ = [
    '"John Chan" <chenfazhun@hi-wifi.cn>'
]


# from urllib import urlencode,quote
#
#
# print quote('http://www.baidu.com')
#
# import urllib
#
# url = 'http://test.com/s?wd=哈哈'
#
# url = url.decode('gbk', 'replace')
#
# print urllib.quote(url.encode('utf-8', 'replace'))

# from datetime import datetime,date,timedelta
# d =  date.today()
# print d
# y = d - timedelta(hours=24)
# print y

from datetime import datetime,date,timedelta
today = datetime.now().strftime('%y%m%M')
print today


rank = '170305000099'
rank_d = int(rank[6:])
rank_d = rank_d+1
rank_num = len(str(rank_d))
rank = '0'*(6-rank_num)+str(rank_d)
print rank