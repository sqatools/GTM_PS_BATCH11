# Home work:
# 1.  write a python program to max value from tuple.
# 2.  write a python program to remove duplicate values from tuple
# 3.  write a python program to get second max value from tuple.

# 1.  write a python program to max value from tuple.
# Tuple1 = (10, 40, 70, 233, 13, 45)
# print("Tuple1",max(Tuple1))
#
# # 2.  write a python program to remove duplicate values from tuple
# Tuple2=(100, 440, 233, 233, 103, 405)
#
# Tuple2_no_duplicates = tuple(set(Tuple2))
#
# print("Original Tuple:", Tuple2)
# print("Tuple after removing duplicates:", Tuple2_no_duplicates)

# 3.  write a python program to get second max value from tuple.
Tuple3=(1, 4, 2, 3, 10, 6)

max_val = 0
sec_max_val = 0

for val in Tuple3:

    if val > max_val:
        sec_max_val = max_val # 4
        max_val = val # 76
    # 76 > 60 > 4
    elif max_val > val > sec_max_val:
        sec_max_val = val
    print("max :", max_val, "sec max :", sec_max_val)

print("Max val :", max_val)
print("Sec max val :", sec_max_val)
