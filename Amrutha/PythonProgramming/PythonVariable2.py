"""
# program to solve:
1. (a+b)^2 = a^2 + b^2 + 2ab
2. (a-b)^2 = a^2 + b^2 - 2ab
3. (a+b)(a-b) = a^2 - b^2
"""
print("-"*50) # types hyphen 50 times
# 1. (a+b)^2 = a^2 + b^2 + 2ab
a = 5
b = 4
lhs = (a+b)**2
print('LHS output: ', lhs)
rhs = a**2 + b**2 + 2*a*b
print('RHS output: ', rhs)
print('LHS = RHS is ', lhs==rhs)
################################################################################
print("-"*50) # types hyphen 50 times
# 2. (a-b)^2 = a^2 + b^2 - 2ab
a = 3
b = 1
lhs1 = (a-b)**2
print('LHS output: ', lhs1)
rhs1 = a**2 + b**2 - 2*a*b
print('RHS output: ', rhs1)
print('LHS = RHS is ', lhs1==rhs1)
#############################################################################
print("-"*50) # types hyphen 50 times
# 3. (a+b)(a-b) = a^2 - b^2
a = 2
b = 3
lhs2 = (a+b)*(a-b)
print('LHS output: ', lhs2)
rhs2 = a**2 - b**2
print('RHS output: ', rhs2)
print('LHS = RHS is ', lhs2==rhs2)


