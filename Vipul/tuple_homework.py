# Home work:
# 1.  write a python program to max value from tuple.
# 2.  write a python program to remove duplicate values from tuple
# 3.  write a python program to get second max value from tuple.

# 1.  write a python program to max value from tuple.
t = (40, 6, 22, 78, 101, 52, 86, 46, 17, 9)
max = 0
for i in t:
    if i > max:
        max = i

print(max)

# 2.  write a python program to remove duplicate values from tuple
t = (40, 86, 9, 22, 78, 17, 52, 86, 46, 17, 9)
t1 = tuple(set(t))
print(t1)

# 3.  write a python program to get second max value from tuple.
t = (40, 6, 22, 78, 101, 52, 96, 46, 17, 9)
max = 0
sec_max = 0
third_max = 0

for i in t:
    if i > max:
        max = i
    elif i > sec_max and i < max:
        sec_max = i
    elif i > third_max and  i < sec_max and i < max and sec_max > third_max:
        third_max = i
print("max",max)
print("sec_max", sec_max)
print("third_max", third_max)
