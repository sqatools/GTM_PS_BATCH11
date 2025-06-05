#(a-b)(a+b)=a^2-b^2
a = 15
b = 8
lhs = (a-b)*(a+b)
print("Left hand side output:", lhs)

rhs = a**2-b**2
print("Right hand side output:", rhs)

print(lhs == rhs)
print(lhs, "=", rhs)
