for _ in range(1, 5):
    print('Hello World')

list1 = [5, 7, 9, 23]
# for val in list1:
#     print(val, ":", val**2)


for _ in range(3):
    for val in list1:
        print(val, ":", val**2)


print("_"*50)
######################################
list1 = [4, 6, 7, 23, 45, 67, 2, 47]
first_max = second_max = 0

for val in list1:
    if val > first_max:
        second_max = first_max
        first_max = val
    elif first_max > val > second_max:
        second_max = val

print("second max  :", second_max)
