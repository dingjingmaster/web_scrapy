#!/usr/bin/env python
# -*- coding = "utf-8" -*-
import requests
import sys


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

    def __norm_url(self, url):
        url = url.replace('http://', '')
        url = url.replace('https://', '')
        while url.endswith('/'):
            url = url[:-1]
        while not self.__is_alpha(url[0]):
            url = url[1:]
        return url

    @staticmethod
    def __is_alpha(char):
        ascii = ord(char)
        if ((ascii >= 48) and (ascii <= 57)) or ((ascii >= 65) and (ascii <= 90)) or ((ascii >= 97) and (ascii <= 122)):
            return True
        return False

    def run(self):
        try:
            if self.method == "GET":
                self.response = requests.get('http://' + self.url)
        finally:
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


