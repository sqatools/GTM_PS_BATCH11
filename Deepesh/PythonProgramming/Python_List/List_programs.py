#Q1 : write a python program to max value from list without using max function.
list_a = [4, 6, 8, 34, 56, 12]
max_val = 0 # 4, 6, 8, 34, 56

for val in list_a:
    if val > max_val:
        max_val = val # 4, 6, 8, 34, 56
    else:
        continue

print("Max value :", max_val)


#########################
print("_"*50)
#import pdb; pdb.set_trace()

#Q2 : write a python program to second max value from list without using max function.
list_a = [4, 76, 60, 8, 34, 56, 12, 13, 100]
max_val = 0  # 4, 6, 8, 34, 56
# val < max_val and val > sec_max
sec_max_val = 0 # 0, 4, 6, 8, 34


for i in range(len(list_a)):
    print("max val :", max_val)
    print("sec max val :", sec_max_val)
    print("list_a[i] :", list_a[i])
    if list_a[i] > max_val:
        max_val = list_a[i]

    if i == 0:
        continue
    elif list_a[i-1] < max_val and list_a[i-1] > sec_max_val:
        sec_max_val = list_a[i-1]
    print("_"*50)


print("Max value :", max_val)
print("Sec max value :", sec_max_val)
