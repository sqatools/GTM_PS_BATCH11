##### 1.Add two integer values in Python ###
s1 = 20
s2 = 30

sum =  s1 + s2

print ( "The sum of integer value is :", sum)

print ("-"*50)

##### 2.subtract two integer values in Python ###
s1 = 20
s2 = 30

print ( "subtract of s1-s2  :", s1 - s2)

print ("-"*50)

##### 3.multiply two integer values in Python ###
s1 = 10
s2 = 5

print ( "Multiply of s1*s2  :", s1*s2)

print ("-"*50)

##### 4.repeat a given string 5 times in Python ###
str1 = 'SQATools'
print(str1*5)

print ("-"*50)

##### 5.Python program to get the Average of given numbers. ###
### Formula: sum of all the number/ total number ###
a = 40
b = 50
c = 30

s = ((a + b + c)/3)

print ("Average of given numbers :",s)

print ("-"*50)

'''
7.Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729
'''
num1 = 9

print(num1**2)
print(num1**3)

print ("-"*50)

### 8.Python program to interchange values between variables. ###

a = 10
b = 20

a , b = b , a

print("a:",a)
print("b:",b)

print ("-"*50)

###### 10.Python program to solve the given math Formula : (a + b)2 = a^2 + b^2 + 2ab ###

a = 1
b = 2

RHS = a**2 + b**2 + 2*a*b
print("(a + b)^2:",RHS)

print ("-"*50)

### Python program to solve the given math formula.Formula : (a – b)2 = a^2 + b^2 – 2ab ##
a = 1
b = 2

Result = a**2 + b**2 - 2*a*b
print("(a – b)2:",Result)

print ("-"*50)

# Q1: code for following pattern
"""
* * * * *
* * * *
* * *
* *
*
"""

n = 5
i = 1
while i <= n :
    j = n
    while j >=i:
        print ("*", end = " ")
        j -=1
    print()
    i +=1

print("-"*50)

################################
for i in range(1, 6):
    for j in range(6, i, -1):
        print("*", end=" ")
    print()

print("-"*50)

##Q2: list of all the prime number from1 to 100 ##
'''
for num in range(2,101):
    for i in range(2, num):
        if num % i ==0:
           break
    else:
         print(num, end=" ")
'''
###########################

print("-"*50)

"""
   * * *       # i = 0
       *   *   # i = 1
   * * * * *   # i = 2
   *   *       # i = 3
       * * *   # i = 4
"""

for i in range(5):
    for j in range (1,6):
        if i == 0 and j in (1,2,3):
            print ("*", end = " ")
        elif i == 1 and j in (3,5):
            print("*", end=" ")
        elif i == 2 and j in (1,2,3,4,5):
            print("*", end=" ")
        elif i == 3 and j in (1,3):
            print("*", end=" ")
        elif i == 4 and j in (3,4,5):
            print("*", end=" ")
        else:
            print ( " ", end = " ")
    print()
#####################
print("-"*50)

##################
'''
*   * * *    # i = 0
*   *        # i = 1
* * * * *    # i = 2
    *   *    # i = 3
* * *   *    # i = 4

'''
for i in range(5):
    for j in range (1,6):
        if i == 0 and j in (1,3,4,5):
            print ("*", end = " ")
        elif i == 1 and j in (1,3):
            print("*", end=" ")
        elif i == 2 and j in (1,2,3,4,5):
            print("*", end=" ")
        elif i == 3 and j in (3,5):
            print("*", end=" ")
        elif i == 4 and j in (1,2,3,5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("-"*50)


