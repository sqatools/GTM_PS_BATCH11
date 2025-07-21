#                1  2  3  4  5
#                *     *  *  *      i=0
#                *     *            i=1
#                *  *  *  *  *      i=2
#                      *     *      i=3
#                *  *  *     *      i=4



for i in range(5):
    for j in range(6):
        if i==0:
            if j in [1, 3, 4, 5]:
                print("*", end=" ")
            else:
                print(" ", end =" ")
        elif i==1:
            if j in [1,3]:
              print("*", end =" ")
            else:
              print(" ", end =" ")
        elif i==2:
            if j in[1,2,3,4,5]:
                print("*", end=" ")
            else:
                print(" ",end =" ")
        elif i==3:
            if j in [3,5]:
                print("*",end=" ")
            else:
                print(" ",end =" ")
        elif i==4:
            if j in [1,2,3,5]:
                print("*", end=" ")
            else:
                print(" ",end =" ")


    print()

