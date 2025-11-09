# Q1:  write a python Program to sort positive and negative separately.
list_a = [45, 67, 80, -3, 4, -56, -4, 23]

#output = [45, 67, 80, 4, 23, -3, -56, -4]

pos_list =[]
neg_list =[]
for val in list_a:
    print(val, pos_list, neg_list)
    if val > 0:
        pos_list.append(val)
    else:
        neg_list.append(val)

print("output :", pos_list+neg_list)

# list_a = [45, 67, 80, -3, 4, -56, -4, 23]
# pos_list =[]
# neg_list =[]
#
# for val in list_a:
#     if val>0:
#         pos_list.append(val)
#     else:
#         neg_list.append(val)
# print("output" , pos_list+neg_list)
#
