#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import os

def loadFile(url, fileName):
    '''
    根据url发送请求，获取服务器响应文件
    :param url: 需要爬取的url地址
    :param fileName: 对爬取的文件处理的文件名
    :return 服务器响应的文件内容
    '''
    print fileName + "正在请求"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38"
}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request).read()
    return response

def writePage(responseHtml, fileName):
    '''
    将服务器响应的文件写入到本地
    :param responseHtml: 响应数据
    :param fileName: 写入到本地的文件名称
    '''
    filePath = "/Users/mofeini/Desktop/pythonDemoFile/"
    if not os.path.exists(filePath):  # 判断是否存在新文件夹，否则创建
        os.mkdir(filePath)
    filePath = filePath + fileName
    # 文件写入
    with open(filePath, "w") as f:
        f.write(responseHtml)
    print "-" * 30

def tiebaSpider(url, beginPage, endPage):
    '''
    贴吧爬虫调度器，负责组合处理每个url
    :param url 贴吧url的前半部分
    :param beginPage 起始页
    :param endPage 结束页
    '''
    for page in range(beginPage, endPage + 1):
        if page < 1:
            page = 1
        pn = (page - 1) * 50
        fileName = "第" + str(pn) + "页.html"
        fullURLPath = url + "&pn=" + str(pn)
        html = loadFile(fullURLPath, fileName)
        writePage(html, fileName)
        print "谢谢使用"

if __name__ == "__main__":
    kw = raw_input("请输入需要爬虫的贴吧名:")
    beginPage = int(raw_input("请输入起始页:"))
    endPage = int(raw_input("请输入结束页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullURL = url + key
    tiebaSpider(fullURL, beginPage, endPage)






