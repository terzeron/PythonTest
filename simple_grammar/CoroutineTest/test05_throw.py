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
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away. Goodbye")

search = grep("coroutine")
# without next(search)
search.send("I love you")
search.send("I love coroutine")

# 코루틴 안쪽으로 예외를 던지기
search.throw(RuntimeError, "You're hosed")
# yield에서 예외 발생

