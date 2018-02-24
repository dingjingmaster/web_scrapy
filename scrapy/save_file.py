#!/usr/bin/env python
# -*- coding: utf-8 -*-


def save(file, content):
    with open(file, 'w') as writer:
        writer.write(content.encode("utf-8"))
        writer.close()