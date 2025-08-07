"""
Properties :
1. Tuple is immutable data type, we can not modify the values.
2. Tuple can contain any type of data.
   e.g. int, float, complex, string, list, tuple, dict, set, boolean, None
3. Tuple also follows positive and negative indexing.
4. We can use tuple where the data is going to be fixed.
  e.g. days in a week, months in year, any information that we don't want to update further
"""

tup1 = (3, 4.5, 'Hello', [4, 2, 7], (8, 6, 10), {'a': 123, 'b': 345}, {1, 4, 5}, True)
print(tup1, type(tup1))
# (3, 4.5, 'Hello', [4, 2, 7], (8, 6, 10), {'a': 123, 'b': 345}, {1, 4, 5}, True) <class 'tuple'>

# Apply loop on tuple with indexing
print("__"*40)
tup2 = (3, 4.5, 'Hello', [4, 2, 7], (8, 6, 10), {'a': 123, 'b': 345}, {1, 4, 5}, True)
for i in range(len(tup2)):
    print(i, tup2[i])
"""
0 3
1 4.5
2 Hello
3 [4, 2, 7]
4 (8, 6, 10)
5 {'a': 123, 'b': 345}
6 {1, 4, 5}
7 True
"""

# get values with +ve and -ve slicing
print("__"*40)
tup3 = (3, 4.5, 'Hello', [4, 2, 7], (8, 6, 10), {'a': 123, 'b': 345}, {1, 4, 5}, True)
print(tup3[:6:]) # (3, 4.5, 'Hello', [4, 2, 7], (8, 6, 10), {'a': 123, 'b': 345})
print(tup3[-1:-6:-1]) # (True, {1, 4, 5}, {'a': 123, 'b': 345}, (8, 6, 10), [4, 2, 7])
print(tup3[::-1]) # (True, {1, 4, 5}, {'a': 123, 'b': 345}, (8, 6, 10), [4, 2, 7], 'Hello', 4.5, 3)
print(tup3[-5::-1]) # ([1, 2, 3], 'Hello', 4.5, 3)
print(tup3[3::-1]) # ([1, 2, 3], 'Hello', 4.5, 3)


###################################
# Home work:
# 1.  write a python program to max value from tuple.
# 2.  write a python program to remove duplicate values from tuple
# 3.  write a python program to get second max value from tuple.

print("__"*40)
# 1.  write a python program to max value from tuple.
tup4 = (4, 9, 25, 44, 150, 80, 180, 12)
print("Max Value:", max(tup4)) # Max Value: 180

print("__"*40)
# 2.  write a python program to remove duplicate values from tuple
# tuple is immutable datatype, to remove duplicate values in tuple have to convert it into list or set
tup6 = (5, 9, 25, 44, 5, 9, 30, 12)
result = []
for i in tup6:
        if i not in result:
            result.append(i)
            print("", result)
        else:
            continue
print("__"*40)
print(tuple(result))
# [5, 9, 25, 44, 30, 12]

print("__"*40)
tup7 = (5, 9, 25, 44, 5, 9, 30, 12)
result = tuple(set(tup7))
print(result) # (5, 9, 44, 12, 25, 30)

print("__"*40)
# # 3.  write a python program to get second max value from tuple.
tup5 = (5, 9, 25, 44, 150, 80, 180, 12)
max_val = 0
sec_max_val = 0

for val in tup5:

    if val > max_val: # 5 > 0, 9>5, 25 > 9, 44 > 25, 150 > 44, 150 > 80, 180 > 150, 180 >12
        sec_max_val = max_val # 5 9
        max_val = val

print("Max value :", max_val)
print("Second Max Value :", sec_max_val)

