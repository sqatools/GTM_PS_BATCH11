# Q1 : write a python function to check given number is prime or not return True or False value.


def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


result = prime(2)
print(result)


# for i in range(2, num): # i =2, 3, 4
#     print(i) # 2
#     if num%i == 0: # 13%4 == 0
#         # prime = False
#         break
#     else:
#         continue

def get_prime_number(num):

    prime = 1
    for i in range(2, num): # (2, 15)
        if num%i == 0:
            prime = False
            break
        else:
            continue

    return prime

print("_"*50)
print(get_prime_number(11)) # True
print("_"*50)
print(get_prime_number(15)) # False

