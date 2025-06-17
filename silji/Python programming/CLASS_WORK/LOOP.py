# Q1: code for following pattern
"""
* * * * *
* * * *
* * *
* *
*
"""



"""

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
"""

# a=5
# for i in range(5, 0, -1):
#     print('* ' * i)


# a=5
# for i in range(5,  -1):
#     for j in range(5, i-1):
#         print("*", end=" ")
#     print()


a = 5
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()