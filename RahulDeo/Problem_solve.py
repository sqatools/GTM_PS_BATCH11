
"""
Slicing Home Work
"""
"""
str1 = Virat is Great India Batsman
# repeat first and last character three times
op1 = VVVirat is Great India Batsmannn
"""

strhm1 = "Virat is Great India Batsman"
first_char = strhm1[0]
last_char = strhm1[-1]

print(first_char * 3 + strhm1[1:-1] + last_char * 3)


# repeat first and last character 2 times of each word.
# op2 = VViratt iiss GGreatt IIndiaa BBatsmann

strhm2 = "Virat is Great India Batsman"
first_char1 = strhm2[0:1]
first_char2 = strhm2[4:5]
second_char1 = strhm2[6:8]
third_char1 = strhm2[9:10]
fourth_char1 = strhm2[13:14]
fifth_char1 = strhm2[15:16]
sixth_char1 = strhm2[19:20]
seventh_char1 = strhm2[21:22]
Eight_char1 = strhm2[27:28]

print(first_char,first_char2,second_char1,third_char1,fourth_char1,fifth_char1,sixth_char1,seventh_char1,Eight_char1)

print(first_char1 * 2 + strhm2[1:4] +  first_char2 * 2 + " " + second_char1 * 2 + " " + third_char1 * 2 + strhm2 [10:13] + fourth_char1 * 2 + " " + fifth_char1 * 2 + strhm2[16:19] + sixth_char1 * 2 + " " + seventh_char1 * 2 + strhm2[22:27] + Eight_char1 * 2)



# replace first and last character each word from given string
# op3 = tiraV si treaG andiI natsmaB
second_char2 = strhm2[-21:-23:-1]
print(second_char2)

print(first_char2 + strhm2[1:4] +  first_char1 + " " + second_char2 + " " + fourth_char1 + strhm2 [10:13] + third_char1 +
     " " + sixth_char1 + strhm2[16:19] + fifth_char1 + " " + Eight_char1 + strhm2[22:27] + seventh_char1)



# repeat each vowels 2 times in given string
# op4 = Viiraat iis Greeaat IIndiiaa Baatsmaan


strhm3 = "Virat is Great India Batsman"
vowels = "AEIOUaeiou"

result=""
for ch in strhm3:
    if ch in vowels:
        result += ch * 2
    else:
        result += ch

print(result)

print('_'*100)
# write a python program to calculate the bill amount.
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]

total_bill = 0

for i in range (len(item_list)):
    item = item_list[i]
    price= price_list[i]
    purchase = purchase_list[i]

    item_total = price * purchase
    total_bill += item_total



print('_'*100)

# write a python program to calculate the bill amount and update the inventory
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]


#up_inventory_list = [190, 145, 490, 280]
print('_'*100)

total_bill = 0

for i in range(len(item_list)):
    item = item_list[i]
    price = price_list[i]
    qty = purchase_list[i]
    item_total = price * qty
    total_bill += item_total

    new_stock = inventory_list[i] - qty
    inventory_list[i]=new_stock

print(total_bill)
print(inventory_list)


# 1.  write a python program to max value from tuple.

print('_'*50)
tup1 = (25, 56, 85, 4, 2, 78, 95, 0)
print("MAx value :", max(tup1))
# 2.  write a python program to remove duplicate values from tuple

print('_'*50)
tup2 = (25, 6, 45, 4, 6, 78, 56, 45, 8)
remove_duplicate = set(tup2)
print(remove_duplicate, type(remove_duplicate))
tup3 = tuple(remove_duplicate)
print(tup3)

# 3.  write a python program to get second max value from tuple.

print('_'*50)
tup4 = (25, 56, 85, 4, 2, 78, 95, 0)
#value = sorted(tup4)

