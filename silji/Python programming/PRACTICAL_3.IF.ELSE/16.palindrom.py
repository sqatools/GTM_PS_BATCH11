# Python program to check whether any given number is a palindrome.



# num1 = 121
# num2 = str(num1)
#
# if num1 == int(num2[::-1]):
#     print("It is a palindrome number")
# else:
#     print("It is not a palindrome number")



num = 121
str1 = str(num)        # Convert number to string
str2 = str1[::-1]      # Reverse the string

if str1 == str2:
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")