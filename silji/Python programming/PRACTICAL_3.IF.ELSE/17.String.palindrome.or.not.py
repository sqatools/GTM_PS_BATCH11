# Python program to check if any given string is palindrome or not.

str1 = 'jaj'
str2 = str1[::-1]

if str1 == str2:
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")