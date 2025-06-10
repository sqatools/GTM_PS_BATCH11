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
print("_"*40)
################ Integer ##########
"""
Properties:
1.  Integer is immutable data type. once it is define can not update.
2.  Integer can contain both positive and negative.
3.  Integer only contains whole number.
4.  There is not specific limit for integer data type.
"""

n1 = 50
print("n1 :", n1, type(n1))
# n1 : 50 <class 'int'>

# 100 will replace the 50
n1 = 100
print(n1, type(100))

n2 = 0 # 0 <class 'int'>
n3 = -100 # -100 <class 'int'>
n4 = 54345435435345435435435808098908098349054
# 54345435435345435435435808098908098349054 <class 'int'>

print(n2, type(n2))
print(n3, type(n3))
print(n4, type(n4))

print("_"*50)
################ float #############
"""
Properties:
1.  float is immutable data type. once it is define can not update.
2.  Float can contain both positive and negative value.
3.  float only contains pointer value.
4.  There is not specific limit for float data type.
"""

f1 = 0.0
f2 = 0.25
f3 = -55.67
f4 = 675656546546.4654645
print(f1, type(f1)) # 0.0 <class 'float'>
print(f2, type(f2)) # 0.25 <class 'float'>
print(f3, type(f3)) # -55.67 <class 'float'>
print(f4, type(f4)) # 675656546546.4655 <class 'float'>


print("_"*50)
################# Complex Number #############
"""
Properties of complex number
->  complex number is immutable data type
->  complex number is combination of real and imaginary value
    x+yj
    x = read number
    y = imaginary number

-> complex can contains positive and negative values.
"""

p1 = 10 + 40j
p2 = 0-4j
p3 = -100+50j
print(p1, type(p1))
# (10+40j) <class 'complex'>

print(p2, type(p2))
# -4j <class 'complex'>

print(p3, type(p3))
# (-100+50j) <class 'complex'>

p4 = 40 + 50j
print("real value :", p4.real) # 40.0
print("imaginary value :", p4.imag) # 50.0


print("_"*50)
###################### string ###################
"""
properties:
1. string is immutable data type
2. Any value in single/double/triple quote will consider as string
3. String can contains any type of value in quotes, e.g. 
   int, float, string, num, special characters.
4. String follows positive and negative indexing.
"""

s1 = ""
s2 = 'A'
s3 = "We are Learning Python Programming"
s4 = """
very good morning
Python is easy learn
RCB Won IPL Title first time
"""

# we can write string single triple quotes as multi lines string paragraph
s5 = '''
we are
learning 
Python
Programming
123
&*^*&%^
'''

print("_"*50)
print(s1, type(s1)) # <class 'str'>
print("_"*50)
print(s2, type(s2)) # A <class 'str'>
print("_"*50)
print(s3, type(s3)) # We are Learning Python Programming <class 'str'>
print("_"*50)
print(s4, type(s4))
"""
very good morning
Python is easy learn
RCB Won IPL Title first time
 <class 'str'>
"""
print("_"*50)
print(s5, type(s5))
"""
we are
learning 
Python
Programming
123
&*^*&%^
 <class 'str'>
"""

str_a = "Python"

"""
 0  1  2  3  4  5  +ve indexing
 P  y  t  h  o  n
-6 -5 -4 -3 -2 -1  -ve indexing

"""
print("get t with +ve indexing :", str_a[2])
# get t with +ve indexing : t

print("get h with +ve indexing :", str_a[-3])
# get h with +ve indexing : h

print(str_a[4])  # o

########################### List ####################
"""
Properties :
1. List is mutable data type, we can modify the values.
2. List can contains any type of data.
   e.g. int, float, complex, string, list, tuple, dict, set, boolean, None
3. List also follows positive and negative indexing.
4. Usage of list, we generally list data type where is changing rapidly and we can update
   whenever required e.g. student registration, employee management.
"""

list1 = []
list2 = [2, 3.4, 'Hello', [3, 4, 5], (6, 8, 9),
         {'a': 123}, {4, 5, 7}, True, None]
print(list1, type(list1)) # [] <class 'list'>

print(list2, type(list2))
# [2, 3.4, 'Hello', [3, 4, 5], (6, 8, 9), {'a': 123}, {4, 5, 7}, True, None] <class 'list'>


list3 = [5, 7, 8]
list3.append(100)
print(list3, type(list3)) # [5, 7, 8, 100] <class 'list'>

# list follows +ve and -ve indexing
#        0  1  2   3   4   5
list4 = [5, 7, 12, 88, 45, 67]
#       -6  -5 -4 -3   -2  -1

print(list4[4]) # 45
print(list4[-5]) # 7


list5 = [25, 17, [3, 5, 7], 88, 12, 'Python']


print(list5[2]) # [3, 5, 7]
print(list5[2][1]) # 5
print(list5[-1]) # Python
print(list5[-1][-4]) # h

print("-"*40)
############################# Tuple #######################
"""
Properties :
1. Tuple is immutable data type, we can not modify the values.
2. Tuple can contains any type of data.
   e.g. int, float, complex, string, list, tuple, dict, set, boolean, None
3. Tuple also follows positive and negative indexing.
4. We can use tuple where the data is going to be fixed.
  e.g. days in a week, months in year, any information that we dont want to update further
"""


t1 = tuple()  #
t2 = (2, 3.4, 5+60j, 'Hello', [4, 5, 6], (2, 5, 8), {'a': 234}, {5, 7, 89}, True)
print(t1, type(t1)) # () <class 'tuple'>
print(t2, type(t2))
# (2, 3.4, (5+60j), 'Hello', [4, 5, 6], (2, 5, 8), {'a': 234}, {89, 5, 7}, True) <class 'tuple'>


# tuple also follows positive and negative indexing
#     0  1   2         3           4
t3 = (4, 6, (4, 7, 1), [5, 8, 2], 'Hello')
#    -5  -4  -3        -2          -1

print(t3[1]) # 6
print(t3[2]) # (4, 7, 1)
print(t3[2][1]) # 7


########################### Dictionary data type ################
"""
Properties :
1. Dictionary is mutable data type, we can modify the values.
2. Dict store data in key value pair with curly braces e.g. {'k': 'value'}
3. Dict only contains unique keys, duplicate keys are not allowed.
  -> if dictionary has duplicate keys then it will consider only latest key data
4. Only immutable data type can be key in dictionary
   e.g. int, float, string, tuple, boolean
   Can not  contains list, dict, set and key in dict.
   
5. All types of data can be value in dictionary.
  e.g. int, float, string, list, tuple, dict, set, boolean.
6. Dictionary does not follow indexing. 
"""

dict1 = {'a': 123,
         34 : 56.78,
         23.33 : (5, 7, 8),
         (4, 5, 7) : [5, 88, 12],
         True : {'a': 123, 'b': 345},
          #[1, 2, 3 ]: 'Python'} # TypeError: unhashable type: 'list'
         }

print(dict1, type(dict1))
# {'a': 123, 34: 56.78, 23.33: (5, 7, 8), (4, 5, 7): [5, 88, 12], True: {'a': 123, 'b': 345}} <class 'dict'>

# get value from dict
print(dict1['a']) # 123
print(dict1[23.33]) #  (5, 7, 8)
print(dict1[23.33][-1]) # 8
print(dict1.keys())  # dict_keys(['a', 34, 23.33, (4, 5, 7), True])
print(dict1.values())  #dict_values([123, 56.78, (5, 7, 8), [5, 88, 12], {'a': 123, 'b': 345}])
print(dict1[True]) # {'a': 123, 'b': 345}
print(dict1[True]['b']) # 345



print("_"*50)
# if duplicate keys are there then it will consider last value
dict2 = {'a' : 567, 'b': 333, 'c': 777, 'a': 800, 'e': 'Python'}
print(dict2)
# {'a': 800, 'b': 333, 'c': 777}

str1 = "We are 'learning' python"
print(str1[11]) # r


print("_"*50)
########################### set data type ################
"""
Properties:
-> Set is mutable data type.
-> Set contains unique values, duplicate data is not allowed
-> Set store values in random order.
-> Set only contains immutable data type as member. 
   e.g. int, float, string, tuple, boolean
"""

set1 = {4, 5, 5.6, 'Hello', (5, 7, 8), True, None, 4, 5}
print(set1, type(set1))
# {None, True, 'Hello', 4, 5.6, 5, (5, 7, 8)} <class 'set'>

set1.add(200)
print("set1 :", set1)
# {None, True, 4, 5, 5.6, 'Hello', 200, (5, 7, 8)}

# List, set, dict can not be a member of set data type
#set2 = {4, 5, 5.6, 'Hello', (5, 7, 8), True, None, 4, 5, [5, 11, 4]}
#print(set2)
# TypeError: unhashable type: 'list'

print("_"*50)
########################### Boolean ################
"""
Properties:
->  Boolean is immutable data type
->  Boolean has two values only True or False
->  Boolean values are output of any condition that we are matching.
"""

v1 = True
v2 = False
print(v1, type(v1))  # True <class 'bool'>
print(v2, type(v2))  # False <class 'bool'>

n1 = 500
n2 = 700
n3 = 500
print(n1 == n2) # False
print(n1 == n3) # True
