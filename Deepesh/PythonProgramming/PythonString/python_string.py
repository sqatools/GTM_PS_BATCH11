str1 = "Hello we are Learning Python"
print(str1, type(str1))
# Hello we are Learning Python <class 'str'>

print("_"*50)
########## String Formatting #############
# Name = input("Please enter your name :")
# Age = int(input("Please enter your age :"))
# City = input("Please enter your city name :")
Name = "Rahul"
Age = 25
City = "Mumbai"

# My name is Rahul and age is 25, I live in Mumbai

# 1. String concatenation
result1 = "My name is "+Name+" and age is "+str(Age)+" I live in "+City
print(result1)
# My name is Rahul and age is 25 I live in Mumbai

# 2. Format Method
result2 = "My name is {} and age is {} I live in {}".format(Name, Age, City)
print(result2)
# My name is Mohit and age is 30 I live in Pune


# 2. F string formatting Method
result3 = f"My name is {Name} and age is {Age} I live in {City}"
print(result3)
# My name is Mohit and age is 25 I live in Pune

print("_"*50)
##########################################################
# Apply loop on string.

# 1.  Loop without indexing
str1 = "Programming"
for val in str1:
    print(val, end=",")
# P,r,o,g,r,a,m,m,i,n,g,


print()
print("_"*50)

# 1.  Loop with indexing
str2 = "Learning"
str_len = len(str2)
for i in range(str_len):
    print(i, str2[i])

"""
0 L
1 e
2 a
3 r
4 n
5 i
6 n
7 g
"""


print("_"*50)
######################## +ve and -ve indexing of string ###########
str_a  = "Progamming"
""" 
 0   1  2  3  4  5   6  7  8  9  # +ve
 P   r  o  g  a  m   m  i  n  g
-10 -9 -8 -7 -6 -5 -4  -3 -2  -1  # -ve
"""
print(str_a[4]) # a
print(str_a[-3]) # i

############################ Slicing in String ##############################
"""
Rule1 : str[start_index: last_index]
->  output string will include start_index and exclude the last index.
->  Output string will always from left to right, can not get string in reverse
->  If we dont define the start_index, then default first_index value is Zero (0)
->  If we dont define the last_index, then default last_index value is end of string

"""
strx = "India is a Best Country"
print(strx[0:5])  # India

# default start_index is zero
print(strx[:10]) # India is a

# default end_index is end of string
print(strx[-12:]) # Best Country

# start_index and last_index may has +ve and -ve value combination
print(strx[1:-1])  # ndia is a Best Countr
print(strx[-14:17]) # a Best C

print(strx[10:0]) # Empty list
