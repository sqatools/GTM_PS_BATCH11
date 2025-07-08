"""
read mode(r): ->  when we want to read file data, then we will open file in a read mode(r).
write mode(w): -> when we want write content to the file, then we will open file in write mode(w)
               ->  when we write content with write then it will overwrite the previous content.
append mode(a):

"""

def read_file(file_path):
    file = open(file_path, "r")
    data = file.read()
    print(data)
    file.close()

# read file from current file
#read_file("read_data.txt")

# read file from specific path
#read_file(r"E:\Filesdata\count_name.txt")



########################### write content to file #################

def write_file(file_path, content):
    file = open(file_path, "w")
    file.write(content)
    file.close()

# 1. write content to non-existing file
# ->  It will create new file and name provide and write content to the file
# ->  if we don't provide the file path, then it will create file in current location.
new_content = "We are learning Python Programming"
#write_file("write_data.txt", new_content)

# write_file(r"E:\Filesdata\batch11\write_data.txt", new_content)

# 2. write content to existing file:
# ->  It will overwrite the old content of the file and write new content
"""
new_data = "India Won Second Test Match"
write_file("new_data.txt", new_data)
"""

########################### Append content to file #################
# when we open file in append mode, then it will add content to the file at end of existing content.


def append_content_to_file(file_path, content):
    file = open(file_path, "a")
    file.write(content)
    file.close()

# 1. Append to non-existing File: It means the target file does not exist
# -> It will new create file and append content to the file.
"""
new_content1 = "Learning Python is Fun\n"
append_content_to_file("append_data.txt", new_content1)
"""

# 1. Append to existing File: It means the target file is available to add content
# -> It will add content at end of existing file content.
"""
new_content2 = "Good Morning, Hope you are doing good\n"
append_content_to_file("new_data_append.txt", new_content2)
"""

######################### context manager #####################
# context manager has its own enter and exist method, so no need to close the file or object explicitly.
# Once we move out of context manager, then it will close file automatically.

def read_file_context(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(data)
        print("file close status, in the context manager  :", file.closed) # False
    print("file close status, outside of the context manager  :", file.closed) # True


#read_file_context("read_data.txt")


######################### File read option #####################

# 1. Read specific number of bytes data.
def read_no_bytes_data(file_path, no_of_bytes):
    with open(file_path, "r") as file:
        data = file.read(no_of_bytes)
        print(data)


# This will return specific number of characters from beginning of the target file.
read_no_bytes_data("read_data.txt", 20)
"""
1. When I started pl
"""

# 2. Read specific number of lines with file.readline
# readline:  this method return one line a time, from the file
#            If we want to read multiple times, then we have to repeat this method that number of times.


def read_no_lines(file_path, no_of_lines):
    with open(file_path, "r") as file:
        for _ in range(no_of_lines):
            data = file.readline()
            print(data, end="")

#read_no_lines("read_data.txt", 5)

"""
1. When I started playing for SA, I was nowhere near good enough.
2.They gave me a lot of opportunities to learn from retired players,
3.really polish and improve my game. Going to England helped me under
4.stand technical things in my game, and helped me understand what
5.kind of cricketer I want to be. The head coach of Zimbabwe Justi
"""

# 3. Read specific number of lines with range using readlines method
# readlines:  This method return list of lines from target file.


def read_list_of_lines_with_range(file_path, start=0, end=1):
    with open(file_path, "r") as file:
        # readlines method return list of lines
        lines_list = file.readlines()
        #print(lines_list)
        for i in range(start, end+1):
            print(lines_list[i-1], end="")

#read_list_of_lines("read_data.txt", 4, 9)
"""
4.stand technical things in my game, and helped me understand what
5.kind of cricketer I want to be. The head coach of Zimbabwe Justi
6.n Simmons helped massively in my development, he helped in my g
7.ame against the short ball. (On the thoughts overnight) Whatâ€™s g
8.oing on between your ears is most important, and there were a
9.lot of thoughts that I had. There was so much negative after

"""
