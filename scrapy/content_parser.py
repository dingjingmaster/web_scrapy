#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as PQ
from scrapy.downloader import Downloader
from scrapy.utils import url as URL


class ContentParse:
    """
        获取文章内容
    """
    def __init__(self, url):
        self.url = url
        self.title = ""
        self.content = ""
        self.canStop = False

    def __del__(self):
        del self.url
        del self.content

    def run(self):
        self._parse_passage(self.url, True)
        return self.content

    def _parse_passage(self, url, first):
        if self.canStop:
            return
        down = Downloader(url)
        html = down.run()                                       # 获取到 html 内容
        info = PQ(html)
        self._parse_title(info('div').filter('.readbox'))
        self._parse_content(info('div').filter('.reads'))
        nextUrl = self._parse_next_page(info('div').filter('.page'))
        if nextUrl is not None:
            self._parse_passage(nextUrl, False)
        else:
            self.canStop = True

    def _parse_next_page(self, div):
        url = None
        a = div('a')
        for i in range(len(a)):
            if '下一页' == a.eq(i).attr('title'):
                url = URL.norm_url(a.eq(i).attr('href'))
        if self._right_url(url):
            return url
        return None

    @staticmethod
    def _right_url(url):
        if url is None:
            return False
        if url.find('javascript:') >= 0:
            return False
        return True

    def _parse_content(self, div):
        self.content = self.content + div('p').text()
        return None

    def _parse_title(self, div):
        self.title = div('h1').text()
        return None

    def _print_content(self):
        print self.content
        return None


if __name__ == '__main__':
    cont = ContentParse("http://www.cnys.com/zixun/77211.html")
    cont.run()
    cont._print_content()

