#!/usr/bin/env python
# -*- coding: utf-8 -*-


def save(file, content):
    writer = open(file, 'wb')
    writer.write(content.encode('utf-8'))
    writer.close()