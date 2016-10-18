#coding=utf-8
from django.db import connection,transaction
from myblog.models import LoginRecord
from myblog.db.util import getTotalRecordNum

def insertReqLog(LoginRecord):
    cursor = connection.cursor()
    id = getTotalRecordNum('myblog_loginrecord')+1
    sql = 'insert into myblog_loginrecord(id,ip,region,time,url,account) values(%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, [id,LoginRecord.ip, LoginRecord.region, LoginRecord.time,LoginRecord.url,LoginRecord.account])
    transaction.commit()

def getReqLog(page,pageNum):
    start = (page-int(1))*pageNum
    end = start+pageNum
    raw_sql = "".join(['select * from myblog_loginrecord t where _rowid >',str(start),' and _rowid <= ',str(end)])
    print raw_sql
    LoginRecords = LoginRecord.objects.raw(raw_sql)
    return LoginRecords

def getReqLogTotalNum():
    cursor = connection.cursor()
    sql = "select count(1) from myblog_loginrecord "
    cursor.execute(sql)
    row = cursor.fetchone()
    return row[0]

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