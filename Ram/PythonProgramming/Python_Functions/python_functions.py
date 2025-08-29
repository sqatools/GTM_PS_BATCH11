def function1():
    print("Learning Python Function")


function1()
# calling of function
# function1()
# function1()
# function1()
# function1()

# Q1 : write a python function to check given number is prime or not return True or False value.
# Q2 :  write a python function to get fabonacci serise till 10 values return as list
# Q3 : Write a python function to check given string in palindrome or not, return output as True or False

# Q1 : write a python function to check given number is prime or not return True or False value.
print("_" * 50)


def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
        else:
            continue
    return prime


print("_" * 50)
print(is_prime(13))  # True
print("_" * 50)
print(is_prime(12))  # False

print("_" * 50)


# Q2 :  write a python function to get fabonacci series till 10 values return as list

def fab_series(num=10):
    """
    0,1,2,3,5,8,13,21,34,55
    :param num:
    :return:
    """
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(num):
        a, b = b, a + b
        print(b, end=" ")


fab_series()
# 0 1 1 2 3 5 8 13 21 34 55 89

print("_" * 50)


# Q3 : Write a python function to check given string in palindrome or not, return output as True or False
def check_palindrome(str1):
    if str1 == str1[::-1]:
        return True
    else:
        return False


print(check_palindrome("python"))  # False
print(check_palindrome("markram"))  # True

print("_" * 50)


# Python function to get sum of all the values in list
def sum_list(list):
    a = 0
    for val in list:
        a += val
    print("Sum of list: ", a)


sum_list([3, 4, 6, 9, 8])  # 30

# Python function to get max and min values from list
print("_" * 50)


def max_list(num=[12, 5, 9, 8, 15, 40, 6]):
    max_1 = max(num)
    print(max_1)  # 40
    min_1 = min(num)
    print(min_1)  # 5


max_list()

print("_" * 50)


# Pytho function to get factorial numbers
def get_factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i  # 1*5 = 5 | 5*4 = 20 | 20*3 = 60 | 60*2 = 120 | 120*1 = 120
        print(i)
    print(f"Factorials of {num}:", fact)


# pass by value
get_factorial(5)

############## *args Parameters ############
print("_" * 50)


def get_values(*args):
    print("args :", args)  # (2, 'Python', (1, 2, 3), [3, 4, 6], {'a': 234})
    for val in args:
        print(val)


get_values(2, 'Python', (1, 2, 3), [3, 4, 6], {'a': 234})
"""
2
Python
(1, 2, 3)
[3, 4, 6]
{'a': 234}
"""

print("_" * 50)


def get_values(*abc):
    print("args :", abc)  # (2, 'Python', (1, 2, 3), [3, 4, 6], {'a': 234})
    for val in abc:
        if isinstance(val, str):
            print(val * 2)
        else:
            print(val)


get_values(2, 'Python', (1, 2, 3), [3, 4, 6], {'a': 234})
"""
2
PythonPython
(1, 2, 3)
[3, 4, 6]
{'a': 234}
"""

####################### **kwargs ##############
print("_" * 50)


def get_details(**kwargs):
    print(kwargs)  # {'name': 'Ram', 'email': 'ram@gmail.com', 'age': 34}
    for k, v in kwargs.items():
        print(k, ":", v)


get_details(name='Ram', email='ram@gmail.com', age=34)
"""
name : Ram
email : ram@gmail.com
age : 34
"""
print("_" * 50)


def print_number(num):
    print(num, "Ram")
    print_number(num= num+1)

print_number(1)
