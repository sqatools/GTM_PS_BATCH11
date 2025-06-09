#  Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a=2
b=3
lhs = (a + b)**3
print("lhs output :", lhs)

rhs = a**3 + b**3 + 3*a*b*(a+b)
print("rhs output :", rhs)

print(lhs == rhs)

