#!/usr/bin/env python3.8

# 07
# Let’s say I give you a list saved in a variable:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#   Write one line of Python that takes this list
#   a and makes a new list that has only the even
#   elements of this list in it.


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(a)

b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])

print(b)

c = []
for i in a:
    if i % 2 == 0:
        c.append(i)

print(c)

d = []
for i in a:
    d.append(i) if i % 2 == 0 else ""

print(d)

e = []
#Single Line
for i in a: e.append(i) if i % 2 == 0 else ""

print(e)

