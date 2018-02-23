#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.downloader import Downloader
from scrapy.url_parser import URLParse


class Engine:
    def __init__(self, url, method="get", para=None):
        self.success = set()
        self.failure = set()

        self.page = set()
        self.other = set()
        self.pageMain = set()

        self.baseUrl = url
        self.__add_url_main(self.baseUrl)
        self.method = method
        self.para = para

    def __del__(self):
        pass

    def stop(self):
        pass

    def run(self):
        while True:
            if len(self.page) <= 0 and len(self.pageMain) <= 0:
                self.stop()
            self.__download_url(self.__get_url_main())                      # 获取url
            #self.__download_passage(self)
            pass
        pass

    def __download_passage(self, url):
        if url is None:
            return
        # 解析出文章,递归调用
        pass

    def __download_url(self, url):
        if url is None:
            return
        download = Downloader(url)
        html = download.run()
        if 'error' != html:
            purl = URLParse(self.baseUrl, html)
            page, pm, other = purl.run()
            # 检查是否重复#####################################
            self.__insert_set(page, self.page)
            self.__insert_set(pm, self.pageMain)
            self.__insert_set(other, self.other)
            self.success.add(url)
        else:
            self.failure.add(url)
        return None

    @staticmethod
    def __insert_set(lis, mse):
        for i in lis:
            mse.add(i)
        return None

    def __add_url_main(self, url):
        self.pageMain.add(url)

    def __get_url_main(self):
        if len(self.pageMain) > 0:
            return self.pageMain.pop()
        return None

    def __add_url_page(self, url):
        self.page.add(url)

    def __get_url_page(self):
        if len(self.page) > 0:
            return self.page.pop()
        return None

    def __add_url_other(self, url):
        self.other.add(url)


if __name__ == '__main__':
    eng = Engine("http://www.cnys.com")
    eng.run()

