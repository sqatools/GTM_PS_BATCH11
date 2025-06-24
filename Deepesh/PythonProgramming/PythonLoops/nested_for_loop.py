# each address deliver three packages
"""
# outer loop
for i in range(1, 5): # i =1
    print("address :", i)
    # inner loop
    for j in range(1, 4):
        print("item :", j)
    print("_"*50)
"""
#
# # each address deliver increamentals number of packages
# # outer loop
# for i in range(1, 5): # i =1
#     print("address :", i)
#     # inner loop
#     for j in range(1, i+1):
#         print("item :", j)
#     print("_"*50)



"""
*
* *
* * *
* * * *
* * * * *

* * * * *
* * * * 
* * * 
* * 
*
        *
      * *
    * * *
  * * * *
* * * * *
"""

for i in range(1, 6): # i =1
    for j in range(1, i+1):
        print("*", end=" ")
    print()



for i in range(6, 0, -1): # i =1
    for j in range(1, i+1):
        print("*", end=" ")
    print()


print("_"*50)
"""
        * i= 0
      * * i =1
    * * * i =2
  * * * * i =3
* * * * * i =4
"""

for i in range(5):
    for j in range(5):
        if i == 0:
            if j == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 1:
            if j in [3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i == 2:
            if j in [2, 3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        elif i == 3:
            if j in [1, 2, 3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        elif i == 4:
            if j in [0, 1, 2, 3, 4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            print("*", end=" ")

    print()

