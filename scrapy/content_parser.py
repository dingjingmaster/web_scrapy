#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as PQ
from scrapy.downloader import Downloader
from scrapy.utils import url as URL


class ContentParse:
    """
        获取文章内容
    """
    def __init__(self, burl, url):
        self.baseUrl = burl
        self.url = url
        self.reqUrl = url
        self.title = ""
        self.content = ""
        self.requested = set()

    def __del__(self):
        del self.url
        del self.content

    def run(self):
        self._parse_passage()
        return self.url, self.title, self.content

    def _parse_passage(self):
        while(True):
            down = Downloader(self.reqUrl)
            html = down.run()                                       # 获取到 html 内容
            info = PQ(html)
            self.requested.add(self.reqUrl)
            all = info('div').filter('.readbox')
            page = all('div').filter('.reads')
            self._parse_title(all)
            self._parse_content(page)
            self.reqUrl = self._parse_next_page_url(info('div').filter('.page'))
            if (self.reqUrl is None) or (self.reqUrl in self.requested):
               break

    def _parse_next_page_url(self, div):
        url = None
        a = div('a')
        for i in range(len(a)):
            try:
                if u'下一页' == a.eq(i).text():
                    url = URL.norm_url(a.eq(i).attr('href'))
            except:
                continue
        url = self._revise_url(url)
        return url

    def _revise_url(self, url):
        if (url is None) or (url.find('javascript') >= 0):
            return None
        if url.find(self.baseUrl) < 0:
            url = self.baseUrl + '/' + url
        return url

    def _parse_content(self, div):
        self.content = self.content + '\n' + div.text()
        return None

    def _parse_title(self, div):
        self.title = div('h1').text()
        return None

    def _print_content(self):
        print self.content
        return None


'''
if __name__ == '__main__':
    cont = ContentParse("http://www.cnys.com/zixun/77211.html")
    cont.run()
    cont._print_content()
'''

