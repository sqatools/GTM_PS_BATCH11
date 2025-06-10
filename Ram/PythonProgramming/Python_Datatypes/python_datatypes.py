### INTEGER ####

int1 = 40
print(int1, type(int1))   # int1 -- 40 <class 'int'>
int2 = -100
int3 = 3524236487958697585684
print(int2, type(int2))  # int2 -- -100 <class 'int'>
print(int3, type(int3))  # int3 -- 3524236487958697585684 <class 'int'>

print("_"*80)
### FLOAT ###

a1 = 25.5
a2 = -30.33
a3 = 5564343.65465
print(a1, type(a1))  #  25.5 <class 'float'>
print(a2, type(a2))  # -30.33 <class 'float'>
print(a3, type(a3))  # 5564343.65465 <class 'float'>

print("_"*80)
### Complex Number ###
"""
Properties of complex number
->  complex number is immutable data type
->  complex number is combination of real and imaginary value
    x+yj
    x = read number
    y = imaginary number

-> complex can contains positive and negative values.
"""

c1 = 5 + 8j
c2 = 0 - 15j
c3 = -20 + 6j
print(c1, type(c1))  # (5+8j) <class 'complex'>
print(c2, type(c2))  # -15j <class 'complex'>

print("Real Value:", c1.real)       # Real Value: 5.0
print("Imaginary Value:", c1.imag)  # Imaginary Value: 8.0


print("_"*80)

