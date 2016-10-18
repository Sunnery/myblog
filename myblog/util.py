# -*- coding: utf-8 -*-
import requests
import time
from myblog.db.user import insertReqLog
from myblog.models import LoginRecord

def get_client_ip(request):
    try:
      real_ip = request.META['HTTP_X_FORWARDED_FOR']
      regip = real_ip.split(",")[0]
    except:
      try:
        regip = request.META['REMOTE_ADDR']
      except:
        regip = ""
    lookup(regip)

def lookup(ip):
    ips = {'ip': ip}
    URL = 'http://ip.taobao.com/service/getIpInfo.php'
    region = ''
    try:
        r = requests.get(URL, params=ips, timeout=3)
    except requests.RequestException as e:
        region = 'None'
    else:
        try:
            json_data = r.json()
            if json_data[u'code'] == 0:
                region = json_data[u'data'][u'country'].encode('utf-8')+json_data[u'data'][u'area'].encode('utf-8')+json_data[u'data'][u'region'].encode('utf-8')+json_data[u'data'][u'city'].encode('utf-8')+json_data[u'data'][u'isp'].encode('utf-8')
                # print '所在国家： ' + json_data[u'data'][u'country'].encode('utf-8')
                # print '所在地区： ' + json_data[u'data'][u'area'].encode('utf-8')
                # print '所在省份： ' + json_data[u'data'][u'region'].encode('utf-8')
                # print '所在城市： ' + json_data[u'data'][u'city'].encode('utf-8')
                # print '所属运营商：' + json_data[u'data'][u'isp'].encode('utf-8')
            else:
                region = 'None'
        except Exception, ex:
            region = 'None'
    LoginRecord.ip = ip
    LoginRecord.region = region
    ISOTIMEFORMAT ='%Y-%m-%d %X'
    LoginRecord.time = time.strftime(ISOTIMEFORMAT, time.localtime())
    LoginRecord.url = '哈哈'
    LoginRecord.account = 'None'
    insertReqLog(LoginRecord)