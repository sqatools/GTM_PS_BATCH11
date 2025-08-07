######## Syntax for If Else ###########
"""
if condition:
   code
else:
   code
"""
x = 20
y = 15
if x > y:
    print("Condition is True:", x, y)
else:
    print("Failed")

print("_" * 50)
# Program to check if a number is divisible by 3
n1 = 30
if n1 % 3 == 0:
    print("Number is divisible by 3", n1)  # Number is divisible by 3 30
else:
    print("Number is not divisible by 3", n1)

print("_" * 50)
# Program to check if given numbers are divisible or not
n1 = 30
if n1 % 3 == 0 and n1 % 5 == 0:
    print("Number is divisible by 3 and 5", n1)  # Number is divisible by 3 and 5 30
else:
    print("Number is not divisible by 3 and 5", n1)

print("_" * 50)
# Program to get all numbers divided by 3 between 1 to 30
for val in range(1, 31):
    if val % 3 == 0:
        print(val, end=" ")  # 3 6 9 12 15 18 21 24 27 30
    else:
        continue

print("_" * 50)
x = 40
y = 15
z = 30
if x > y and x > z:

    print("Condition is True:", x, y, z)
else:
    print("Failed")

x = 40
y = 15
z = 30
if x > y and y > z or x > y:

    print("Condition is True:", x, y, z)
else:
    print("Failed")

"""
Python if-elif-else condition

if cond1:
    code
elif cond2:
    code
elif cond3:
    code
else:
    code
"""

x = 50
y = 30
z = 50

if x > y and y > z or x == z:
    print("Condition is True:")
elif z > y and z == x:
    print("True", x, y, z)
else:
    print("Failed")

x = 50
y = 30
z = 50

if x > y and y > z or x == y:
    print("Condition is True:")
elif z > y and z == x:
    print("True", x, y, z)
else:
    print("Failed")

"""
# Nested if condition
if cond1:
  code
  if cond2:
     code
  else:
     code
else:
  code
"""

a, b, c = 1, 2, 3

if a == 1:
    print("First Condition is pass", a)
    if b == 2:
        print("Second Condition is pass:", b)
        if c == 3:
            print("Third Condition is pass")
        else:
            print("Third condition is Failed:", c)
    else:
        print("Second Condition is Failed", b)
else:
    print("First Condition is Failed", a)

a, b, c = 1, 2, 3

# nesterd if conditions: every if condition will have its own else condition
# if first condition is true then only it will go to the next condition
print("_" * 60)
a = "pass"
b = "pass"
c = "fail"
d = "pass"

if a == "pass":
    print("First Condition is Success")
    if b == "pass":
        print("Second Condition is success")
        if c == "pass":
            print("Third condition is success")
            if d == "pass":
                print("Fourth condition is success")
            else:
                print("Fourth condition is fail")
        else:
            print("Third condition is fail")
    else:
        print("Second Condition is fail")

else:
    print("First Condition is Fail")

print("_" * 50)
# Python program to print the square of the number if it is divided by 11.

num2 = 33
if num2 % 11 == 0:
    print("square of the number is:", num2 ** 2)  # 33*33 = 1089
else:
    print("Number is not divisible by 11", num2)

print("_" * 50)
# Python program to check given number is a prime number or not.
num = 43
count = 0
for i in range(2, num):
    if num % i == 0:
        count += 1
if count > 0:
    print("It is not a prime number")
else:
    print("It is a prime number")

print("_" * 50)
# Python program to check given number is odd or even.

num2 = 10
if num2 % 2 == 0:
    print("Given number is even number :", num2)  # Given number is even number : 10
else:
    print("Given number is odd number :", num2)

print("_" * 50)
# Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 45, 79]
num3 = 10
if num3 in fib:
    print("Given number is part of the Fibonacci series :", num3)
else:
    print("Given number is not in the part of the Fibonacci series :", num3)
# Given number is not in the part of the Fibonacci series : 10

print("_" * 50)
# Python program to check authentication with the given username and password.
username = "ram123"
pwd = "ram123"

if username == pwd:
    print("authentication is success :", username, "=", pwd)  # authentication is success : ram123 = ram123
else:
    print("authentication is fail :", username, pwd)

print("_" * 50)
# Python program to validate user_id in the list of user_ids.
user_ids = [1, 2, 3, 4, 8, 9, 11, 15, 18]
id = 10
if id in user_ids:
    print(id)
else:
    print("Not in list:", id)  # Not in list: 10

print("_" * 50)
# Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

num4 = 9
if num4 % 3 == 0:
    print("square of given num is:", num4 ** 2)  # square of given num is: 81
else:
    print("Num not divisible by 2", num4)

print("_" * 50)
# Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

num4 = 3
if num4 % 3 == 0:
    print("cube of given num is:", num4 ** 3)  # square of given num is: 27
else:
    print("Num not divisible by 3", num4)

print("_" * 50)
# Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible
age = 18
if age >= 18:
    print("Eligible :", age)  # Eligible : 18
else:
    print("Not Eligible:", age)

print("_" * 50)
# Python program to check whether any given number is a palindrome.
# Input: 121
val = 121
val1 = str(val)  # convert int into string, then apply indexing concept to reverse the order by using -ve indexing

if val == int(val1[-1::-1]):
    print("It is a Palindrome:", val)  # It is a Palindrome: 121
else:
    print("It is not a Palindrome:", val)

print("_" * 50)
# Python program to check if any given string is palindrome or not.
str1 = "markram"
if str1 == str1[::-1]:
    print("It is a Palindrome :", str1)  # It is not a Palindrome : markramm
else:
    print("It is not a Palindrome :", str1)

print("_" * 50)
# 21. Python program to check whether the given number is positive or negative and even or odd.
num5 = -20
if num5 > 0:
    if num5 % 2 == 0:
        print("Number is Positive and Even :", num5)  # Number is Positive and Even : 20
    else:
        print("Number is Positive and Odd :", num5)  # # Number is Positive and 0dd : 29
else:
    if num5 % 2 == 0:
        print("Number is negative and Even :", num5)  # Number is negative and Even : -20
    else:
        print("Number is Negative and Odd :", num5)  # Number is Negative and Odd : -19

print("_" * 50)
# 22). Python program to print the largest number from two numbers.
num6 = 25
num7 = 63
if num6 > num7:
    print(f"{num6} is largest number")
else:
    print(f"{num7} is Largest Number")

print("_" * 50)
# 23). Python program to check whether a given character is uppercase or not.
str2 = "a"
if str2.isupper():
    print("True")  # True
else:
    print("False")  # False

print("_"*50)
# 25). Python program to check whether the given number is an integer or not.
num8 = "123"
# num8 = 56
if type(num8) == int:
    print("True")  # True
else:
    print("False")  # False

print("_"*50)
# Python program to check whether the given number is float or not.
# num9 = 18.9
num9 = 18
if type(num9) == float:
    print("True")  # True
else:
    print("False")  # False

print("_"*50)
# 28). Python program to print all the numbers from 10-15 except 13
for i in range(10, 16):
    if i != 13:
        print(i)

"""
10
11
12
14
15
"""
print("_"*50)
"""
29). Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill
Input = 350
Output = 438.75
"""
val2 = 250
bill = 0
if val2 <= 50:
    bill = bill + val2*0.50
    print(bill)
elif 50 < val2 <= 100:
    bill = bill + val2*0.75
    print(bill)
elif 100 < val2 <= 250:
    bill = bill + val2*1.25
    print(bill)
elif val2 > 250:
    bill = bill + val2*1.50
    print(bill)

surcharge = bill * 0.17
print("Surcharge :", surcharge)
total_bill = bill + surcharge
print("Total Bill Amount :", total_bill)

print("_"*50)



