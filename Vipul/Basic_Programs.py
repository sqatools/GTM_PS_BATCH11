# Python Program to add two integer values.
a = 10
b = 20
print(a+b)

print('*'*200)
# Python Program to subtract two integer values.
a = 10
b = 20
print(a-b)

print('*'*200)
# Python program to multiply two numbers.
a = 10
b = 20
print(a*b)

print('*'*200)
'''Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools” '''

str1 = "SQATools"
print(str1*5)

print('*'*200)
#Python program to get the Average of given numbers.
a = 40
b = 50
c = 30
avg = (a+b+c)/3
print("The average is :: ", avg)

print('*'*100)
'''
Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
'''
Input = [45, 60, 61, 66, 70, 77, 80]
n = len(Input)
median = (n+1)/2
print("the median is ::", median)

print('*'*100)
# Python program to print the square and cube of a given number.

num1 = 9
print("square is ::", num1*num1)
print("cube is ::", num1*num1*num1)

print('*'*100)
#Python program to interchange values between variables.
a = 10
b = 20
a, b = b, a
print(a,b)

print('*'*100)
#Python program to solve this Pythagoras theorem.
a = 3
b = 4
c = 5

print((a**2 + b**2) == c**2)

print('*'*100)
#Python program to solve the given math formula. (a + b)2 = a^2 + b^2 + 2ab
a = 10
b = 20
lhs = (a+b)**2
rhs = a**2 + b**2 + 2*a*b
print(lhs == rhs)

print('*'*100)
#Python program to solve the given math formula. (a – b)2 = a^2 + b^2 – 2ab
a = 10
b = 20
lhs = (a-b)**2
rhs = a**2 + b**2 - 2*a*b
print(lhs == rhs)

print('*'*100)
#Python program to solve the given math formula. (a + b)3 = a3 + 3ab(a+b) + b3
a = 10
b = 20
lhs = (a+b)**3
rhs = a**3 + b**3 + 3*a*b*(a+b)
print(lhs == rhs)

print('*'*100)
#Python program to solve the given math formula. (a – b)3 = a3 - 3ab(a-b) - b3
a = 10
b = 20
lhs = (a-b)**3
rhs = a**3 - b**3 - 3*a*b*(a-b)
print(lhs == rhs)

print('*'*100)
#Python program to calculate the area of the square. area = a*a
side = 10
print("area of a square is :: ", side**2)

print('*'*100)
#Python program to calculate the area of a circle. PI*r*r
r = 15
pi = 3.14
print("area of a circle is :: ", pi*r**r)

print('*'*100)
#Python program to calculate the area of a cube. 6*a*a
side = 5
print("area of a cube is :: ", 6*side**2)

print('*'*100)
#Python program to calculate the area of the cylinder. 2*PI*r*h + 2*PI*r*r
r = 5
h = 10
pi = 3.14
print("area of a circle is :: ", (2*pi*r*h) + (2*pi*r**2))

print('*'*100)
#Python program to check whether the given number is an Armstrong number or not. 153 = 1*1*1 + 5*5*5 + 3*3*3
n = 153
temp = n
l = len(str(n))
s = 0
while temp > 0:
    digit = temp%10
    s = s + digit**l
    temp = temp//10
if s == n:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")


print('*' * 100)
#Python program to calculate simple interest. P+(P/r)*t
p = 10000
r = 10
t =10
SI = (p*r*t)/100
print("SI is ::", SI)
print("total amount is ::", SI+p)