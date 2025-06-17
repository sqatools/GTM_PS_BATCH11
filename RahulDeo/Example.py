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
