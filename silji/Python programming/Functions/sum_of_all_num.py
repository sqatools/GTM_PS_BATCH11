# sum of all the numbers in a list
#
# def num(a,b,c):
#     print(a+b+c)
#
# num(5,2,1)

def total(list1):
    t = 0
    for val in list1:
        t =t+ val
    print("Sum of given list: ",t)

l = [1,2,3]
total(l)