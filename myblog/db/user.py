#coding=utf-8
from django.db import connection,transaction
from myblog.db.util import getMaxId,getRecords
import  time


def insertReqLog(LoginRecord):
    cursor = connection.cursor()
    id = getMaxId('myblog_loginrecord')+1
    sql = 'insert into myblog_loginrecord(id,ip,region,time,url,account) values(%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, [id,LoginRecord.ip, LoginRecord.region, LoginRecord.time,LoginRecord.url,LoginRecord.account])
    transaction.commit()

def register(user):
    cursor = connection.cursor()
    id = getMaxId('myblog_user')
    sql = 'insert into myblog_user(id,email,creatTime,latestLogin,status,iconUrl,password,nickName,iconUrl_small) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql,[id, user.email, user.creatTime, user.latestLogin, user.status, user.iconUrl,user.password,user.nickName,user.iconUrl_small])
    transaction.commit()

def getUserModel(nickName):
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    userModel = getRecords(1,1,'myblog_user','',''.join(['and nickName = "',str(nickName),'"']),'id')
    ISOTIMEFORMAT = '%Y-%m-%d'
    u = userModel[0]
    u.creatTime = time.strftime(ISOTIMEFORMAT, userModel[0].creatTime.timetuple())
    return u


# def db():
#     cursor = connection.cursor()  # 获得一个游标(cursor)对象
#     # 更新操作
#     cursor.execute('update other_other2 set name ="李四" where id=%s', [3])  # 执行sql语句
#     transaction.commit_unless_managed()  # 提交到数据库
#     # 查询操作
#     cursor.execute('select * from other_other2 where id>%s', [1])
#     raw = cursor.fetchone()  # 返回结果行 或使用 #raw = cursor.fetchall()
#
#     # 如果连接多个数据库则使用django.db.connections
#     from django.db import connections
#     _cursor = connections['other_database'].cursor()
#     # 如果执行了更新、删除等操作
#     transaction.commit_unless_managed(using='other_databases')