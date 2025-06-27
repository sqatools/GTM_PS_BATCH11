n = 53
f = 0
for i in range(2, n+1):
    if n % i == 0:
        f += 1

if f == 1:
    print("prime")
else:
    pass

print("*"*100)
for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

print("*"*100)
# solve below pattern program with the help of nested loop
"""
*         # i =1
* *       # i =2
* * *     # i =3
* * * *   # i =4
* * * * * # i =5
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()


print("*"*100)
# pyramid with numbers
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

for i in range(1, 6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print("*"*100)
# pyramid with numbers
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

for i in range(1, 6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

print("*"*100)
# pattern with stars
"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range(1, 6):
    for j in range(6, i, -1):
        print("*", end=" ")
    print()


print("*"*100)
for i in range(5, 0, -1):
        print("* "*i)

print("*"*100)
for i in range(6, 1, -1):
    for j in range(1, i, 1): # j = (1, 6)
        print(j, end=" ")
    print()

