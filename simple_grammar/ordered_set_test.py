#!/usr/bin/env python

from ordered_set import OrderedSet

s1 = OrderedSet([5, 3, 1, 4])
s2 = OrderedSet([2, 4, 1, 9, 7])

print("s1=", s1)
print("s2=", s2)
print("s1 & s2 = ", s1 & s2)
print("s2 & s1 = ", s2 & s1)
print("s1 | s2 = ", s1 | s2)
print("s2 | s1 = ", s2 | s1)
print("s1 - s2 = ", s1 - s2)
print("s2 - s1 = ", s2 - s1)

s3 = OrderedSet([4, 1, 5])
print("s3=", s3)
s3.add(3)
print("s3=", s3)

l1 = [1, 2, 3, 4, 2, 3, 1]
print("l1=", l1)
l2 = list(OrderedSet(l1))
print("l2=", l2)
