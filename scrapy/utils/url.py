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

#def is_url(burl):



