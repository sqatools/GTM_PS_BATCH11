"""
Data types in Python.

1. Numbers:
   i) integer
   ii) Float
   iii) Complex number

2. Sequential:
   i) String
   ii) List
   iii) Tuple

3. Dictionary
4. Set
5. Boolean

"""

############################ Integer ###############################
### int ->  float #####
n1 = 56
f1 = float(n1)
print(f1, type(f1))
# 56.0 <class 'float'>

print("_"*50)
### int ->  string #####
n2 = 56734
s2 = str(n2)
print(s2, type(s2), s2[2])
# 56734 <class 'str'> 7


print("_"*50)
### int ->  list ##### # conversion is not possible
"""
n3 = 897
l3 = list(n3)
print(l3)
# TypeError: 'int' object is not iterable
"""
print("_"*50)
### int ->  tuple ##### # conversion is not possible
### int ->  dict ##### # conversion is not possible
### int ->  set ##### # conversion is not possible

print("_"*50)
### int ->  boolean #####
n5 = 0
b1 = bool(n5)
print(b1, type(b1)) # False <class 'bool'>

n6 = 88789
b2 = bool(n6)
print(b2, type(b2)) # True <class 'bool'>

############################################# Float ####################################

print("_"*50)
### float ->  int #####
f1 = 67.56
n1 = int(f1)
print(n1, type(n1))
# 67 <class 'int'>

print("_"*50)
### float ->  string #####
f2 = 67.56
s2 = str(f2)
print(s2, type(s2), s2[-2], s2[-3])
#67.56 <class 'str'> 5 .

print("_"*50)
### float ->  list ##### conversion is not possible
### float ->  tuple ##### conversion is not possible
### float ->  dict ##### conversion is not possible
### float ->  set ##### conversion is not possible

### float ->  boolean ##### conversion is not possible

f3 = 0.0
b1 = bool(f3)
print(b1, type(b1)) # False <class 'bool'>

f4 = -54.78
b2 = bool(f4)
print(b2, type(b2)) # True <class 'bool'>

######################################## String ############################
print("_"*50)
### string - int ####
# 1. if string contains letters then string to int conversion is not possible
"""
str1 = "Hello"
n1 = int(str1)
print(n1)
# ValueError: invalid literal for int() with base 10: 'Hello'
"""

#2. If string contains only numbers then conversion string to int is possible.
str2 = "54456546"
n2 = int(str2)
print(n2, type(n2), n2*2)
# 54456546 <class 'int'> 108913092


print("_"*50)
### string - float ####
# 1. if string contains letters then string to float conversion is not possible
# 2. If string contains only numbers with or without pointer then  string to float is possible.
s3 = "56.78"
f3 = float(s3)
print(f3, type(f3), f3*10)
# 56.78 <class 'float'> 567.8

print("_"*50)
### string - list ####
s4 = "Python Programing"
l4 = list(s4)
print(l4, type(l4))
# ['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g'] <class 'list'>


print("_"*50)
### string - tuple ####
s5 = "Python"
t5 = tuple(s5)
print(t5, type(t5))
# ('P', 'y', 't', 'h', 'o', 'n') <class 'tuple'>

print("_"*50)
### string - dictionary ####
# 1.  If string contains letter then string to dict conversion is not possible
"""
s6 = "Python"
d6 = dict(s6)
print(d6)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""
import json

details = '{"name": "Rahul", "age": 25, "mobile": 8908098}'
print(details, type(details))
# {"name": "Rahul", "age": 25, "mobile": 8908098} <class 'str'>

result = json.loads(details)
print(result, type(result))
# {'name': 'Rahul', 'age': 25, 'mobile': 8908098} <class 'dict'>
print(result['name']) # Rahul



print("_"*50)
### string - set ####
str7 = "Learning Python"
set7 = set(str7)
print(set7, type(set7))
# {'h', 'y', ' ', 't', 'a', 'o', 'e', 'L', 'P', 'g', 'i', 'r', 'n'} <class 'set'>


print("_"*50)
### string - boolean ####
s8 = ""
b1 = bool(s8)
print(b1, type(b1)) # False <class 'bool'>

s9 = "Hello"
b2 = bool(s9)
print(b2, type(b2))  # True <class 'bool'>



################################ List ########################
### list -> int #### conversion is not possible
### list -> falot #### conversion is not possible

print("_"*50)
### list -> string ####
l1 = [5, 7, 8]
s1 = str(l1)
print(s1, type(s1), s1[0], s1[-2], s1[4])
# [5, 7, 8] <class 'str'> [ 8 7

print("_"*50)
### list -> tuple ####
l2 = [5, 7, 8, 78, 4]
t2 = tuple(l2)
print(t2, type(t2))
# (5, 7, 8, 78, 4) <class 'tuple'>


print("_"*50)
### list -> dictionary ####
# list to dictionary direct conversion is not possible

l1 = ['a', 'b', 'c']
l2 = [44, 77, 22, 78]
result = dict(zip(l1, l2))
print("dict result :", result)
# {'a': 44, 'b': 77, 'c': 22}


print("_"*50)
### list -> set ####

list_a = ['a', 'b', 'c',  'a', 'b', 'd']
set_a = set(list_a)
print(set_a,  type(set_a))
# {'d', 'b', 'a', 'c'} <class 'set'>

print("_"*50)
### list -> boolean ####
l1 = []
b1 = bool(l1)
print(b1, type(b1)) # False <class 'bool'>

l2 = [4, 7, 8]
b2 = bool(l2)
print(b2, type(b2)) # True <class 'bool'>


################################ Tuple ################################
## tuple -> int ### conversion is not possible
## tuple -> float ### conversion is not possible

print("_"*50)
## tuple -> string ###
t1 = (5, 7, 2, 8)
s1 = str(t1)
print(s1, type(s1), s1[0], s1[7])
# (5, 7, 2, 8) <class 'str'> ( 2


print("_"*50)
## tuple -> list ###
t2 = (5, 7, 2, 8)
l2 = list(t2)
print(l2, type(l2))
# [5, 7, 2, 8] <class 'list'>


print("_"*50)
## tuple -> dictionary ### direct conversion is not possible
t3 = (5, 7, 2, 8)
t4 = ('P', 'Q', 'R', 'S')
result = dict(zip(t4, t3))
print(result, type(result))  # {'P': 5, 'Q': 7, 'R': 2, 'S': 8} <class 'dict'>


print("_"*50)
## tuple -> set ###
t3 = (5, 7, 2, 8, 5, 8, 7)
s3 = set(t3)
print(t3)
# (5, 7, 2, 8, 5, 8, 7)
print(s3, type(s3))
# {8, 2, 5, 7} <class 'set'>


print("_"*50)
## tuple -> boolean ###
t1 = tuple()
b1 = bool(t1)
print(b1, type(b1))  # False <class 'bool'>


t2 = (4, 6, 7)
b2 = bool(t2)
print(b2, type(b2)) # True <class 'bool'>


################################ dict ################################
print("_"*50)
## dict -> int ###onversion is not possible
## dict -> float ###onversion is not possible
## dict -> string ###onversion is not possible
dict1 = {'a': 123, 'b': 456}
str1 = str(dict1)
print(str1, type(str1), str1[0], str1[6])
# {'a': 123, 'b': 456} <class 'str'> { 1


print("_"*50)
#### dict ->  list ######
dict2 = {'a': 123, 'b': 456}
list2 = list(dict2)
print(list2, type(list2)) # ['a', 'b'] <class 'list'>


print("_"*50)
#### dict ->  tuple ######
dict3 = {'a': 123, 'b': 456}
tup3 = tuple(dict3)
print(tup3, type(tup3))  # ('a', 'b') <class 'tuple'>


print("_"*50)
#### dict ->  set ######
dict4 = {'a': 123, 'b': 456, 'c': 678}
set4 = set(dict4)
print(set4, type(set4))
# {'a', 'b', 'c'} <class 'set'>


print("_"*50)
#### dict ->  bool ######
d1 = {}
b1 = bool(d1)
print(b1, type(b1))  # False <class 'bool'>

d2 = {'A': 123}
b2 = bool(d2)
print(b2, type(b2))  # True <class 'bool'>


################################################### Set ##########################################
print("_"*50)
#### set ->  int ###### conversion is not possible
#### set ->  float ###### conversion is not possible
#### set ->  string ######
set1 = {6, 2, 7, 12}
str1 = str(set1)
print(str1, type(str1), str1[1])
# {2, 12, 6, 7} <class 'str'> 2


print("_"*50)
#### set ->  list ######
set2 = {6, 2, 7, 12}
list2 = list(set2)
print(list2, type(list2))
# [2, 12, 6, 7] <class 'list'>


print("_"*50)
#### set ->  tuple ######
set3 = {6, 2, 7, 12, 5, 77}
tup2 = tuple(set3)
print(tup2, type(tup2))
# (2, 5, 6, 7, 12, 77) <class 'tuple'>


print("_"*50)
#### set ->  dict ###### # conversion not possible


print("_"*50)
#### set ->  bool ######
set1 = set()
b1 = bool(set1)
print(b1, type(b1)) # False <class 'bool'>

set2 = {5, 7, 8}
b2 = bool(set2)
print(b2, type(b2))  # True <class 'bool'>



########################### Bool #########################


print("_"*50)
#### bool ->  int ######
b1 = True
n1 = int(b1)
print(n1, type(n1))  # 1 <class 'int'>


print("_"*50)
#### bool ->  float ######
b2 = False
f2 = float(b2)
print(f2) # 0.0


print("_"*50)
#### bool ->  string ######
b3 = True
s3 = str(b3)
print(s3, type(s3), s3[0])
# True <class 'str'> T


print("_"*50)
#### bool ->  list ###### conversion is not possible
#### bool ->  tuple ###### conversion is not possible
#### bool ->  dict ###### conversion is not possible
#### bool ->  set ###### conversion is not possible
