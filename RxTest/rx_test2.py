#!/usr/bin/env python

from rx.core import Observer
from rx import of, range, operators as op

class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)
        
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("Sequence completed")

print("------ observer ------")
range(5).subscribe(MyObserver())

print("------ of ------")
of(7,8).pipe(
    op.map(lambda x: x * 3)
).subscribe(print)
of([7,8]).pipe(
    op.map(lambda x: x * 3)
).subscribe(print)

print("------ map ------")
range(10).pipe(
    op.map(lambda x: x * 2)
).subscribe(print)

print("------ map ------")
range(10, 20, 2).pipe(
    op.map(lambda x: "%d" % (x * 2))
).subscribe(print)

print("------ merge ------")
s1 = range(1, 5)
s2 = of("abcde", "def")
s1.pipe(
    op.merge(s2)
).subscribe(print)
