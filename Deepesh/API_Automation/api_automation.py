# install lib using below command
# pip install requests
import requests
from pprint import pprint
import json


def get_all_objects():
    url = "https://api.restful-api.dev/objects"
    response = requests.get(url)
    print(response.status_code) # 200
    pprint(response.json())


#get_all_objects()


def get_specific_objects():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"
    response = requests.get(url)
    print("status code :", response.status_code)
    pprint(response.json())


#get_specific_objects()


def get_one_single_object():
    url = "https://api.restful-api.dev/objects/7"
    response = requests.get(url)
    print("status code :", response.status_code)
    pprint(response.json())

#get_one_single_object()


def add_new_object():
    url = "https://api.restful-api.dev/objects"
    user_data = json.dumps({
   "name": 'Apple MacBook Pro 16',
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": '1 TB'
      }
    })

    header_val = {"Content-Type": "application/json"}
    response = requests.post(url, data=user_data, headers=header_val)
    print(response.status_code)
    pprint(response.json())


#add_new_object()

"""
200
{'createdAt': '2025-09-03T16:32:25.593+00:00',
 'data': {'CPU model': 'Intel Core i9',
          'Hard disk size': '1 TB',
          'price': 1849.99,
          'year': 2019},
 'id': 'ff8081819782e69e0199106c1ff931e2',
 'name': 'Apple MacBook Pro 16'}
"""



def update_new_object(id):
    url = f"https://api.restful-api.dev/objects/{id}"
    user_data = json.dumps({
   "name": 'Apple MacBook Pro 16 update',
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": '2 TB'
      }
    })

    header_val = {"Content-Type": "application/json"}
    response = requests.put(url, data=user_data, headers=header_val)
    print(response.status_code)
    pprint(response.json())

#update_new_object("ff8081819782e69e0199106c1ff931e2")


def update_specific_entry(id):
    url = f"https://api.restful-api.dev/objects/{id}"
    user_data = json.dumps({
   "data": {
      "year": 2025
      }
    })

    header_val = {"Content-Type": "application/json"}
    response = requests.patch(url, data=user_data, headers=header_val)
    print(response.status_code)
    pprint(response.json())

update_specific_entry("ff8081819782e69e0199106c1ff931e2")


def delete_entry(id):
    url = f"https://api.restful-api.dev/objects/{id}"
    response = requests.delete(url)
    print(response.status_code)
    pprint(response.json())

#delete_entry("ff8081819782e69e0199106c1ff931e2")


