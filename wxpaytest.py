# -*- coding:utf-8 -*-

__author__ = 'john'
import urllib2, hashlib

url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
key = '000000000000000000000000000'
appid = '00000000000000'
mch_id = '000000000000'


def copy_params(params):
    ret = {}
    for key in params.keys():
        ret[key] = params[key]
    return ret


def populateURLStr(params):
    new_params = copy_params(params)
    ks = new_params.keys()
    ks.sort()
    rlt = ''
    for k in ks:
        new_params[k] = str(new_params[k])
        if new_params[k] is None or len(new_params[k]) == 0 \
                or k == "sign":
            continue
        rlt = "%s&%s=%s" % (rlt, k, new_params[k])

    print '===============', rlt[1:]
    return rlt[1:]


def sign(params):
    sign = hashlib.md5(populateURLStr(params) + "&key=" + key).hexdigest()
    return sign.upper()


def test():
    params = dict(body='Hi-WiFi充值 900Hi点', out_trade_no='123', total_fee='1',
                  spbill_create_ip='127.0.0.1', notify_url='http://test.api.hi-wifi.cn/pay/notify/alipay', trade_type="APP")
    params['appid'] = appid
    params['mch_id'] = mch_id
    import uuid
    params['nonce_str'] = str(uuid.uuid1())[:16]

    sign1 = sign(params)
    print '----------------sign---------------', sign1
    print '------------------------weixin-------------', params
    data = '''<xml>
               <appid>%s</appid>
               <body>%s</body>
               <mch_id>%s</mch_id>
               <nonce_str>%s</nonce_str>
               <notify_url>%s</notify_url>
               <out_trade_no>%s</out_trade_no>
               <spbill_create_ip>%s</spbill_create_ip>
               <total_fee>%s</total_fee>
               <trade_type>%s</trade_type>
               <sign>%s</sign>
               </xml>''' % (
        appid, params['body'], mch_id, params['nonce_str'], params['notify_url'], params['out_trade_no'],
        params['spbill_create_ip'],
        params['total_fee'], params['trade_type'], sign1)
    print 'data------------------', data
    data = '''<xml>
    <appid>wx11eaa73053dd1666</appid>
               <body>Hi-WiFi充值 900Hi点</body>
               <mch_id>1254530101</mch_id>
               <nonce_str>6831103a-41d4-11</nonce_str>
               <notify_url>http://test.api.hi-wifi.cn/pay/notify/alipay</notify_url>
               <out_trade_no>1223</out_trade_no>
               <spbill_create_ip>116.226.33.208</spbill_create_ip>
               <total_fee>1</total_fee>
               <trade_type>APP</trade_type>
               <sign>B20085B47CD7C30591A995C9580B6C60</sign>
               </xml>'''

    print 'data===',data

    req = urllib2.Request(url=url, headers={'Content-Type': 'application/xml', 'charset': 'UTF-8'}, data=data)
    res = urllib2.urlopen(req)
    print 'res-----------------------------', res.read()





test()
