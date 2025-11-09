# sort negative and positive
list1 = [45, 67, 80, -3, 4 -54, -4, 23]
# output = [45, 67, 80, 4, 23, -3,-4, -54]

positive=[]
negative=[]
for i in  list1:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)

print("result",positive+negative)