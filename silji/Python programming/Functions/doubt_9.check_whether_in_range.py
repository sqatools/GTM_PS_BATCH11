# 9). Python function program to check whether a number is in a given range.
# Input : num = 7, range = 2 to 20
# Output: 7 is in the range


def input(num,start,end):
    if  num in range(start,end+1):
         print(f"{num} there in range")
    else:
            print(f"{num} is not in the range" )

input(7,2,20)

# def check_in_range(num, start, end):
#     if num in range(start, end + 1):
#         print(f"{num} is in the range")
#     else:
#         print(f"{num} is not in the range")
#
# check_in_range(7, 2, 20)