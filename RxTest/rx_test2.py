#!/usr/bin/env python3

import rx
from rx import Observable, Observer

class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)
        
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("Sequence completed")

'''
xs = Observable.from_iterable(range(100))
d = xs.subscribe(MyObserver())
'''
        
'''
xs = Observable.from_(range(10))
d = xs.filter(
        lambda x: x % 2
    ).subscribe(print)
'''

xs = Observable.from_(range(10))
d = xs.map(
        lambda x: x * 2
    ).subscribe(print)

xs = Observable.from_(range(10, 20, 2))
d = xs.map(
        lambda x, i: "%s: %s" % (i, x * 2)
    ).subscribe(print)

xs = Observable.range(1, 5)
ys = Observable.from_("abcde")
zs = xs.merge(ys).subscribe(print)
