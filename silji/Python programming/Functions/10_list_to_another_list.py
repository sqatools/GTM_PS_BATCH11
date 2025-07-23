#  Python function program that takes a list and returns a new list with unique elements of the first list.
# Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
# Output : [2, 3, 1, 4, 6 ]

def unique_value(list1):
    print(list(set(list1)))

l = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
unique_value(l)
