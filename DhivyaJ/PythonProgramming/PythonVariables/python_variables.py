a = 20
# a : variable
# = : assignment operator
# 10 : data value
print(a)

print(id(a)) # 140715319904984

b = 20
print(b, id(b))
print(a, id(a))

# if multiple variable are holding same value, then their address is also same.

# Assign same value to multiple variable at a time.
p = q = r = 50
print("value of p :", p)
print("value of q :", q)
print("value of r :", r)

# multiline comment
"""
value of p : 50
value of q : 50
value of r : 50
"""


# Assign different values to different variables at a time.
x, y, z = 70, 80, 90
print("value of x:", x)
print("value of y:", y)
print("value of z:", z)

"""
value of x: 70
value of y: 80
value of z: 90
"""

print("value of x, y, z:", x, y, z)
# value of x, y, z: 70 80 90

#####################################################
# Rules to define variable names
# 1. There is no space variable name
# var 1 = 50 Invalid
var_1 = 60 # correct

# 2. There is no limit to define variable name
a = 40
abc = 70
hello_we_Are_learning_python = 100


# 3. Variable name can not start with number.
# 123var = 700 # invalid
var123 = 800 # valid
var_1_python_456 = 'Hello' # valid

# 4. Variable name can not contain special character except _
# temp_& = 800  # invalid
# output_%_value = 900 # invalid
var_123 = 600 # valid

# 5. Variable names are case-sensitive.

name = 'Rahul'
Name = 'Mohan'
NAME = 'John'
namE = 'pankaj'

print(name, Name, NAME, namE)
# Rahul Mohan John pankaj


var_p = -100
print("var_p :", var_p)
# var_p : -100
_var1 = 400
__var2 = 500


age = 50
age = 60
age = 70
age = 80
print(age, age, age, age)
# 80 80 80 80


"""
# Math operator
+ : plus
- : minus
* :  multiplication
/ : division with single /
// : division with double //
% : remainder operator
== : equal to operator
!= : not equal operator
** : power operator
"""

print("_"*50)
# addition of values
n1 = 50
n2 = 60
n3 = n1 + n2
print("addition :", n3) # addition : 110
print("addition :", n1+n2) # addition : 110


print("_"*50)
#### multiplication of values ####
a1 = 6
a2 = 5
a3 = ' Python'
print("multiplication :", a1*a2)
# multiplication : 30
print("multiply word :", a3*5)
# multiply word : Python Python Python Python Python


print("_"*50)
#### subtraction of values ####
p1 = 700
p2 = 300

print("subtraction of values :", p2-p1)
# subtraction of values : -400

print("_"*50)
#### division of values ####
d1 = 15
d2 = 4

# This will return output with pointer
print("division of single / :", d1/d2) # 3.75
# This will return only whole number
print("division of double // :", d1//d2) # 3


print("_"*50)
#### remainder of values ####
q1 = 20
q2 = 3
print("remainder output :", q1%q2)  #  2


print("_"*50)
#### power operator ####
x1 = 7
print("square of x1 :", x1**2) # square of x1 : 49
print("cube of x1 :", x1**3) # cube os x1 : 343
print("power 4 of x1 :", x1**4) # power 4 os x1 : 2401


print("_"*50)
#### equal operator ==, not eqaul != ####
t1 = 60
t2 = 70
t3 = 60
print(t1 == t2) # False
print(t1 == t3) # True
print(t3 != t2) # True

###################################
"""
# program to solve below equations
1. (a+b)^2 = a^2 + b^2 + 2ab
2. (a-b)^2 = a^2 +b^2 - 2ab
3. (a-b)(a+b) = a^2 -b^2
"""

print("_"*50)
# 1. (a+b)^2 = a^2 + b^2 + 2ab

a = 5
b = 6
lhs = (a+b)**2
print("lhs output :", lhs)

rhs = a**2 + b**2 + 2*a*b
print("rhs output :", rhs)

print(lhs == rhs) # True
