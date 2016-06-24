# -*- coding:utf-8 -*-
import json
import urllib2
import time
import os

__author__ = [
    '"John Chan" <chenfazhun@163.com>'
]




url = 'https://buy.itunes.apple.com/verifyReceipt'
test_url = "https://sandbox.itunes.apple.com/verifyReceipt"


class ApplePay(object):

    def __init__(self):
        pass

    @classmethod
    def admin_check_pay_result(self, path):
        receipt_data =''
        #now = datetime.datetime.now()
        #year = now.year
        #month = now.month
        #path = '/var/www/upload/apple'+os.sep+str(year)+os.sep+str(month)
        pj = file(path, 'rb')
        for line in pj:
            receipt_data += line
        params = json.dumps({'receipt-data': receipt_data})
        conn = urllib2.Request(url=url, data=params)
        res_data = urllib2.urlopen(conn)
        res = res_data.read()
        json_res = json.loads(res)
        status = json_res.get('status')
        if int(status) == 21007:
            conn = urllib2.Request(url=test_url, data=params)
            res_data = urllib2.urlopen(conn)
            res = res_data.read()
            json_res = json.loads(res)
        receipt = json_res.get('receipt')
        in_app = receipt.get('in_app')
        in_app_array = sorted(in_app, key=lambda x: x['original_purchase_date_ms'], reverse=True)
        for app in in_app_array:
            original_purchase_date_ms = app.get('original_purchase_date_ms')
            if (time.time()-int(original_purchase_date_ms)/1000)/86400 > 7:
                return False
            product_id = app.get('product_id')
            transaction_id = app.get('transaction_id')
            return product_id,transaction_id
        return 0,0



def id_run(path,id):
    product_id,transaction_id =ApplePay.admin_check_pay_result(path+os.sep+id)
    print id,'-',product_id,'-',transaction_id

def all_run(path):
    db_file = os.walk(path)
    for f in db_file:
        print f
        for d_f in f[2]:
            print 'list file',d_f
            id_run(path,d_f)

path = '/var/www/upload/apple/2016/6'

id_run(path,1101326564)
#all_run(path)