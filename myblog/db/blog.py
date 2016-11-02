#coding=utf-8
from django.db import connection,transaction
from myblog.db.util import getMaxId
from myblog.models import blog

def insert(blog):
    cursor = connection.cursor()
    id = getMaxId('myblog_blog')
    sql = 'insert into myblog_blog(id,title,content,timestamp,view,authorid) values(%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, [id,blog.title, blog.content, blog.timestamp,blog.view,blog.authorid])
    transaction.commit()
    return id