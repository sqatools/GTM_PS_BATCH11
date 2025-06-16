#1). Python program to check given number is divided by 3 or not.

#digit_sum % 3 == 0

# num=12
# if num%3==0:
#     print("yes, it is")
# else:
#     print("No it is not")

num = int(input("Enter a number: "))
if num % 3 == 0:
    print("Yes, it is divisible by 3")
else:
    print("No, it is not divisible by 3")