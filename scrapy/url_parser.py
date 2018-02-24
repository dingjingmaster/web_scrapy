#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as PQ


class URLParse:
    """
        获取文章主页
    """
    def __init__(self, url, html, deep=0):
        self.baseUrl = url
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

    def run(self):
        self._find_url()
        return self.pageUrls, self.pageMain, self.otherUrl

    def _find_url(self):
        a = PQ(self.html).find('a')
        for i in range(len(a)):
            url = a.eq(i).attr('href')
            if url is not None:
                self._distribute_url(url)
        return None

    def _distribute_url(self, url):
        if url.find(self.baseUrl) > -1:
            if url.endswith('.html'):
                self.pageUrls.add(url)
            else:
                self.pageMain.add(url)
        else:
            self.otherUrl.add(url)
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
