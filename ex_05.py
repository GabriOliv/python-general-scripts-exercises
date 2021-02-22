#!/usr/bin/env python3.8

# 05
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that
#   contains only the elements that are common between the lists
#   (without duplicates).
#   Make sure your program works on two lists of different sizes.

# Extras:
#   Randomly generate two lists to test this
#   Write this in one line of Python

import random

while True:
    try:
        size_list_01 = int(input("Enter the First Size: "))
        assert size_list_01 > 0
    except ValueError:
        print("\n[!] Sorry, Only Positive Numbers")
    except AssertionError:
        print("\n[!] Sorry, Only Positive Numbers")
    else:
        break

while True:
    try:
        size_list_02 = int(input("Enter the Second Size: "))
        assert size_list_02 > 0
    except ValueError:
        print("\n[!] Sorry, Only Positive Numbers")
    except AssertionError:
        print("\n[!] Sorry, Only Positive Numbers")
    else:
        break

#Empty List
a = []

#Row 01
a.append([])
for i in range(size_list_01):
    #append Random Int 1-100
    a[len(a)-1].append(random.randint(1,100))

#Row 02
a.append([])
for i in range(size_list_02):
    #append Random Int 1-100
    a[len(a)-1].append(random.randint(1,100))

#Sort Lists
for i in range( len(a) ):
    a[i].sort()

#Last Row
a.append([])

#run row 01
for i in range(size_list_01):
    flag = 0
    #run row 02
    for j in range(size_list_02):
        if a[0][i] == a[1][j]:
            flag = 1
    #run row 03
    for j in range( len( a[2] ) ):
        if a[0][i] == a[2][j]:
            flag = 0
    #append Copied Number
    if flag == 1:
        a[2].append(a[0][i])

#Show Final Lists
for i in range( len(a) ):
    print("\n", a[i])

print()
