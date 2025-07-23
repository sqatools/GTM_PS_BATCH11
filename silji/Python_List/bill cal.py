# write a python program to calculate the bill amount.
# item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
# price_list = [100, 250, 50, 80]
# purchase_list = [10, 5, 10, 20]
#
# total_bill = 0


# Define the lists
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

# Initialize total bill
total_bill = 0

# Calculate total bill
print("Itemized Bill:")

for i in range(len(item_list)):
    item = item_list[i]
    price = price_list[i]
    quantity = purchase_list[i]
    cost = price * quantity
    total_bill += cost
    print(f"{item:10} x {quantity:2} = ₹{cost}")


print(f"Total Bill Amount: ₹{total_bill}")