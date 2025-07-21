# Python function program that take a number as a parameter and checks whether the number is prime or not.
# Input : 7
# Output : True

#
# def prime(num):
#     if num<=1:
#         return false
#     for i in range(num):
#        if num % i == 0:
#             return false
#        return True
# num=10
# prime(num)
def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


result = prime(2)
print(result)
