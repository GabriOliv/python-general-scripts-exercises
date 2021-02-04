#!/usr/bin/env python3.8

# 03
# Take a list, say for example this one:
#       a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
#   Instead of printing the elements one by one,
#       make a new list that has all the elements less than 5
#       from this list in it and print out this new list.
#   Write this in one line of Python.
#   Ask the user for a number and return a list that contains
#       only elements from the original list
#       a that are smaller than that number given by the user.

#List
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("\nOriginal List:\n\t", a)

#List Size
list_size = len(a)

print("\nList of Less Than 5:")
#List Output
for i in range(list_size):
    #Less than 5
    if a[i] < 5:
        #Print Same Line
        print("\t [", a[i], "] ", end="")

#2 New Lines
print()

print("\nNew List:")
#Create New Empty List
b = []
#New List
for i in range(list_size):
    #Less than 5
    if a[i] < 5:
        b.append(a[i])

print("\t", b, "\n\n")

#Input
#Try Exception
while True:
    #Input
    try:
        barrier = int(input("Enter a Number: "))
        assert barrier >= 0
    #Error
    except ValueError:
        print("\n[!] Sorry, Only Non-Negative Numbers.")
    #No Error
    except AssertionError:
        print("\n[!] Sorry, Only Non-Negative Numbers.")
    else:
        break

#Create New Empty List
b = []
#New List
c = []
for i in range(list_size):
    #Less than 5
    if a[i] < barrier:
        c.append(a[i])

#\b (Backspace) 
print("\nList of Less Than", barrier,"\b: ")
print("\t", c, "\n\n")



