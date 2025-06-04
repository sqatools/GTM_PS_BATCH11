# program to solve below equations
# 1. (a+b)^2 = a^2 + b^2 + 2ab
# 2. (a-b)^2 = a^2 +b^2 - 2ab
# 3. (a-b)(a+b) = a^2 -b^2


print("_"*50)
# 1. (a+b)^2 = a^2 + b^2 + 2ab

a = 5
b = 6
lhs = (a+b)**2
print("lhs output :", lhs)

rhs = a**2 + b**2 + 2*a*b
print("rhs output :", rhs)

print(lhs == rhs) # True


#2. (a-b)^2 = a^2 +b^2 - 2ab

a = 10
b = 20
lhs = (a-b)**2
print("lhs output :", lhs)

rhs = a**2 + b**2 - 2*a*b
print("rhs output :", rhs)

print(lhs == rhs)

## 3. (a-b)(a+b) = a^2 -b^2

a = 5
b = 2
lhs = (a-b)*(a+b)
print("lhs output :", lhs)

rhs = a**2 - b**2
print("rhs output :", rhs)

print(lhs == rhs)