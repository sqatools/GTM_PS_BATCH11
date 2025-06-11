# range class accept three parameters
# range(start value, end value, step value)
# default start value is zero and step value e.g. range(10), start_val=0, step_val=1
# output will include only start value and exclude the end value.

# output will include values from 1 to 9
for i in range(1, 10, 1):
    print(i)

"""
1
2
3
4
5
6
7
8
9

"""


print("_"*50)
# with default initial value (0) and default step value (1)
for j in range(5):
    print(j)

"""
0
1
2
3
4

"""

print("_"*50)
# print reverse numbers
for k in range(5, 0, -1):
    print(k)

"""
5
4
3
2
1
"""



print("_"*50)
# print  numbers step value 2
for k in range(1, 15, 2):
    print(k)

"""
1
3
5
7
9
11
13
"""

print("_"*50)
#####################################
# program to print the table of any given number
num1 = 7
for j in range(1, 11):
    print(j, "*", num1, "=", j*num1)

"""
1 * 7 = 7
2 * 7 = 14
3 * 7 = 21
4 * 7 = 28
5 * 7 = 35
6 * 7 = 42
7 * 7 = 49
8 * 7 = 56
9 * 7 = 63
10 * 7 = 70
"""

print("_"*50)
#######################################
# program to get all the number which are divisible by 3 and 5 between 1 to 50

for i in range(1, 50):
    if i%3 == 0 and i%5 ==0:
        print(i)
    else:
        pass


"""
15
30
45
"""

print("_"*50)
##########################
# continue and break statement in for loop
# continue statement :  whenever code match if continue condition, then it will not execute the remaining code and jump
# to the nest iteration of loop

for i in range(1, 11):
    if i in [4, 7, 9]:
        continue
    print(i)


print("_"*50)
# break statement :  whenever code match with break condition, then it will break the loop execution immediately.
for j in range(1, 11):
    if j == 5:
        break
    print(j)


print("_"*50)
######################################
# program to check given number is prime or not
num = 15
prime = True
for i in range(2, num): # i =2, 3, 4
    print(i) # 2
    if num%i == 0: # 13%4 == 0
        prime = False
        break
    else:
        continue

if prime:
    print("This is prime number :", num)
else:
    print("This is not a prime number :", num)


