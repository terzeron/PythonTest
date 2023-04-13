#!/usr/bin/env python


from tornado import gen
from tornado.httpclient import AsyncHTTPClient


async def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    raise gen.Return(response.body)
