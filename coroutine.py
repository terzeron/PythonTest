#!/usr/bin/env python3

def sendme():
    while True:
        something = yield
        if something is None:
            raise StopIteration()
        print(something)



gen = sendme()
next(gen)
gen.send('a')
gen.send('b')
gen.send(None)
