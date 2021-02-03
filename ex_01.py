#!/usr/bin/env python3.8

# 01
# Create a program that
#     asks the user to enter their name and their age.
#     Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:
#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#         (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines.
#         (Hint: the string "\n" is the same as pressing the ENTER button)

from datetime import datetime

#Input Name
name = input("Enter your Name: ")

#Input Age
#Throw Exception
while True:
    try:
        age = int(input("Enter your Age: "))
        assert age >= 0
    #Int Convert Error
    except ValueError:
            print("\n\tSorry, Only Positive Number.")
    #Assert Error
    except AssertionError:
            print("\n\tSorry, Only Positive Number.")
    #No Error
    else:
        break

#Print Value
print ("\n\nName: \t", name,"\nAge: \t", age)


#Current Year
now = datetime.now().year

#Calc Age
if age <= 100:
    print("\nYou will get 100 years old in ", ((100-age)+now), "\n")
else:
    print("\nYou already got 100 years old\n")

#Input Message
msg = input("\nTalk a Message: ")

#Input Repeat
#Throw Exception
while True:
    try:
        repeat_times = int(input("Times to Repeat: "))
        assert repeat_times >= 0
    #Int Convert Error
    except ValueError:
        print("\n\tSorry, Only Positive Number.")
    #Assert Error
    except AssertionError:
        print("\n\tSorry, Only Positive Number.")
    #No Error
    else:
        break

#Jump Line
print()

#Repeat Message
for x in range(repeat_times):
    print("[ ", (x+1), " ]", "\t", msg)

#Jump Line
print()
