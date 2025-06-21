# print("First Program")


for i in range (6):
    for j in range (5):
        if i == 0:
           if j == 1:
               print(" ", end="")
           else:
               print("*", end="")
        elif i == 1:
           if j in [1,3,4]:
             print(" ", end="")
           else:
             print("*", end="")
        elif i == 2:
           if j in [0,1,2,3,4]:
             print("*", end=" ")
        elif i == 3:
           if j in [2,4]:
             print("*", end="")
           else:
               print(" ", end="")
        elif i ==4:
           if j == 3:
               print(" ", end="")
           else:
               print("*", end="")
