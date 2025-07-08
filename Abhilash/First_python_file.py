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


print("-"*50)

"""

* * *       # i = 0
    *   *   # i = 1
* * * * *   # i = 2
*   *       # i = 3
    * * *   # i = 4
    
"""

for i in range(5):
    for j in range (6):
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
    for j in range (6):
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


# Python program to find the **maximum** and **second maximum**
# values from a list **without using `max()` function**:



list_a = [4, 60, 8, 34, 56, 12, 13, 80, 100]

max_val = list_a[0]
second_max = list_a[0]


for num in list_a:
    if num > max_val:
        second_max = max_val
        max_val = num
    elif num > second_max and num != max_val:
        second_max = num

print("Maximum value:", max_val)
print("Second maximum value:", second_max)

print("-"*50)

## whether the given number is an Armstrong number

num = 100
temp = num
b = 0

while temp > 0:
    c =  temp % 10
    b = b + c**3
    temp = temp//10
if num == b:
    print("It is a Armstrong number")
else:
    print("It is not a Armstrong number")

print('_'*50)

################# list ##########

list_1 = [25, 17, [3, 5, 7], 88, 12, 'Python']

list_1.append(40)
print(list_1) # [25, 17, [3, 5, 7], 88, 12, 'Python', 40]

print(list_1[2]) # [3, 5, 7]

print(list_1[2][1]) # 5


print('_'*50)
############## Boolean ##########
v1 = 100
v2 = 100

print(v1 == v2)

print('_'*50)

########### int to float ######
'''
n1 = 507
l1 = list(n1)
print ("int to float  :" , l1)

print("_"* 50)
'''
list_a = [3,6,8,2,7,9,1,4]
output = []

for i in range(len(list_a)):
    for j in range (i+1, len(list_a)):
        if list_a[i] + list_a[j] == 10:
            output.append([list_a[i], list_a[j]])
print(output)

print ("_"*50)

###write a python program to calculate the bill amount.
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

total_bill = 0

for i in range (len(item_list)):
    total_bill += price_list[i] * purchase_list[i]
print("Total bill amount :",total_bill)

print("_"*50)
#############################################
'''list1 = [45, 67, 80, -3, 4 -54, -4, 23]
output = [45, 67, 80, 4, 23, -3,-4, -54]'''

list1 = [45,67,80,-3,4,-54,-4,23]

positive_val = []
negative_val = []

for num in list1:
    if num >= 0:
        print(num, positive_val, negative_val)

        positive_val.append(num)
    else:
        negative_val.append(num)


print("output:", positive_val + negative_val)

print('_'*50)

# write a python program to calculate the bill amount and update the inventory
item_list = ['Apple', 'Mango', 'Banana', 'lichi']
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

#up_inventory_list = [190, 145, 490, 280]
total_bill = 0

for i in range (len(item_list)):

    total_bill += price_list[i] * purchase_list[i]
    inventory_list[i] -= purchase_list[i]

print ("Updated Inventory:", inventory_list)
print("Total bill amount :",total_bill)

print("-"*40)
