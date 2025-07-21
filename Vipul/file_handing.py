########## read file ###############
def file_read(file_path):
    file = open(file_path, 'r')
    data = file.read()
    print(data)

file_read("text.txt")

########## write file ###############

def write_file(file_path):
    file = open(file_path, 'w') # create file in write mode
    file.write("I love java")

write_file("text1.txt")
write_file("text2.txt")

def write_file(file_path):
    file = open(file_path, 'a') # create file in append mode
    file.write("I love java\n")

write_file("text3.txt")
write_file("text3.txt")
write_file("text3.txt")

########## context manager ###############

def read_file(file_path, bytes):
    with open(file_path, 'r') as file:
        data = file.read(bytes)
        print(data)
        
read_file('text1.txt', 7)


def read_file_lines(file_path, lines):
    with open(file_path, 'r') as file:
        for _ in range(lines):
            data = file.readline()
            print(data, end = ' ')


read_file_lines('text3.txt', 4)
