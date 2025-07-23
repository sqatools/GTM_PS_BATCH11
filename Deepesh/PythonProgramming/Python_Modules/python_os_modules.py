import os
import shutil
import sys

# get current working directory
print("current directory :", os.getcwd())
# current directory : E:\Trainings\GTM_PS_Batch11_26May25\GTM_PS_BATCH11\Deepesh\PythonProgramming\Python_Modules


########### create directory in local folder #############
#os.mkdir('folder1')


################ remove folder #####################
#os.rmdir("folder1") # remove folder from current location

#############create folder tree ############
#os.makedirs(r"E:\Filesdata\batch11\f1\f2\f3\f4\f5")

############# remove folder tree ############
#os.removedirs(r"E:\Filesdata\batch11\f1\f2\f3\f4\f5")


########### get list of all files and folder #########
data_list = os.listdir(r"E:\Filesdata")
print("totals files/folder :", len(data_list))
for val in data_list:
    print(val)

print("_"*50)
################ os.path operation ############
dest_path = r"E:\Filesdata"
file_name = "count_name.txt"

file_path = os.path.join(dest_path, file_name)
print("filepath :", file_path)
# filepath : E:\Filesdata\count_name.txt

#### check given path is exist or not ####

file1 = r"E:\Filesdata\count_name.txt"
file2 = r"E:\Filesdata\count_name_new.txt"
folder_path = r"E:\Filesdata\batch11"

print("check file1 exist  :", os.path.exists(file1)) # True
print("check file2 exist  :", os.path.exists(file2)) # False

# check given path is file or folder
print("check folder path 1:", os.path.isdir(folder_path)) # True
print("check folder path 2:", os.path.isdir(file1)) # False

print("check file path :", os.path.isfile(file1)) # True


#################### execute windows command using os ################
# open control panel
#os.system("control")

# return list of files/folder
#os.system("dir C:\\")

#os.system("notepad.exe")

os.system("python hello_word.py") # True


########################## copy file from one location to another ############
src = r"E:\Filesdata\count_name.txt"
dest = r"E:\Filesdata\batch11\count_name.txt"
dest2 = r"E:\Filesdata\batch11\count_name_update.txt"
shutil.copy(src, dest)
shutil.copy(src, dest2)

print("_"*50)
############## Get platform name #############
print("platform name :", sys.platform) # win32

print("current python version :", sys.version)
# 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]