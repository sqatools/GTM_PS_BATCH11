#Q1 write a python program to read two files data and add it to 3rd file.

def read_different_files(f1, f2, f3):
    # read data from file1
    with open(f1, "r") as file1:
        data1= file1.read()

     # read data from file2
    with open(f2, "r") as file2:
        data2 = file2.read()

    #  append data to file3
    with open(f3, "a") as file3:
        file3.write(data1)
        file3.write(data2)


#read_different_files("test_file1.txt", "test_file2.txt", "test_file3.txt")


#Q2 write a python program to read two files data and add it to 3rd file with alternate line of each file.


def read_different_files_add_alternate_lines(f1, f2, f3):
    # read data from file1
    with open(f1, "r") as file1:
        data1_lines= file1.readlines()

     # read data from file2
    with open(f2, "r") as file2:
        data2_lines  = file2.readlines()

    #  append data to file3
    with open(f3, "a") as file3:
        for i in range(len(data1_lines)):
            file3.write(data1_lines[i])
            file3.write(data2_lines[i])

read_different_files_add_alternate_lines("test_file1.txt", "test_file2.txt", "test_file4.txt")
