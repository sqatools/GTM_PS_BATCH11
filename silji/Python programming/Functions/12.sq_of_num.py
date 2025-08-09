# Python function program to create and print a list where the values are squares of numbers between 1 to 10.
# Input: 1 to 10
# Output: 1, 4, 9, 16, 25, 36, 49, 64, 81

def val(list):
    for i in range(1,10):
        i=i**2
        print(i)

list=[1,2,3,4,5,6,7,8,9,10]
val(list)