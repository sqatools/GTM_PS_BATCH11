# Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

num=9

if num%2==0:
    print("num is divided by 2:", num**2)
elif num%3==0:
    print("num is divided by 3:",num**3)
else:
    print("none")