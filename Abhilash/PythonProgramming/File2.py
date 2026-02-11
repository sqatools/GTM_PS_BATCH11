# import keyword
# print(keyword.kwlist)

""" ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del','elif', 'else','except', 'finally', 'for', 'from', 'global',
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
 'raise', 'return', 'try', 'while', 'with', 'yield'] """

str1 = "Hello we are learning python"
output = { Text: len(Text) for Text in str1.split() if len(Text) >=5}
print(output)



print("-"*40)

keys = ["Ho", "we", "ae", "Lg", "Py"]
words = ["Hello", "we", "are", "Learning", "Python"]

output2 = {}

for i in range(len(keys)):
    word = words[i]
    new_word = ""
    for char in word:
        new_word += char * 2
    output2[keys[i]] = new_word

print(output2)

print("-"*50)
####  write a python program to remove duplicate from list.

list1 = [54, 8, 12, 5, 7, 23, 67, 5, 8, 7]

unique_list = []
for i in list1:
    if i not in unique_list:
        unique_list.append(i)

print("Unique values :", unique_list)

print("-"*50)

# write a python program to add all multiple repeated values.
# list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4, ]
# output = [10, 16, 12, 8, 4, 3]

list2 = [5, 4, 6, 8, 2, 4, 6, 2, 5, 3, 4, 4]

result = []  # Final output
checked = [] # Mark  numbers already processed

for i in list2:
    if i not in checked: # if the number has already been processed
        total = list2.count(i) * i
        result.append(total)
        checked.append(i)

print("Add all multiple repeated values:", result)

print('-'*50)

list3 = [[3, 4, 5, 3], [1, 3, 4, 1], [5, 7, 12, 7]]
output3 = []

for sub in list3:
    new_sub = []
    temp = []
    for i in sub:
        if i not in temp:
            total = sub.count(i) * i
            new_sub.append(total)
            temp.append(i)
    output3.append(new_sub)

print("Output:", output3)

print('-'*50)

def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

read_file(r"C:\PythonAutomation\AutomationRepo\First_git_file.txt")

print('_'*50)



import os

print("current directory: ", os.getcwd())

#os.system("control")

#os.system("dir C:\\")

os.system("Notepad.exe")

