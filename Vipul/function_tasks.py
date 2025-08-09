# Q1 : write a python function to check given number is prime or not return True or False value.
# Q2 :  write a python function to get fabonacci serise till 10 values return as list
# Q3 : Write a python function to check given string in palindrome or not, return output as True or False


# Q1 : write a python function to check given number is prime or not return True or False value.

def prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

print(prime(16))

print("*"*100)

# Q2 :  write a python function to get fabonacci serise till 10 values return as list

def fibonacci(num):
    n1 = 0
    n2 = 1
    sum = 0
    print(n1)
    print(n2)
    for i in range(2, num):
        sum = n1 + n2
        print(sum)
        n1 = n2
        n2 = sum

print(fibonacci(10))

print("*"*100)

# Q3 : Write a python function to check given string in palindrome or not, return output as True or False
def palin(s):
    if s == s[::-1]:
        return True
    return False

print(palin("mom"))