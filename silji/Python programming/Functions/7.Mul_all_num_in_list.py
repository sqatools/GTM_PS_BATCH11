# Python function program to multiply all the numbers in a list.
# Input : [-8, 6, 1, 9, 2]
# Output: -864

def multi_num(list1):
    t = 1
    for val in list1:
        t = t * val  # Update t every time
    print("Product of elements in the given list: ", t)

val = [-8, 6, 1, 9, 2]
multi_num(val)