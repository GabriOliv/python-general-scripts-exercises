#!/usr/bin/env python3.8

# 10
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that
#   contains only the elements that are common between the lists
#   (without duplicates).
#   Make sure your program works on two lists of different sizes.
#       Write this in one line of Python using at least one list comprehension.

# Extras:
#   Randomly generate two lists to test this

import random

c = []

while True:
    try:
        c.append(int(input("Enter the First Size: ")))
        assert c[0] > 0
    except ValueError: print("\n[!] Sorry, Only Positive Numbers")
    except AssertionError: print("\n[!] Sorry, Only Positive Numbers")
    else: break


while True:
    try:
        c.append(int(input("Enter the Second Size: ")))
        assert c[1] > 0
    except ValueError: print("\n[!] Sorry, Only Positive Numbers")
    except AssertionError: print("\n[!] Sorry, Only Positive Numbers")
    else: break



# Empty List
a = [[],[]]

# Fill List
for i in range(2):
    for j in range(c[i]): a[i].append(random.randint(0,99))

# Sort Lists
for i in range(len(a)): a[i].sort()

# Final List
b = []
for i in a[0]:
    if (i in a[0]) and (i in a[1]) and (i not in b):
        b.append(i)

# Print
for i in range( len(a) ): print("\n", a[i])
print("\n", b, "\n\n")
