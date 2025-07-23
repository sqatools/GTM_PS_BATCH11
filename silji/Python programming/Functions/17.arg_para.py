# 18). Python function program to create a function with *args as parameters.
# Input: 5, 6, 8, 7
# Output: 125 216 512 343
def func(*args):
    for num in args:
        print(num**3,end=" ")
func(5, 6, 8, 7)