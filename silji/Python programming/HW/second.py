#Q2 : write a python program to add all multiple repeated values.
list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4, ]
output = [10, 16, 12, 8, 4, 3]

list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4]

output2 = []
for num in list2:
    if num not in output2:
        count = list2.count(num)
        if count > 1:
            output2.append(num * count)
        else:
            output2.append(num)

print(output2)