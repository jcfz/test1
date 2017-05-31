# -*- coding:utf-8 -*-
import requests
from AESCipher import AESCipher
url='http://api.hi-wifi.cn/user/login?uname=18621365260&pwd=123456'
r=requests.get(url)
data=r.json()
seid=data.get("msg")
print 'seid=',seid


AES_KEY = "gf59l!h98$cwks7c"

def check_password(self, password):
	cipher = AESCipher(self.AES_KEY)
	if password == cipher.decrypt(self.password):
		return True
	return False


def set_password(self, password):
	cipher = AESCipher(self.AES_KEY)
	self.password = cipher.encrypt(password)


def get_password(password):
	cipher = AESCipher(AES_KEY)
	return cipher.decrypt(password)



url = 'https://wlan.ct10000.com/wispr_auth.jsp?nasIp=221.239.159.233&amp;wlanuserip=101.225.249.151'
UserName='ad57230218@df.backward.sh'
Password='ck2oK38xOeiqlH38Le9kXQ=='
pwd = get_password(Password)
print pwd
http_url = url+'&seid='+seid
data=dict(UserName=UserName,Password=pwd,button='Login',OriginatingServer=url)
rr=requests.post(url,data=data)
print rr
print rr.status_code
print rr.text


