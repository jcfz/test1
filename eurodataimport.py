# -*- coding:utf-8 -*-

import MySQLdb
import datetime
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
path = os.path.split(os.path.realpath(__file__))[0]

#INSERT INTO `luhu`.`european_cup_charge_detail`(`uid`,`role_name`,`charge_amount`,`charge_time`)VALUES('608387','绿茵豪门','25','2016-06-14');



def fuck():
    dbfile = isExist()
    for line in dbfile:
        s = line.strip('\n').split(",")
        print 'INSERT INTO european_cup_charge_detail(uid,role_name,charge_amount,charge_time)VALUES(%s,\'%s\',%s,\'%s 00:00:00\');'%(s[0],s[1],s[3],s[2])


def isExist():
    dbfile = file(path+os.sep+'db', 'rb')
    return dbfile
    dbfile.close()

fuck()