# 5). Python program to get the Average of given numbers.
# Formula: sum of all the number/ total number
# Input:
# a = 40
# b = 50
# c = 30
# Output :
# Average = 40;
############## way1#####################
def Average(a,b,c):

    sum=a+b+c
    Total_num=3
    print(sum/ Total_num)

Average(40,50,30)

#######################way 2###############
def Average(*nums):
    total = sum(nums)
    count = len(nums)
    print(total / count)

Average(40, 50, 30, 20, 10)
