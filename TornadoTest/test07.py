#!/usr/bin/env python
import tornado
from tornado import gen


@gen.coroutine
def divide(x, y):
    return x / y

def bad_call():
    divide(1, 0)

@gen.coroutine
def good_call():
    yield divide(1, 0)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_async(lambda: divide(1, 0))