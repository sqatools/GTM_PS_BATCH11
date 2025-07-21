# * * * * * *   # i = 0
# * * * * * *   # i = 1
#     * *       # i = 2
#     * *       # i = 3
#     * *       # i = 4
#     * *       # i = 5
# * * * * * *   # i = 6
# * * * * * *   # i = 7


for i in range(8):
    for j in range(1,7):
        if i in [0,1,6,7]:

          print("*", end =" ")

        elif i in [2,3,4,5]:
            if j in [3,4]:
               print("*", end =" ")
            else:
                 print(" ", end =" ")
    print()


