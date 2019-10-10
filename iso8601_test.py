#!/usr/bin/env python

from datetime import datetime

print("today=", datetime.today())
print("now=", datetime.now())
print("isoformat=", datetime.now().isoformat())
print("astimezone, isoformat=", datetime.now().astimezone().isoformat())
print("replace microsecond, isoformat=", datetime.now().replace(microsecond=0).isoformat())
print("replace microsecond, astimezone, isoformat=", datetime.now().replace(microsecond=0).astimezone().isoformat())
print("astimezone, timespec, isoformat=", datetime.now().astimezone().isoformat(timespec="seconds"))

import time
print("tzname=", time.tzname)

import pytz
print("utc isoformat=", datetime.now(tz=pytz.utc).isoformat())

import dateutil.parser
datetime_str = "2019-07-09T14:07:17+09:00"
dt = dateutil.parser.parse(datetime_str)
print("date=", dt)
