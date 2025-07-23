import random

# get random number from 1, 10
var1 = random.randint(1, 10)
print(var1)

# get random value from list
list1 = [6, 8, 3, 5, 16]
var2 = random.choice(list1)
print("var2 :", var2)

# shuffle list data
list2 = [5, 7, 2, 15, 6]
random.shuffle(list2)
print("list2 :", list2) # [2, 15, 5, 7, 6]

# get sample values
list3 = [4, 7, 2, 14, 1]
var3 = random.sample(list3, 2)
print("random sample :", var3) # [1, 7]
