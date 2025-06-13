#A = "[a,b,c]"

#list1NZXZ = []


list5 = [25, 17, [3, 5, 7], 88, 12, 'Python']


print(list5[2]) # [3, 5, 7]
print(list5[2][1]) # 5
print(list5[-1]) # Python
print(list5[-1][-4]) # h

print("-"*100)



dict1 = {'a': 123,
         34 : 56.78,
         23.33 : (5, 7, 8),
         (4, 5, 7) : [5, 88, 12],
         True : {'a': 123, 'b': 345},
         (2) : (2,3,4),
          #[1, 2, 3 ]: 'Python'} # TypeError: unhashable type: 'list'
         }
print(dict1);


set1 = {4, 5, 5.6, 'Hello', (5, 7, 8), True, None, 4, 5,}
print(set1)

"""

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
"""


"""

num = (1, 101)
prime = True
for i in range(2, 101):
    for i in range(2, i+1 ):

    if num%i == 0:
        prime = False
        break
    else:
        continue

if prime:
    print("This is prime number :", num)
else:
    print("This is not a prime number :", num)
"""

print("_"*100)


for i in range(5, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()



print("_"*50)
# infinite loop
n2 = 1
while True:
    print(n2)
    n2 += 1
    # break the loop if n2 value is equal to 100000
    if n2 == 100000:
       break  # 99999



print("__"*50)
n1 = 1
while n1 <= 10:
    print(n1)
    n1 +=1