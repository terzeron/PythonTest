#!/usr/bin/env python

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep("coroutine")
next(search) # or search.send(None)
search.send("I love you")
search.send("I love coroutine")
search.close()