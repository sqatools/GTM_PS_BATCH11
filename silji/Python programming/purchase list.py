
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]


#up_inventory_list = [190, 145, 490, 280]
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

up_inventory_list = []

for i in range(len(inventory_list)):
    updated = inventory_list[i] - purchase_list[i]
    up_inventory_list.append(updated)

print("Updated Inventory List:", up_inventory_list)