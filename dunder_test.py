#!/usr/bin/env python

from pprint import pprint 


class X:
    static_b: int = 4.7

    def __init__(self):
        self.a = 3
        self.c = "hello world"
        self.d = True
    
    def get_a(self):
        return self.a

def func1():
    return "python"


x = X()
pprint(x.a)
pprint(X.static_b)
d1 = set(dir(X))
d2 = set(dir(x.a))
d3 = set(dir(x.c))
d4 = set(dir(x.static_b))
d5 = set(dir(x.d))
d6 = set(dir(x.get_a))
d7 = set(dir(func1))

print("-------- common attributes & methods --------")
d = d1 & d2 & d3 & d4 & d5 & d6 & d7
pprint(d)
print("-------- attributes & methods for class --------")
pprint(d1 - d)
print("-------- attributes & methods for class attribute --------")
pprint((d2 & d3 & d5) - d)
print("-------- attributes & methods for class static attribute --------")
pprint(d4 - d)
print("-------- attributes & methods for various methods & functions --------")
pprint((d4 & d6 & d7) - d)

