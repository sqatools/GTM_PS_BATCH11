
# Q3 : Write a python function to check given string in palindrome or not, return output as True or False
def is_palindrome(s):

    return s == s[::-1]


print(is_palindrome("malayalam"))
print(is_palindrome("happy"))



