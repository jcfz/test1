# -*- coding:utf-8 -*-
from datetime import datetime
import json
import os
from xml.dom import minidom
from luhu_sharper.lib.axmlparser import axmlprinter

#e4/8a8/548/6f1588cbf558168a.apk
apk_path = "/home/john/cfz/28fe8c1f70038834.apk"

to_dir = "/tmp/%s" % apk_path[apk_path.rfind("/") + 1:-4]
print 'cfz-----1------',to_dir

os.system('unzip %s -d %s >> /dev/null' % (apk_path, to_dir))
print 'cfz-----2------',to_dir
# 读取app manifest信息
ap = axmlprinter.AXMLPrinter(open('%s/AndroidManifest.xml' % to_dir, 'rb').read())
print 'cfz-----3------',ap
buff = minidom.parseString(ap.getBuff())
print 'cfz-----4------',buff
ele = buff.getElementsByTagName("manifest")[0]
print 'cfz-----5------',ele
dic = {}
for k, v in ele.attributes.items():
    print 'cfz-----kv------',k,v
    dic[k] = v
ret = dict()
# 填充apk信息
ret['size'] = os.path.getsize(apk_path)
ret['package_name'] = dic.get('package', None)
ret['version_code'] = dic.get('android:versionCode', None)
ret['version_name'] = dic.get('android:versionName', None)
print 'cfz-----6------',ret
# AppLog.write(AppAction.AppTrack, key1="back_delete2", key2=to_dir,
# key3=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))