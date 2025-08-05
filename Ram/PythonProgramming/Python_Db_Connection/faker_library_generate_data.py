# pip install faker

from faker import Faker

fk = Faker()

print("username :", fk.user_name())
print("email :", fk.email())
print("phone :", fk.phone_number())
print("address :", fk.address())

