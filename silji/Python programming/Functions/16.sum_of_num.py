
# 16). Python function program to calculate the sum of numbers from 0 to 10.
# Output: 55


def sum_numbers():
    total = 0
    for i in range(0, 11):  # From 0 to 10 inclusive
        total =total+ i
    return total
# Call the function and print result
result = sum_numbers()
print("Sum from 0 to 10 is:", result)