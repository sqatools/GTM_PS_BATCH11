#Python program to check given number is a prime number or not.

# count = 0
# # Iterate over numbers
# for i in range(2,num):
# # Check for division
#     if num%i == 0:
#  #    Add 1 to the count variable
#         count += 1
# # Check for prime number
# if count > 0:
#  Print output
#     print("It is not a prime number")
# else:
# #Print output
#     print("It is a prime number")

# num = 15
# # prime = True
# for i in range(2, num): # i =2, 3, 4
#     print(i) # 2
#     if num%i == 0: # 13%4 == 0
#         # prime = False
#         break
#     else:
#         continue
#
# if True:
#     print("This is prime number :", num)
# else:
#     print("This is not a prime number :", num)
num =  int(input("Enter a number: "))
count = 0
# Iterate over numbers
for i in range(2,num):
# Check for division
    if num%i == 0:
    # Add 1 to the count variable
        count += 1
# Check for prime number
if count > 0:
# Print output
    print("It is not a prime number")
else:
#Print output
    print("It is a prime number")