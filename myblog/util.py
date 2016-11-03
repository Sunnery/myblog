# -*- coding: utf-8 -*-
import requests
import time
from myblog.db.user import insertReqLog
from myblog.models import LoginRecord
from qiniu import Auth, put_data
import hashlib


def get_client_ip(request):
    try:
      real_ip = request.META['HTTP_X_FORWARDED_FOR']
      regip = real_ip.split(",")[0]
    except:
      try:
        regip = request.META['REMOTE_ADDR']
      except:
        regip = ""
    lookup(regip,request)


def lookup(ip,request):
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
        except Exception:
            region = 'None'
    LoginRecord.ip = ip
    LoginRecord.region = region
    fmt ='%Y-%m-%d %X'
    LoginRecord.time = time.strftime(fmt, time.localtime())
    LoginRecord.url = request.get_full_path()
    LoginRecord.account = request.user.id
    insertReqLog(LoginRecord)


def getTime():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT, time.localtime())


def qiniuUpload(key,data):
  # 需要填写你的 Access Key 和 Secret Key
  access_key = "6Ct_gOzm6X2bo_LQchKhOKMkSMhYmajFJiuPh5oc"
  secret_key = "sbQMnyz96cQnh97uRaTkSqOQj022F0EX8hhuo-n-"
  # 构建鉴权对象
  q = Auth(access_key, secret_key)
  # 要上传的空间
  bucket_name = 'publicpicture'
  # 生成上传 Token，可以指定过期时间等
  token = q.upload_token(bucket_name, key, 3600)
  # 要上传文件的本地路径
  ret, info = put_data(token, key, data)
  return 'http://ofjorzzw5.bkt.clouddn.com/' + key


def getMD5(str):
    m2 = hashlib.md5()
    m2.update('str')
    return m2.hexdigest()