import sqlite3
from faker import Faker

fk = Faker()

def create_db_connection(db_name='school.db'):
    con = sqlite3.connect(database=db_name)
    return con


def create_table(query):
    connect = create_db_connection()
    connect.execute(query)
    connect.close()


def insert_data(query):
    connect = create_db_connection()
    connect.execute(query)
    connect.commit()
    connect.close()


def select_data(query):
    connect = create_db_connection()
    data = connect.execute(query)
    return data


# create_table_query = """create table student(name char[20], email char[20], phone char[20], address char[60])"""
# create_table(create_table_query)


# insert_data_query = """insert into student(name, email, phone, address) values('Mohit', 'mohit@gmail.com', '54354354354', 'Pune, Baner balewadi')"""
# insert_data(insert_data_query)

for i in range(50):
    name = fk.user_name()
    phone = fk.phone_number()
    email= fk.email()
    address = fk.address()
    insert_data_query = f"""insert into student(name, email, phone, address) values('{name}', '{email}', '{phone}', '{address}')"""
    insert_data(insert_data_query)

select_query = """select * from student"""
data = select_data(select_query)
for val in data:
    print(val)






