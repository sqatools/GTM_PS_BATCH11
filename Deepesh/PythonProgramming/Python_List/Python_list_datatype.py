"""
Properties :
1. List is mutable data type, we can modify the values.
2. List can contain any type of data.
   e.g. int, float, complex, string, list, tuple, dict, set, boolean, None
3. List also follows positive and negative indexing.
4. Usage of list, we generally list data type where is changing rapidly and we can update
   whenever required e.g. student registration, employee management.
"""
list1 = [1, 2.3, 'Python', [4, 6, 7], (1, 5, 7), {'a': 123}, {5, 7, 9, 7}, True, False]
print(list1, type(list1))
# [1, 2.3, 'Python', [4, 6, 7], (1, 5, 7), {'a': 123}, {9, 5, 7}, True, False] <class 'list'>

#        0  1  2  3  4
list2 = [4, 6, 8, 9, 1]
#       -5 -4 -3 -2  -1

print(list2[1]) # 6
print(list2[-2]) # 9

print("_"*50)
list3 = [1, 2.3, 'Python', [4, 6, 7], (1, 5, 7), {'a': 123, 'b': 567}, {5, 7, 9, 7}, True, False]
print(list3[4]) # (1, 5, 7)
print(list3[4][1]) # 5
print(list3[-4]) # {'a': 123, 'b': 567}
print(list3[-4]['a']) # 123
print(list3[2][2]) # t

print("_"*50)
#################################### Slicing in list ###################
list4 = [1, 2.3, 'Python', [4, 6, 7], (1, 5, 7), {'a': 123, 'b': 567}, {5, 7, 9, 7}, True, False]
print(list4[6:10]) # [{9, 5, 7}, True, False]
print(list4[6:]) # [{9, 5, 7}, True, False]
# print(list4[10])  # IndexError: list index out of range
print(list4[2:5]) # ['Python', [4, 6, 7], (1, 5, 7)]
print(list4[-7: -3]) # ['Python', [4, 6, 7], (1, 5, 7), {'a': 123, 'b': 567}]
print(list4[-3:-8:-1])  # [{9, 5, 7}, {'a': 123, 'b': 567}, (1, 5, 7), [4, 6, 7], 'Python']
print(list4[-6:-3: -1]) # []
print(list4[-6::-1]) # [[4, 6, 7], 'Python', 2.3, 1]
print(list4[-7::-1]) # ['Python', 2.3, 1]
print(list4[2::-1]) # ['Python', 2.3, 1]
print(list4[::-1])
# [False, True, {9, 5, 7}, {'a': 123, 'b': 567}, (1, 5, 7), [4, 6, 7], 'Python', 2.3, 1]



print("_"*50)
################### Apply loop in list data ###################
list5 = [5, 7, 89, 23, 15, 6]

# Apply loop without index
for val in list5:
    print(val)

"""
5
7
89
23
15
6
"""

print("_"*50)
# Apply loop with index
for i in range(len(list5)):
    print(i, ":", list5[i])

"""
0 : 5
1 : 7
2 : 89
3 : 23
4 : 15
5 : 6
"""

print("_"*50)
list6 = [5, 7, 89, 23, 15, 6]
print(list6[1:-1]) # [7, 89, 23, 15]

for val in list6[1:-1]:
    print(val, end= " ")
# 7 89 23 15

print()
print("_"*50)
for i in range(1, len(list6)-1, 1):
    print(i, list6[i])
"""
1 7
2 89
3 23
4 15
"""

print("_"*50)
################################### List Methods ###########################
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("_"*50)
############### Append method ########
# append method() : This method add one value to the list at the end of list.
list7 = [5, 7, 8, 23, 24]
list7.append(100)
list7.append('Python')
list7.append([65, 7, 8, {'a': 123}, (3, 5, 6)])
print("list7 :", list7)
# list7 : [5, 7, 8, 23, 45, 6, 7, 100, 'Python', [65, 7, 8]]
list7.append({'a': 345, 'b': 789})

print("list7 :", list7)
# list7 : [5, 7, 8, 23, 45, 6, 7, 100, 'Python', [65, 7, 8], {'a': 345, 'b': 789}]


print("_"*50)
############### extend method ########
# extend method() : Extend method add any iterable data type to list at the end
list8 = [5, 7, 8, 23, 45]
# add list with extend method
list8.extend([15, 17, 12])
print("list8 :", list8) # list8 : [5, 7, 8, 23, 45, 15, 17, 12]

# add list with extend method
list8.extend(('A', 'B'))
print("list8 :", list8)
# list8 : [5, 7, 8, 23, 45, 15, 17, 12, 'A', 'B']

# add list with extend method
list8.extend(('A', 'B'))
print("list8 :", list8)
# [5, 7, 8, 23, 45, 15, 17, 12, 'A', 'B', 'A', 'B']

# add string with extend method
list8.extend('Hello')
print("list8 :", list8)
# [5, 7, 8, 23, 45, 15, 17, 12, 'A', 'B', 'A', 'B', 'H', 'e', 'l', 'l', 'o']

# add dict with extend method
list8.extend({'a': 456, 'b': 789})
print("list8 :", list8)
# [5, 7, 8, 23, 45, 15, 17, 12, 'A', 'B', 'A', 'B', 'H', 'e', 'l', 'l', 'o', 'a', 'b']

# add set with extend method
list8.extend({1111, 555, 'P', 'Q', 1111})
print("list8 :", list8)
# list8 : [5, 7, 8, 23, 45, 15, 17, 12, 'A', 'B', 'A', 'B', 'H', 'e', 'l', 'l', 'o', 'a', 'b', 'P', 555, 'Q', 1111]


print("_"*50)
############### insert method ########
