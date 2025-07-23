list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8,7]

list2 = []

for item in list1:
    if item not in list2:
        list2.append(item)
print("After removed duplicate values = ",list2)


print("-"*50)



#Q2 : write a python program to add all multiple repeated values.
list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4, ]
output = [10, 16, 12, 8, 4, 3]

count_dict = {}
for num in list2:
    if num in count_dict:
        count_dict[num] += num  # Add current number to its sum
    else:
        count_dict[num] = num
print(count_dict)



n = 3

if n%2 != 0:
    print("p")
else:
    print("prime number")


