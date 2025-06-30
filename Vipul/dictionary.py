from copy import deepcopy

str1 = "Hello we are Learning Python"
# output = {"Hello": 5, "we": 2, "are": 3, "Learning": 8, "Python": 6}
l1 = str1.split()
l2 = []
print(l1)
for i in l1:
    l2.append(len(i))
output = dict(zip(l1, l2))
print(output) # {'Hello': 5, 'we': 2, 'are': 3, 'Learning': 8, 'Python': 6}


# output2 = {"Ho": "HHeelllloo", "we": "wwee", "ae": "aarree", "Lg": "LLeeaarrnniinngg", "Pn": "PPyytthhoonn"}

l1 = str1.split()

d1 = {}

for i in l1:
    key = i[0] + i[-1]
    value = ''.join([char*2 for char in i])
    d1[key] = value
print(d1)

# ques 1:
d = {}
d['name'] = "tester"
d['age'] = "39"
print(d)

# ques 2:
dictionary = {'a': 5, 'b':3, 'c': 6, 'd': 8}
for i in dictionary:
    print(i, ":", dictionary[i]**2)

# ques 3:
dict1 = {'name':'john','city':'Landon','country':'UK'}
dict2 = {}
dict2 = dict1
print('dict2',dict2)
# dict2['name'] = 'Wamika'
print('dict1',dict1)
print('dict2',dict2)
dict3 = deepcopy(dict1)
print('dict3', dict3)
dict3['name'] = "Wamika"
print('dict1', dict1)
print('dict3',dict3)

# ques 4
dict1 = {'Name':'Harry','Rollno':345,'Address':'Jordan'}
dict2 = {'Age':25,'salary': '$25k'}
dict1.update((dict2))
print(dict1)

# ques 5 :
d1 = {'a':2, 'b':3, 'c':4, 'd':5, 'e':6, 'f':7}
l1 = [[k,v] for  k, v in d1.items() if v%2==0]
l2 = [[k,v] for k, v in d1.items() if v%2 != 0]

print('even list', l1)
print('odd list', l2)

# ques 6 :
list1 = [4, 5, 6, 2, 1, 7, 11]
dict1 = {}
for i in list1:
    if i%2==0:
        dict1[i] = i**2
    else:
        dict1[i] = i**3

print(dict1)

# ques 7:
dict2 = {x:x**2 if x%2==0 else x**3 for x in list1 }
print(dict2)

dict2.clear()
print(dict2)

# ques 8:
dict1 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
dict2 = {}

for k, v in dict1.items():
    print(k, v)
    if v not in dict2.values():
        dict2[k] = v

print(dict2)

# ques 9 :
string = "SQAToolss"
dict1 = {}
for i in string:
    dict1[i] = string.count(i)
print(dict1)
print('dict1')
# ques 10 :
s = "kavita love me and me love kavita"
l = s.split()
dd = {}
for i in l:
    dd[i] = l.count(i)
print(dd)

# ques 11 :
dict1 = {'d':21,'b':53,'a':13,'c':41}
for i in sorted(dict1):
    print(i, dict1[i]*2)

# ques 12 :
D1 = {'name':'yash','city':'pune'}
D2 = {}
for k, v in D1.items():
    D2[v] = k
print(D2)

# ques 13 :
D1 =  {'x':23,'y':10,'z':7}
sum = 0
for i in D1.values():
    sum += i
print(sum)