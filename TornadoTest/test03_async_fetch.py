#!/usr/bin/env python

from tornado.httpclient import AsyncHTTPClient


def asynchronous_fetch(url, callback):
    print("start")
    http_client = AsyncHTTPClient()
    def handle_response(response):
        callback(response.body)
    http_client.fetch(url, callback=handle_response)
    print("end")


if __name__ == "__main__":
    def handle_response(response):
        print(response)

    asynchronous_fetch("https://terzeron.net", handle_response)
