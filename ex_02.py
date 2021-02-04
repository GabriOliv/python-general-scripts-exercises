#!/usr/bin/env python3.8

# 02
# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user.
#   Hint: how does an even / odd number react differently when divided by 2?

# Extras:
#   If the number is a multiple of 4, print out a different message.
#   Ask the user for two numbers:
#       one number to check (call it num)
#       and one number to divide by (check).
#   If check divides evenly into num, tell that to the user.
#   If not, print a different appropriate message.

#Input
#Try Exception
while True:
    #Input
    try:
        nmb_01 = int(input("Enter a Number: "))
    #Error
    except ValueError:
        print("\n\t[!] Sorry, Only Number.")

    #No Error
    else:
        break

if nmb_01 % 2 == 0 :
    print("\n\tYour Number is EVEN")
elif nmb_01 % 2 == 1 :
    print("\n\tYour Number is ODD")

if nmb_01 % 4 == 0 :
    print("\n\t... Your Number is a Multiple of 4 too")

print("\n\n")

#Input
#Try Exception
while True:
    #Input
    try:
        nmb_02 = int(input("Enter a Numerator: "))
        nmb_03 = int(input("Enter a Denominator: "))
    #Error of Value
    except ValueError:
        print("\n\t[!] Sorry, Only Numbers.")
    #No Error
    else:
        break

if nmb_02 % nmb_03 == 0:
    print("\n\t", nmb_02, " is a Multiple of ",nmb_03, "\n")
else:
    print("\n\t", nmb_02, " is NOT a Multiple of ",nmb_03, "\n")

