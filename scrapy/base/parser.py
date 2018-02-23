#!/usr/bin/env python
# -*- coding = "utf-8" -*-
from bs4 import BeautifulSoup as BS
from scrapy.downloader import Downloader
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class BSParser:
    """

    """
    def __init__(self):
        pass
    pass


if __name__ == '__main__':
    down = Downloader("http://blog.csdn.net/qiannianguji01/article/details/50397046", "get", "")
    html = down.run()
    soup = BS(html)
    tag = soup.body.find_all('a')
    for i in tag:
        print i
        #print BS(i).a