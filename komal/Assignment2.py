#(a-b)^2=a^2+b^2-2ab

a = 15
b = 7
lhs = (a-b)**2
print("Left hand side output:", lhs)

rhs = a**2+b**2-2*a*b
print("Right hand side output:", rhs)

print(lhs == rhs)
print(lhs, "=", rhs)
