#coding=utf-8
'''
Created on 2016-8-15

@author: 研发
'''
from pyquery import PyQuery as jq
import sys
sys.path.append("C:\\workSpace\\tools.py")
import tools

#解析Html
def parse_body(html):
    movies = []
    doc = jq(html)('.x-item')
    for item in doc:
        item = jq(item)
        name = tools.parse_words(item, '.title')
        magnet = jq(item('.title')[1]).attr('href')
        detail = jq(item('.tail')[0]).text()
        #print '名称          ：',name
        #print '详细          ：',detail
        #print '磁力链接: ',magnet
        #print '--------------------------------------------------------------'
        movie = []
        movie.append(name)
        movie.append(detail)
        movie.append(magnet)
        movies.append(movie)
    return movies

def get_bt(key):
    print key
    for i in range(1,1+1):
        url = ''.join(['http://www.nimasou.net/l/',key,'-hot-desc-',str(i)])
        html = tools.getHTML(url)
        movies = parse_body(html)
    return movies

if __name__ == '__main__':
    movies = get_bt('你妹')
    for movie in movies:
        print movie[0]
        print movie[1]
        print movie[2]
        


