# -*- coding:utf-8 -*-
import urllib2
import flask
import requests
import chardet
# python3 shixian
#page = urllib.request.urlopen('http://www.meituba.com/tag/juesemeinv.html')  # 打开网页
#htmlCode = page.read()  # 获取网页源代码


url = "https://www.baidu.com"
response = urllib2.urlopen(url)
code = response.getcode()
content = response.read()
print "状态码：", code
print "网页内容", content




