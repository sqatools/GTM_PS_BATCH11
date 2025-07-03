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

# Q1 . write a python function get max value list
# Q2.  write a python function get factorial of given number.
# Q3.  write a python function get sum of all the values in the list.

def get_max_value(list1):
    max_value = max(list1)
    print("max value :", max_value)

get_max_value([4, 6, 8, 34, 654, 23])

print("_"*50)
def get_factorial(num):
    fact =1
    for i in range(num, 0, -1):
        fact = fact*i # 1*5 = 5 | 5*4 = 20 | 20*3 = 60 | 60*2 = 120 | 120*1 = 120
        #print(i)
    print(f"Factorials of {num}:", fact)

# pass by value
get_factorial(7)

# pass by reference
x = 5
get_factorial(x)

for x in range(6, 10):
    get_factorial(x)

print("_"*50)
#################################
# Q3.  write a python function get sum of all the values in the list.

def get_sum_of_all_values(l1: list):
    sum = 0
    for val in l1:
        sum = sum + val

    print("sum of all values :", sum)

# pass by value
get_sum_of_all_values([5, 7, 3, 6, 23])
# sum of all values : 44

# pass by reference
list_a = [6, 8, 34, 56, 23]
get_sum_of_all_values(list_a)
# sum of all values : 127

#get_sum_of_all_values("Hello")

print("_"*40)
#############################################################
# **kwargs parameter
# kwargs parameter accept the values in key value pair
# kwargs value are store in dictionary format

def get_user_details(**abc):
    print(abc)
    for k, v in abc.items():
        print(k, ":", v)


get_user_details(name='Mohan', email='mohan@gmail.com', phone=4534543, address="Mumbai, Boriwali")
"""
{'name': 'Mohan', 'email': 'mohan@gmail.com', 'phone': 4534543, 'address': 'Mumbai, Boriwali'}
name : Mohan
email : mohan@gmail.com
phone : 4534543
address : Mumbai, Boriwali
"""


def login(**kwargs):
    db_username = 'user1'
    db_password = 'user@1234'
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successfully")
    else:
        print("Invalid Credentials")


print("_"*50)
login(username='user2', password='user@123') # Invalid Credentials
login(username='user1', password='user@1234') # Login Successfully

print("_"*50)
#############################################################
# Recursion function:  when a function call itself, then it is called recursion function

def greeting(msg):
    print(msg)
    greeting(msg)

#greeting("Good Morning")
# RecursionError: maximum recursion depth exceeded

def print_number(num):
    print(num, "Nidhi")
    if num == 20:
        return num
    print_number(num=num+1)

print_number(1)


print("_"*50)
####################################
# return value of function:  If we use return keyword in the function, then it will return value from function
# that we can store in variable and stop execution of the function immediately.

def get_sum_values(n1, n2, n3):
    return n1+n2+n3

output = get_sum_values(40, 50, 60)
print("Addition of values :", output)

print("multiplication :", output*2)
# multiplication : 300




def print_values(num):
    for i in range(num):
        if i == 5:
             return i
        print(i)

print("_"*50)
result = print_values(10)
print("result :", result)


print("_"*50)
######### return multiple value from function ##############
# if we return multiple values from function, then it will return in form of tuple
def math_operation(n1: int, n2: int) -> tuple:
    add = n1+n2
    multi = n1*n2
    divide = n1//n2
    return add, multi, divide


var = math_operation(40, 5)
print("output :", var)
# output : (45, 200, 8)

# a, b, c = (45, 200, 8)

a, b, c = math_operation(50, 6)
print("addition:", a) # addition: 56
print("multiplication :", b) # multiplication : 300
print("division :", c) # division : 8


# Q1 : write a python function to check given number is prime or not return True or False value.
# Q2 :  write a python function to get fabonacci serise till 10 values return as list
# Q3 : Write a python function to check given string in palindrome or not, return output as True or False
