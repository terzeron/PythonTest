#!/usr/bin/env python

import time
import random
import multiprocessing
from threading import current_thread
from rx import range, operators as op
from rx.scheduler import NewThreadScheduler, ThreadPoolScheduler


def work_slowly(value):
    print("{0}\t: work_slowly({1}) -> {2}".format(current_thread().name, value, value * 2))
    time.sleep(random.randint(5, 20) * 0.1)
    return value * 2

def work_another_job(value):
    print("{0}\t: work_another_job({1}) -> {2}".format(current_thread().name, value, value * 2))
    time.sleep(random.randint(5, 20) * 0.1)
    return value * 2


print("{0}\t: main".format(current_thread().name))

#scheduler = ThreadPoolScheduler(multiprocessing.cpu_count())
scheduler = NewThreadScheduler()

range(10).pipe(
    op.map(lambda num: work_slowly(num)),
    op.observe_on(scheduler),
    op.map(lambda num: work_another_job(num)),
    #op.subscribe_on(scheduler),
    #op.reduce(lambda acc, item: acc + item),
).subscribe(
    on_next=lambda i: print("{0}\t: subscribe {1}".format(current_thread().name, i)),
    on_error=lambda e: print(e),
    #scheduler=scheduler,
)

input("Press any key to exit\n")
