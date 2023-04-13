#!/usr/bin/env python


from tornado.httpclient import HTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    print(response.body)


if __name__ == "__main__":
    synchronous_fetch("http://terzeron.net")
