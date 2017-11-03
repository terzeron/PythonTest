#!/usr/bin/env python

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep("coroutine")

# next(search) 없이 사용가능함
# @coroutine 장식자 내부에서 next(cr)를 호출했음
search.send("I love you")
search.send("I love coroutine")
search.close()