# write a python program to calculate the bill amount.
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

total_bill = 0

for i in range(len(item_list)):
    total_bill = total_bill + (price_list[i] * purchase_list[i])

print(total_bill)
# write a python program to sort the list in positive and negative order
list1 = [45, 67, 80, -3, 4 -54, -4, 23]
#output = [45, 67, 80, 4, 23, -3,-4, -54]
output = []
for i in range(len(list1)):
    if list1[i] > 0:
        output.append(list1[i])
    else:
        output.insert(list1.index(list1[i], 0), list1[i])
print(output)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
#write a python program to calculate the bill amount and update the inventory
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]


#up_inventory_list = [180, 145, 490, 280]
total_bill = 0

for i in range(len(item_list)):
    total_bill=total_bill+(price_list[i]*purchase_list[i])
    inventory_list[i]=inventory_list[i]-purchase_list[i]

print(total_bill)
print(inventory_list)

print("_"*50)
touple1=(2,4,5,6,7,6,4)
print(tuple(sorted(touple1)))

# Home work:
# 1.  write a python program to max value from tuple.
# 2.  write a python program to remove duplicate values from tuple
# 3.  write a python program to get second max value from tuple.
"""
tup1=(2,4,5,7,6,1)

max_value=0
for i in range(len(tup1)):
    if tup1[i]>max_value:
        max_value=tup1[i]

print(max_value)
"""
# 2.  write a python program to remove duplicate values from tuple
tup1=(2,4,5,7,6,1,6,5)

for i in range(len(tup1)):
    for j in range(i+1, len(tup1)):
        if tup1[i]==tup1[j]:
            tup1=tup1[:j]+tup1[j+1:]
            break
print(tup1)



