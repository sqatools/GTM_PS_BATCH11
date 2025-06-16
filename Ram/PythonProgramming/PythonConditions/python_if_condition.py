
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
    print("Condition is True:", x,y)
else:
    print("Failed")

x = 40
y = 15
z = 30
if x > y and x > z:

    print("Condition is True:", x,y,z)
else:
    print("Failed")

x = 40
y = 15
z = 30
if x > y and y > z or x > y :

    print("Condition is True:", x,y,z)
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
    print("True", x,y,z)
else:
    print("Failed")

x = 50
y = 30
z = 50

if x > y and y > z or x == y:
    print("Condition is True:")
elif z > y and z == x:
    print("True", x,y,z)
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

if a == 1:
    print("First Condition is pass", a)
    if b == 3:
        print("Second Condition is pass:", b)
        if c == 3:
            print("Third Condition is pass")
        else:
            print("Third condition is Failed:", c)
    else:
        print("Second Condition is Failed", b)
else:
    print("First Condition is Failed", a)
