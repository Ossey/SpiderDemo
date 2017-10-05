#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2

def youdaoSpider():
    # post 请求url 可通过抓包的方式获取的url，并不是浏览器上显示的url
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null"

    headers = {
        #"Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        #"Accept-Language": "zh-cn",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://fanyi.youdao.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38",
        "Connection": "keep-alive",
        "Referer": "http://fanyi.youdao.com/",
    }

    kw = raw_input("请输入需要翻译的文本:")
    fromData = {
        "i": kw,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1507207229255",
        "sign": "394d4da72743568ba556388c323a81b9",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "true"
    }

    # 转码
    data = urllib.urlencode(fromData)

    # post请求: 如果Request()方法中的data参数有值就是一个post请求，否则就是get请求
    request = urllib2.Request(url, data=data, headers=headers)
    response = urllib2.urlopen(request).read()
    print response

if __name__ == "__main__":
    youdaoSpider()

