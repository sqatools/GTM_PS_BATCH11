#   * * *     # i = 0
# *       *   # i = 1
# *       *   # i = 2
# *       *   # i = 3
# *       *   # i = 4
# *       *   # i = 5
#   * * *     # i = 6
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



