#19_Python function program to get the factorial of a given number.
# Input: 5
# Output: 120

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result* i
    return result

# Example usage
num = 5
output = factorial(num)
print("Factorial of", num, "is:", output)
