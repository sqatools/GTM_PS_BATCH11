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
# insert() method :  This method help to insert data at specific index position.

list9 = [5, 15, 17, 12, 'A', 'B']
list9.insert(2, 100)
print("list9:", list9) # [5, 15, 100, 17, 12, 'A', 'B']

list9.insert(-1, 500)
print("list9:", list9)
# [5, 15, 100, 17, 12, 'A', 500, 'B']

print("_"*50)
############### list concatenation ########
list9 = [5, 15, 17, 12, 'A', 'B']
list10 = [10, 20, 30]

result = list9 + list10
print("result :", result)
# [5, 15, 17, 12, 'A', 'B', 10, 20, 30]


print("_"*50)
############### list repeatation ########
# when we multiply any number with the list, then it will repeat the list values that number of times.
list11 = [5, 'A', 'B']
result = list11*3
print("result :", result)
#result : [5, 'A', 'B', 5, 'A', 'B', 5, 'A', 'B']


print("_"*50)
############### Remove method ########
# remove method : This method will remove any specific value from list, if value is reapted multiple times
#                 then it will remove only first occurrence of given value.

list12 = [5, 15, 17, 12, 5, 'A', 'B', 5]
list12.remove(5)
print("list12 :", list12)
# list12 : [15, 17, 12, 5, 'A', 'B', 5]

list13 = [5, 15, 17, 12, 5, 'A', 5, 'B', 5]

for _ in range(4):
    list13.remove(5)

print("list13 :", list13)
# [15, 17, 12, 'A', 'B']

print("_"*50)
############### pop method ########
# pop method : This method will remove any specific value from list with the help of index position.
#              default index position is -1,  pop method return removed value.

list14 = [5, 15, 17, 12, 5, 'A', 'B', 5, 12, 5, 13]

# remove value default index position -1
v1 = list14.pop()
print("removed value  :", v1)
# removed value  : 13
print("list14 :", list14)
#list14 : [5, 15, 17, 12, 5, 'A', 'B', 5, 12, 5]



# remove value from specific index position
v2 = list14.pop(4)
print("removed value  :", v2)
# removed value  : 5
print("list14 :", list14)
# list14 : [5, 15, 17, 12, 'A', 'B', 5, 12, 5]


print("_"*50)
############### clear method ########
# clear method : clear method remove all the data from list remain as empty list

list15 = ['A', 'B', 5, 12, 5, 13]
list15.clear()
print("cleared value :", list15)
# cleared value : []


print("_"*50)
############### del keyword #########
# del keyword : del keyword remove entire variable from memory.
list16 = ['A', 'B', 5, 12, 5, 13, 100, 500]
del list16
# print("list16 :", list16)
# NameError: name 'list16' is not defined


# remove specific number data from list with del keyword
list17 = ['A', 'B', 'C', 5, 12, 34,  5, 13, 100, 500]
del list17[3:7]  # remove : 5, 12, 34,  5
print("list17 :", list17) #  ['A', 'B', 'C', 13, 100, 500]


# ['A', 'B', 'C', 13, 100, 500] :  this is updated list
del list17[:3]  # remove : 'A', 'B', 'C'
print("list17 :", list17) # [13, 100, 500]



print("_"*50)
############### replace values in the list with slicing/indexing #########
list18 = ['A', 'B', 'P', 'Q',  5, 12, 5, 13, 100, 500]

# mention index position to remove value
list18[2:4] = ['X', 'Y']
print("list18 :", list18) # ['A', 'B', 'X', 'Y', 5, 12, 5, 13, 100, 500]


#  ['A', 'B', 'X', 'Y', 5, 12, 5, 13, 100, 500] : updated list
list18[1], list18[5], list18[-2] = 'Python', 'Programming', 'Language'
print("list18 :", list18)
# list18 : ['A', 'Python', 'X', 'Y', 5, 'Programming', 5, 13, 'Language', 500]



print("_"*50)
############### count method #########
# count method:  This method return no of occurrences of any specific value in the list.
list18 = ['A', 'B', ['P', 'Q'],  5, 12, 5, 13, 100, 500, 5, 100, ['P', 'Q'], 13, 13, 13]
print("count of 5 :", list18.count(5))
# count of 5 : 3

print(list18.count(['P', 'Q'])) # 2

for val in list18:
    print(val, ":", list18.count(val))

print("_"*50)
for val in [5, 100, 13]:
    print(val, ":", list18.count(val))

"""
5 : 3
100 : 2
13 : 4
"""

print("_"*50)
############### index method #########
# index method:  This method return index position of any particular value
#                ->  if value is repeated multiple time, then it will return index of first occurrence
list19 = ['A', 'B', ['P', 'Q'],  5, 12, 5, 13, 100, 500, 5, ['P', 'Q']]

var1 = list19.index(['P', 'Q'])
print("var1 :", var1) # var1 : 2

var2 = list19[2].index('Q')
print("var2:", var2) # var2: 1


print("_"*50)
############### sort method #########
# sort method() :  This method sort the list in place and modify original list.
#                  it can sort list value in ascending and descending order

# sort in ascending order
list20 = [5, 7, 1, 23, 5, 78]
list20.sort()
print("list20 :", list20)  # [1, 5, 5, 7, 23, 78]


# sort in descending order
list21 = [5, 7, 1, 23, 5, 78]
list21.sort(reverse=True)
print("list21 :", list21)  # [78, 23, 7, 5, 5, 1]


print("_"*50)
############### reverse method #########
# reverse method() : This method will reverse list value and modify the original list

list22 = [5, 7, 1, 23, 5, 78]
list22.reverse()
print("list22 :", list22)  # [78, 5, 23, 1, 7, 5]


print("_"*50)
############### reversed function #########
# reversed function:  This function take list as input and return the reverse list value

list23 = [100, 500, 5, 7, 1, 23, 5, 78]
result = list(reversed(list23))
print("reversed result :", result)
# [78, 5, 23, 1, 7, 5, 500, 100]


str1 = "Python"
result2 = list(reversed(str1))
print(result2) # ['n', 'o', 'h', 't', 'y', 'P']

print("".join(result2))  # nohtyP


print("_"*50)
##################### Copy Method ################
# shallow copy :  When we assign one listA to listB and modify the listB, so in case of shallow copy, we are just
# passing the reference of one list data to another list, then changes will reflect in both the list.


list_a = [100, 500, 5, 8]
list_b = list_a
list_b.append('P')
list_b.append('Q')
print("list_a :", list_a) # [100, 500, 5, 8, 'P', 'Q']
print("list_b :", list_b) # [100, 500, 5, 8, 'P', 'Q']


# Deep Copy : In case of deep copy if modify any list value, then changes will reflect in respective list only.

list_X = [100, 500, 5, 8, 12, 34]
list_Y = list_X.copy()
list_Y.append('A')
list_Y.append('B')
list_X.append('P')

print("list x :", list_X) # [100, 500, 5, 8, 12, 34, 'P']
print("list y :", list_Y) # [100, 500, 5, 8, 12, 34, 'A', 'B']

print("_"*50)
################### Get Max, Min, and Sum of all values #######
list_P = [100, 500, 5, 8, 12, 34]

print("Max value :", max(list_P))
# Max value : 500

print("Min value :", min(list_P))
# Min value : 5

print("Sum of values :", sum(list_P))
# Sum of values : 659

print("_"*50)
#############################################

print("Max of string :", max('helvo')) # v
print("min of string :", min('Zhello')) # e
# 65-90 A-z
# 97-122 a-z

#print("sum of string :", sum('hello')) #
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


print("_"*50)
#############################################
print("Max of dict :", max({'a': 123, 'b': 567})) #
# Max of dict : b
print("min of dict :", min({'a': 123, 'b': 567}))
# min of dict : a

print("sum of dict keys:", sum({10: 'Hello', 20: 'Python'}))
# sum of dict keys : 30

############################# List Comprehension #################
# write a program to get square of each value in list and store in a list
list1 = [5, 7, 10, 13, 9, 3]
result1 = []

for val in list1:
    result1.append(val**2)

print("result :", result1)
# [25, 49, 100, 169, 81, 9]


##################
# solve above program with list comprehension
result2 = [val**2 for val in list1]
print("result2 :", result2)


################################
print("_"*50)
# write a program to get square of even value in list and store in a list
list1 = [4, 7, 10, 13, 9, 12]
output = []
for val in list1:
    if val%2 == 0:
        output.append(val**2)
    else:
        continue

print("output :", output)

####################
# solve above program to list comprehension
output2 = [val**2 for val in list1 if val%2 == 0]
print("output2 :", output2)



################################
print("_"*50)
#write a program to get below output
list2 = [4, 7, 10, 13, 9, 12]
#output = [(4, 'even'), (7, 'odd'), (10, 'even'), (13, 'odd'), (9, 'odd'), (12, 'even')]

output = []
for val in list2:
    if val%2 ==0:
        output.append((val, 'even'))
    else:
         output.append((val, 'odd'))

print("output :", output)
#  [(4, 'even'), (7, 'odd'), (10, 'even'), (13, 'odd'), (9, 'odd'), (12, 'even')]

################################
# solve above program with list comprehension
output3 = [(val, 'even') if val%2 ==0 else (val, 'odd') for val in list2]
print("output3 :", output3)
# [(4, 'even'), (7, 'odd'), (10, 'even'), (13, 'odd'), (9, 'odd'), (12, 'even')]





print("_"*50)
################################
# write a list comprehension program to generate below output
list_a = ['a', 'b', 'c']
list_b = ['P', 'Q']
output = [('a', 'P'), ('a', 'Q'), ('b', 'P'), ('b', 'Q'), ('c', 'P'), ('c', 'Q')]

output4 = [(x, y) for x in list_a for y in list_b]
print("output :", output4)
# [('a', 'P'), ('a', 'Q'), ('b', 'P'), ('b', 'Q'), ('c', 'P'), ('c', 'Q')]
