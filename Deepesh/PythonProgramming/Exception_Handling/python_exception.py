# Error : when user provide some unexpected keyword or some variable issue, then it is called error wihtout executing
#  error will be visible

# Exception :  When program throws any error during the runtime of the program then it is called exception.
# we handle the exception error msg with custom message from user.

"""
try:
    code
except Exception as e:
 print(e)
"""


# print("addition :", 50+'Hello')
# print("Good Morning")

def addition(num1, num2):
    try:
        print("Addition :", num1 + num2)
    except Exception as e:
        print(e)
        print("Can not add int with string")


# addition(40, 50)
# addition(40, "60")
"""
unsupported operand type(s) for +: 'int' and 'str'
Can not add int with string
"""


# print("Good Morning")


# Raise explicit exception
def try_exception_raise(num1, num2):
    try:
        print("Addition :", num1 + num2)
    except Exception as e:
        print("Can not add int with string")
        raise e


# try_exception_raise(50, 'Hello')
# print("Hello Nidhi, How are you?")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


print("_" * 50)


########### try-except-else condition ##############
# else block will only execute when there is not exception in the code

def try_except_else(num1, num2, num3):
    try:
        print("addition :", num1 + num2)
        print("subtraction :", num2 - num3)
        print("Division :", num1 // num3)

    except Exception as e:
        print(e)
        print("Please provide all inputs as integer")
    else:
        print("Code execution is successful")


# try_except_else(10, 20, 30)
"""
addition : 30
subtraction : -10
Division : 0
Code execution is successful

"""

# try_except_else(10, 20, 0)
"""
addition : 30
subtraction : 20
integer division or modulo by zero
Please all inputs as integer

"""


#########################try-except-else-finally ################
# finally block :  This block always executes the code, even there is exception or not exception in the code.

def try_except_else_finally(num1, num2, num3):
    try:
        print("addition :", num1 + num2)
        print("subtraction :", num2 - num3)
        print("Division :", num1 // num3)

    except Exception as e:
        print(e)
        print("Please provide all inputs as integer")
    else:
        print("Code execution is successful")

    finally:
        print(f'------print table of {num1}-------')
        for i in range(1, 11):
            print(i, "*", num1, "=", i * num1)


# try_except_else_finally(5, 7, 2)
"""
addition : 12
subtraction : 5
Division : 2
Code execution is successful
------print table of 5-------
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50


"""

#try_except_else_finally(6, 7, 0)
"""
addition : 13
subtraction : 7
integer division or modulo by zero
Please provide all inputs as integer
------print table of 6-------
1 * 6 = 6
2 * 6 = 12
3 * 6 = 18
4 * 6 = 24
5 * 6 = 30
6 * 6 = 36
7 * 6 = 42
8 * 6 = 48
9 * 6 = 54
10 * 6 = 60
"""


############################# Nested Exception ################

def try_except_nested_exception(num1, num2, num3):
    try:
        print("addition :", num1 + num2)
        try:
            print("subtraction :", num2 - num3)
            print("Division :", num1 // num3)
        except Exception as e1:
            print("---- Inner exception -----")
            print(e1)
    except Exception as e2:
        print("-----outer exception ------")
        print(e2)


# Get outer exception
#try_except_nested_exception(40, '10', 20)
"""
-----outer exception ------
unsupported operand type(s) for +: 'int' and 'str'
"""


# Get inner exception
# try_except_nested_exception(40, 20, 0)
"""
addition : 60
subtraction : 20
---- Inner exception -----
integer division or modulo by zero
"""


################## Different message for different exception ##########

def handle_multiple_exception(num1, num2, num3):
    try:
        print("addition :", num1 + num2)
        print("subtraction :", num2 - num3)
        print("Division :", num1 // num3)
        assert num1 == num3

    except TypeError:
        print("Please provide correct numbers inputs")
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except AssertionError:
        print("Both the values are not same")
    except Exception as e:
        print(e)
        raise


#handle_multiple_exception(40, 30, 20)


########################## create custom exception class ##################

class NidhiException(Exception):
    def __init__(self, *args, **kwargs): # real signature unknown
        print("This is my custom error msg")



for i in range(10):
    if i == 7:
        raise NidhiException

    print(i)