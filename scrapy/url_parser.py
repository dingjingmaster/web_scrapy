#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as PQ


class URLParse:
    """
        获取文章主页
    """
    def __init__(self, url, html, deep=0):
        self.baseUrl = self._norm_base_url(url)
        self.deep = deep
        self.html = html
        self.pageUrls = set()
        self.pageMain = set()
        self.otherUrl = set()

    def __del__(self):
        del self.html
        del self.pageUrls
        del self.pageMain
        del self.otherUrl

    @staticmethod
    def _norm_base_url(burl):
        burl = burl.replace('http://', '')
        burl = burl.replace('https://', '')
        if burl.endswith('/'):
            burl = burl[:-1]
        return burl

    def run(self):
        self._find_url()
        return self.pageUrls, self.pageMain, self.otherUrl

    def _norm_url(self, url):
        url1 = ""
        pos = url.find(self.baseUrl)
        if -1 != pos:
            url1 = url[pos:]
        else:
            self.otherUrl.add(url.replace('http://', ''))                                               # 保存其它网站链接
        if url1.endswith('/'):
            url1 = url1[:-1]
        if url1 != "" and url1 != self.baseUrl:
            return url1
        return None

    def _distribute_url(self, url):
        if url.endswith('.html'):
            self.pageUrls.add(url)
        else:
            self.pageMain.add(url)
        return None

    def _find_url(self):
        a = PQ(self.html).find('a')
        for i in range(len(a)):
            url = self._norm_url(a.eq(i).attr('href'))
            if url is not None:
                self._distribute_url(url)
        return None

    def _print_url(self):
        for i in self.pageUrls:
            print '文章url: ' + i
        for i in self.pageMain:
            print '主页url: ' + i
        for i in self.otherUrl:
            print '其它网站url:' + i
        return None


'''
if __name__ == '__main__':
    down = Downloader("http://www.cnys.com", "get", "")
    html = down.run()
    urls = URLParse("www.cnys.com", html, 2)
    urls.run()
    urls._print_url()
'''
