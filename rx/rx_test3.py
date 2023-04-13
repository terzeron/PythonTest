#!/usr/bin/env python

from rx.core import Observer
from rx import of

#source = Observable.from_list([1, 2, 3, 4, 5])
source = of([1,2,3,4,5])

class PrintObserver(Observer):
    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error occurred: {0}".format(error))

source.subscribe(PrintObserver())
