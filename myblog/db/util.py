#coding=utf-8
from django.db import connection
from myblog.models import LoginRecord
import math

def getMaxId(tableName):
    cursor = connection.cursor()
    sql = ''.join(['select max(id) from ',tableName])
    cursor.execute(sql)
    row = cursor.fetchone()
    id = 1
    if not row[0] == None:
        id = row[0]+1
    return id

def getRecords(page,pageNum,pageTable,select,condition,orderby):
    start = (page-int(1))*pageNum
    end = start+pageNum
    raw_sql = "".join(['select * from (select ',select,' @rownum:=@rownum+1 rownum,t.* From (SELECT @rownum:=0,t.* from ',pageTable,' t ORDER BY t.',orderby,' desc ) t WHERE 1=1 ',condition,') t1 where t1.rownum >',str(start),' and t1.rownum <= ',str(end)])

    print raw_sql
    LoginRecords = LoginRecord.objects.raw(raw_sql)
    return LoginRecords

def getTotalNum(tableName):
    cursor = connection.cursor()
    sql = ''.join(["select count(1) from ",tableName])
    cursor.execute(sql)
    row = cursor.fetchone()
    return row[0]

def getPages(request,pageTable,select,condition,orderby):
    pageNum = int(5)
    page = request.GET.get('page')
    content = {}
    if page == None:
        page = 1
    page = int(page)
    records = getRecords(page, pageNum,pageTable,select,condition,orderby)
    totalNum = getTotalNum(pageTable)
    pages = []
    totalPages = math.ceil(float(totalNum) / pageNum)
    start = (page - 4) > 0 and (page - 4) or 1
    end = page + 4
    if end > totalPages:
        end = int(totalPages)
        start = int(totalPages - 9)
    if (end - start) < 8:
        end = end + (9 - end)
    if start < 1:
        start = 1
    for i in range(start, end + 1):
        pages.append(i)
    content['page'] = page
    content['records'] = records
    content['totalPages'] = int(totalPages)
    content['pages'] = pages
    return content