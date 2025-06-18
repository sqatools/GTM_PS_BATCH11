print("_"*50)
########## String Formatting #############
# Name = input("Please enter your name :")
# Age = int(input("Please enter your age :"))
# City = input("Please enter your city name :")
Name = "Rahul"
Age = 25
City = "Mumbai"

# 1. String concatenation
result1 = "My name is " +Name+ " and age is " +str(Age)+ " I live in"+City
print(result1)

print("_"*50)
# 2. Format Method
result2 = "My name is {} and age is {} I live in {}".format(Name, Age, City)
print(result2)

print("_"*50)
# 3. F string formatting Method

result3 = f"My name is {Name} and age is {Age} I live in {City}"
print(result3)

print("_"*50)
##########################################################
# Apply loop on string.

str1 = "Programming"
for val in str1:
    print(val, end=",,")

print()
print("_"*50)
# 1.  Loop with indexing

str2 = "Learning"
str_len = len(str2)
for i in range(str_len):
    print(i, str2[i])

print("_"*50)
######################## +ve and -ve indexing of string ###########
str_a  = "Progamming"
""" 
 0   1  2  3  4  5   6  7  8  9  # +ve
 P   r  o  g  a  m   m  i  n  g
-10 -9 -8 -7 -6 -5  -4 -3 -2 -1  # -ve
"""
print(str_a[5])
print(str_a[-6])

############################ Slicing in String ##############################
"""
Rule1 : str[start_index: last_index]
->  output string will include start_index and exclude the last index.
->  Output string will always from left to right, can not get string in reverse
->  If we dont define the start_index, then default first_index value is Zero (0)
->  If we dont define the last_index, then default last_index value is end of string
<<<<<<< HEAD
=======
->  start_index and last_index could be negative as well.
->  both +ve -ve or -ve +ve value can be included in the output.
>>>>>>> a082c4bbec2b3be11c133106bb237162eb5739fa
"""

strx = "India is a best country"
print(strx[0:4])

# default start_index is zero
print(strx[:10])

# default end_index is end of string (left to right)
print(strx[-3:])

# start_index and last_index may has +ve and -ve value combination
print(strx[1:-5])
print(strx[-15:17])

print(strx[10:0]) #Empty list (Right to left)

"""
Rule2 : str[start_index: last_index: step_value]
-> output string will include start_index and exclude last_index value.
-> start_index and end_index could be +ve or -ve
-> default start_index value is zero (0) if step value is +ve.
-> default start_index value is -1 if step value is -ve
-> default last_index value is end of the string if step_value is +ve
-> default last_index value is start of the string if step_value is -ve

"""

stry = "We Are Learning Python"

print(stry[3:15:1])
print(stry[2:16:2])

# default start_index value is zero (0) if step_value is +ve.
print(stry[:10:1])

# default start_index value is -1 if step value is -ve
print(stry[:15:-1]) # nohtyP
print(stry[:-16:-1]) # nohtyP gninraeL
print(stry[:10:-2]) # nhy nn
print(stry[:-20:-2]) # nhy nnaLeA

# default last_index value is end of the string if step_value is +ve
strz = "We Are Learning Python"
print(strz[3::1])

# default last_index value is start of the string if step_value is -ve
print(strz[-5::-1]) #yP gninraeL erA eW

print(strz[::1])
print(strz[::-1])

#Question = print Python to Pytnoh

w1 = strz[16:]
print(w1) #Python
w1p1 = w1[0:3:1]
w1p2 = w1[-1:-4:-1]
print(f"{w1p1}{w1p2}")



"""
Slicing Home Work
"""
"""
str1 = Virat is Great India Batsman
# repeat first and last character three times
op1 = VVVirat is Great India Batsmannn
"""

strhm1 = "Virat is Great India Batsman"
first_char = strhm1[0]
last_char = strhm1[-1]

print(first_char * 3 + strhm1[1:-1] + last_char * 3)


# repeat first and last character 2 times of each word.
# op2 = VViratt iiss GGreatt IIndiaa BBatsmann

strhm2 = "Virat is Great India Batsman"
first_char1 = strhm2[0:1]
first_char2 = strhm2[4:5]
second_char1 = strhm2[6:8]
third_char1 = strhm2[9:10]
fourth_char1 = strhm2[13:14]
fifth_char1 = strhm2[15:16]
sixth_char1 = strhm2[19:20]
seventh_char1 = strhm2[21:22]
Eight_char1 = strhm2[27:28]

print(first_char,first_char2,second_char1,third_char1,fourth_char1,fifth_char1,sixth_char1,seventh_char1,Eight_char1)

print(first_char1 * 2 + strhm2[1:4] +  first_char2 * 2 + " " + second_char1 * 2 + " " + third_char1 * 2 + strhm2 [10:13] + fourth_char1 * 2 +
     " " + fifth_char1 * 2 + strhm2[16:19] + sixth_char1 * 2 + " " + seventh_char1 * 2 + strhm2[22:27] + Eight_char1 * 2)



# replace first and last character each word from given string
# op3 = tiraV si treaG andiI natsmaB
second_char2 = strhm2[-21:-23:-1]
print(second_char2)

print(first_char2 + strhm2[1:4] +  first_char1 + " " + second_char2 + " " + fourth_char1 + strhm2 [10:13] + third_char1 +
     " " + sixth_char1 + strhm2[16:19] + fifth_char1 + " " + Eight_char1 + strhm2[22:27] + seventh_char1)



# repeat each vowels 2 times in given string
# op4 = Viiraat iis Greeaat IIndiiaa Baatsmaan

strhm3 = "Virat is Great India Batsman"
vowels = "AEIOUaeiou"

result=""
for ch in strhm3:
    if ch in vowels:
        result += ch * 2
    else:
        result += ch

print(result)


print("_" * 50)
############################ String Methods ##############################

#print(dir(str))

"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

"""

# upper() and lower() : This method convert str1 into upper case and lower cases
str_md = "Hi my self rahul deo and i am working as senior QA"
print("Upper case:", str_md.upper())

print("_" * 50)
str_md1 = "HI I HOPE YOU ARE DOING WELL"
print("Lower case:", str_md1.lower())

print("_" * 50)
############################
# isupper() and islower() :  These method check the given string is in upper or in lower case, it will return boolean output.
str_md2 = "CHECK THIS IS IN UPPER CASE OR NOT"
print("Is this in uppercase:", str_md2.isupper())

str_md3 = "check this is in lower case or noT"
print("Is this in lowercase:", str_md3.islower())

print("_" * 50)
############################
# swapcase method : This method convert lower case char to upper case and upper case characters to lower case.
str_md4 = "CONVERSION of the letter wiTH SHOWcase"
print("swap the letters:", str_md4.swapcase())

print("_" * 50)
############################
# capitalize method : This method change only first letter of string into upper and remaining into lower case
str_md5 = "i WILL CAPItaliZE this SENtense"
print("Capitalize the sentense:", str_md5.capitalize())

print("_" * 50)
############################
# title() method : This method convert first letter of each word into capital case and rest into small
str_md6 = "This method conveRT fIRST letter in to caps"
print("Caps the first letter of each word:", str_md6.title())

print("_" * 50)
############################
# istitle() method : This method check the given string follow the rules of title case method.
str_md7 = "This method conveRT fIRST letter in to caps"
print("Check istitle:", str_md7.istitle())

print("_" * 50)
############################
# count() method : count method return the number of occurrences of char/substring in given string.
str_md8 = "occurrence of the char"
print("count of r:", str_md8.count("r"))

print("_" * 50)
# write a python to print the count of each character without repeatation.
str9 = "Lets print the count of each character without repeatation of letter"
temp=""
for char in str9:
    if char not in temp:
        print(char , ":" , str9.count(char))
        temp = temp + char
    else:
        continue


print("_" * 50)
# write a python program to check the given 2 string are anagram or not
str10 = "Hello"
str11 = "lpoeh"

anagram = True
if len(str10) != len(str11):
    anagram = False
for char in str10:
    if str11.count(char) == str10.count(char):
        continue
    else:
        anagram = False

if anagram:
    print("These are anagram strings:", str10,str11)
else:
    print("These are not anagram strings:", str10,str11)


print("_" * 50)
#################### second solution ######################
str12 = "pythoncode"
str13 = "cdeothpnyo"
# sorted function :  This function sort the string in alphabetical order and return as list of characters.
V1 = sorted(str12)
V2 = sorted(str13)
print(V1, V2)

if V1 == V2:
    print("This is anagram")

else:
    print("This is not anagram")


print("_"*50)
########################################################################
# Q3 :  write a python program to get most simuntaneounly repeated character




print("_"*50)
########################################################################
# Q3 :  write a python program to get count of each character from given without using count method.

str14 = "Pythonprogram"
result = {}

for char in str14:
    print(result)
    if char not in result:
        result[char] = 1
    else:
        result[char] += 1

print("output:", result)




