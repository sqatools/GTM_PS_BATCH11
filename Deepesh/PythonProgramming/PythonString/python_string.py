str1 = "Hello we are Learning Python"
print(str1, type(str1))
# Hello we are Learning Python <class 'str'>

print("_" * 50)
########## String Formatting #############
# Name = input("Please enter your name :")
# Age = int(input("Please enter your age :"))
# City = input("Please enter your city name :")
Name = "Rahul"
Age = 25
City = "Mumbai"

# My name is Rahul and age is 25, I live in Mumbai

# 1. String concatenation
result1 = "My name is " + Name + " and age is " + str(Age) + " I live in " + City
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

print("_" * 50)
##########################################################
# Apply loop on string.

# 1.  Loop without indexing
str1 = "Programming"
for val in str1:
    print(val, end=",")
# P,r,o,g,r,a,m,m,i,n,g,


print()
print("_" * 50)

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

print("_" * 50)
######################## +ve and -ve indexing of string ###########
str_a = "Progamming"
""" 
 0   1  2  3  4  5   6  7  8  9  # +ve
 P   r  o  g  a  m   m  i  n  g
-10 -9 -8 -7 -6 -5 -4  -3 -2  -1  # -ve
"""
print(str_a[4])  # a
print(str_a[-3])  # i

############################ Slicing in String ##############################
"""
Rule1 : str[start_index: last_index]
->  output string will include start_index and exclude the last index.
->  Output string will always from left to right, can not get string in reverse
->  If we dont define the start_index, then default first_index value is Zero (0)
->  If we dont define the last_index, then default last_index value is end of string
->  start_index and last_index could be negative as well.
->  both +ve -ve or -ve +ve value can be included in the output.

"""
strx = "India is a Best Country"
print(strx[0:5])  # India

# default start_index is zero
print(strx[:10])  # India is a

# default end_index is end of string
print(strx[-12:])  # Best Country

# start_index and last_index may has +ve and -ve value combination
print(strx[1:-1])  # ndia is a Best Countr
print(strx[-14:17])  # a Best C

print(strx[10:0])  # Empty list

print(strx[-15:-5])  # a Best Co

print("_" * 50)
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

print(stry[2: 10: 1])  # Are Lea
print(stry[1: 12: 2])  # eAeLan

# default start_index value is zero (0) if step_value is +ve.
print(stry[:15:1])  # We Are Learning

# default start_index value is -1 if step value is -ve
print(stry[:15:-1])  # nohtyP
print(stry[:-16:-1])  # nohtyP gninrae
print(stry[:10:-2])  # nhy nn
print(stry[:-20:-2])  # nhy nnaLeA

# default last_index value is end of the string if step_value is +ve
strz = "We Are Learning Python"
print(strz[2::1])  # Are Learning Python

# default last_index value is start of the string if step_value is -ve
print(strz[-2::-1])  # ohtyP gninraeL erA eW

print(strz[::1])  # We Are Learning Python
print(strz[::-1])  # nohtyP gninraeL erA eW
# print(strz[-1:-len(str):-1])

w1 = strz[16:]
print(w1)  # Python
w1p1 = w1[:3]
w1p2 = w1[:-4:-1]
print(f"{w1p1}{w1p2}")  # Pytnoh

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

print("_" * 50)
############################ String Methods ##############################
print(dir(str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 
'zfill'
"""

print("_" * 50)
############################
# upper() and lower() : This method convert str1 into upper case and lower cases.
str1 = "We Are Learning Python"
print("Upper Case :", str1.upper())
# WE ARE LEARNING PYTHON
print("Lower Case :", str1.lower())
# we are learning python

print("_" * 50)
############################
# isupper() and islower() :  These method check the given string is in upper or in lower case, it will return boolean output.
str2 = "PYTHON PORGRAMMING"
str3 = "Good Morning"
str4 = "good evening"

print("isupper for str2:", str2.isupper())  # True
print("isupper for str3:", str3.isupper())  # False

print("islower for str4:", str4.islower())  # True
print("islower for str3:", str3.islower())  # False

print("_" * 50)
############################
# swapcase method : This method convert lower case char to upper case and upper case characters to lower case.
str5 = "India Is BesT Country"
print(str5.swapcase())
# iNDIA iS bESt cOUNTRY


print("_" * 50)
############################
# capitalize method : This method change only first letter of string into upper and remaining into lower case
str6 = "india Is BesT Country"
print(str6.capitalize())  # India is best country

print("_" * 50)
############################
# title() method : This method convert first letter of each word into capital case
str7 = "india IS BesT CoUnTry"
print(str7.title())
# India Is Best Country

print("_" * 50)
############################
# istitle() method : This method check the given string follow the rules of title case method.
str8 = "india IS BesT CoUnTry"
str9 = "Python Programming"
print("str8 istitle():", str8.istitle())  # False
print("str9 istitle():", str9.istitle())  # True

print("_" * 50)
############################
# count() method : count method return the number of occurrences of char/substring in given string.
str10 = "Learning Python is Fun"
print("count of n  :", str10.count('n'))  # count of n  : 4

print("_" * 50)
# write a python to print the count of each character without repeatation.
str11 = "Learning Python is Fun"
temp = ""  # Learni
for char in str11:  # Learni
    if char not in temp:  #
        print(char, ":", str11.count(char))
        temp = temp + char
    else:
        continue

print("_" * 50)
# write a python program to check the given 2 string are anagram or not
str_a = "Hello"
str_b = "elHloe"

anagram = True
if len(str_a) != len(str_b):
    anagram = False
for char in str_a:
    if str_b.count(char) == str_a.count(char):
        continue
    else:
        anagram = False

if anagram:
    print("These are anagram strings :", str_a, str_b)
else:
    print("These are not anagram strings :", str_a, str_b)

print("_" * 50)
#################### second solution ######################
str_p = "Python"
str_q = "nyhtoPn"
# sorted function :  This function sort the string in alphabetical order and return as list of characters.
v1 = sorted(str_p)
v2 = sorted(str_q)
print(v1, v2)
if v1 == v2:
    print("This is anagram")
else:
    print("This is not anagram")

print("_"*50)
########################################################################
# Q3 :  write a python program to get most simuntaneounly repeated character

str_x = "HHllo WWWWWWWe areeee LLLLLLLLLearning Python"

max_rep_char = ''
max_rep_count = 0
char_count = 1

for i in range(len(str_x)-1):
    # check current char and next char is same
    if str_x[i] == str_x[i+1]: # HHllo WWWW
        char_count += 1 # 2, 2, 2, 3, 4, 5
        if char_count > max_rep_count: # 2 > 0 | 2 > 2 | 3> 2 | 4 > 4 | 5 > 4 | 7> 6
            max_rep_count = char_count # 2, 3, 4, 5, 7
            max_rep_char = str_x[i] # H, W, W
        else:
            continue
    else:
        char_count = 1

"""
Max repeated char : L
Max repeated count : 9
"""

print("Max repeated char :", max_rep_char)
print("Max repeated count :", max_rep_count)


print("_"*50)
########################################################################
# Q3 :  write a python program to get count of each character from given without using count method.

str_w = "Programming"
# output = {'P': 1, 'r': 2, 'o':1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
result = {} # empty dictionary
#
for char in str_w: # P
    print(result)
    if char not in result:
        result[char] = 1
    else:
        result[char] += 1

print("output :", result)
# {'P': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

