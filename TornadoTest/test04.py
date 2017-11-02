#!/usr/bin/env python

from tornado.concurrent import Future
from tornado.httpclient import AsyncHTTPClient


def async_fetch_future(url):
    print("start")
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result())
    )
    print("end")
    return my_future

