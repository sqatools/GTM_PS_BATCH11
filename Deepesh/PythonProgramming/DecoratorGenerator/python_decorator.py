"""
decorator is the external that decorate any specific any other without changing the existing functionality
"""

def decorate(func):
    def inner(*args):
        print("_"*50)
        func(*args)
        print("_"*50)
    return inner


@decorate
def greeting(msg):
    print(msg)

greeting("Hello, Good Morning")

def restrict(func):
    def inner(n1, n2):
        if n2-n1 > 10:
            n1 = n1
            n2 = n1+10
            func(n1, n2)

        else:
            func(n1, n2)
    return inner



@restrict
def get_square_value(start, end):
    for i in range(start, end+1):
        print(i, i**2)

get_square_value(20, 50)
