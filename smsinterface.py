# -*- coding:utf-8 -*-

import time
import urllib
import types
import os
import json
import socket

import urllib3
import ConfigParser
cf = ConfigParser.ConfigParser()
#read config
cf.read("pw.conf")

platform_api_url = cf.get('sms','platform_api_url')
APP_KEY = cf.get('sms','APP_KEY')
app_id = cf.get('sms','app_id')
APP_KEY = cf.get('sms','APP_KEY')


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


class HttpPoolUtils(object):
    __metaclass__ = Singleton

    http_pool = None
    #http = None

    def __init__(self):
        print 'aa'
        self.http_pool = urllib3.HTTPConnectionPool('platformapi.hi-wifi.cn', maxsize=102400, timeout=10)
        self.http_pool.ConnectionCls.default_socket_options + [
                (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
            ]
        #self.http = urllib3.PoolManager()
        print 'bb'

    def md5(self, s):
        import hashlib
        if type(s) is not types.StringType:
            s = str(s)
        m = hashlib.md5()
        m.update(s)
        return m.hexdigest()

    def doParams(self, params):
        """
        客户端接口签名算法 把参数(包括系统参数和业务参数)除sign和空值外, 按照key的首字母顺序排序, 用key1+value1+key2+value2+...的方式拼接在一起,
        再在最后加上app_key,然后转UTF-8编码进行MD5后, 得到字符串再转小写。 即: md5(utf-8:k1+v1+k2+v2+...+kn+vn + app_key).toLowerCase()
        服务端接口签名算法 算法同上, 唯一不同的是将app_key替换成app_secret
        :param params:
        :return:重载后的params
        """
        params = sorted(params.iteritems(), key=lambda k: k[0], reverse=False)
        s = ''
        p_list = []
        for p_key, p_value in params:
            if p_value is not None and p_value is not '':
                if type(p_value) is unicode:
                    p_value = p_value.encode('utf-8')
                p_list.append([p_key,p_value])
                s += p_key+str(p_value)
        sign = self.md5((s+APP_KEY)).lower()
        params = dict(p_list)
        params.update(dict(sign=sign))
        return params


    def doPost(self,url, params):
        params = self.doParams(params)
        params = urllib.urlencode(params)
        r = self.http_pool.urlopen('POST', url=url,body=params, redirect=False)
        res = r.data
        return res


def send_sms(phone, msg):
    url = platform_api_url + '/sms/mt'
    params = dict(app_id=app_id,
                  timestamp=str(int(time.time())),
                  sign_method='md5',
                  phone=phone,
                  msg=msg,
                  biz_type=2,
                  biz_code=6,
                  client_ip='180.150.177.130',
                  sp='chuanglan')
    return HttpPoolUtils().doPost(url, params)

msg='《最佳阵容》欧洲杯竞猜火热上线！累计充值送好礼，登录乐无限WiFi客户端，点首页活动图片参与，小积分赢大奖，分分钟赚积分！退订回T'
try:
    path = os.path.split(os.path.realpath(__file__))[0]
    csvfile = file(path+'/aa.csv', 'rb')
except Exception as e:
    print 'no success ',e
bbfile=file(path+'/bb.csv','w')
for line in csvfile:
    if line:
        lines=line.strip('\n').split(",")
        print '尝试向',lines[0],"发送短信"
        res=send_sms(lines[0],msg)
        return_data = json.loads(res)
        print return_data
        if int(return_data.get('return_code')) != 0:
            print '向',lines[0],'发送短信，失败！保存到bb.csv'
            bbfile.write(lines[0]+"\n")
            time.sleep(2)
        else:
            print '已向',lines[0],'发送短信，成功！'
bbfile.close()
