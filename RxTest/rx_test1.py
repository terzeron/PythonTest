#!/usr/bin/env python

import time
import rx

def work_slowly(value):
    def go_make_big(subscriber):
        subscriber.on_next(make_big(value))
        subscriber.on_completed()
    return rx.Observable.create(go_make_big)

def make_big(value):
    print("Make big {}".format(value))
    time.sleep(1)
    print("Done for big {}".format(value))
    return value * 2

scheduler = rx.concurrency.NewThreadScheduler()
rx.Observable.from_([1, 2, 3, 4]) \
    .flat_map(lambda num: work_slowly(num).subscribe_on(scheduler)) \
    .reduce(lambda a, b: a + b) \
    .subscribe(print)

time.sleep(1.01)
