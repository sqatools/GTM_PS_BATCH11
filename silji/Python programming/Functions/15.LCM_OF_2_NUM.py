# 15). Python function program to find the LCM of two numbers.
# Input: 12, 20
# Output: 60

# GCD(12, 20) = 4
#
# Product: 12 × 20 = 240
#
# LCM: 240 // 4 = 60

import math

def find_lcm(a, b):
    return (a * b) // math.gcd(a, b)

num1 = 12
num2 = 20

result = find_lcm(num1, num2)
print("LCM of", num1, "and", num2, "is:", result)
