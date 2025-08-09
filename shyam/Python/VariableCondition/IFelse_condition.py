#Q1 write a python program to remove duplicate from list.
list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8, 7]

for i in  range(len(list1)):
    if list1[i] not in list1[i+1:]:
        print(list1[i])
"""
54
12
23
67
5
8
7

"""
print("_"*50)

#Q2 : write a python program to add all multiple repeated values.
list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4]
tem_list=[]
out=[]
for value in list2:
    value_count=list2.count(value)  

# Program to print the T pattern with for loop
"""
* * * * * *   # i = 0
* * * * * *   # i = 1
    * *       # i = 2
    * *       # i = 3
    * *       # i = 4
    * *       # i = 5
* * * * * *   # i = 6
* * * * * *   # i = 7
"""
"""
for i in range(8):
    for j in range(6):
        if i in [0, 1, 6, 7]:
           print("*", end=" ")
        elif i in [2, 3, 4, 5]:
            if j in [2, 3]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()
"""
"""
* * * * *    # i = 0
    *        # i = 1
    *        # i = 2
    *        # i = 3
    *        # i = 4
* * * * *    # i = 5
"""

for i in range(6):
    for j in range(5):
        if i in [0,5]:
           print("*", end=" ")
        elif i in [1, 2, 3, 4]:
            if j in [2]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()


#Q3 : write a python program to add all multiple repeated values.
list3 = [[3, 4, 5, 3], [1, 3, 4, 1], [5, 7, 12, 7]]
# Add all duplicate values in child list
#output3 = [[6, 4, 5], [2, 3, 4], [5, 14, 12]]

for i in range(len(list3)):
    for j in range(i+1, len(list3)):
        if list3[i]==list3[j]:
            print(list3[i])
            break


            