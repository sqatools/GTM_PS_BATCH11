
# Q1: code for following pattern
# a = 5
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Q2: list of all the prime number from1 to 100

# print("Prime numbers from 1 to 100:")
#
# for num in range(2, 101):  # numbers from 2 to 100
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print(num, end=" ")

# num = 15
# prime = True
# for i in range(2, num): # i =2, 3, 4
#     print(i) # 2
#     if num%i == 0: # 13%4 == 0
#         prime = False
#         break
#     else:
#         continue
#
# if prime:
#     print("This is prime number :", num)
# else:
#     print("This is not a prime number :", num)