# write a python program to remove duplicate from list.
list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8, 7]
# output = [54, 8, 12, 5, 7, 23, 67]


list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8, 7]

output = []

for item in list1:
    if item not in output:
        output.append(item)

print("after removing duplicates:", output)