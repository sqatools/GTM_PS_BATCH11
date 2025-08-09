# Q1 : write a python function to check given number is prime or not return True or False value.
# Q2 :  write a python function to get fabonacci serise till 10 values return as list
# Q3 : Write a python function to check given string in palindrome or not, return output as True or False

# Q1 : write a python function to check given number is prime or not return True or False value.

def prime(num):
    if num <=1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
result = prime(7)
print(result)

# Q2 :  write a python function to get fabonacci serise till 10 values return as list

def fabonacci(num):
    a = 0
    b = 1
    for i in range(num):
        print(a)
        a = b
        b=+1

fabonacci(10)

# Q3 : Write a python function to check given string in palindrome or not, return output as True or False

def palindrom(string):
    rev = string[::-1]
    if string == rev:
        return True
    else:
        return False
print(palindrom("level"))