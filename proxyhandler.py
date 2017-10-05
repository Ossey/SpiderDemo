#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

# 代理开关，表示是否使用代理
proxySwitch = True

# 构建一个Handler处理对象，参数一个字典类型对象，包括代理类型和代理服务器的ip+端口号
httpproxy_handler = urllib2.ProxyHandler({"http": "122.224.227.202:3128"})

# 构建一个没有代理的处理器对象, 参数为一个{}空的字典类型
nullproxy_handler = urllib2.ProxyHandler({})

if proxySwitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

# 构建一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
urllib2.install_opener(opener)
# response = opener.open("http://www.baidu.com/")

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)

print response.read()





