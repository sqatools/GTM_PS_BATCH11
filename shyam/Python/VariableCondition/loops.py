
#Q1 write a python program to remove duplicate from list.
list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8, 7]
#output1 = [54, 8, 12, 5, 7, 23, 67]

list1=[]
for i in range(len(list1)):
    if list1[i] not in list1[i+1:]:
        list1.append(list1[i])
print(list1)


#Q2 : write a python program to add all multiple repeated values.
list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4]
# Add all the duplicate values in the list
#output2 = [10, 16, 12, 8, 4, 3]


#Q3 : write a python program to add all multiple repeated values.
list3 = [[3, 4, 5, 3], [1, 3, 4, 1], [5, 7, 12, 7]]
# Add all duplicate values in child list
#output3 = [[6, 4, 5], [2, 3, 4], [5, 14, 12]]

    