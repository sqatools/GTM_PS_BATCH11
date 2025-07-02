# Python Function.
var1 = 100

def function1():
    print("Learning Python Function")

# calling of function
# function1()
# function1()
# function1()
# function1()


def function2():
    for i in range(1, 11):
        print(i)


# function with parameter
def addition(n1, n2):
    print("addition of numbers :", n1+n2)

# 1. Pass by value :  when we call the function and provide values in place of parameter.
#addition(50, 60)
# addition of numbers : 110

# 2. Pass by reference : In pass by reference we can pass reference of variable to the function instead of values.
x = 500
y = 800
# addition(x, y)
# addition of numbers : 1300


print("_"*50)
##################################
# function with default parameter value.
"""
->  If we don't defined value for parameter of function, then it will consider default value assigned
->  If we assign new value to default parameter of function, then it will override default value.
->  Default parameter always comes after non-default parameters as per sequence.

"""

def math_operations(n1, n2=40, n3=50):
    print("n1 :", n1, "n2 :", n2, "n3 :", n3)
    # print("add :", n1+n2)
    # print("multiply :", n2*n3)
    # print("subtract :", n3-n1)
    print("Addition  :", n1+n2, "\nmultiplication :", n2*n3,"\nsubtraction :", n3-n1)

# n1 will consider value 2, remain parameter will consider default value n2=40 and n3=50
#math_operations(2)

# override default param values, n1 =2, n2=4, n3=6
#math_operations(2, 4, 6)

# can not provide more than required parameters
# math_operations(40, 60, 70, 80)
# TypeError: math_operations() takes from 1 to 3 positional arguments but 4 were given

# can not provide less than required parameters
# math_operations()
# math_operations() missing 1 required positional argument: 'n1'

# provide param value with their name
#math_operations(n1=20, n3=10)
"""
n1 : 20 n2 : 40 n3 : 10
add : 60
multiply : 400
subtract : -10
"""


# we can change the sequence of param calling with their names
math_operations(n3=10, n2=15, n1=30)
"""
n1 : 30 n2 : 15 n3 : 10
add : 45
multiply : 150
subtract : -20
"""

print("_"*50)
#################
# *args : Parameter
# this parameter accepts n number of value and consider in form of tuple

def get_values(*args):
    print("args :", args)
    for val in args:
        if isinstance(val, str) or isinstance(val, list):
            print(val*2)
        else:
            print(val)


get_values(3, 'Hello', [4, 6, 8], (2, 4, 6), {'a': 123})


# tup = (5, 7, 8)
# for val in tup:
#     print(val)
"""
args : (3, 'Hello', [4, 6, 8], (2, 4, 6), {'a': 123})
3
HelloHello
[4, 6, 8, 4, 6, 8]
(2, 4, 6)
{'a': 123}
"""

#Q1 . write a python function get max value list
#Q2.  write a python function get factorial of given number.
#Q3.  write a python function get sum of all the values in the list.
