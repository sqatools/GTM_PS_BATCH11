# 1). Python Program to add two integer values.
x = 1
y = 2
print (x+y)

# Python Program to subtract two integer values.
num1 = 10
num2 = 20
print( "Difference between two numbers:",num2-num1)

# 3). Python program to multiply two numbers.

num3 = 2
num4 = 5
print("Product of two numbers:",num3*num4)

# 4). Python program to repeat a given string 5 times.
str1 = "SQATools"
n1=5
print("Result:",str1*5)

# 5). Python program to get the Average of given numbers.
# Formula: sum of all the number/ total number
# Input:
a = 40
b = 50
c = 30
# Output :
# Average = 40
print("Average of 3 numbers:",(a+b+c)/3)

# 6). Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order
# Formula : (n+1)/2
# n = Number of values
Input= [45, 60, 61, 66, 70, 77, 80]
Output:  66

i = len(Input)
median = int((i+1)/2)
print (i)
print (median)
print("Median of the given numbers:",Input[median-1])

values = [20,30,40,50,60,70]

values.sort()
print(values)

n = len(values)
print(n)

print('x =', n%2)

if n%2 ==1:
    Median_value = values[n//2]
else:
    Median_value = (values[n//2-1]+values[n//2]/2)

print(f"The median is :{int(Median_value)}")


# 7). Python program to print the square and cube of a given number.
z = 9
print("Square of z:",z**2)
print("cube of num1:",z**3)

# 8). Python program to interchange values between variables.

a = 10
b = 20
a,b = b,a
print("value of a:",a)
print("value of b:",b)

# 9). Python program to solve this Pythagorous theorem.

# Theorem : (a2 + b2 = c2)
#
# 10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab

a = 5
b = 6
Rs = ((a+b)**2)
print("Rs:",Rs)
Ls = ((a**2)+(b**2)+2*(a*b))
print("Ls:",Ls)
if Rs == Ls:
    print("The formula is valid")

# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab

a= 6
b =10
result = a**2+b**2-2*(a*b)

print("(a-b)^2 =",result)

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)

a = 15
b = 10
result = (a-b)*(a+b)

print("a^2-b^2 =", result)

# 13). Python program to solve the given math formula.
# # Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a = 9
b = 3
result = a**3+3*(a*b)*(a+b)+b**3

print("(a+b)^3 =",result)

# 14). Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a = 9
b = 3
result = a**3-(3*(a**2)*b) +(3*a*(b**2))-b**3

print("(a-b)^3 =",result)

# 15). Python program to calculate the area of the square.
# Formula : area = a*a

a = 4
area = (a*a)
print("Area of the square:",area)

# side = int(input("Enter the side of the square:"))
# print ("Area of the square:",side**2)

# 16). Python program to calculate the area of a circle.
# Formula = PI*r*r

# radius = int(input("Enter Radius of the circle: "))
radius = 13
area = 3.14*radius*radius
# area = 3.14*radius**2

print("Area of the circle: ",area)

# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a

side = 12
area = 6*side*side
# area = 6*side**2

print("Aread of the cube:", area)

# 18). Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r

# r = int(input("Enter \"Radius\" of the cylinder:"))
# h = int(input("Enter \"height\" of the cylinder:"))

r = 6
h = 7

area = 2*3.14*r*h + 2*3.14*r*r
print("Area of the cylinder:",int(area))
#
# 19). Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

# num1 = input("Enter the number to check Armstrong number:")
num1 = str(153)
b = 0
for i in num1:
    a= int(i)**3
    print (a)
    b = b+a
    print(b)
if b == int(num1):
    print("The given number is Armstrong number", num1)
else:
    print("The given number is not an Armstrong number", num1)

# 20). Python program to calculate simple interest.
# Formula = P+(P/r)*t
# P = Principle Amount
# r = Anual interest rate
# t = time

P = 10000
r = 10
t = 7
SI = P+(P/r)*t
print("Simple interest :", SI)
#
# 21). Python program to print the current date in the given format
# Output: 2023 Jan 05
# Note: Use the DateTime library

import datetime
date = datetime.datetime.now()
print(date.strftime("%Y %b %d"))
#
# 22). Python program to calculate days between 2 dates.
# Input date : (2023, 1, 5) (2023, 1, 22)
# Output: 17 days
from datetime import date
date_1 = date(2023, 1, 24)
date_2 =date(2023, 1, 27)
diff = (date_1 - date_2).days
print(diff)

# 23). Python program to get the factorial of the given number

# 24). Python program to reverse a given number.

int = 23
rev = str(int)
print("reversed number is ",rev[::-1])

# 25). Python program to get the Fibonacci series between 0 to 50.

num1 = 0
num2 = 1
count = 0

while count < 50:
    print(num1, end = " ")
    n = num1 + num2
    num1 = num2
    num2 = n
    count +=1
print ( )

n = 20
a = 0
b = 1


for i in range (1,n):
    print(a)
    i = b
    a,b = b, a + b

# 26). Python program to check given number is palindrome or not.


n = 7557
new_n = n
rev = 0

while new_n > 0:
    rem = new_n%10
    rev = rev*10+rem
    new_n = new_n//10
    print(rev, rem,new_n)

if n == rev:
    print("Given number is a palindrome number")
else:
    print("Given number is not a palindrome number")


# 27). Python program to calculate compound interest.
# formula =  p*((1+r/100)**n)
princi = 1000
roi = 5
nom = 18

CI = princi*((1+roi/100)**nom)
print(CI, "new princi",(princi+CI))

# 28). Python program to check the prime number.

n = 24
count = 0

for i in range (1,n+1):
     if n%i == 0:
        count += 1
        print(n, i, count)
if count > 2:
    print("The given numnber is not a prime number: ",n)
else:
    print("The given number is a prime number:",n)

# 29). Python program to check leap year.

year = 2025

if(year%400==0 or year%100 !=0) and year%4 ==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
# 29) Python program to check for the anagram.
word = "python"
combination = 0
characters = len(word)

while characters>0:
    combination += characters
    characters -= 1
    print(characters, combination)

print("Total combinations without repetaation: ",combination)
