#!/usr/bin/env python

def oops():
    1/0

def ooops():
    try:
        oops()
    except ZeroDivisionError:
        raise RuntimeError("Ooops!")

ooops()
