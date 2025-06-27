"""
Properties :
1. Dictionary is mutable data type, we can modify the values.
2. Dict store data in key value pair with curly braces e.g. {'k': 'value'}
3. Dict only contains unique keys, duplicate keys are not allowed.
  -> if dictionary has duplicate keys then it will consider only latest key data
4. Only immutable data type can be key in dictionary
   e.g. int, float, string, tuple, boolean
   Can not  contain list, dict, set as key in dict.

5. All types of data can be value in dictionary.
  e.g. int, float, string, list, tuple, dict, set, boolean.
6. Dictionary does not follow indexing.
"""

# if we provide duplicate keys in the dictionary, then it will consider the latest value
dict1 = {'a': 123, 'b': 456, 'c': 789, 'a': 898}

print("dict1 :", dict1)
# dict1 : {'a': 898, 'b': 456, 'c': 789}

# add new key value in the dictionary
dict1['d'] = 560

print("dict1 :", dict1)
# dict1 : {'a': 898, 'b': 456, 'c': 789, 'd': 560}

# get value from dictionary with the help of keys
print("value of c :", dict1['c'])
# value of c : 789


# dictionary with multiple values
dict2  = {'P' : {'X': {'I' : 555, 'II': 789, 'III': 345}},
          'Q' : [
              {'name': 'user1', 'email': 'user1@gmail.com', 'phone': 4567555532},
              {'name': 'user2', 'email': 'user2@gmail.com', 'phone': 56645645645}
          ]}

print(dict2['P']['X']['III']) # 345
print(dict2['Q'][1]['phone']) # 56645645645

"""
{
  "firstName": "John",
  "lastName": "Doe",
  "age": 30,
  "address": {
    "streetAddress": "1600 Amphitheatre Parkway",
    "city": "Mountain View",
    "state": "CA",
    "postalCode": "94043"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "210-555-1234"
    },
    {
      "type": "fax",
      "number": "650-555-4567"
    }
  ],
  "isEmployed": true,
  "hobbies": ["reading", "hiking", "coding"]
}


"""

print("_"*50)
###################################################
# apply loop on dict data
dict3 =  {'name': 'user1', 'email': 'user1@gmail.com', 'phone': 4567555532}

# get keys with from keys
for k in dict3:
    print(k)

"""
name
email
phone
"""
# items methods in the dictionary
print("items data :", dict3.items())
#dict_items([('name', 'user1'), ('email', 'user1@gmail.com'), ('phone', 4567555532)])

# Apply loop with items method:
for data in dict3.items():
    print(data)

"""
('name', 'user1')
('email', 'user1@gmail.com')
('phone', 4567555532)
"""


# Apply loop with items method with 2 variables:
for k, v in dict3.items():
    print("key :", k)
    print("value :", v)
    print("_"*10)

"""
key : name
value : user1
__________
key : email
value : user1@gmail.com
__________
key : phone
value : 4567555532
__________
"""

print("_"*40)
## write a python code to get square of dict values.
dict4 = {'P': 4, 'Q': 10, 'R': 12}
for k, v in dict4.items():
    print(k, ":", v**2)
"""
P : 16
Q : 100
R : 144
"""

print("_"*50)
##############################
# write a python to calculate the bill amount as per user purchase
fruit_price = {'Apple': 100, 'Mango': 150, 'Banana': 50, 'watermelon': 300}
fruit_inventory = {'Apple': 500, 'Mango': 400, 'Banana': 300, 'watermelon': 200}
user_purchase = {'Apple': 10, 'Mango': 20, 'Banana': 30, 'watermelon': 40}

total_bill = 0
print("Name | Price|No.Fruits|Fruit Bill")
for name, price in fruit_price.items():
    fruit_name = name
    frt_price = price
    frt_purchase = user_purchase[fruit_name]

    frt_bill = price * frt_purchase
    total_bill = total_bill + frt_bill
    fruit_inventory[fruit_name] = fruit_inventory[fruit_name] - frt_purchase
    print(fruit_name, "|", frt_price, "|", frt_purchase, "|", frt_bill)

print("total bill :", total_bill)
print("Updated inventory:", fruit_inventory)


# get each value of dict without using loop
home_word_dict = {
  "firstName": "John",
  "lastName": "Doe",
  "age": 30,
  "address": {
    "streetAddress": "1600 Amphitheatre Parkway",
    "city": "Mountain View",
    "state": "CA",
    "postalCode": "94043"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "210-555-1234"
    },
    {
      "type": "fax",
      "number": "650-555-4567"
    }
  ],
  "isEmployed": True,
  "hobbies": ["reading", "hiking", "coding"]
}

print("_"*50)
############################### Dict Methods #######################
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#################################
# update method :  If we want to update one dict data to another dict, then we can use update method.
dict_a = {'a': 234, 'b': 567, 'c': 890}
dict_b = {'p': 222, 'q': 678, 'r': 888}

dict_a.update(dict_b)
print("dict_a :", dict_a)
# {'a': 234, 'b': 567, 'c': 890, 'p': 222, 'q': 678, 'r': 888}
print("dict_b :", dict_b)
# {'p': 222, 'q': 678, 'r': 888}


print("_"*50)
#################################
# get method : get method return the value with the help of keys
dict_c = {'p': 222, 'q': 678, 'r': 888}
print("value of r :", dict_c.get('r'))
# value of r : 888

print(dict_c['r']) # 888
dict_c['r'] = 999
print("dict_c :", dict_c)
# dict_c : {'p': 222, 'q': 678, 'r': 999}


print("_"*50)
#################################
# keys() and values() method:
# keys method return list of keys
# values method return list of values

dict_d = {'p': 222, 'q': 678, 'r': 888}
print("list of keys :", dict_d.keys())
# dict_keys(['p', 'q', 'r'])
print("list of values :", dict_d.values())
# dict_values([222, 678, 888])


print("_"*50)
#################################
# pop method :  pop method remove any specific key value pair that we want to remove from dict and return value.

dict_e = {'a': 234, 'b': 567, 'c': 890, 'p': 222, 'q': 678, 'r': 888}
var1 = dict_e.pop('r')
print("removed value :", var1)
# removed value : 888
print("dict_e :", dict_e)
# {'a': 234, 'b': 567, 'c': 890, 'p': 222, 'q': 678}
# dict_e.pop()
# TypeError: pop expected at least 1 argument, got 0

print("_"*50)
#################################
# popitems() method :"  This method remove key value pair and return as tuple from dict.
dict_f = {'a': 234, 'b': 567, 'c': 890, 'p': 222, 'q': 678}
var1 = dict_f.popitem()
print("removed data :", var1) # 'q': 678}
print("dict_f :", dict_f) # {'a': 234, 'b': 567, 'c': 890, 'p': 222}

var2 = dict_f.popitem()
print("removed data :", var2)  # ('p', 222)
print("dict_f :", dict_f) # {'a': 234, 'b': 567, 'c': 890}
