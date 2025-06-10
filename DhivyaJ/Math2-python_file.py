a = 6
b = 4
lsh = (a-b)*(a+b)
print("lsh output:",lsh)
rhs = a**2 - b**2
print("rhs output:",rhs)
print(lsh==rhs)

num1 = 121
num2 = str(num1)
if num1 == int(num2[::-1]):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")