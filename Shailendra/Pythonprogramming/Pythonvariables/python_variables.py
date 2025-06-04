"""""
1. (a-b)^2 = a^2 +b^2 - 2ab
2. (a-b)(a+b) = a^2 -b^2
"""""

a = 2
b = 4
lhs = (a-b)**2
print("LHS output : ", lhs)

rhs = a**2 + b**2 - 2*a*b
print("RHS output : ", rhs)

print(lhs == rhs)

"""
LHS output :  4
RHS output :  4
True
"""

print("_"*50)

a = 8
b = 10
lhs = (a+b) * (a-b)
print("LHS output : ", lhs)

rhs = a**2 - b**2
print("RHS output : ", rhs)
print(lhs == rhs)

"""
LHS output :  -36
RHS output :  -36
True
"""