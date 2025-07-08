# item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
# price_list = [100, 250, 50, 80]
# purchase_list = [10, 5, 10, 20]
#
# total_bill = 0
#
# for i, j in zip(price_list, purchase_list):
#     total_bill += i*j
#
# print(total_bill)
#
# list1 = [45, 67, 80, -3, 4 -54, -4, 23]
#  # output = [45, 67, 80, 4, 23, -3,-4, -54]
#
#
#
# print(list1)
# post_list = [x for x in list1 if x >= 0]
# nega_list = [x for x in list1 if x < 0]
# output = post_list + nega_list
# print(output)
#
# # write a python program to calculate the bill amount and update the inventory
# item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
# inventory_list = [200, 150, 500, 300]
# price_list = [100, 250, 50, 80]
# purchase_list = [10, 5, 10, 20]
#
#
# #up_inventory_list = [180, 145, 490, 280]
# total_bill = 0
#
# updated_list = []
# for i in range(len(item_list)):
#     inventory_list[i] = inventory_list[i] - purchase_list[i]
#
#
# print(inventory_list)

# list11 = [3, 6, 7, 81, 2]
# sum = 0
# for i in list11:
#     sum += i
#
# print("sum", sum)

l = ['Apple', 'Mango', 'Banana', 'Lichi']
# d = {}
value = []
for i in l:
    value.append(len(i))
print(value)
d = dict(zip(l, value))
print(d)

#Input list
list1 = [{'Hello': 5},{'student': 7},{'are': 3},{'learning': 8},
         {'Python': 6},{'Its': 3},{'Language': 8},{'are':3}]
list2 = []

for value in list1:
    if value not in list2:
        list2.append(value)

#Printing output
print(list2)