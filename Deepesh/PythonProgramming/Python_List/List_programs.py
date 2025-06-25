#Q1 : write a python program to max value from list without using max function.
list_a = [4, 6, 8, 34, 56, 12]
max_val = 0 # 4, 6, 8, 34, 56

for val in list_a:
    if val > max_val:
        max_val = val # 4, 6, 8, 34, 56
    else:
        continue

print("Max value :", max_val)


#########################
print("_"*50)

#Q2 : write a python program to second max value from list without using max function.
list_a = [4, 76, 60, 8, 34, 56, 12, 13, 100]
max_val = 0
sec_max_val = 0

for val in list_a:

    if val > max_val:
        sec_max_val = max_val # 4
        max_val = val # 76
    # 76 > 60 > 4
    elif max_val > val > sec_max_val:
        sec_max_val = val
    print("max :", max_val, "sec max :", sec_max_val)

print("Max val :", max_val)
print("Sec max val :", sec_max_val)

print("_"*50)
#############################################################
# write a python program to get below output
list1 = [3, 6, 8, 2, 7, 9, 1, 4]
#output = [[3, 7], [6, 4], [8, 2], [9, 1]]
output = []

for i in range(len(list1)): # (0, 8)
    for j in range(i+1, len(list1)): # (1, 8)
        if list1[i] + list1[j] == 10:
            output.append([list1[i], list1[j]])


print(output)

print("_"*50)
############################################
# write a python program to calculate the bill amount.
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

total_bill = 0

for i in range(len(item_list)):
    item_name = item_list[i]
    item_price = price_list[i]
    item_purchased = purchase_list[i]
    item_bill = item_price*item_purchased
    print(item_name ,"|", item_price, "|", item_purchased, "|", item_bill )
    total_bill = total_bill + item_bill


print("total bill :", total_bill)

"""
Apple | 100 | 10 | 1000
Mango | 250 | 5 | 1250
Banana | 50 | 10 | 500
Lichi | 80 | 20 | 1600
total bill : 4350
"""


print("_"*509)
#######################################################
# Q1:  write a python Program to sort positive and negative separately.

list_a = [45, 67, 80, -3, 4, -56, -4, 23]
#output = [45, 67, 80, 4, 23, -3, -56, -4]

pos_list =[]
neg_list =[]
for val in list_a:
    print(val, pos_list, neg_list)
    if val > 0:
        pos_list.append(val)
    else:
        neg_list.append(val)

print("output :", pos_list+neg_list)
# [45, 67, 80, 4, 23, -3, -56, -4]


#########################################################
# Home work
# write a python program to calculate the bill amount and update the inventory
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]


#up_inventory_list = [180, 145, 490, 280]
total_bill = 0
