#!/usr/bin/env python
# -*- coding = "utf-8" -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Downloader:
    """ download
    """
    def __init__(self, url, method="get", para=None):
        self.method = method.upper()
        self.para = para
        self.response = None
        if url != "":
            self.url = self.__norm_url(url)
        else:
            return

    @staticmethod
    def __norm_url(url):
        url = url.replace('http://', '')
        url = url.replace('https://', '')
        if url.endswith('/'):
            url = url[:-1]
        return url

    def run(self):
        if self.method == "GET":
            self.response = requests.get('http://' + self.url)
        if self.response is not None and 200 == int(self.response.status_code):
            return self.response.content
        return 'error'

    def __del__(self):
        del self.url
        del self.method
        del self.para
        del self.response


'''
if __name__ == '__main__':
    down = Downloader("http://blog.csdn.net/qiannianguji01/article/details/50397046", "get", "")
    print down.run()
'''


