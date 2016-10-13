#coding=utf-8
'''
Created on 2016-8-15

@author: 研发
'''
from pyquery import PyQuery as jq
import sys
from myblog.tools import getHTML,parse_words

#解析Html
def parse_body(html):
    movies = []
    doc = jq(html)('.x-item')
    for item in doc:
        item = jq(item)
        name = parse_words(item, '.title')
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

#解析http://www.cilisou.cn/
def parse_cilisou(html):
    movies = []
    doc = jq(html)('.search-item')
    for item in doc:
        item = jq(item)
        name = parse_words(item, '.item-title')
        magnet = jq(item('a')[1]).attr('href')
        detail = jq(item('span')).text()
        # print '名称          ：',name
        # print '详细          ：',detail
        # print '磁力链接: ',magnet
        # print '--------------------------------------------------------------'
        movie = []
        movie.append(name)
        movie.append(detail)
        movie.append(magnet)
        movies.append(movie)
    return movies

def get_bt(key,page):
    try:
        url = ''.join(['http://www.btsousousou.com/search/', key, '-first-asc-',page, '.html'])
        html = getHTML(url)
        movies = parse_cilisou(html)
    except Exception, ex:
        url = ''.join(['http://www.nimasou.net/l/',key,'-hot-desc-',page])
        html = getHTML(url)
        movies = parse_body(html)
    print url
    return movies

def test(key):
    url = ''.join(['http://www.btsousousou.com/search/', key, '-first-asc-', '1','.html'])
    print url
    html = getHTML(url)
    # html
    movies = parse_cilisou(html)

if __name__ == '__main__':
    test('haha')
        


