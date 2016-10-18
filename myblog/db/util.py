#coding=utf-8
from django.db import connection,transaction

def getTotalRecordNum(tableName):
    cursor = connection.cursor()
    sql = 'select max(id) from myblog_loginrecord '
    cursor.execute(sql)
    row = cursor.fetchone()
    return row[0]