# print the numbers from 1 to 10 using while loop
n1 = 1
while n1 <= 10:
    print(n1)
    n1 +=1

"""
 1
2
3
4
5
6
7
8
9
10 
"""

"""
print("_"*50)
# infinite loop
n2 = 1
while True:
    print(n2)
    n2 += 1
    # break the loop if n2 value is equal to 100000
    if n2 == 100000:
        break  # 99999

"""

"""
while True:
    print("_"*50)
    # write a program to take inputs user and perform math operation as per user input
    operation = int(input("1.  Addition :\n"
                    "2.  Subtraction: \n"
                    "3.  Division:   \n"
                    "4.  Multiplication:"))

    v1 = int(input("Please enter first value:"))
    v2 = int(input("Please enter second value:"))
    if operation == 1:
        print("addition :", v1+v2)
    elif operation == 2:
        print("Subtraction :", v1-v2)
    elif operation == 3:
        print("Division :", v1/v2)
    elif operation == 4:
        print("Multiplication :", v1*v2)
    else:
        print("---- Application Stopped ---")


"""

print("_"*50)
##############################################
# program to reverse the number with help while loop

#num = 123
#output = 321
# num = 54678239 # 93287645
reverse = 0

while num > 0: # 12 > 0 | 1 > 0 | 0> 0
    temp = num%10 # 3, 2, 1
    reverse = reverse*10 + temp # 0*10 + 3 = 3 | 3*10 + 2 = 32 | 32*10 + 1 = 321
    num = num//10 # 12, 1, 0

print("reverse value :", reverse)

