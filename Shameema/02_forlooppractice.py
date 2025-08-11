
class Custom_exception(Exception):

   def __init__(self):
        print("Wer are calling custom exception class")
        # super().__init__()

# class ABC:
   def print_number(self):
         for i in range(1, 11):
            if i == 5:
                pass
                # raise Custom_exception()
                # continue
            print(i)

obj1 = Custom_exception()
# obj1.print_number()

class Loop_learning:
#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).
# Input1:1500
# Input2:2700
# print("The numbers divisible both by 5 and 7 are:")
# for i in range (1500,2701):
#    if i%7==0 and i%5==0:
#         print(i)

  def __init__(self):
      print("Learning loops")

  def art(self):
      print("Hey this works")

  @classmethod
  def clos(cls):
      print("Hey its class method")
  # question 07/24: what if there is error in print statment?
# when to use what type of exceptions - like : valueerror, exception?
  @staticmethod
  def numloop():
      try:
           temp = 0
           for i in range (1500,2701):
              if i%5 ==0 and i%7 ==0:
                 print(i, end=",")
                 temp += 1
                 if temp == 10:
                      print()
                      temp = 0
  #     print()
      except Exception as y:
        print(y)
        print(" Please check the values")
Loop_learning()
Loop_learning.clos()
# obj =loop_learning()
# loop_learning.art(obj)
Loop_learning.numloop()


# loop_learning.num_loop(obj)
# loop_learning
# obj.numloop()

# 2). Python Loops program to construct the following pattern, using a nested for loops.
# Output :

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
print()
n =6
for i in range (1,6):
    print(i, i*'* ')

for i in range(6):
    print(i, i * '* ')

word = "Logic"

for i in word:
    print (i,end = "")
print()
print(len(word))

for i in word:
    z = word.index(i)
    print(i,z)

try:
    y = word.index("q")
    print(y)
except ValueError:
    print("Substring not found")
x = word.find("q")
print(x)

# 3). Python Loops program that will add the word from the user to the empty string using

str1 = "Python Programming"
str_new = ""

for i in str1:
    # str_new +=i
    ind = str1.index(i)
    print(ind,i)

# print(str_new)
#
print(len(str1))

for i in range(len(str1)):
    stro = str1[i]
    print (i,stro)
print("-"*50)
str_given = "I LOVE INDIA"
str_new1 = ""
print( )
print("-"*50)
for i in str_given:
    print(i)
    str_new1 += str1
print(str_new1,end=" ")
# Question2 07/23: why is the "Python Programming" printed as per the length of str_given?

# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python
# Question1 07/23: is the series here is considered as tuple?

print("_"*50)
Input = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0

for i in Input:
    if i%2 == 0:
        even +=1
    else:
        odd +=1

print("Number of even numbers:",even)
print("Number of odd numbers:",odd)

# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

for i in range(6):
    if i != 0 or i !=6:
      print(i,end = " ")
print()
print ("-"*50)
# 6). Write a program to get the Fibonacci series between 0 to 20 using python.

num1 = 0
num2 = 1
count = 0


while count <20:
    print(num1,end=" ")
    n = num1+num2
    num1 = num2
    num2 = n

    count +=1


# 7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz”
print()
for i in range (1,31):
    if i%3 ==0:
        print(i, "Fizz")
    elif i%5 ==0:
        print(i,"Buzz")
    elif i%3 == 0 and i%5 ==0:

        print(i,"FizzBuzz")

# 8). Write a program that accepts a word from the user and converts all uppercases in the word
# to lowercase using python.
word1 = "SqaTools"
low_word1 = word1.lower()
print(low_word1)

# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.

input ="python1234"
lett = 0
dig = 0
for i in input:
    if i.isnumeric():
        dig +=1
    if i.isalpha():
        lett +=1
print(dig)
print(lett)

print("_"*50)
# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
# Need to practice
for i in range (7):
    # print(i)
    for j in range(5):
        if (i==0 or i ==6) and (0<j<4):
            print("*",end =" ")
        elif(0< i < 7) and (0<j< 5):
            print("*",end=" ")
        else:
            print(" ",end =" ")
print()

# 11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.

n = 10
count = 1
while count<=10:
    print(count, end = " ")
    count +=1
print ()
# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

n = 12
count = n
while count != 0:
    print(count,end=" ")
    count -= 1
print ( )
# 13). Python Loops program to print all alphabets from a to z using for loop

# Take chr method help to print characters with ASCII values

import string

for letter in string.ascii_lowercase:
    print(letter,end = " ")
print()

for letter in string.ascii_uppercase:
    print(letter, end = " ")
print()
# question 07/24: how to print this with space?

ul = string.ascii_uppercase
for i in range(-1, -len(ul)-1,  -1):
    print(ul[i], end=" ")
#print(ul[::-1])

print()
# why even using end = " " space is not seen
ul = string.ascii_uppercase
print("test value:", ul[::-1],end ="     ")
print( )
# while reversing should we use "join?"
ul = string.ascii_uppercase
spaced = " ".join(ul)
# for i in range(len(ul)):
print(spaced[::-1])


# question 07/24: how to print this with space?
print( )

# ul1 = string.ascii_uppercase
# print("ul1:", ul1)
# rev = len(ul)
# print("length:",rev)
# for i in range(rev,0,-1):
#     print(i)
#     # letter = ul1[i]
#     # print(letter,end =" ")