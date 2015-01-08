#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def filter_file(filename):
    lines = []
    f = open(filename)
    for line in f:
        if not line.startswith("#"):
            lines.append(line)
            
    f.close()
    return lines

if __name__ == "__main__":
    filename = sys.argv[1]
    lines = filter_file(filename)
    print lines