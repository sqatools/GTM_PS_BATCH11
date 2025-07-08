# Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Output :
# Number of even numbers: 4
# Number of odd numbers: 5

numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9)

even=0
odd=0

for val in numbers:
    if val%2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)