"""
if condition:
   code
else:
   code
"""

num1 = 50
num2 = 60
print(num1 == num2) # False

if num1 == num2:
    print("The values are same")
else:
    print("The values are not same")

# The values are not same


print("_"*50)
#################################
# check given number is even or odd
n1 = 25

if n1%2 == 0:
    print("This is even number :", n1)
else:
    print("This is odd number :", n1)

"""
AND Logic
cond1 and cond2
True and False : False
False and True : False
False and False :  False
True and True :  True

OR Logic
cond1 or cond2
True or False :  True
False or True :  True
True or True :  True
False or False :  False

Operators:
> : greater than
< : less than
>= :  greater than equal
<= : less than equal
!= : not equal
== :  equal
is : is operator
is not : is not operator
in : in operator
not in : not in operator
"""

print("_"*50)
####################################
# program to check given number is divisible by 3 and 5
n1 = 15
if n1%3 == 0 and n1%5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")


print("_"*50)
####################################
# program to check given numbers is divisible by 7 or 5
p1 = 49
p2 = 25
if p1%7 == 0 or p2%5 == 0:
    print("Number is divisible by 5 or 7 :", p1, p2)
else:
    print("Number is not divisible by 5 or 7", p1, p2)


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

print("_"*50)
####################################
# write a program to get greater value among three numbers
"""

a = 90
b = 80
c = 90

# code with and condition

if a > b and a  > c:
    print("A has greater value :", a)
elif b > a and b  > c:
    print("B has greater value :", b)
elif c > a and c > b:
    print("C has greater value :", c)
else:
    print("No one has greater value")
    
"""


############################################
# program to get output with and , or condition
a = 101
b = 103
c = 90
d = 104

# code with and condition

if a > b and a > c or a > d:
    print("A has greater value :", a)
elif b > a and b  > c or b > d:
    print("B has greater value :", b)
elif c > a and c > b or c > d:
    print("C has greater value :", c)
else:
    print("No one has greater value")

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

print("_"*50)
################################################
# write a python program to demostrade the interview process
round1 = "fail"
round2 = "pass"
round3 = "fail"

if round1 == "pass":
    print("congrats first round is cleared")
    if round2 == "pass":
        print("congrats second round is cleared")
        if round3 == "pass":
            print("congrats you are selected")
        else:
            print("Failed in last round")
    else:
        print("sorry failed in second round")

else:
    print("Sorry failed in first round")




