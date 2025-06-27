#Addition
a = 5
b = 2
print("addition of a+b=", a+b)

#substrction
num1 = 20
num2 = 10
print("Substraction num1 - num2 = ", num1-num2)

#Multiplication
num1 = 25
num2 = 2
print("Multiplication num1 * num2 = ", num1*num2)

#Div
num1 = 25
num2 = 5
print("Div num1 / num2 = ", num1/num2)

#Repeate string 5 times
A= "Mahesh"
print("Reapete String 5times=", A*5)

#Average numbers
a = 10
b = 20
c = 30
d = 40
print("avrage of four numbers =",(a+b+c+d)/2)

#meddian value
values = [10, 20, 30, 40, 50]
values.sort()
n = len(values)
if n % 2 == 1:
    median_value = values[n // 2]
else:
    median_value = (values[n // 2 - 1] + values[n // 2]) / 2
print(f"The median is: {median_value}")

#print squre of number

n = 3
print("Squre of 3 =", n**2)
print("qube of 3 = ", n**3)

#print interchange values of variables
a = 5
b = 10
a, b = b, a
print("value of a =",a)
print("value of b = ", b)

print("-"*50,)
#################################

a = 8
b = 6

lhs = (a+b)**2
print("lhs", lhs)

rhs = a**2 + b**2 - 2*a*b
print("rhs",rhs)
print(lhs == rhs)

print("-"*50)

c = 5
d = 10

lhs = (a-b)* (a+b)
print("lhs",lhs)
rhs = a**2 - b**2
print("rhs",rhs)
print(lhs==rhs)

print("-"*50)
"""
"""""
*       * * * * *
*       *
*       *
* * * * * * * * *
        *       *
        *       *
* * * * *       *


for i in range (7):
    for j in range (9):
        if i in [0,1,2,3,6]:
            print("*", end=" ")
        elif j in [0,4,5,6,7,8]:
            print("*", end=" ")


    print()
"""
item_list = ['Apple', 'Mango', 'Banana', 'Lichi']
inventory_list = [200, 150, 500, 300]
price_list = [100, 250, 50, 80]
purchase_list = [10, 5, 10, 20]
total_bill = 0

#up_inventory_list = [180, 145, 490, 280]



for i in range (len(item_list)):
    item = item_list[i]
    available_stock = inventory_list[i]
    price = price_list
"""