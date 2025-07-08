# * * *
# * * * * * *
# * * * *
# * * * *
# * * * * * *
# * * * * * *
# * * * *
# * * * *
# * * * *

for i in range(9):
    for j in range(1,7):
        if i==0:
            if j in [1,2,3]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        elif i in [1,4,5]:
            if j in [1,2,3,4,5,6]:
                print("*", end=" ")
        elif  i in [2,3,6,7,8]:
            if j in [1,2,3,4]:
                print("*", end =" ")
            else:
                print(" " ,end=" ")



    print()