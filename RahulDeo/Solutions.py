# Question 1
import datetime
from audioop import avg

a = 30
b = 40
print(a+b)

# Question 2
print("_"*50)

a = 99
b = 19
print(a-b)

# Question 3
print("_"*50)

a = 15
b = 6
print(a*b)

# Question 4
print("_"*50)

str1 = "SQATools"
print(str1 *5)

# Question 5
print("_"*50)

a=40
b=50
c=30
print("Average of three no: ",(a+b+c)/3)

"""
# Question 6
print("_"*50)

value = [45,60,61,66,70,77,80]
n = len(value)

if n % 2 ==1:
    median_value = value[n//2]
else:
    median_value = (value[n//2-1]+ value[n//2])/2
    print("The median is: {median_value}")
    
    """

# Question 7
print("_"*50)

a = 9
print("The square is:", a**2)
print("The cube is:", a**3)

# Question 8
print("_"*50)

a = 10
b = 25
a,b = b,a

print("value of a:", a)
print("value of b:", b)

"""
# Question 9
print("_"*50)

def is_pythagorean (a, b, c):
    return a**2 + b**2 == c**2

"""

# Question 10
print("_"*50)

#(a + b)2 = a^2 + b^2 + 2ab

a=6
b=5

lhs = ((a+b)**2)
print("lhs output :", lhs)

rhs = (a**2 + b**2 + 2*a*b)
print("rhs output :", rhs)

print(lhs == rhs)

# Question 11
print("_"*50)

#(a – b)2 = a^2 + b^2 – 2ab

a=10
b=5

lhs = ((a-b)**2)
print("lhs output :", lhs)

rhs = (a**2 + b**2 - 2*a*b)
print("rhs output :", rhs)

print(lhs == rhs)

# Question 12
print("_"*50)

#a2 – b2 = (a-b)(a+b)

a=20
b=10

lhs = (a**2 - b**2)
print("lhs output :", lhs)

rhs = ((a-b) * (a+b))
print("rhs output :", rhs)

print(lhs == rhs)

# Question 13
print("_"*50)

#(a + b)3 = a3 + 3ab(a+b) + b3

a=10
b=12

lhs = ((a+b)**3)
print("lhs output :", lhs)

rhs = (a**3 + 3*a*b*(a+b) + b**3)
print("rhs output :", rhs)

print(lhs == rhs)

# Question 14
print("_"*50)

#(a – b)3 = a3 – 3a2b + 3ab2 – b3

a=10
b=5

lhs = ((a-b)**3)
print("lhs output :", lhs)

rhs = (a**3 - 3*a**2*b + 3*a*b**2 - b**3)
print("rhs output :", rhs)

print(lhs == rhs)

# Question 15
print("_"*50)

#area = a*a

a = 16
print("Area of square is:", (a*a))

# Question 16
print("_"*50)

Pi = 3.14
r = 10
print("Area of circle is:", (Pi*r*r))

# Question 17
print("_"*50)

a=12
print("Area of cube is: ", (6*a*a))

# Question 18
print("_"*50)

Pi=3.14
r=5
h=4
print("Area of cylinder is: ", (2*Pi*r*h + 2*Pi*r*r))

# Question 19
print("_"*50)

#Armstrong number
lhs = 153
print("lhs output :", lhs)

rhs = (1*1*1 + 5*5*5 + 3*3*3)
print("rhs output :", rhs)

print(lhs == rhs)

# Question 20
print("_"*50)

P=1000
r=10
t=5

print ("simple interest: ", (P+(P/r)*t))

# Question 20
print("_"*50)

import datetime
date = datetime.datetime.now()
print(date)