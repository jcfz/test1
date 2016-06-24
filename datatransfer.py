# -*- coding:utf-8 -*-

import MySQLdb
import datetime
import os
import ConfigParser
cf = ConfigParser.ConfigParser()
#read config
cf.read("pw.conf")

path = os.path.split(os.path.realpath(__file__))[0]
user1 = cf.get('transfer','user')
password = cf.get('transfer','password')
db = cf.get('transfer','db')


def fuck(num=0):
    try:
        i = 0
        conn = MySQLdb.connect(host='127.0.0.1', user=user1, passwd=password, port=23306)
        cur = conn.cursor()
        conn.select_db(db)
        cur.execute('select DISTINCT user_id from user_login order by create_time desc;')
        results = cur.fetchall()
        cur.close()
        conn.close()
        print results
        if not os.path.exists(path+os.sep+'db'):
            os.makedirs(path+os.sep+'db')
        dbfile = file(path+os.sep+'db'+os.sep+str(datetime.date.today()), 'w')
        for user in results:
            print user[0]
            if not isExist(str(user[0])):
                i += 1
                if i > num:
                    break
                dbfile.write('104,1002,{\"user_id\":\"'+str(user[0])+'\",\"flag\":1}'+'\n')
        dbfile.close()
    except MySQLdb.Error, e:
            print e


def isExist(s=None):
    db_file = os.walk(path+os.sep+'db')
    for f in db_file:
        print 'open old db file。。。'
        for d_f in f[2]:
            print 'list file',d_f
            old_file = file(path+os.sep+'db'+os.sep+d_f, 'rb')
            for o_f in old_file:
                if o_f.find(s) >= 0:
                    print s,'imported！'
                    return True


fuck(10)