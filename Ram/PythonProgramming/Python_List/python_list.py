"""
Properties :
1. List is mutable data type, we can modify the values.
2. List can contains any type of data.
   e.g. int, float, complex, string, list, tuple, dict, set, boolean, None
3. List also follows positive and negative indexing.
4. Usage of list, we generally list data type where is changing rapidly and we can update
   whenever required e.g. student registration, employee management.
"""

list = [2, 3.4, [5, 6, 7], {'a': 678}, (2, 3, 4), {4, 5, 6, 7}, True, False]
print(list, type(list))

print("__" * 40)
list1 = [2, 3.4, [5, 6, 7], {'a': 678}, (2, 3, 4), {4, 5, 6, 7}, True, False]
print(list1[4])  # (2, 3, 4)
print(list1[4][1])  # 3  Multi Indexing
print(list1[-5])  # {'a': 678}
print(list1[-5]['a'])  # 678

print("__" * 40)
##################### Slicing in List #############
list2 = [2, 3.4, [5, 6, 7], {'a': 678}, (2, 3, 4), {4, 5, 6, 7}, True, False]
print(list2[-6: -9: -1])  # [[5, 6, 7], 3.4, 2]
print(list2[2:5])  # [[5, 6, 7], {'a': 678}, (2, 3, 4)]
print(list2[-6::-1])  # [[5, 6, 7], 3.4, 2]  reverse order with -ve indexing
print(list2[2:: -1])  # [[5, 6, 7], 3.4, 2] reverse order with +ve indexing
print(list2[::-1])  # reverse of entire list
# [False, True, {4, 5, 6, 7}, (2, 3, 4), {'a': 678}, [5, 6, 7], 3.4, 2]

print("__" * 40)
##################### Apply Loop in List #############

list3 = [2, 4, 15, 60, 38, 10]
for i in list3:
    print(i)
"""
2
4
15
60
38
10
"""
# Apply Loop with Index
print("__" * 40)
for i in range(len(list3)):
    print(i, ":", list3[i])
"""
0 : 2
1 : 4
2 : 15
3 : 60
4 : 38
5 : 10
"""

print("__" * 40)
list4 = [2, 4, 15, 60, 38, 10]
for val in list4[1:-1: 1]:
    print(val, end=" ")  # 4 15 60 38

print("__" * 40)
list5 = [2, 4, 15, 60, 38, 10]
for val in range(1, len(list5) - 1, 1):
    print(val, list5[val])
    print(val, list5[val])
"""
1 4
2 15
3 60
4 38
"""

print("__" * 40)
# write a python program to calculate the bill amount.
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

total_bill = 0
item_bill = 0

for i in range(len(item_list)):

    item_name = item_list[i]
    item_price = price_list[i]
    item_purchased = purchase_list[i]
    item_bill = item_price * item_purchased
    print(item_name, "|", item_price, "|", item_purchased, "|", item_bill)
    total_bill = total_bill + item_bill

print("Total Bill :", total_bill)

"""
    print("-" * 40)
    list4 = [45, 67, 80, -3, 4, - 54, -4, 23]
    j = 0
    # output = [45, 67, 80, 4, 23, -3, -4, -54]
    for i in range(0, len(list4)):
        if (list4[i] > 0):
            a = list4[i]
            list4[i] = list4[j]
            list4[j] = a
            j += 1

    print(list4)
"""
print("__" * 40)
# write a python program to calculate the bill amount.
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

total_bill = 0
item_bill = 0
inventory = 0

for i in range(len(item_list)):

    item_name = item_list[i]
    item_price = price_list[i]
    item_purchased = purchase_list[i]
    # print(purchase_list[i])
    inventory = inventory_list[i]
    # print(inventory_list[i])

    item_bill = item_price * item_purchased
    inventory_list[i] = inventory_list[i] - item_purchased

    total_bill = total_bill + item_bill

    print(item_name, "|", item_price, "|", item_purchased, "|", item_bill, "|", inventory)

print("_"*60)
print("Total Bill :", total_bill)
print("Updated Inventory :", inventory_list)
