
# write a python program to calculate the bill amount.
# item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
# price_list = [100, 250, 50, 80]
# purchase_list = [10, 5, 10, 20]
#
# total_bill = 0
# for i, j in range(price_list, purchase_list):
#     total_bill += i*j
#
# print(total_bill)

item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

total_bill = sum(p * q for p, q in zip(price_list, purchase_list))
print("Total Bill Amount: ", total_bill)
