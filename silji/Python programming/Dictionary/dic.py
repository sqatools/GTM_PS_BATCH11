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

# Access each value without using a loop
first_name = home_word_dict["firstName"]
last_name = home_word_dict["lastName"]
age = home_word_dict["age"]

#  address
street = home_word_dict["address"]["streetAddress"]
city = home_word_dict["address"]["city"]
state = home_word_dict["address"]["state"]
postal_code = home_word_dict["address"]["postalCode"]

#  phone numbers
home_phone_type = home_word_dict["phoneNumbers"][0]["type"]
home_phone_number = home_word_dict["phoneNumbers"][0]["number"]
fax_phone_type = home_word_dict["phoneNumbers"][1]["type"]
fax_phone_number = home_word_dict["phoneNumbers"][1]["number"]

# Other values
is_employed = home_word_dict["isEmployed"]
hobbies = home_word_dict["hobbies"]

print(first_name)
print(last_name)
print(age)
print(street, city, state, postal_code)
print(home_phone_type, home_phone_number)
print(fax_phone_type, fax_phone_number)
print(is_employed)
print(hobbies)