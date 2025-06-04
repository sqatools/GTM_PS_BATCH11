a = 10
b = 10
# a = Variabale
# = assigment operator
# 10 : data value

print(a, id(a))
print(b, id(b))

# if multiple variable are holding same value, then their address is also same.

# assign same value to multiple variable at a time.

p = q = r = 40
print("Value of p :", p)
print("Value of q :", q)
print("Value of r :", r)

print ("-"*50)
a = 22
b = 12
LHS = (a-b)**2
print("LHS output :",LHS)

RHS = a**2 + b**2 - 2*a*b
print("RHS output :", RHS)

print(LHS == RHS)

print ("-"*50)

a = 11
b = 12

LHS = (a-b)*(a-b)

print("LHS output :", LHS)

RHS = a**2 - b**2
print("RHS output :", RHS)
