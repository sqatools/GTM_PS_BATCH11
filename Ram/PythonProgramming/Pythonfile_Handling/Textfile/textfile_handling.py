"""
read mode(r): ->  when we want to read file data, then we will open file in a read mode(r).
write mode(w): -> when we want write content to the file, then we will open file in write mode(w)
               ->  when we write content with write then it will overwrite the previous content.
append mode(a):

"""

def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

# read file from current file location
#read_file("read_data.txt")

# read file from specific path
#read_file(r"D:\python1.txt")

############# write mode(w) ##############
def write_file(filepath, content):
    file = open(filepath, "w")
    file.write(content)
    file.close()

new_content = "We are Learning Python"
#write_file("write_data.txt", new_content)

def append_content(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()

#new_content1 = "India Won Second Test Match"
#write_file("append_data.txt", new_content1)

def append_content(filepath, content):
    file = open(filepath, "a")
    file.write(content)
    file.close()

new_content2 = "Hope you are doing good\n"
#append_content("append_data.txt", new_content2)


######################### context manager #####################
# context manager has its own enter and exist method, so no need to close the file or object explicitly.
# Once we move out of context manager, then it will close file automatically.

def read_file_context(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(data)
        print("file close status, in the context manager  :", file.closed)      # False
    print("file close status, outside of the context manager  :", file.closed)  # True


#read_file_context("read_data.txt")

# 3. Read specific number of lines with range using readlines method
# readlines:  This method return list of lines from target file.

def read_list_of_lines(file_path, start=0, end=1):
    with open(file_path, "r") as file:
        lines_list = file.readlines()
        for i in range(start, end):
            print(lines_list[i], end="")

#read_list_of_lines("read_data.txt", 0, 3)
"""
1. Python File Handling Programs refers to the process of manipulating files on a
2. computer using Python programming language. In Python, you can perform various
3. operations on files such as reading, writing, appending, and deleting files.
"""

# OR
def read_list_of_lines1(file_path, start=0, end=1):
    with open(file_path, "r") as file:
        lines_list = file.readlines()
        for i in range(start, end+1):
            print(lines_list[i-1], end="")

read_list_of_lines1("read_data.txt", 1, 3)
"""
1. Python File Handling Programs refers to the process of manipulating files on a
2. computer using Python programming language. In Python, you can perform various
3. operations on files such as reading, writing, appending, and deleting files.
"""