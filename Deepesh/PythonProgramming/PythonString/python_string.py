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
<<<<<<< HEAD
=======
->  start_index and last_index could be negative as well.
->  both +ve -ve or -ve +ve value can be included in the output.
>>>>>>> a082c4bbec2b3be11c133106bb237162eb5739fa

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
<<<<<<< HEAD
=======

print(strx[-15:-5]) #  a Best Co


print("_"*50)
##########################
"""
Rule2 : str[start_index: last_index: step_value]
-> output string will include start_index and exclude last_index value.
-> start_index and end_index could be +ve or -ve
-> default start_index value is zero (0) if step value is +ve.
-> default start_index value is -1 if step value is -ve
-> default last_index value is end of the string if step_value is +ve
-> default last_index value is start of the string if step_value is -ve

"""

stry = "We Are Learning Python"

print(stry[2: 10: 1]) # Are Lea
print(stry[1: 12: 2]) # eAeLan

# default start_index value is zero (0) if step_value is +ve.
print(stry[:15:1]) # We Are Learning

# default start_index value is -1 if step value is -ve
print(stry[:15:-1]) # nohtyP
print(stry[:-16:-1]) # nohtyP gninrae
print(stry[:10:-2]) # nhy nn
print(stry[:-20:-2])  # nhy nnaLeA


# default last_index value is end of the string if step_value is +ve
strz = "We Are Learning Python"
print(strz[2::1]) #  Are Learning Python

# default last_index value is start of the string if step_value is -ve
print(strz[-2::-1]) # ohtyP gninraeL erA eW


print(strz[::1]) # We Are Learning Python
print(strz[::-1]) # nohtyP gninraeL erA eW
#print(strz[-1:-len(str):-1])

w1 = strz[16:]
print(w1) # Python
w1p1 = w1[:3]
w1p2 = w1[:-4:-1]
print(f"{w1p1}{w1p2}") # Pytnoh

"""
Slicing Home Work
str1 = Virat is Great India Batsman
# repeat first and last character three times
op1 = VVVirat is Great India Batsmannn

# repeat first and last character 2 times of each word.
op2 = VViratt iiss GGreatt IIndiaa BBatsmann

# replace first and last character each word from given string
op3 = tiraV si treaG andiI natsmaB

# repeat each vowels 2 times in given string
op4 = Viiraat iis Greeaat IIndiiaa Baatsmaan

"""
>>>>>>> a082c4bbec2b3be11c133106bb237162eb5739fa
