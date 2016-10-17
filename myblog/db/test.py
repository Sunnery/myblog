#coding=utf-8
'''
Created on 2016-8-12

@author: 研发
'''

import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123',
        db ='wyyz',
        charset="utf8"
        )
cur = conn.cursor()

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
sql = "insert into myblog_loginrecord(id,ip,region,time,url,account) values(23,'阿瑟东','阿瑟东','阿瑟东','阿瑟东','阿瑟东')"
cur.execute(sql)


#修改查询条件的数据
#cur.execute("SELECT * from pokemon")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

#插入多条数据
#sqlStr = "insert into pokemon (id,name) values (%s,%s)"
#cur.executemany(sqlStr,[(3,"妙蛙种子"),(4,"皮卡丘"),(5,"杰尼龟")])

#查询
# cur = conn.cursor()
# totalNum = cur.execute("select * from pokemon")
# print totalNum
# totalRecord = cur.fetchmany(totalNum)
# for record in totalRecord:
#     for i in record:
#         print i

cur.close()
conn.commit()
conn.close()
