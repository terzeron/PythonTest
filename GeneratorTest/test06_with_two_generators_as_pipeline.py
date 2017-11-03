#!/usr/bin/env python
import time


def follow(thefile):
    thefile.seek(0, 2)

    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


logfile = open("access-log")

# 파이프라인을 구축할 수 있음
loglines = follow(logfile)
pylines = grep("python", loglines)

print(pylines)
next(pylines)
next(pylines)
next(pylines)
