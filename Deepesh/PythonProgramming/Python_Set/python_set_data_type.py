"""
Properties:
-> Set is mutable data type.
-> Set contains unique values, duplicate data is not allowed
-> Set store values in random order.
-> Set only contains immutable data type as member.
   e.g. int, float, string, tuple, boolean
"""

set1 = {3, 4.5, (4, 6, 8), 'Hello', True, None, 3, 4.5}
print(set1, type(set1))
# {None, True, 3, 4.5, 'Hello', (4, 6, 8)} <class 'set'>

# Apply loop on set data type
for val in set1:
    print(val)

"""
None
True
3
4.5
Hello
(4, 6, 8)
"""

################################# Set Methods ########################
print(dir(set))
"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 
'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 
'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 
'update'
"""

print("_"*50)
#######################
set_a = {5, 7, 9, 23, 56, 2}
# add method :  This method add one value at a time to the set data type.

set_a.add(100)
print("set_a :", set_a)
# set_a : {2, 23, 5, 100, 7, 56, 9}


print("_"*50)
#######################
# update method :  This method add one set to another set.

set_b = {5, 7, 9, 23, 56, 2}
set_c = {'a', 'b', 'c'}

# set_c will be updated with all the data from setr_b
set_c.update(set_b)
print("set_c :", set_c)
# set_c : {2, 5, 7, 9, 'b', 23, 56, 'a', 'c'}
print("set_b :", set_b) # {2, 23, 5, 7, 56, 9}


print("_"*50)
#######################
# union() method :  This method combine multiple set data and combine all the values

set_d = {5, 7, 9}
set_e = {'a', 'b', 'c', 7}
set_f  = {'P', 'Q', 'R', 5}

result = set_d.union(set_e, set_f)
print("result :", result)
# {'c', 5, 7, 'R', 9, 'b', 'P', 'a', 'Q'}

print("set_d :", set_d) # {9, 5, 7}
print("set_e :", set_e) # {'a', 'c', 7, 'b'}
print("set_f :", set_f) # {'R', 'P', 'Q', 5}


print("_"*50)
#######################
# remove() method :  This method remove any specific value from set, if the target value is not
# available then it will throw error.

set_g = {5, 7, 9, 6, 8, 3}

# remove existing value
set_g.remove(8)
print("set_g :", set_g)
# {3, 5, 6, 7, 9}

# remove non-existing value
#set_g.remove(20)
#print("set_g :", set_g)
# KeyError: 20

print("_"*50)
#######################
# discard() method :  This method remove any specific value from set, if the target value is not
# available then it will not throw any error.

set_h = {15, 17, 19, 16, 18, 13, 10}

# discard existing value
set_h.discard(17)
print("set_h :", set_h)
#  {16, 18, 19, 10, 13, 15}


# discard existing value
set_h.discard(30)
# If the target is not available, then discard method does not throw any error.


print("_"*50)
#######################
# pop() method :  This method remove any random value from set and return it, that we can store in a variable.

set_i = {15, 27, 29, 26, 18, 13, 10}
value = set_i.pop()
print("removed value :", value) # 18
print("updated set :", set_i) # {26, 29, 10, 27, 13, 15}

print("_"*50)
#######################
# clear() method : clear method remove all the data from set and remain only empty set.

set_j = {15, 27, 29, 26, 18, 13, 10}
set_j.clear()

print("set_j :", set_j)
# set_j : set()


print("_"*50)
#######################
# del keyword to remove complete variable from memory
set_k = {15, 27, 29, 26, 18, 13, 10}
del set_k
#print("set_k :", set_k)
# NameError: name 'set_k' is not defined

print("_"*50)
#######################
# difference method: This method return the difference of value from one set to another set.

set_1 = {4, 6, 8, 9, 10}
set_2 = {'a', 'b', 'c', 6, 9, 4}

print("difference from set_1 to set_2 :", set_1.difference(set_2)) #  {8, 10}
print("difference from set_2 to set_1 :", set_2.difference(set_1)) # {'b', 'c', 'a'}

print("set_1 :", set_1) # {4, 6, 8, 9, 10}
print("set_2 :", set_2) # {'a', 'c', 4, 6, 'b', 9}


# difference_update method :  This method get difference value from one to another set and update in the target
set_1.difference_update(set_2)
print("set_1 :", set_1) # {8, 10}

print("_"*50)
#######################
# symmetric_difference method: This method return the all difference values between both sets

set_3 = {4, 6, 8, 9, 10, 11, 12}
set_4 = {'a', 'b', 'c', 6, 9, 4}

print("set_3 to set_4 symm diff output:", set_3.symmetric_difference(set_4)) # {8, 10, 11, 12, 'b', 'a', 'c'}
print("set_4 to set_3 symm diff output:", set_4.symmetric_difference(set_3)) # {8, 10, 11, 12, 'b', 'a', 'c'}

print("set_3 :", set_3) # {4, 6, 8, 9, 10, 11, 12}
print("set_4 :", set_4) # {4, 6, 8, 9, 10, 11, 12}

# symmetric_difference_update: This method get the all difference values between both sets and update the output
# in target set
set_3.symmetric_difference_update(set_4)
print("set_3 :", set_3) # {'c', 8, 10, 11, 'a', 12, 'b'}
print("set_4 :", set_4) # {'c', 4, 6, 9, 'a', 'b'}


print("_"*50)
#######################
# intersection method: This method return the common values between both sets.

set_13 = {4, 6, 8, 9, 10, 11, 12}
set_14 = {'a', 'b', 'c', 6, 9, 4}

common_value = set_13.intersection(set_14)
print("common value :", common_value) # {9, 4, 6}

print("set_13 :", set_13)
print("set_14 :", set_14)

print("_"*50)
#### intersection update:  This method will update any of the set with intersection output.

set_13.intersection_update(set_14)
print("set_13 :", set_13) # {9, 4, 6}
print("set_14 :", set_14) # {4, 'c', 6, 9, 'a', 'b'}


print("_"*50)
#######################
# isdisjoint: This method check the target set is completely different from other set or not.

set_15 = {4, 6, 8, 9, 10, 11, 12}
set_16 = {'a', 'b', 'c', 6, 9, 4}
set_17 = {'P', 'Q', 'R'}

# set_15 and set_16 has common values
print(set_15.isdisjoint(set_16)) # False

# set_15 and set_17 doesn't have common values
print(set_15.isdisjoint(set_17)) # True



print("_"*50)
#######################
# superset and subset method: superset is considered as parent set and subset is considered child set.

set_18 = {4, 6, 8, 9, 10, 11, 12}
set_19 = {6, 9, 4}
set_20 = {'P', 'Q', 'R', 12, 11}

print("set_18 is superset of set_19:", set_18.issuperset(set_19)) #  True
print("set_18 is superset of set_20:", set_18.issuperset(set_20)) # False

print("set_19 is subset of set_18 :", set_19.issubset(set_18)) #  True
print("set_20 is subset of set_18 :", set_20.issubset(set_18)) # False


print("_"*50)
#######################
# copy method:

print("_"*50)
# Shallow copy :  In shallow copy we pass reference of one set to another set. If we modify any set value, then changes
# #                 will reflect in both the sets.
set_A = {4, 6, 8, 20}
set_B = set_A
set_B.add(30)
set_B.add(50)
set_A.add(100)

print("Set_A :", set_A) # {4, 100, 6, 8, 50, 20, 30}
print("Set_B :", set_B) # {4, 100, 6, 8, 50, 20, 30}


##############################################
print("_"*50)
# Deep copy :  In Deep copy we have use copy method and copy content from one set to another set. If we modify any set value, then changes
#                 will reflect respective set only, not in both sets.

set_P = {4, 6, 8}
set_Q  = set_P.copy()
set_Q.add(30)
set_P.add(50)

print("set_P :", set_P) # {8, 50, 4, 6}
print("set_Q :", set_Q) # {8, 4, 6, 30}


##############################################################
#Q1 write a python program to remove duplicate from list.
list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8, 7]
output1 = [54, 8, 12, 5, 7, 23, 67]

print("_"*50)
#Q2 : write a python program to add all multiple repeated values.
list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4]
# Add all the duplicate values in the list
output2 = [10, 16, 12, 8, 4, 3]

temp = []
output = []
for val in list2:
    val_count = list2.count(val)
    if val not in temp:
        if val_count > 1:
            output.append(val*val_count)
            temp.append(val)
        else:
            output.append(val)
            temp.append(val)

print("solution :", output) # [10, 16, 12, 8, 4, 3]


#Q3 : write a python program to add all multiple repeated values.
list3 = [[3, 4, 5, 3], [1, 3, 4, 1], [5, 7, 12, 7]]
# Add all duplicate values in child list
output3 = [[6, 4, 5], [2, 3, 4], [5, 14, 12]]

output = []

for child_list in list3:
    temp = []
    r1 = []
    for val in child_list:
        val_cnt = child_list.count(val)
        if val not in temp:
            if val_cnt > 1:
                r1.append(val*val_cnt)
                temp.append(val)
            else:
                r1.append(val)
                temp.append(val)
    output.append(r1)


print("solution 2 :", output)
# [[6, 4, 5], [2, 3, 4], [5, 14, 12]]



