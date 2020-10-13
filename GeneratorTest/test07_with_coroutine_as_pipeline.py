#!/usr/bin/env python
import time


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start

def follow(thefile, target):
    thefile.seek(0, 2)

    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.5)
            continue
        target.send(line)

@coroutine
def printer():
    while True:
        line = (yield)
        print(line, end="")

logfile = open("access-log")

# 파이프라인을 구축할 수 있음
loglines = follow(logfile, printer())


# 비교
# generator는 iteration을 이용하여 다음 generator에게 전달
# pull 방식
# 보내는 쪽은 yield로 보내고 받는 쪽은 next()로 받음
# coroutine은 send()를 이용하여 다음 coroutine에게 전달
# push 방식​
# 보내는 쪽은 send()로 보내고 받는 쪽은 (yield)로 받음
