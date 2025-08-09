# for i in range(1, 4): # i = 1, 2
#     print("address :", i)
#     for j in range(1, 4): # j = 1, 2, 3
#         print("Package :", j)
#         for k in range(1, 3):
#             print("Item :", k)

#############################################################

# for i in range(1, 6):
#     for j in range(2, i+1):
#         print("*", end=" ")
#     print()
################################

# for i in range(1, 6): # i = 1, 2, 3, 4, 5
#     for j in range(6, i, -1): # j = (6, 1)
#         print("*", end=" ")
#     print()

# for i in range(1, 6):             # i = 1, 2, 3, 4, 5
#     for j in range(5, i, -1):     # j = (5, i)
#         print("*", end=" ")
#     print()

for i in range(6, 1, -1):
    for j in range(1, i, 1): # j = (1, 6)
        print(j, end=" ")
    print()