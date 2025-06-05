
"""
# program to solve below equations
1. (a+b)^2 = a^2 + b^2 + 2ab
2. (a-b)^2 = a^2 +b^2 - 2ab
3. (a-b)(a+b) = a^2 -b^2
"""

# 2. (a-b)^2 = a^2 +b^2 - 2ab
a = 10
b = 12
lhs = (a-b)**2
print("lhs output :", lhs)

rhs = a**2 + b**2 - 2*a*b
print("rhs output :", rhs)
print(lhs == rhs)  # true

print("_"*80)
# 3. (a-b)(a+b) = a^2 -b^2
a = 12
b = 15
lhs = (a-b)*(a+b)
print("lhs value", lhs)
rhs = a**2 - b**2
print("rhs value", rhs)
print(lhs == rhs)  # true

print("_"*80)
# 1. Program to add two integers
int1 = 45
int2 = 60
print("Addition :", int1+int2)  # 105

print("_"*80)
# 2. Program to subtract two integers
int1 = 45
int2 = 60
print("Subtract two values :", int2-int1)  # 15

print("_"*80)
# 3. Program to multiply two numbers
v1 = 12
v2 = 6
print("multiply two values :", v1*v2)  # 72

print("_"*80)
# 4. Python program to repeat a given string 5 times
a1 = " Python"
a2 = 4
print("Multiplication of a String:", a1*a2)  # Python Python Python Python

print("_"*80)
# 5. Program to get the Average of given numbers
a1, a2, a3, a4 = 30, 40, 50, 60
print("Avg of Numbers:", (a1+a2+a3+a4)/4)  # 45.0

print("_"*80)
# 7. Print the square and cube of a given number
x1 = 4
print("Print Square :", x1**2)  # 16
print("Print Cube :", x1**3)    # 64

print("_"*80)
# 8. Program to interchange values between variables
x = 40
y = 80
x, y = y, x
print("Value of x:", x)  # Value of x: 80
print("Value of y:", y)  # Value of y: 40

print("_"*80)
# 10. Python program to solve the given math formula
# Formula : a2 – b2 = (a-b)(a+b)
a = 8
b = 4
lhs = (a**2) - (b**2)
print("lhs :", lhs)  # 48
rhs = (a-b)*(a+b)
print("rhs:", rhs)   # 48
lhs == rhs           # True

a = 3
b = 2
result = (a-b)*(a+b)
print("(a^2-b^2): ", result)  # 5













