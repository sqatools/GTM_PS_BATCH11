a = 10
# a - Variable
# = - assignment operator
# 10 - data value
print(a)
# NOTE: data is stored in certain memory location we can identify the memory location through below code.
print(id(a))

# if multiple variable are holding same value, then their address is also same.
b = 10
print(b, id(b))

print("-"*50) # types hyphen 50 times
# Assign same value to multiple variable at a time.
p = q = r = 30
print("Value of p:", p)
print("Value of q:", q)
print("Value of r:", r)
print("-"*50) # types hyphen 50 times

# # for single line comment
# multi line comment
"""
Value of p: 30
Value of q: 30
Value of r: 30
"""

# Assign Different values to different variable at a time
x, y, z = 30, 50, 70
print("Value of x, y ,z:", x, y, z)
print("-"*50) # types hyphen 50 times
####################################################################################################
# Rules to define variable names:
# 1. there should be no space in variable name
#       var 1 = 50 INVALID
#       var_1 = 50 VALID

# 2. There is no limit to define variable name
#       hello_we_are_learning_python = 100 VALID

# 3. Variable name cannot start with number
#       123var = 50 INVALID
#       var123 = 30 valid

# 4. Variable name cannot contain special character except _
#       temp_$@ = 40 INVALID

# 5. Variable names are case-sensitive
name = 'Rahul'
Name = 'Mohan'
NAME = 'Raju'
print(name, Name, NAME)

#      All the above variables are different

print("-"*50) # types hyphen 50 times
# Addition of values
n1 = 50
n2 = 60
n3 = n1 + n2
print("addition: ", n3)
print("addition: ", n1 + n2)

print("-"*50) # types hyphen 50 times
# Multiplication of Values
a1 = 8
a2 = 3
print("multiplication: ", a1*a2)
a3 = ' Python '
print("multiplication of string - ", a3*5)

print("-"*50) # types hyphen 50 times
# Subtraction of values
p1 = 500
p2 = 200
print('Subtraction:', p1-p2)

print("-"*50) # types hyphen 50 times
# Division of values
x1 = 100
x2 = 20
print('Division with single slash:', x1/x2) # returns 5.0
print('Division with double slash', x1//x2) # returns 5(only whole numbers)

print("-"*50) # types hyphen 50 times
# Modulus operator
y1 = 14
y2 = 3
print('Modulus operator:', y1%y2)

print("-"*50) # types hyphen 50 times
# Power operator
q1 = 3
print('Square of q1:', q1**2)
print('Cube of q1:', q1**3)
print('Power 4 of q1:', q1**4)

print("-"*50) # types hyphen 50 times
# Equal to and not equal to operator
s1 = 80
s2 = 60
s3 = 60
print(s1==s2)
print(s2==s3)
print(s1==s3)
print(s1!=s2)
