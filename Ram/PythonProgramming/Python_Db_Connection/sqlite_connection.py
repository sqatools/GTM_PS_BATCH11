import sqlite3

def create_db_connection(db_name = 'school.db'):
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


def delete_data(query):
    connect = create_db_connection()
    connect.execute(query)
    connect.commit()
    connect.close()

#delete_data_query = """DELETE FROM student"""
#delete_data(delete_data_query)

#create_table_query = """create table student(name char[20], email char[20], phone char[20], address char[60])"""
#create_table(create_table_query)
#insert_data_query = """insert into student(name, email, phone, address) values('Ram', 'ram@gmail.com', '9876543123', 'Hyderabad')"""
#insert_data(insert_data_query)

select_query = """select * from student"""
data1 = select_data(select_query)
for val in data1:
    print(val)



