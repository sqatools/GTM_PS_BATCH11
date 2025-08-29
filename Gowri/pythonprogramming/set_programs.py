#Q1 write a python program to remove duplicate from list.
#  list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8, 7]
# # output1 = [54, 8, 12, 5, 7, 23, 67]
#
# set = ()
# for i in list1:
#     i= i
#     print(set)

# list1 = set(list1)
# print(list1)


#Q2 : write a python program to add all multiple repeated values.
list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4]
# Add all the duplicate values in the list
#output2 = [10, 16, 12, 8, 4, 3]

list2 = set(list2)
print(list2)
for i in list2:
    i= i**i
    print(list2)

# output1 =[]
# for item in list2:
#     if item not in output1:
#         output1.append(item)

# print("Output without duplicates value:", output1)



#Q3 : write a python program to add all multiple repeated values.
 list3 = [[3, 4, 5, 3], [1, 3, 4, 1], [5, 7, 12, 7]]
# # Add all duplicate values in child list
# output3 = [[6, 4, 5], [2, 3, 4], [5, 14, 12]]