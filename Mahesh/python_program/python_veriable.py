
# 1. (a+b)^2 = a^2 + b^2 + 2ab
a = 5
b = 6
lhs = (a+b)**2
print("lhs output :", lhs)

rhs = a**2 + b**2 + 2*a*b
print("rhs output :", rhs)

print(lhs == rhs) # True

#(a-b)^2 = a^2 +b^2 - 2ab
a = 5
b = 20
lhs = (a-b)**2
print("lhs out :", lhs)

rhs = a**2 + b**2 - 2*a*b
print("rhs output :", rhs)

print(lhs == rhs)

#(a-b)(a+b) = a^2 -b^2

a = 10
b = 5

lhs = (a-b)*(a+b)
print("lhs output :", lhs)

rsh = a**2 - b**2
print("rhs output :", rsh)

print(lhs == rsh)

print("-"*50)
for i in range(5, 11):
    for j in range(5, i-1):
        print("*", end=" ")
    print()

print("-"*50)
m =5
for i in range(m, 0, -1):
    print("* " * i)

print("%"*50)
for i in range(5, 11):
    for j in range(5, i-1):
        print("*", end=" ")
    print()