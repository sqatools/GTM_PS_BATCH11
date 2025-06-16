#Python program to check a given number is part of the Fibonacci series from 1 to 10.

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num = int(input("Enter a number: "))

if num in fib:

    print("It is a part of the series :", num)
else:

    print("It is not a part of the series :", num)

