"""
Properties :
1. Tuple is immutable data type, we can not modify the values.
2. Tuple can contain any type of data.
   e.g. int, float, complex, string, list, tuple, dict, set, boolean, None
3. Tuple also follows positive and negative indexing.
4. We can use tuple where the data is going to be fixed.
  e.g. days in a week, months in year, any information that we don't want to update further
"""

tup1 = (3, 4.5, 'Hello', [1, 2, 3], (4, 7, 8), {'a': 123}, {5, 6, 7}, True)
print(tup1, type(tup1))
# (3, 4.5, 'Hello', [1, 2, 3], (4, 7, 8), {'a': 123}, {5, 6, 7}, True) <class 'tuple'>


# Apply loop on tuple without indexing
for val in tup1:
    print(val)
"""
3
4.5
Hello
[1, 2, 3]
(4, 7, 8)
{'a': 123}
{5, 6, 7}
True


"""

print("_"*50)
# Apply loop on tuple with indexing
for i in range(len(tup1)):
    print(i, tup1[i])

"""
0 3
1 4.5
2 Hello
3 [1, 2, 3]
4 (4, 7, 8)
5 {'a': 123}
6 {5, 6, 7}
7 True
"""

print("_"*50)
# get values with +ve and -ve indexing
tup3 = (3, 4.5, 'Hello', [1, 2, 3], (4, 7, 8), {'a': 123}, {5, 6, 7, 6}, True)
print(tup3[-4]) # (4, 7, 8)
print(tup3[-2]) # {5, 6, 7}

print("_"*50)
################### Slicing in Tuple ###################

# get values with +ve and -ve slicing
tup4 = (3, 4.5, 'Hello', [1, 2, 3], (4, 7, 8), {'a': 123}, {5, 6, 7, 6}, True)
print(tup4[3:6]) # ([1, 2, 3], (4, 7, 8), {'a': 123})
print(tup4[-5:-8:-1]) # ([1, 2, 3], 'Hello', 4.5)
print(tup4[-5::-1]) # ([1, 2, 3], 'Hello', 4.5, 3)
print(tup4[3::-1]) # ([1, 2, 3], 'Hello', 4.5, 3)
print(tup4[4:]) # ((4, 7, 8), {'a': 123}, {5, 6, 7}, True)
print(tup4[-1::-1]) # (True, {5, 6, 7}, {'a': 123}, (4, 7, 8), [1, 2, 3], 'Hello', 4.5, 3)
print(tup4[::-1]) # (True, {5, 6, 7}, {'a': 123}, (4, 7, 8), [1, 2, 3], 'Hello', 4.5, 3)

print("_"*50)
#################### tuple methods ##############
print(dir(tuple)) # 'count', 'index'
# count method: This method return number occurrences of any give value.
tup5 = (5, 7, 9, 3, 5, 8, 4, 5, 6)
print("count of 5 :", tup5.count(5))
# count of 5 : 3

print("get index of 8 :", tup5.index(8))
# get index of 8 : 5

print("_"*50)
##################################
# tuple value repetation
tup6 = (6, 7, 8)
result = tup6*3
print("result :", result) #  (6, 7, 8, 6, 7, 8, 6, 7, 8)



print("_"*50)
##################################
# sorting of tuple value
tup7 = (5, 7, 23, 67, 1, 3, 15)
result = tuple(sorted(tup7))
print("sorted result :", result)
# sorted result : (1, 3, 5, 7, 15, 23, 67)

# sort in descending order
result2 = tuple(sorted(tup7, reverse=True))
print("sorted result :", result2)
# sorted result : (67, 23, 15, 7, 5, 3, 1)

print("_"*50)
##################################
# reverse  values of tuple
tup7 = (5, 7, 23, 67, 1, 3, 15)
rev_output = tuple(reversed(tup7))
print("reverse output :", rev_output)
# reverse output : (15, 3, 1, 67, 23, 7, 5)


################# Get Max, Min, Sum of Tuple Values ####################
tup8 = (10, 40, 70, 233, 13, 45)
print("Max value :", max(tup8)) # Max value : 233
print("Min value :", min(tup8)) # Min value : 10
print("Sum of value :", sum(tup8)) # Sum of value : 411


print("_"*50)
########################### Tuple comprehension ####################
tup9 = (6, 8, 3, 6, 2, 7, 12)
# get square of all values
result1 = tuple(val**2 for val in tup9)
print(result1) # (36, 64, 9, 36, 4, 49, 144)


# get all the even values from given tuple
result2 = tuple(val for val in tup9 if val%2 ==0)
print("result2 :", result2) # (6, 8, 6, 2, 12)


# get output of each value with tag as even and odd
result3 = tuple((val, 'even') if val%2 == 0 else (val, 'odd') for val in tup9)
print("result3 :", result3)
# ((6, 'even'), (8, 'even'), (3, 'odd'), (6, 'even'), (2, 'even'), (7, 'odd'), (12, 'even'))


# Apply loop with tuple comprehension
tup_a = ('a', 'b', 'c')
tup_b = (10, 20, 30)
result4 = tuple(((x, y) for x in tup_a for y in tup_b))
print("result4 :", result4)
# (('a', 10), ('a', 20), ('a', 30), ('b', 10), ('b', 20), ('b', 30), ('c', 10), ('c', 20), ('c', 30))


###################################
# Home work:
# 1.  write a python program to max value from tuple.
# 2.  write a python program to remove duplicate values from tuple
# 3.  write a python program to get second max value from tuple.
