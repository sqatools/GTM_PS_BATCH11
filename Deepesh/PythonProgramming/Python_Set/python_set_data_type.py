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


