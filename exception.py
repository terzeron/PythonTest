#!/usr/bin/env python3

def oops():
    1/0

def ooops():
    try:
        oops()
    except ZeroDivisionError:
        raise RuntimeError("Ooops!")

ooops()
