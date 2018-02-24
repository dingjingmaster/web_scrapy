#!/usr/bin/env python
# -*- coding = "utf-8" -*-


def norm_url(burl):
    burl = burl.replace('http://', '')
    burl = burl.replace('https://', '')
    while burl.endswith('/'):
        burl = burl[:-1]
    while burl.startswith('/'):
        burl = burl[1:]
    return burl


def revise_url(baseUrl, url):
    if (url is None) or (url.find('javascript') >= 0):
        return None
    if url.find(baseUrl) < 0:
        url = baseUrl + '/' + url
    return url



