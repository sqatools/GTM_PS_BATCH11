"""
  * * *     # i = 0
*       *   # i = 1
*       *   # i = 2
*       *   # i = 3
*       *   # i = 4
*       *   # i = 5
  * * *     # i = 6
"""

for i in range(7):
    for j in range(1, 6):
        if i in [0, 6]:
            if j in [1, 5]:
                print(" ", end= " ")
            else:
                print("*", end= " ")
        elif i in [1, 2, 3, 4, 5]:
            if j in [1, 5]:
                print("*", end= " ")
            else:
                print(" ", end= " ")


    print()


print("_"*50)
# Program to print the T pattern with for loop
"""
* * * * * *   # i = 0
* * * * * *   # i = 1
    * *       # i = 2
    * *       # i = 3
    * *       # i = 4
    * *       # i = 5
* * * * * *   # i = 6
* * * * * *   # i = 7
"""

for i in range(8):
    for j in range(6):
        if i in [0, 1, 6, 7]:
           print("*", end=" ")
        elif i in [2, 3, 4, 5]:
            if j in [2, 3]:
                print("*", end=" ")
            else:
                print(" ", end=" ")

    print()




# str1 = "Mahesh"
# for i in range(len(str1)):
#     print(str1[i], end=" ")

# Home work
# design a swastik pattern program with the help of nested for loop

"""

*   * * * 
*   *
* * * * *  
    *   * 
* * *   *

"""
