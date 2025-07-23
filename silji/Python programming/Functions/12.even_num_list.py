# 11). Python function program to find the even numbers from a given list.
# Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output : [2, 4, 6, 8]

# def even(list):
#     evens=[]
#     for num in list:
#         if num % 2 == 0:
#             evens.append(num)
#     return evens
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = even(numbers)
# print("Even numbers are:", result)



def even(lst):
    evens = []  # Empty list to store even numbers
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

# Test list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = even(numbers)
# # print("Even numbers are:", result)