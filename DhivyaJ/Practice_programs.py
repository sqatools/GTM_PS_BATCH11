# Print a string n number of times
str = "test"
n = 10
print("Result", str*n)


# check if pass or fail

mark = int(input("Enter marks:"))
if mark < 40:
   print("Fail")
elif mark >40 and mark <= 100:
   print("Pass")
else:
   print("invalid")

print("_"*50)
# Find number with index
tup = (34, 45, 56, 67, 78, 89, 91, 23, 45, 34, 44, 68)
print("Number in tuple with index 5:", tup[5])


print("_"*50)
#create dic from string

str1 = "TesTing python"
dic = {}

for char in str1:
   dic[char] = str1.count(char)

print(dic)


print("_"*50)

# concatenate two dic
dict1 = {'name':'dj','place':'chn'}
dict2 = {'job':'prt','status':'married'}
dict1.update(dict2)
print(dict1)

