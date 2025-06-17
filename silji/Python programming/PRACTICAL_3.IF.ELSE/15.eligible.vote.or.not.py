# Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible


age=int(input("Enter age:"))

if age>=18:
    print(" eligible")
else:
    print("not eligible")