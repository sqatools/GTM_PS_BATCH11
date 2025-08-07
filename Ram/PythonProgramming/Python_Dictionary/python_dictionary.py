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
 # dictionary with multiple values
dict2  = {'P' : {'X': {'I' : 555, 'II': 789, 'III': 345}},
          'Q' : [
              {'name': 'user1', 'email': 'user1@gmail.com', 'phone': 4567555532},
              {'name': 'user2', 'email': 'user2@gmail.com', 'phone': 56645645645}
          ]}

print(dict2['P']['X']['III']) # 345
print(dict2['Q'][1]['phone']) # 56645645645

# get each value of dict without using loop

dict_1 = {
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

print(dict_1['firstName'])
print(dict_1['lastName'])
print(dict_1['age'])
print(dict_1['address']['streetAddress'])
print(dict_1['address']['city'])
print(dict_1['address']['state'])
print(dict_1['address']['postalCode'])
print(dict_1['phoneNumbers'][0]['type'])
print(dict_1['phoneNumbers'][0]['number'])
print(dict_1['phoneNumbers'][1]['type'])
print(dict_1['phoneNumbers'][1]['number'])
print(dict_1['isEmployed'])
print(dict_1['hobbies'])
"""
John
Doe
30
1600 Amphitheatre Parkway
Mountain View
CA
94043
home
210-555-1234
fax
650-555-4567
True
['reading', 'hiking', 'coding']
"""
str1 = "hello am learning python"
#words = str1.split()
#print(words)
j = {i: len(i) for i in str1.split()}
print(j)

#output2 = {"Ho": "HHeelllloo", "we": "wwee", "ae": "aarree", "Lg": "LLeeaarrnniinngg", "Pn": "PPyytthhoonn"}

str2 = "Hello we are Learning Python"

words = str2.split()
print(words)
result = {}

for word in words:
    key = word[0] + word[-1]
    value = ''.join([char * 2 for char in word])
    result[key] = value

print(result)
"""
for word in words:
    key = word[0] + word[-1]  # first + last letter
    value = ''.join([char * 2 for char in word])  # duplicate each character
    result[key] = value

print(result)
"""