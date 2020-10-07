#!/usr/bin/env python

from rx import of

source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

source.subscribe(lambda value: print("Received {0}".format(value)))
